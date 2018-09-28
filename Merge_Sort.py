#merge_sort is a recursive function that calls merge to return the final sorted list.
def merge(list1, list2):
    new_list=[]
    while len(list1)!=0 and len(list2)!=0:
        if list1[0] < list2[0]:
            new_list.append(list1[0])
            list1.remove(list1[0])
        else:
            new_list.append(list2[0])
            list2.remove(list2[0])

    if len(list1)== 0:
        new_list+= list2
    if len(list2)== 0:
        new_list+= list1
            
    return new_list

def merge_sort(numList):
    mid= len(numList)//2
    left= numList[:mid]
    right= numList[mid:]
    
    if len(numList)==1:
        return numList
    else:
        list1= merge_sort(left)
        list2= merge_sort(right)
        return merge(list1, list2)

#test case
'''
print(merge_sort([12,35,87,26,9,28,7]))
print(merge([12,26, 35, 87], [7,9,28]))
print(merge([12, 35], [26, 87]))
