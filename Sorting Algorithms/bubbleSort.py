
def sortData(data):
    print("Before bubble sort:")
    print(data)
    
    arraylen = len(data)
    for i in range(arraylen):
        for j in range(0,arraylen-i-1):
            if data[j]>data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    
    return data
    


inputArray = [9,1,8,2,7,3,6,0,4,5,3,2,9,0,1,7]
sortedArray = sortData(inputArray)
print("After bubble sort:")
print(sortedArray)