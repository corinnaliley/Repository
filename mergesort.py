def merge_sort(arr):
    """
    Sorts an array in ascending order using the merge sort algorithm.
    
    Args:
        arr (list): List of elements to be sorted.
        
    Returns:
        None: The list is sorted in place.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Check if any element was left in the left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Check if any element was left in the right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def plot_list(data, title):
    x = range(len(data))
    plt.bar(x, data, color='skyblue')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    # Plot before sorting
    plot_list(my_list, 'List Before Sorting')

    # Sort the list
    merge_sort(my_list)

    # Plot after sorting
    plot_list(my_list, 'List After Sorting')