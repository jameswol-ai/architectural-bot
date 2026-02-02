# app.py
import streamlit as st

st.title("Architectural AI Assistant (Connected ASCII Floor Plan)")

st.header("Project Requirements")
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=2)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, value=4)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=5, value=2)
living_rooms = st.number_input("Number of Living Rooms", min_value=0, max_value=5, value=1)
kitchens = st.number_input("Number of Kitchens", min_value=0, max_value=3, value=1)

generate = st.button("Generate Floor Plan")
analyze = st.button("Analyze Layout")

# --- Generate ASCII Map with Zones ---
def generate_connected_ascii(bedrooms, bathrooms, living_rooms, kitchens):
    layout = "Floor Plan (Simplified Connected Layout)\n"
    layout += "="*50 + "\n"

    # Living/Kitchen Zone
    layout += "Living/Kitchen Zone:\n"
    for i in range(living_rooms):
        layout += f"[Living Room {i+1}]--"
    for i in range(kitchens):
        layout += f"[Kitchen {i+1}]"
    layout += "\n" + "-"*50 + "\n"

    # Bedroom Zone
    layout += "Bedroom Zone:\n"
    for i in range(bedrooms):
        layout += f"[Bedroom {i+1}]--"
    layout = layout.rstrip("--") + "\n"

    # Bathroom Zone
    layout += "Bathroom Zone:\n"
    for i in range(bathrooms):
        layout += f"[Bath {i+1}]--"
    layout = layout.rstrip("--") + "\n"

    layout += "="*50
    return layout

# --- Layout Analysis ---
def analyze_layout(bedrooms, bathrooms, living_rooms, kitchens):
    messages = []
    if bedrooms < bathrooms:
        messages.append("⚠ Warning: More bathrooms than bedrooms.")
    if bedrooms > 6:
        messages.append("💡 Suggestion: Split the house into zones for better space utilization.")
    if bathrooms == 0:
        messages.append("⚠ At least one bathroom is required.")
    if living_rooms == 0:
        messages.append("💡 Suggestion: Add at least one living room.")
    if kitchens == 0:
        messages.append("⚠ At least one kitchen is required.")
    if not messages:
        messages.append("✅ Layout seems reasonable.")
    return messages

# --- Display Floor Plan ---
if generate:
    st.subheader("Generated Floor Plan")
    floor_plan_text = generate_connected_ascii(bedrooms, bathrooms, living_rooms, kitchens)
    st.text(floor_plan_text)

# --- Display Analysis ---
if analyze:
    st.subheader("Layout Analysis")
    analysis = analyze_layout(bedrooms, bathrooms, living_rooms, kitchens)
    for msg in analysis:
        st.info(msg)
