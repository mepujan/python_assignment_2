# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(data_list,start,end,search_data):
    if start > end:
        return -1
    else:
        mid_value = (start + end ) // 2
        if data_list[mid_value] == search_data:
            return mid_value
        elif data_list[mid_value] > search_data:
            return binary_search(data_list,start,mid_value-1,search_data)
        else:
            return binary_search(data_list,mid_value+1,end,search_data)



data=[4,5,7,8,9,20,18,30]
search_data = 4
sorted_data=sorted(data)
print('sorted data = ', sorted_data)
index= binary_search(sorted_data,0,len(data)-1,search_data)
if index == -1:
    print('Element is not found')
else:
    print("Element is found at index : ",index)


