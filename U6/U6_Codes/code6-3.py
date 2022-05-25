# -*- coding: utf-8 -*-   [    Code 6-3 : Jaccard Similary   V1   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))

#a_list = [2, 44, 12, 6, 77]
# b_list = [2, 54, 13, 15, 55]
a_list = ['dog', 'cat', 'rat']
b_list = ['dog', 'cat', 'mouse']

print(jaccard_similarity(a_list, b_list))

# ~~~    The intersection is ['dog', 'cat']
# ~~~    union is ['dog', 'cat', 'rat', 'mouse]

