"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import Iterable


# return list
def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if not isinstance(ele, str) and isinstance(ele, Iterable):
            flatten(ele, output_arr)    #tail-recursion
        else:
            output_arr.append(ele)      #produce the result
    return output_arr


# returns iterator
def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if not isinstance(element, str) and isinstance(element, Iterable):
            yield from flatten_iter(element)    
        else:
            yield element


# without recursion
def flatten_used_stack(iterable):
    stack = [iterable]
    output_arr = []

    while stack:
        itr = stack.pop()
        if not isinstance(itr, list):
            output_arr.append(itr)
            continue

        for idx in range(len(itr)):
            if isinstance(itr[idx], list):
                stack.append(itr[idx + 1:])
                stack.append(itr[idx])
                break
            output_arr.append(itr[idx])

    return output_arr
