import timeit
arr = []
print("enter the size of the array : ")
n = int(input())
print("enter "+str(n)+" numbers: ")
for i in range(n):
    arr.append(int(input()))
def selectionsort(arr):
        for i in range(n-1):
           chk = 0
           small = arr[i]
           for j in range(i+1,n):
               if small > arr[j]:
                  small = arr[j]
                  chk=chk+1
                  index=j
        if chk!=0:
            temp = arr[i]
            arr[i] = small
            arr[index] = temp
        return arr
arr = selectionsort(arr)

execution_time = timeit.timeit(stmt=lambda: selectionsort(arr.copy()), number=1)

print("\nsorted list : ")
for i in range(n):
    print(arr[i])
print("execution time : {:.6f} milliseconds".format(execution_time*1000))
