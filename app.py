# app.py
import streamlit as st
import matplotlib.pyplot as plt
import random

st.title("Architectural AI Assistant")

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
def generate_floor_plan(floors, bedrooms, bathrooms):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Simplified Floor Plan Diagram")
    
    # Randomly generate room blocks for demonstration
    for i in range(bedrooms):
        x = random.uniform(0, 7)
        y = random.uniform(0, 7)
        ax.add_patch(plt.Rectangle((x, y), 2, 2, fill=None, edgecolor="blue", linewidth=2))
        ax.text(x+0.5, y+0.5, f"Bedroom {i+1}", fontsize=8)
    for i in range(bathrooms):
        x = random.uniform(0, 8)
        y = random.uniform(0, 8)
        ax.add_patch(plt.Rectangle((x, y), 1.5, 1.5, fill=None, edgecolor="red", linewidth=2))
        ax.text(x+0.2, y+0.2, f"Bath {i+1}", fontsize=7)
    
    return fig

# --- Layout Analysis ---
def analyze_layout(bedrooms, bathrooms):
    messages = []
    if bedrooms < bathrooms:
        messages.append("Warning: More bathrooms than bedrooms.")
    if bedrooms > 6:
        messages.append("Consider splitting the house into zones for better space utilization.")
    if bathrooms == 0:
        messages.append("Add at least one bathroom.")
    if not messages:
        messages.append("Layout seems reasonable.")
    return messages

# --- Display Floor Plan ---
if generate:
    st.subheader("Generated Floor Plan")
    fig = generate_floor_plan(floors, bedrooms, bathrooms)
    st.pyplot(fig)

# --- Display Analysis ---
if analyze:
    st.subheader("Layout Analysis")
    analysis = analyze_layout(bedrooms, bathrooms)
    for msg in analysis:
        st.info(msg)
