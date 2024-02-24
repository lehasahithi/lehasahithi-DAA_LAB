import timeit
arr = []
print("enter the size of the array : ")
n = int(input())
print("enter "+str(n)+" numbers: ")
for i in range(n):
    arr.insert(i, int(input()))

def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
arr = bubblesort(arr)


execution_time = timeit.timeit(stmt=lambda: bubblesort(arr.copy()), number=1)

print("the sorted array : ")
for i in range(n):
    print(arr[i])


print("execution time : {:.6f} milliseconds".format(execution_time*1000))
