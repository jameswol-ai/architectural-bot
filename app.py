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
floor_plan_text = ""
if generate:
    st.subheader("Generated Multi-Floor Plan")
    floor_plan_text = generate_multi_floor_plan(floors, bedrooms, bathrooms, living_rooms, kitchens)
    st.text(floor_plan_text)

    # --- Download Button ---
    st.download_button(
        label="Download Floor Plan as .txt",
        data=floor_plan_text,
        file_name="floor_plan.txt",
        mime="text/plain"
    )

# --- Display Analysis ---
if analyze:
    st.subheader("Layout Analysis")
    analysis = analyze_layout(bedrooms, bathrooms, living_rooms, kitchens)
    for msg in analysis:
        st.info(msg)
