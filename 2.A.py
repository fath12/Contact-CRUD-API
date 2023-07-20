def merge_lists(list1, list2):
    merged_list = list1.copy()
    merged_list.extend(list2)
    return merged_list

# Test the function
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
merged_result = merge_lists(list1, list2)
print(merged_result)  # Output: ['a', 'b', 'c', 1, 2, 3]
