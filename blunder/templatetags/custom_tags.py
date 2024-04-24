from django import template

register = template.Library()


@register.filter(name="format_number")
def format_number(value):
    if value < 1000:
        return str(value)
    elif value < 1000000:
        return f"{value / 1000:.1f}K"
    elif value < 1000000000:
        return f"{value / 1000000:.1f}M"
    else:
        return f"{value / 1000000000:.1f}B"
