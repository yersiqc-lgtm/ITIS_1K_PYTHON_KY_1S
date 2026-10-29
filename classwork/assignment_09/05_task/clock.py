"""
29.10.2026
classwork 5
"""

def to_minutes(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)

def to_time(minutes):
    minutes = minutes % (24 * 60)
    return f"{minutes // 60:02}:{minutes % 60:02}"

def add_minutes(t, delta):
    return to_time(to_minutes(t) + delta)
