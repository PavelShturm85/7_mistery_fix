from math import sqrt


def get_roots(a, b, c):
    # a=0 makes the function linear, not quadratic.
    if a == 0:
        return None, None
    else:
        discriminant = b ** 2 - 4 * a * c
        # The square root is extracted only from a nonnegative number.
        if discriminant < 0:
            return None, None
        # If discriminant is 0, then roots of the quadratic equation 1.
        elif discriminant == 0:
            root1 = (-b - sqrt(discriminant)) / (2 * a)
            return root1, None
        # If discriminant > 0, then roots of the quadratic equation 2.
        else:
            root1 = (-b - sqrt(discriminant)) / (2 * a)
            root2 = (-b + sqrt(discriminant)) / (2 * a)
            return root1, root2
