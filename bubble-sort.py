def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


inp_arr = (input('enter the elements to be sorted:'))
arr = list(map(int,inp_arr.split()))
print(bubble_sort(arr))

