def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j=i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1],arr[j]=arr[j],arr[j - 1]
            j -= 1
    return arr

inp_arr = (input('enter the elements to be sorted:'))
arr = list(map(int,inp_arr.split()))
print(insertion_sort(arr))