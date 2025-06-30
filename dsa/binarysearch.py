def BinarySearch(Arr,Target,Pivot=0):
    if(len(Arr)==0):
        print("Array does not exist")
    else:
        Mid=len(Arr)//2
        if Target==Arr[Mid]:
            print(f"Element Found at{Mid+Pivot} index")
        else:
            if(Target<Arr[Mid]):
                return BinarySearch(Arr[:Mid],Target,Pivot)
            elif(Target>Arr[Mid]):
                return BinarySearch(Arr[Mid+1:],Target,Pivot+Mid)
            else:
                print("Element does not exist")
Ouput=BinarySearch([1,2,3,4,5],4)