# logic/site.py

def plot_analysis(plot_length, plot_width, front_setback, back_setback, side_setback):
    usable_length = plot_length - front_setback - back_setback
    usable_width = plot_width - 2 * side_setback

    coverage = usable_length * usable_width
    total_area = plot_length * plot_width
    coverage_percent = round((coverage / total_area) * 100, 1)

    analysis = {
        "total_plot_area": total_area,
        "usable_area": coverage,
        "coverage_percent": coverage_percent,
        "front_setback": front_setback,
        "back_setback": back_setback,
        "side_setback": side_setback
    }

    # Basic compliance message
    messages = []
    if coverage_percent > 60:
        messages.append("❌ Coverage exceeds 60% limit")
    else:
        messages.append("✔ Coverage within allowed limits")

    return analysis, messages
