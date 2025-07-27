def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if arr[j]< arr[minpos]:
                minpos = j
        arr[i],arr[minpos]=arr[minpos],arr[i]
    return arr


inp_arr = (input('enter the elements to be sorted:'))
arr = list(map(int,inp_arr.split()))
print(selection_sort(arr))

