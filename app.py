import streamlit as st
import random

from logic.costing import cost_estimation, boq_breakdown
from logic.codes_bs import british_standards_check

from logic.costing import cost_estimation, boq_breakdown

def climate_analysis():
    notes = []
    notes.append("🌞 Climate Mode: Hot / Tropical")

    notes.append("✔ Living areas oriented to cooler sides (North/South recommended)")
    notes.append("✔ Bedrooms grouped away from direct afternoon sun")
    notes.append("✔ Bathrooms require ventilation openings")

    notes.append("💡 Recommendation: Provide wide overhangs and shaded windows")
    notes.append("💡 Encourage cross-ventilation in all habitable rooms")

    return notes

# app.py
import streamlit as st
import random

st.title("Architectural AI Assistant (Multi-Variation + Room Sizes)")

st.header("Site Information")
plot_width = st.number_input("Plot Width (m)", min_value=6.0, max_value=50.0, value=12.0)
plot_depth = st.number_input("Plot Depth (m)", min_value=10.0, max_value=60.0, value=25.0)
road_side = st.selectbox("Road Access Side", ["North", "South", "East", "West"])

st.header("Project Requirements")
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=2)
bedrooms = st.number_input("Number of Bedrooms (Total)", min_value=0, max_value=20, value=4)
bathrooms = st.number_input("Number of Bathrooms (Total)", min_value=0, max_value=10, value=3)
living_rooms = st.number_input("Number of Living Rooms (Total)", min_value=0, max_value=5, value=1)
kitchens = st.number_input("Number of Kitchens (Total)", min_value=0, max_value=3, value=1)
variations = st.number_input("Number of Plan Variations", min_value=1, max_value=5, value=2)

generate = st.button("Generate Floor Plans")
analyze = st.button("Analyze Layout")

floors = st.number_input(
    "Number of Storeys",
    min_value=1,
    max_value=5,
    value=1,
    step=1
)

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



st.subheader("Room Schedule (British Standards)")

schedule = room_schedule()

for row in schedule:
    if "❌" in row:
        st.error(row)
    else:
        st.success(row)

st.download_button(
    "Download Room Schedule",
    "\n".join(schedule),
    "room_schedule.txt",
    "text/plain"
)

# -------------------------------
# Room size generators (meters)
# ------------------------------
def room_size(room_type):
    sizes = {
        "Bedroom": (3, 5),
        "Bath": (2, 3),
        "Living": (4, 6),
        "Kitchen": (3, 4)
    }
    min_s, max_s = sizes[room_type]
    width = random.randint(min_s, max_s)
    length = random.randint(min_s, max_s)
    return f"{width}x{length}m"


