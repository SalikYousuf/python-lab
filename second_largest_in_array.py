arr = list(map(int,input("enter numbers that are seperated : ").split()))

arr = list(set(arr))

if len(arr)<2:
    print("array size should be greater than 2.")
else:
    arr.sort()
    print(f"\nsecond largest number in the given array is:  {arr[-2]}")


