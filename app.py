0pp⁰import streamlit as st
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --------------------------
# Imports from logic modules
# --------------------------
from logic.costing import cost_estimation, boq_breakdown
from logic.codes_bs import british_standards_check
from logic.site import plot_analysis
from logic.orientation import room_orientation_recommendation

st.title("Architectural Feasibility Tool – Internal Use")

# ====================
# Building Inputs
# ====================
st.subheader("Building Inputs")

bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=4)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
living_rooms = st.number_input("Number of Living Rooms", min_value=1, max_value=5, value=1)
kitchens = st.number_input("Number of Kitchens", min_value=1, max_value=3, value=1)
floors = st.number_input("Number of Storeys", min_value=1, max_value=5, value=1)

seed = st.number_input("Design Seed (for repeatable results)", value=1)
random.seed(seed)

# ====================
# British Standards Compliance
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
st.subheader("Room Schedule")

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

# Download button for room schedule
st.download_button(
    "Download Room Schedule",
    "\n".join(schedule),
    "room_schedule.txt",
    "text/plain"
)

# ====================
# Site & Plot Logic
# ====================
st.subheader("Site Information")

plot_length = st.number_input("Plot Length (m)", min_value=10, max_value=200, value=30)
plot_width = st.number_input("Plot Width (m)", min_value=10, max_value=200, value=20)
front_setback = st.number_input("Front Setback (m)", min_value=0, max_value=20, value=5)
back_setback = st.number_input("Back Setback (m)", min_value=0, max_value=20, value=5)
side_setback = st.number_input("Side Setback (m)", min_value=0, max_value=20, value=3)

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

# Type-safe ASCII plot
st.subheader("Basic Plot Layout (Text Representation)")
ascii_width = max(1, int(round((analysis['usable_area'] ** 0.5))))  # safe width

layout = (
    f"Front Setback: {front_setback}m\n"
    f"{'=' * ascii_width}\n"
    f"Usable Plot Area: {analysis['usable_area']} m²\n"
    f"{'=' * ascii_width}\n"
    f"Back Setback: {back_setback}m"
)

st.text(layout)

# ====================
# Phase 4: Orientation Recommendations
# ====================
st.subheader("Room Orientation Recommendations")

orientation_msgs = room_orientation_recommendation(
    plot_length, plot_width, living_rooms, bedrooms, kitchens
)

for msg in orientation_msgs:
    st.info(msg)

st.subheader("Orientation Alerts")
for msg in orientation_msgs:
    if "west" in msg.lower() and "living room" in msg.lower():
        st.warning(msg + " ⚠ May overheat in afternoon.")

# ====================
# Phase 5: Floorplan Visualization
# ====================
st.subheader("Floorplan Visualization – Scaled & Adjacent")

fig = draw_floorplan_adjacent(schedule, plot_length, plot_width)
st.pyplot(fig)
    fig, ax = plt.subplots(figsize=(8, 8))
    x_offset = 0
    y_offset = 0
    max_row_height = 0

    for idx, room in enumerate(schedule):
        parts = room.split("|")
        name = parts[0].strip()
        dims = parts[1].strip().split("x")
        width = float(dims[0])
        length = float(dims[1])
        area = float(parts[2].strip().split()[0])

        # Color based on room type
        if "Bedroom" in name:
            color = "lightblue"
        elif "Bathroom" in name:
            color = "skyblue"
        elif "Living" in name:
            color = "lightgreen"
        elif "Kitchen" in name:
            color = "orange"
        else:
            color = "grey"

        # Draw rectangle
        rect = patches.Rectangle(
            (x_offset, y_offset), width, length,
            linewidth=1, edgecolor='black', facecolor=color
        )
        ax.add_patch(rect)

        # Label rectangle
        ax.text(
            x_offset + width/2, y_offset + length/2,
            f"{name}\n{area} m²",
            ha='center', va='center', fontsize=8
        )

        # Update offsets
        x_offset += width + 0.5
        max_row_height = max(max_row_height, length)
        if x_offset > 15:
            x_offset = 0
            y_offset += max_row_height + 0.5
            max_row_height = 0

    ax.set_xlim(0, 20)
    ax.set_ylim(0, y_offset + 10)
    ax.set_aspect('equal')
    ax.set_title("Floorplan Visualization (Approximate)")
    ax.axis('off')
    return fig

fig = draw_floorplan(schedule)
st.pyplot(fig)
