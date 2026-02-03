# logic/codes_bs.py

def british_standards_check(bedrooms, bathrooms, living_rooms, kitchens, floors):
    issues = []

    # Minimum sanitary provision
    required_bathrooms = max(1, bedrooms // 4)
    if bathrooms < required_bathrooms:
        issues.append("❌ Insufficient bathrooms (BS guidance: 1 per 4 bedrooms)")
    else:
        issues.append("✔ Bathroom provision meets BS guidance")

    # Multi-storey requirement
    if floors > 1:
        issues.append("✔ Staircase required and assumed compliant (≥900mm width)")

    # Basic spatial checks
    if living_rooms == 0:
        issues.append("❌ At least one living room required")
    else:
        issues.append("✔ Living room provision acceptable")

    if kitchens == 0:
        issues.append("❌ Kitchen required")
    else:
        issues.append("✔ Kitchen provision acceptable")

    return issues
