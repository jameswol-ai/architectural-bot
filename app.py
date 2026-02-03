import streamlit as st
import random

# Imports from refactored modules
from logic.costing import cost_estimation, boq_breakdown
from logic.codes_bs import british_standards_check
from logic.site import plot_analysis

st.title("Architectural Feasibility Tool – Internal Use")

# ====================
# Inputs
# ====================
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=4)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
living_rooms = st.number_input("Number of Living Rooms", min_value=1, max_value=5, value=1)
kitchens = st.number_input("Number of Kitchens", min_value=1, max_value=3, value=1)
floors = st.number_input("Number of Storeys", min_value=1, max_value=5, value=1)

st.subheader("Site Information")

plot_length = st.number_input("Plot Length (m)", min_value=10, max_value=200, value=30)
plot_width = st.number_input("Plot Width (m)", min_value=10, max_value=200, value=20)

front_setback = st.number_input("Front Setback (m)", min_value=0, max_value=20, value=5)
back_setback = st.number_input("Back Setback (m)", min_value=0, max_value=20, value=5)
side_setback = st.number_input("Side Setback (m)", min_value=0, max_value=20, value=3)

st.subheader("Plot Analysis")

analysis, messages = plot_analysis(
    plot_length, plot_width, front_setback, back_setback, side_setback
)

st.info(f"Total Plot Area: {analysis['total_plot_area']} m²")
st.info(f"Usable Area after Setbacks: {analysis['usable_area']} m²")
st.info(f"Site Coverage: {analysis['coverage_percent']}%")

for msg in messages:
    if msg.startswith("❌"):
        st.error(msg)
    else:
        st.success(msg)
        
st.subheader("Basic Plot Layout (Text Representation)")

layout = (
    f"Front Setback: {front_setback}m\n"
    f"{'=' * int(round(usable_width))}\n"
    f"Usable Plot Area: {analysis['usable_area']} m²\n"
    f"{'=' * int(round(usable_width))}\n"
    f"Back Setback: {back_setback}m"
)

st.text(layout)

# Seed for repeatable randomization
seed = st.number_input("Design Seed (for repeatable results)", value=1)
random.seed(seed)

# ====================
# British Standards Compliance Check
# ====================
st.subheader("British Standards Compliance Check")

bs_issues = british_standards_check(
    bedrooms, bathrooms, living_rooms, kitchens, floors
)

for msg in bs_issues:
    if msg.startswith("❌"):
        st.error(msg)
    else:
        st.success(msg)

# ====================
# Costing Section
# ====================
st.subheader("Preliminary Cost Estimation (UK)")

costs = cost_estimation(bedrooms, bathrooms, living_rooms, kitchens)
area = costs["area"]

st.info(f"Estimated Gross Floor Area: {int(area)} m²")

for level in ["Low Finish", "Medium Finish", "High Finish"]:
    st.success(f"{level}: £{costs[level]:,}")

st.subheader("BOQ-Style Cost Breakdown (Medium Finish)")
boq = boq_breakdown(costs["Medium Finish"])

for item, value in boq.items():
    st.success(f"{item}: £{value:,}")

# ====================
# Room Schedule Section
# ====================
st.subheader("Room Schedule (BS Compliant)")

def room_schedule():
    schedule = []

    def add_room(name, w, l, floor, min_area):
        area = round(w * l, 1)
        status = "✔ BS compliant" if area >= min_area else "❌ Below BS minimum"
        schedule.append(
            f"{name} | {w:.1f}x{l:.1f} m | {area} m² | Floor {floor} | {status}"
        )

    beds_pf = max(1, bedrooms // floors)
    baths_pf = max(1, bathrooms // floors)
    living_pf = max(1, living_rooms // floors)
    kitchens_pf = max(1, kitchens // floors)

    for f in range(1, floors + 1):
        for i in range(beds_pf):
            add_room(
                f"Bedroom {i+1}",
                random.uniform(3.0, 4.2),
                random.uniform(3.0, 4.5),
                f,
                11.5
            )
        for i in range(baths_pf):
            add_room(
                f"Bathroom {i+1}",
                random.uniform(2.0, 2.5),
                random.uniform(2.0, 2.5),
                f,
                3.0
            )
        for i in range(living_pf):
            add_room(
                f"Living Room {i+1}",
                random.uniform(4.0, 5.5),
                random.uniform(4.0, 5.5),
                f,
                13.0
            )
        for i in range(kitchens_pf):
            add_room(
                f"Kitchen {i+1}",
                random.uniform(3.0, 4.0),
                random.uniform(3.0, 4.0),
                f,
                7.0
            )

    return schedule

schedule = room_schedule()

for row in schedule:
    if "❌" in row:
        st.error(row)
    else:
        st.success(row)

# Download button for schedule
st.download_button(
    "Download Room Schedule",
    "\n".join(schedule),
    "room_schedule.txt",
    "text/plain"
    )