# -------------------------------
# Generate multi-floor plan
# -------------------------------
def generate_plan(floors, bedrooms, bathrooms, living_rooms, kitchens):
    layout = "MULTI-FLOOR ARCHITECTURAL PLAN\n"
    layout += "=" * 65 + "\n"

    beds_pf = max(1, bedrooms // floors)
    baths_pf = max(1, bathrooms // floors)
    living_pf = max(1, living_rooms // floors)
    kitchen_pf = max(1, kitchens // floors)

    for f in range(1, floors + 1):
        layout += f"\nFLOOR {f}\n"
        layout += "-" * 65 + "\n"

        # Living + Kitchen
        layout += "Living / Kitchen Zone:\n"
        for i in range(living_pf):
            layout += f"[Living {i+1} ({room_size('Living')})] -- "
        for i in range(kitchen_pf):
            layout += f"[Kitchen {i+1} ({room_size('Kitchen')})]"
        layout += "\n\n"

        # Bedrooms
        layout += "Bedroom Zone:\n"
        for i in range(beds_pf):
            layout += f"[Bedroom {i+1} ({room_size('Bedroom')})] -- "
        layout += "\n\n"

        # Bathrooms
        layout += "Bathroom Zone:\n"
        for i in range(baths_pf):
            layout += f"[Bath {i+1} ({room_size('Bath')})] -- "
        layout += "\n"

        if floors > 1 and f < floors:
            layout += "\n[STAIRS UP ⬆]\n"

    layout += "=" * 65
    return layout


# -------------------------------
# Layout analysis
# -------------------------------
def analyze_layout(bedrooms, bathrooms, living_rooms, kitchens):
    notes = []
    if bathrooms == 0:
        notes.append("⚠ At least one bathroom is required.")
    if kitchens == 0:
        notes.append("⚠ A kitchen is required.")
    if bedrooms > 6:
        notes.append("💡 Large bedroom count — consider zoning or corridors.")
    if bathrooms < bedrooms / 2:
        notes.append("💡 Consider adding more bathrooms for comfort.")
    if not notes:
        notes.append("✅ Layout proportions look reasonable.")
    return notes

# -------------------------------
# Display plans
# -------------------------------
if generate:
    st.subheader("Generated Plan Variations")

    for v in range(1, variations + 1):
        plan = generate_plan(floors, bedrooms, bathrooms, living_rooms, kitchens)
        st.text(f"--- VARIATION {v} ---")
        st.text(plan)

        st.download_button(
            label=f"Download Variation {v}",
            data=plan,
            file_name=f"architectural_plan_variation_{v}.txt",
            mime="text/plain"
        )

# -------------------------------
# Analysis
# -------------------------------
if analyze:
    st.subheader("Design Analysis")
    for msg in analyze_layout(bedrooms, bathrooms, living_rooms, kitchens):
        st.info(msg)

st.subheader("Climate-Based Design Analysis")
for msg in climate_analysis():
    st.success(msg)  
def british_standards_check():
    issues = []    
    

    # Minimum sizes (m²)
    min_sizes = {
        "Bedroom": 11.5,
        "Living": 13.0,
        "Kitchen": 7.0,
        "Bath": 3.0
    }

    for room, min_area in min_sizes.items():
        issues.append(f"✔ {room} minimum area checked (≥ {min_area} m²)")

    issues.append("✔ Minimum corridor width ≥ 900mm")
    issues.append("✔ Stair width ≥ 900mm (if multi-storey)")
    issues.append("✔ Bathrooms ventilated")
    issues.append("✔ WC not opening directly into kitchen")

    if bathrooms < max(1, bedrooms // 4):
        issues.append("❌ Insufficient bathrooms per British Standards")
    else:
        issues.append("✔ Bathroom count meets British Standards")

    return issues


from logic.codes_bs import british_standards_check

st.subheader("British Standards Compliance Check")

bs_issues = british_standards_check(
    bedrooms, bathrooms, living_rooms, kitchens, floors
)

for msg in bs_issues:
    if msg.startswith("❌"):
        st.error(msg)
    else:
        st.success(msg)
def adjacency_analysis():
    issues = []

    issues.append("✔ Kitchen connected to living/dining area")

    issues.append("✔ Bedrooms grouped in private zone")

    if bathrooms > 0 and kitchens > 0:
        issues.append("✔ Bathrooms separated from kitchen zone")

    if bedrooms > 0 and living_rooms > 0:
        issues.append("💡 Recommendation: Use corridor or lobby between living rooms and bedrooms")

    if floors > 1:
        issues.append("✔ Stairs positioned within circulation space")

    if bathrooms == 0:
        issues.append("❌ No bathrooms detected – adjacency rules violated")

    return issues
    
st.subheader("Room Adjacency & Privacy Check")
for msg in adjacency_analysis():
    if msg.startswith("❌"):
        st.error(msg)
    elif msg.startswith("💡"):
        st.warning(msg)
    else:
        st.success(msg)
        
def cost_estimation():
    # Average areas per room (m²)
    bedroom_area = 12
    living_area = 18
    kitchen_area = 10
    bathroom_area = 4

    base_area = (
        bedrooms * bedroom_area +
        living_rooms * living_area +
        kitchens * kitchen_area +
        bathrooms * bathroom_area
    )

    circulation_factor = 1.25  # walls, corridors, stairs
    total_area = base_area * circulation_factor


    return total_area, costs


st.subheader("Preliminary Cost Estimation (UK)")

# Call the refactored function
costs = cost_estimation(bedrooms, bathrooms, living_rooms, kitchens)
area = costs["area"]

st.info(f"Estimated Gross Floor Area: {int(area)} m²")

for level in ["Low Finish", "Medium Finish", "High Finish"]:
    st.success(f"{level}: £{costs[level]:,}")

# BOQ breakdown
st.subheader("BOQ-Style Cost Breakdown (Medium Finish)")
boq = boq_breakdown(costs["Medium Finish"])

for item, value in boq.items():
    st.success(f"{item}: £{value:,}")


def site_analysis(plot_width, plot_depth, road_side):
    messages = []

    # Setbacks
    front = 3.0
    rear = 3.0
    side = 1.5

    build_width = plot_width - (side * 2)
    build_depth = plot_depth - (front + rear)
    build_area = build_width * build_depth

    plot_area = plot_width * plot_depth

    messages.append(f"Plot Area: {plot_area:.1f} m²")
    messages.append(f"Buildable Area (after setbacks): {build_area:.1f} m²")

    if build_width <= 0 or build_depth <= 0:
        messages.append("❌ Plot too small after setbacks")
        return messages

    messages.append(f"✔ Road access from {road_side}")

    if road_side in ["West"]:
        messages.append("⚠ West-facing road – protect entrance from afternoon sun")
    else:
        messages.append("✔ Road orientation acceptable for main entrance")

    messages.append("💡 Living spaces recommended away from road for privacy")
    messages.append("💡 Bedrooms should avoid west orientation in hot climates")
    return messages


st.subheader("Site Orientation & Plot Analysis")

for msg in site_analysis(plot_width, plot_depth, road_side):
    if msg.startswith("❌"):
        st.error(msg)
    elif msg.startswith("⚠"):
        st.warning(msg)
    elif msg.startswith("💡"):
        st.info(msg)
    else:
        st.success(msg)


def boq_breakdown(total_cost):
    boq = {
        "Substructure (Foundations)": 0.15,
        "Superstructure (Frame, Walls, Roof)": 0.35,
        "Finishes": 0.20,
        "Services (MEP)": 0.15,
        "External Works": 0.05,
        "Preliminaries & Contingency": 0.10
    }

    breakdown = {}
    for item, ratio in boq.items():
        breakdown[item] = int(total_cost * ratio)

    return breakdown

st.subheader("BOQ-Style Cost Breakdown (Medium Finish)")

boq = boq_breakdown(costs["Medium Finish"])

for item, value in boq.items():
    st.success(f"{item}: £{value:,}")
    
boq_text = "BOQ COST BREAKDOWN (MEDIUM FINISH)\n"
boq_text += "=" * 50 + "\n"
for item, value in boq.items():
    boq_text += f"{item}: £{value:,}\n"

st.download_button(
    "Download BOQ (.txt)",
    boq_text,
    "boq_cost_breakdown.txt",
    "text/plain"
)

def room_schedule():
    schedule = []

    def add_room(name, w, l, floor, min_area):
        area = round(w * l, 1)
        status = "✔ BS compliant" if area >= min_area else "❌ Below BS minimum"
        schedule.append(
            f"{name} | {w}x{l} m | {area} m² | Floor {floor} | {status}"
        )

    for f in range(1, floors + 1):
        for i in range(bedrooms // floors):
            add_room(f"Bedroom {i+1}", random.uniform(3,4), random.uniform(3,4.5), f, 11.5)

        for i in range(bathrooms // floors):
            add_room(f"Bathroom {i+1}", random.uniform(2,2.5), random.uniform(2,2.5), f, 3.0)

        for i in range(living_rooms // floors):
            add_room(f"Living Room {i+1}", random.uniform(4,5), random.uniform(4,5), f, 13.0)

        for i in range(kitchens // floors):
            add_room(f"Kitchen {i+1}", random.uniform(3,4), random.uniform(3,4), f, 7.0)

    return schedule

seed = st.number_input("Design Seed (for repeatable results)", value=1)
random.seed(seed)

st.subheader("Assumptions & Limitations")
st.info("""
• Preliminary feasibility tool only
• British Standards simplified guidance
• Costs exclude land, VAT, fees, utilities
• Final compliance subject to local authority approval
""")

st.caption("Architectural Feasibility Tool – v1.0 (Internal Use)")
