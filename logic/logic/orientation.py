# logic/orientation.py

def room_orientation_recommendation(plot_length, plot_width, living_rooms, bedrooms, kitchens):
    """
    Simple orientation guide based on UK climate.
    Assumes:
    - North is top
    - East is right
    - South is bottom
    - West is left
    """

    recommendations = []

    # Living rooms: south or east
    for i in range(living_rooms):
        recommendations.append(f"Living Room {i+1}: Prefer south or east-facing for daylight.")

    # Bedrooms: north or east
    for i in range(bedrooms):
        recommendations.append(f"Bedroom {i+1}: Prefer north or east-facing for morning light.")

    # Kitchens: south or west (sun exposure optional)
    for i in range(kitchens):
        recommendations.append(f"Kitchen {i+1}: South or west-facing is acceptable.")

    return recommendations
