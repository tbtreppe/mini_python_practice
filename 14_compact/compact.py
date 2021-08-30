def compact(lst):
    List1 = []
    for i in lst:
        if(bool(i)):
            lst.append(i)
    return lst
compact([0, 1, 2, '', [], False, (), None, 'All done'])
"""Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
"""