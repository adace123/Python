def bubbleSort(lst):
    for j in range(len(lst)):
        for k in range(j+1,len(lst)):
            if lst[k]<lst[j]:
                lst[j],lst[k] = lst[k],lst[j]
    return lst

sortlist = input("Enter 10 numbers: ")
templist2 = sortlist.split()
sortednumbers = [eval(x) for x in templist2]
print("The sorted numbers are:",bubbleSort(sortednumbers))
