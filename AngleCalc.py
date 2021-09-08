class AngleCalc:
    def boundTo180(self, angle):
        """
        :param angle: angle Input angle in degrees.
        :return: The bounded angle in degrees.
        """
        while angle <= -180:
            angle += 360
        while angle > 180:
            angle -= 360
        return angle


    def isAngleBetween(self, first_angle, middle_angle, second_angle):
        """
        :param first_angle:
        :param middle_angle:
        :param second_angle:
        :return:
        """
        if first_angle < 0:
            first_angle += 360
        if middle_angle < 0:
            middle_angle += 360
        if second_angle < 0:
            second_angle += 360
        return first_angle < middle_angle < second_angle or second_angle < middle_angle < first_angle and \
               (abs(first_angle - middle_angle) < 90 or abs(second_angle - middle_angle) < 90)
