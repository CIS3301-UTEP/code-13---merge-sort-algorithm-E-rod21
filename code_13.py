def get_merge_sorted_list(unsorted_list):

    list_length = len(unsorted_list)
    if list_length == 1:
        return unsorted_list
    
    mid_point = list_length //  2 

    left = get_merge_sorted_list(unsorted_list[:mid_point])
    right = get_merge_sorted_list(unsorted_list[mid_point:])
    return merge(left, right )

def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output 

if __name__ == "__main__":
    usorted_list = [1,5,7,3,4,9,8,2]
    print(usorted_list)
    sorted_list = get_merge_sorted_list(usorted_list)
    print(sorted_list)