# logic/costing.py

def cost_estimation(bedrooms, bathrooms, living_rooms, kitchens):
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

    total_area = base_area * 1.25  # circulation & walls

    return {
        "area": total_area,
        "Low Finish": int(total_area * 1200),
        "Medium Finish": int(total_area * 1500),
        "High Finish": int(total_area * 1800),
    }


def boq_breakdown(total_cost):
    return {
        "Substructure (Foundations)": int(total_cost * 0.15),
        "Superstructure (Frame, Walls, Roof)": int(total_cost * 0.35),
        "Finishes": int(total_cost * 0.20),
        "Services (MEP)": int(total_cost * 0.15),
        "External Works": int(total_cost * 0.05),
        "Preliminaries & Contingency": int(total_cost * 0.10),
    }
