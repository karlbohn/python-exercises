def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    last_num = len(lst)
    last_idx = last_num - 1
    if last_num == 0: print('None')
    else: print(lst[last_idx])