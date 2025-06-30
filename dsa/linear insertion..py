def linearsearch(key,arr,len):
    count=0
    for i in range(len):
        if arr[i]==key:
            print(f"element found at index{i}")
            break
    else:
        print(f"element not found")  
res=linearsearch(9,[5,6,2,3,4,1,0,7,8,9],10)        