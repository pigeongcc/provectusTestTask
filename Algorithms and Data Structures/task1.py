# my optimised solution uses dictionaries
#
# I use lists entries as keys, and counters for each list entry as values
# dict2 additionally contains all the keys of dict1, with 0 values if there are no such entries in list2
# the answer is sum of products of dict values with the same keys
#
# it takes linear time O(n) to complete

def count_connections(list1: list, list2: list) -> int:
    count = 0
    dict1 = {}
    dict2 = {}
    
    # initializing dictionaries

    for i in list1:                         # O(list1_size)
        dict1.setdefault(i, 0)
        dict2.setdefault(i, 0)

    for i in list2:                         # O(list2_size)
        dict2.setdefault(i, 0)
        
    # counting number of entries for each list value

    for i in list1:                         # O(list1_size)
        dict1[i] += 1

    for i in list2:                         # O(list2_size)
        dict2[i] += 1

    # here we make dict[i] equals to num of connections for i value if there are pairs,
    # or to 0 if there are no connections for i value

    for i in dict1.keys():                  # O(list1_size)
        dict1[i] *= dict2[i]

        count += dict1[i]
  
    return count