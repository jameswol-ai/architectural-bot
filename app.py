# app.py
import streamlit as st

st.title("Architectural AI Assistant (ASCII Floor Plan)")

st.header("Project Requirements")
building_type = st.selectbox("Building Type", ["Residential", "Commercial", "Office", "Mixed-use"])
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=2)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, value=4)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=5, value=2)
living_rooms = st.number_input("Number of Living Rooms", min_value=0, max_value=5, value=1)
kitchens = st.number_input("Number of Kitchens", min_value=0, max_value=3, value=1)
style = st.selectbox("Architectural Style", ["Modern", "Traditional", "Minimalist", "Tropical"])
climate = st.selectbox("Climate/Region", ["Hot", "Cold", "Temperate", "Humid"])

st.header("Actions")
generate = st.button("Generate Floor Plan")
analyze = st.button("Analyze Layout")

# --- ASCII Floor Plan Generation ---
def generate_ascii_floor_plan(bedrooms, bathrooms, living_rooms, kitchens):
    layout = "Simplified ASCII Floor Plan\n"
    layout += "-"*40 + "\n"
    
    # Bedrooms
    for i in range(bedrooms):
        layout += f"| Bedroom {i+1} "
    layout += "|\n"
    
    # Bathrooms
    for i in range(bathrooms):
        layout += f"| Bath {i+1} "
    layout += "|\n"
    
    # Living rooms
    for i in range(living_rooms):
        layout += f"| Living Room {i+1} "
    layout += "|\n"
    
    # Kitchens
    for i in range(kitchens):
        layout += f"| Kitchen {i+1} "
    layout += "|\n"
    
    layout += "-"*40
    return layout

# --- Layout Analysis ---
def analyze_layout(bedrooms, bathrooms, living_rooms, kitchens):
    messages = []
    if bedrooms < bathrooms:
        messages.append("⚠ Warning: More bathrooms than bedrooms.")
    if bedrooms > 6:
        messages.append("💡 Suggestion: Split the house into zones for better space utilization.")
    if bathrooms == 0:
        messages.append("⚠ Add at least one bathroom.")
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
    floor_plan_text = generate_ascii_floor_plan(bedrooms, bathrooms, living_rooms, kitchens)
    st.text(floor_plan_text)

# --- Display Analysis ---
if analyze:
    st.subheader("Layout Analysis")
    analysis = analyze_layout(bedrooms, bathrooms, living_rooms, kitchens)
    for msg in analysis:
        st.info(msg)
