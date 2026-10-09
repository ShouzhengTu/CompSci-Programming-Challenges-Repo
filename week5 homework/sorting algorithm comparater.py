import time as t
import os 

def set_sort_me():
    sort_me = [4323, 8101, 802, 4965, 7758, 302, 3853, 3655, 26, 9653, 7809, 8807, 1664, 4512, 2461, 5402, 9638
    ]

    return sort_me

def bubble_sort(list):
    arrayAcess = 0 
    comparisons = 0 
    swapped = True
    while swapped == True:
        swapped = False 
        for i in range(len(list)-1):
            arrayAcess += 1 
            comparisons += 1 
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                swapped = True
    return arrayAcess, comparisons
    


def selection_sort(list):
    arrayAcess = 0 
    comparisons = 0 
    highestIndex = len(list)-1
    insertIndex = 0 
    while insertIndex < highestIndex:
        minPosition = insertIndex 
        for i in range(insertIndex,highestIndex+1):
            arrayAcess += 2
            comparisons += 1 
            if list[i] < list[minPosition]:
                minPosition = i
        c = list[minPosition]
        list[minPosition] = list[insertIndex]
        list[insertIndex] = c
        arrayAcess += 3
        insertIndex = insertIndex + 1
    return arrayAcess,comparisons



def parition(sort_me, low, high):
    arrayAcess = 0 
    comparisons = 0
    arrayAcess += 1
    pivot = sort_me[low]
    i = low
    j = high-1


    while True:
        comparisons += 1 
        arrayAcess += 1
        while sort_me[i] < pivot:
            i += 1

        comparisons += 1 
        arrayAcess += 1
        while sort_me[j] > pivot:
            j -= 1 
        
        if i >= j:
            return j, arrayAcess, comparisons
        
        arrayAcess += 4
        c = sort_me[i]
        sort_me[i] = sort_me[j]
        sort_me[j] = c 
        

def quicksort(sort_me, low, high):
    totalComparisons = 0 
    totalArrayAcess = 0
    
    if low < high:
        p,arrayAcess,comparisons = parition(sort_me, low, high)
        totalArrayAcess += arrayAcess
        totalComparisons += comparisons
        quicksort(sort_me, low, p)
        quicksort(sort_me, p+1, high)

    return totalComparisons,totalArrayAcess

def alert(text):
    print("-"*len(text))
    print(text)
    print("-"*len(text))

def run_bubble(sort_me):
    arrayAcess, comparisons = bubble_sort(sort_me)
    out = output(sort_me, arrayAcess, comparisons)
    proceed()
    return out 

def run_selection(sort_me):
    arrayAcess, comparisons = selection_sort(sort_me)
    out = output(sort_me, arrayAcess, comparisons)
    proceed()
    return out 

def run_quicksort(sort_me):
    arrayAcess, comparisons = quicksort(sort_me,0,len(sort_me)-1)
    out = output(sort_me, arrayAcess, comparisons)
    proceed()
    return out 

def proceed():
    alert("Press Any Key to Continue")
    input()
    os.system("clear")

def output(sort_me,arrayAcess,comparisons):
    print(sort_me)
    out = f"SORT COMPLETED| ARRAY ACESS: {arrayAcess}| Comparisons {comparisons} "
    alert(out)
    return out 

def out_summary(summary):

    for i in summary:
        print(i)

def main():
    sorting_algorithm = [run_bubble,run_selection,run_quicksort]
    summary = []
    for i in sorting_algorithm:
        os.system("clear")
        sort_me = set_sort_me()
        out = i(sort_me) 
        summary.append(out)
    out_summary(summary)

main()  