arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 18, 26, 33, 43, 48]

low = 0
high = len(arr)
target = int(input("Enter target element: "))
index = None

while low < high:
    mid = (low + high) // 2

    if arr[mid] == target:
        index = mid
        break

    elif arr[mid] > target:
        high = mid

    else:
        low = mid + 1

if index:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found in list")
