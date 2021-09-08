def boundTo180(angle):
    """
    :param angle: angle Input angle in degrees.
    :return: The bounded angle in degrees.
    """
    while angle <= -180:
        angle += 360
    while angle > 180:
        angle -= 360
    return angle


def isAngleBetween(first_angle, middle_angle, second_angle):
    if (first_angle > 180) or (middle_angle > 180) or second_angle > 180:
        return False
    elif first_angle <= middle_angle <= second_angle:
        return True
    elif second_angle <= middle_angle <= first_angle:
        return True
    else:
        return False

# Test
