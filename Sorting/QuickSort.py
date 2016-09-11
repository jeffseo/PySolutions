def swap(array,index1,index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

# This function takes last element as pivot, places the pivot element
# at its correct position in sorted array, and places all smaller to
# the left of pivot and all greater elements to the right
def partition(array,start_index,end_index):
    i = start_index # Index of partition index
    pivot = array[end_index] # pivot

    for j in range(start_index,end_index):
        # if current element is smaller than or equal to pivot
        if array[j] <= pivot:
            swap(array,i,j)
            i += 1  # increment index of smaller element

    swap(array,i,end_index)
    return (i)

# main function that implements quicksort
def quickSort(array,start_index,end_index):
    if start_index < end_index:
        # partition_index indicates that array[partition_index] is now
        # at correct position in sorted array
        partition_index = partition(array,start_index,end_index)

        # seperately sort elements before partition and after partition
        quickSort(array,start_index,partition_index-1)
        quickSort(array,partition_index+1,end_index)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),