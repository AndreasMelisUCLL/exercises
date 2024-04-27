def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2

    # Check if one of interval2's bounds fall inside interval1
    return all([
        # no empty intervals
        left1 <= right1,
        left2 <= right2,
        
        any([
            left1 <= right2 and left2 <= right1,
            left2 <= right1 and left1 <= right2,
        ])
    ])