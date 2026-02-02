# app.py
import streamlit as st
import random

st.title("Architectural AI Assistant (No Extra Packages)")

st.header("Project Requirements")
building_type = st.selectbox("Building Type", ["Residential", "Commercial", "Office", "Mixed-use"])
floors = st.number_input("Number of Floors", min_value=1, max_value=10, value=2)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=20, value=4)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, value=3)
style = st.selectbox("Architectural Style", ["Modern", "Traditional", "Minimalist", "Tropical"])
climate = st.selectbox("Climate/Region", ["Hot", "Cold", "Temperate", "Humid"])

st.header("Actions")
generate = st.button("Generate Floor Plan")
analyze = st.button("Analyze Layout")

# --- Floor Plan Generation ---
def generate_floor_plan_text(bedrooms, bathrooms):
    layout = "Floor Plan Diagram (Simplified):\n"
    layout += "-"*30 + "\n"
    
    for i in range(bedrooms):
        layout += f"[Bedroom {i+1}]  "
        if (i+1) % 3 == 0:
            layout += "\n"
    
    layout += "\n"
    for i in range(bathrooms):
        layout += f"[Bath {i+1}]  "
    layout += "\n" + "-"*30
    return layout

# --- Layout Analysis ---
def analyze_layout(bedrooms, bathrooms):
    messages = []
    if bedrooms < bathrooms:
        messages.append("⚠ Warning: More bathrooms than bedrooms.")
    if bedrooms > 6:
        messages.append("💡 Suggestion: Consider splitting the house into zones for better space utilization.")
    if bathrooms == 0:
        messages.append("⚠ Add at least one bathroom.")
    if not messages:
        messages.append("✅ Layout seems reasonable.")
    return messages

# --- Display Floor Plan ---
if generate:
    st.subheader("Generated Floor Plan")
    floor_plan_text = generate_floor_plan_text(bedrooms, bathrooms)
    st.text(floor_plan_text)

# --- Display Analysis ---
if analyze:
    st.subheader("Layout Analysis")
    analysis = analyze_layout(bedrooms, bathrooms)
    for msg in analysis:
        st.info(msg)
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
# app.py
import streamlit as st

st.title("Architectural AI Assistant (Multi-Floor ASCII Plan)")

st.header("Project Requirements")
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=2)
bedrooms = st.number_input("Number of Bedrooms (Total)", min_value=0, max_value=20, value=4)
bathrooms = st.number_input("Number of Bathrooms (Total)", min_value=0, max_value=10, value=3)
living_rooms = st.number_input("Number of Living Rooms (Total)", min_value=0, max_value=5, value=1)
kitchens = st.number_input("Number of Kitchens (Total)", min_value=0, max_value=3, value=1)

generate = st.button("Generate Floor Plan")
analyze = st.button("Analyze Layout")

# --- Generate Multi-Floor ASCII Plan ---
def generate_multi_floor_plan(floors, bedrooms, bathrooms, living_rooms, kitchens):
    layout = "Multi-Floor ASCII Floor Plan\n"
    layout += "="*60 + "\n"
    
    # Distribute rooms across floors
    bedrooms_per_floor = max(1, bedrooms // floors)
    bathrooms_per_floor = max(1, bathrooms // floors)
    living_per_floor = max(1, living_rooms // floors)
    kitchens_per_floor = max(1, kitchens // floors)

    for f in range(1, floors+1):
        layout += f"\nFloor {f}\n"
        layout += "-"*60 + "\n"
        # Living/Kitchen Zone
        layout += "Living/Kitchen Zone:\n"
        layout += " ".join([f"[Living {i+1+living_per_floor*(f-1)}]" for i in range(living_per_floor)]) + " "
        layout += " ".join([f"[Kitchen {i+1+kitchens_per_floor*(f-1)}]" for i in range(kitchens_per_floor)]) + "\n"
        
        # Bedroom Zone
        layout += "Bedroom Zone:\n"
        layout += " ".join([f"[Bedroom {i+1+bedrooms_per_floor*(f-1)}]" for i in range(bedrooms_per_floor)]) + "\n"
        
        # Bathroom Zone
        layout += "Bathroom Zone:\n"
        layout += " ".join([f"[Bath {i+1+bathrooms_per_floor*(f-1)}]" for i in range(bathrooms_per_floor)]) + "\n"
        
        # Stairs if multiple floors
        if floors > 1 and f < floors:
            layout += "Stairs Up -->\n"
    
    layout += "="*60
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
    st.subheader("Generated Multi-Floor Plan")
    floor_plan_text = generate_multi_floor_plan(floors, bedrooms, bathrooms, living_rooms, kitchens)
    st.text(floor_plan_text)

# --- Display Analysis ---
if analyze:
    st.subheader("Layout Analysis")
    analysis = analyze_layout(bedrooms, bathrooms, living_rooms, kitchens)
    for msg in analysis:
        st.info(msg)
