find_intersection = lambda list1, list2 : list(set(list1) & set(list2)) 

l1 = [1,2,3,4,5,6,7]
l2 = [3,4,5,6,7,8]
print(find_intersection(l1, l2))