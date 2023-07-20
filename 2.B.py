def alternate_combine(list1, list2):
    combined_list = []
    min_len = min(len(list1), len(list2))

    for i in range(min_len):
        combined_list.append(list1[i])
        combined_list.append(list2[i])

    # Add any remaining elements from the longer list
    if len(list1) > min_len:
        combined_list.extend(list1[min_len:])
    elif len(list2) > min_len:
        combined_list.extend(list2[min_len:])

    return combined_list

# Test the function
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
combined_result = alternate_combine(list1, list2)
print(combined_result)  # Output: ['a', 1, 'b', 2, 'c', 3]
