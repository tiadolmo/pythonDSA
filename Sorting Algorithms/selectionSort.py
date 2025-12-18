def selectionSort(data):
    print("Before selection sort:")
    print(data)

    dataLen = len(data)
    
    for i in range(dataLen):
        minIndex = i
        for j in range(i+1, dataLen):
            if data[j] < data[minIndex]:
                minIndex = j
        if minIndex != i:
            data[i], data[minIndex] = data[minIndex], data[i]
    return data



inputList = [9,1,8,2,7,3,6,4,5,2,9,8,0,3,4,1]
selectionSorted = selectionSort(inputList)
print("After selection sort:")
print(selectionSorted)