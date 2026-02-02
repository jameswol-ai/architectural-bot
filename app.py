# app.py
import streamlit as st
import random

st.title("Architectural AI Assistant (Multi-Variation ASCII Plan)")

st.header("Project Requirements")
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=2)
bedrooms = st.number_input("Number of Bedrooms (Total)", min_value=0, max_value=20, value=4)
bathrooms = st.number_input("Number of Bathrooms (Total)", min_value=0, max_value=10, value=3)
living_rooms = st.number_input("Number of Living Rooms (Total)", min_value=0, max_value=5, value=1)
kitchens = st.number_input("Number of Kitchens (Total)", min_value=0, max_value=3, value=1)
variations = st.number_input("Number of Plan Variations", min_value=1, max_value=5, value=2)

generate = st.button("Generate Floor Plans")
analyze = st.button("Analyze Layout")

# --- Generate Multi-Floor ASCII Plan ---
def generate_multi_floor_plan(floors, bedrooms, bathrooms, living_rooms, kitchens):
    # Same as previous multi-floor function
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
        # Shuffle rooms for variation
        bedroom_list = [f"[Bedroom {i+1+bedrooms_per_floor*(f-1)}]" for i in range(bedrooms_per_floor)]
        bathroom_list = [f"[Bath {i+1+bathrooms_per_floor*(f-1)}]" for i in range(bathrooms_per_floor)]
        living_list = [f"[Living {i+1+living_per_floor*(f-1)}]" for i in range(living_per_floor)]
        kitchen_list = [f"[Kitchen {i+1+kitchens_per_floor*(f-1)}]" for i in range(kitchens_per_floor)]

        random.shuffle(bedroom_list)
        random.shuffle(bathroom_list)
        random.shuffle(living_list)
        random.shuffle(kitchen_list)

        # Living/Kitchen Zone
        layout += "Living/Kitchen Zone:\n"
        layout += " ".join(living_list + kitchen_list) + "\n"

        # Bedroom Zone
        layout += "Bedroom Zone:\n"
        layout += " ".join(bedroom_list) + "\n"

        # Bathroom Zone
        layout += "Bathroom Zone:\n"
        layout += " ".join(bathroom_list) + "\n"

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

# --- Display Multiple Floor Plans ---
if generate:
    st.subheader("Generated Floor Plan Variations")
    for v in range(1, variations+1):
        plan_text = generate_multi_floor_plan(floors, bedrooms, bathrooms, living_rooms, kitchens)
        st.text(f"--- Variation {v} ---")
        st.text(plan_text)
        st.download_button(
            label=f"Download Variation {v} as .txt",
            data=plan_text,
            file_name=f"floor_plan_variation_{v}.txt",
            mime="text/plain"
        )

# --- Display Analysis ---
if analyze:
    st.subheader("Layout Analysis")
    analysis = analyze_layout(bedrooms, bathrooms, living_rooms, kitchens)
    for msg in analysis:
        st.info(msg)
