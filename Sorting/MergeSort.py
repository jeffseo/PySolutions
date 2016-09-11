def merge(array,left_index,middle_index,right_index):
    # determine size of each sub array
    n1 = middle_index - left_index + 1
    n2 = right_index - middle_index

    # create temp arrays
    left_array = [0] * n1
    right_array = [0] * n2

    # copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        left_array[i] = array[left_index + i]

    for j in range(0, n2):
        right_array[j] = array[middle_index + 1 + j]

    # merge the temp arrays back into array
    i = 0 # initial index of first subarray
    j = 0 # initial index of second subarray
    k = left_index # initial index of merged subarray

    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # copy remaining elements of left sub array 
    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1

    # copy remaining elements of right sub array 
    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1

def mergeSort(array,left_index,right_index):
    if left_index < right_index:
        middle_index = (left_index + right_index) / 2
        mergeSort(array, left_index, middle_index)
        mergeSort(array, middle_index + 1, right_index)
        merge(array, left_index, middle_index, right_index)

if __name__ == '__main__':
    # Driver code to test above
    array = [12, 11, 13, 5, 6, 7]
    n = len(array)
    print ("Given array is")
    for i in range(n):
        print ("%d" %array[i]),
     
    mergeSort(array,0,n-1)
    print ("\n\nSorted array is")
    for i in range(n):
        print ("%d" %array[i]),