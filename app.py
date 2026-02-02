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
