def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [ O(n+(n+1)) OR O(n) ]


    """

    if len(s1) != len(s2): # O(1)
        return False

    for i in range(len(s1)): # O(n)
        if s1[i] != s2[i]: # O(1)
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [  O(2n) or O(n)  ]

    """

    if "hippo" in animals or "platpypus" in animals: # list, so n + n 
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [  O(n+3) or O(n) ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers) # O(n)

    for x in s: # O(1)
        if -x in s: # O(1)
            result.append([-x, x]) # O(1)

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [  O(n(n+2)^2)  or O(n^2)  ]

    """

    result = []

    for x in numbers: # O(n)
        for y in numbers: # O(n)
            if x == -y: # O(1)
                result.append((x, y)) # O(1)
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [ O(n((n+2)+1)) or  O(n^2) ]

    """

    result = []

    for x in numbers: # O(n)
        for y in numbers: # O(n)
            if x == -y and (y, x) not in result: # O(1+1) 
                result.append((x, y)) # O(1)
    return result
