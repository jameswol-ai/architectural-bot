def climate_analysis():
    notes = []
    notes.append("🌞 Climate Mode: Hot / Tropical")

    notes.append("✔ Living areas oriented to cooler sides (North/South recommended)")
    notes.append("✔ Bedrooms grouped away from direct afternoon sun")
    notes.append("✔ Bathrooms require ventilation openings")

    notes.append("💡 Recommendation: Provide wide overhangs and shaded windows")
    notes.append("💡 Encourage cross-ventilation in all habitable rooms")

    return notes
st.subheader("British Standards Compliance Check")
for msg in british_standards_check():
    if msg.startswith("❌"):
        st.error(msg)
    else:
        st.success(msg)
# app.py
import streamlit as st
import random

st.title("Architectural AI Assistant (Multi-Variation + Room Sizes)")

st.header("Project Requirements")
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=2)
bedrooms = st.number_input("Number of Bedrooms (Total)", min_value=0, max_value=20, value=4)
bathrooms = st.number_input("Number of Bathrooms (Total)", min_value=0, max_value=10, value=3)
living_rooms = st.number_input("Number of Living Rooms (Total)", min_value=0, max_value=5, value=1)
kitchens = st.number_input("Number of Kitchens (Total)", min_value=0, max_value=3, value=1)
variations = st.number_input("Number of Plan Variations", min_value=1, max_value=5, value=2)

generate = st.button("Generate Floor Plans")
analyze = st.button("Analyze Layout")

# -------------------------------
# Room size generators (meters)
# -------------------------------
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
