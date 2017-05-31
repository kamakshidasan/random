import math
import sys
import numpy as np

"""
Maximum points visible from camera for a given field of view.

Basic Idea:
        This is a sweep-line algorithm, which sweeps in a counter-clockwise direction
        along the angles subtended by each point with that of the origin and counts
        the number of points within its left limit

Running time Complexity:
        - We first iterate across all points to find the angles subtended = O(n)
        - We then sort the points in ascending order = O(n log n)
        - For each distinct point [~O(n)], we perform a modified binary search
          for its lower limit [O(log n)] = O(n log n)

        - Adding all of the above = O(n) + O(n log n) + O(n log n)
                                  ~ O(n log n)

Compilation:

        $ python code_supritha.py

"""


def find_index(data, value):
    """Search for smallest value greater than or equal to a value and return its index
        Args:
            param1 (float []): Array of angles
            param2 (float): Value of angle being searched

        Returns:
            int: index of smallest value greater than or equal to value being searched

        """
    # If the value is greater than the maximum value of the array, return the first position
    if value > data[- 1]:
        return 0
    else:
        # Finds the left and right closer values
        right_side = np.searchsorted(data, value, side='right')
        left_side = np.searchsorted(data, value, side='left')
        # If the value is present in the array
        if right_side != left_side:
            return left_side
        else:
            # Return next greater value
            return np.searchsorted(data, data[right_side], side='left')


def max_points(fov_angle, points):
    """ Returns the maximum number of points for a field of view.

        The function finds the angle of the line each point makes
        with origin.

        Args:
                   param1 (float): Field of View angle
                   param2 (float []): array of points

           Returns:
                   int: The maximum number of points visible within a Field of View angle

        """
    # An array for storing the angle of each point
    angles = []
    # Iterate across all the coordinates
    for x, y in points:
        # Find the angle a point makes with the origin in degrees
        angles.append(math.degrees(math.atan2(float(y), float(x))))
    # The angles can also be negative; Normalize them to [0, 360] range
    angles = [angle % 360 for angle in angles]
    # Sort the angles - The order does not matter any more!

    angles.sort()
    angles = np.asarray(angles)

    # A variable to store maximum number of points within FOV
    maximum_points = 0
    # Iterate from the end of the array till the start
    for index in range(len(angles) - 1, -1, -1):
        # Check if current angle and previous angle are the same
        # If not, then the previous angle changes
        # In a sorted array where duplicates can be present,
        # angles[index-1] will give the position of the last duplicate value
        if (abs(angles[index] - angles[index - 1]) > sys.float_info.epsilon):
            # Find the maximum range to the left of the point
            difference = angles[index - 1] - fov_angle
            # Since we are cycling through the array, this difference can be negative
            # Again, normalize the angle to a [0,360] range
            new_angle = difference % 360
            # We just have two cases now -
            # One in which the lower end of FOV is to left of the point and the
            # other one for which it is on the right
            # For the case where its on the left, find the difference between the indices
            # For the other one, we have to count by cycling over out array

            first_index = find_index(angles, new_angle)
            # Case where you have to cycle over the array [Take care for first index also]
            if ((difference < 0) or (index == 0)):
                # Number of elements between the current point and its FOV sweep
                value = index - first_index
                # If a roll-around is present
                if first_index != 0:
                    value += len(angles)
                # Simpler Case: Count all the elements to the left of the point till possible
            else:
                value = index - first_index
                # Store the maximum value
            maximum_points = max(maximum_points, value)
    return maximum_points


def main():
    test_points = [(1, 1), (2, 1), (1, 2), (4, 0), (1, -2), (-2, -1), (-2, 1), (-1, 1)]

    # Iterate for different fields of view within given range
    for fov in range(0, 180, 45):
        max_pts = max_points(fov, test_points)
        print("Max points for field of view for i = %s is %s" % (fov, max_pts))

if __name__ == "__main__":
    main()
