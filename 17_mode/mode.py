def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    hi_count = 0
    for item in nums:
        if nums.count(item) > hi_count:
            hi_count = item
            hi_num = item
    return hi_num
        
        
