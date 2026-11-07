#Imported libaries 

import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np 


#Array Generation 
def sort_me():
    n = 100
    arr = np.arange(1,n+1)
    np.random.shuffle(arr)
    return arr


#Bubble sort algorithm with tracked arrayacesses and comparisons
def bubblesort(arr):
    arrayAcess = 0 
    comparison = 0 
    arrtrack = {
        "Array Acesses":[0], 
        "comparisons": [0],
        "pivot":[None],  
        "write":[None],
        "access":[None],
        "snapshot":[arr.copy()]
    }

    swapped = True
    while swapped == True:
        swapped = False 
        for i in range(len(arr)-1):
            write_index = None
            arrayAcess += 2
            comparison += 1
            if arr[i] > arr[i+1]:
                t = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = t 
                arrayAcess += 4
                swapped = True
                write_index = i+1

            arrtrack = arrtrack_update(arrtrack,i, write_index,arr,arrayAcess,comparison)
        
    return arrtrack

def arrtrack_update(arrtrack,i,write_index,arr,arrayAcess,comparison,pivot_idx=None):

    arrtrack["access"].append(i)
    arrtrack["write"].append(write_index)
    arrtrack["pivot"].append(pivot_idx)
    arrtrack["Array Acesses"].append(arrayAcess)
    arrtrack["comparisons"].append(comparison)
    arrtrack["snapshot"].append(arr.copy())

    return arrtrack



#Selection sort algorithm with tracked arrayacesses and comparisons
def selection_sort(arr):

    arrayAcess = 0 
    comparison = 0 

    arrtrack = {
        "Array Acesses":[0], 
        "comparisons": [0],  
        "pivot":[None],  
        "write":[None],
        "access":[None],
        "snapshot":[arr.copy()]
    }
    
    highestIndex = len(arr)-1
    insertIndex = 0 
    
    while insertIndex < highestIndex:
        minPosition = insertIndex 
        for i in range(insertIndex+1,highestIndex+1):
            arrayAcess += 2 
            comparison += 1
            if arr[i] < arr[minPosition]:
                minPosition = i

            arrtrack = arrtrack_update(
                arrtrack,i,None,arr,arrayAcess,comparison
                )

        c = arr[minPosition]
        arr[minPosition] = arr[insertIndex]
        arr[insertIndex] = c
        arrayAcess += 4
        
        arrtrack = arrtrack_update(
            arrtrack,minPosition,insertIndex,arr,arrayAcess,comparison
            )

        insertIndex = insertIndex + 1

    return arrtrack


#Quick sort algorithm with tracked arrayacesses and comparisons
def parition(arr, low, high,cA,cC):
    
    arrtrack = {
        "Array Acesses":[], 
        "comparisons": [],
        "pivot":[],  
        "write":[],
        "access":[],
        "snapshot":[]
    }
    arrayAcess = cA 
    comparison = cC

    pivot = arr[low]
    arrayAcess += 1
    i = low
    j = high

    while True:

        arrayAcess += 1 
        comparison += 1

        while arr[i] < pivot:
            i += 1
            arrayAcess += 1 
            comparison += 1

            arrtrack_update(arrtrack,i,None,arr,arrayAcess,comparison,low)
        
        arrayAcess += 1 
        comparison += 1

        while arr[j] > pivot:
            j -= 1 
            arrayAcess += 1 
            comparison += 1

            arrtrack_update(arrtrack,j,None,arr,arrayAcess,comparison,low)
        
        if i >= j:
            return j,arrtrack,arrayAcess,comparison
        
        c = arr[i]
        arr[i] = arr[j]
        arr[j] = c

        arrayAcess += 4 

        arrtrack_update(arrtrack,i,j,arr,arrayAcess,comparison,low)

        i += 1
        j -= 1 

        
def quicksort(arr, low, high, t_arrtrack=None, arrayAcess=0, comparison=0):
    
    if t_arrtrack is None:
        t_arrtrack = {
            "Array Acesses":[0], 
            "comparisons": [0],
            "pivot":[0],  
            "write":[None],
            "access":[None],
            "snapshot":[arr.copy()]
        }

    if low < high:
        p,arrtrack,arrayAcess,comparison = parition(arr, low, high, arrayAcess,comparison)

        updates = {
            "Array Acesses": arrtrack["Array Acesses"],
            "comparisons": arrtrack["comparisons"],
            "pivot": arrtrack["pivot"],
            "write": arrtrack["write"],
            "access": arrtrack["access"],
            "snapshot": arrtrack["snapshot"],
        }

        for key, value in updates.items():
            t_arrtrack[key].extend(value)

        t_arrtrack, arrayAcess, comparison = quicksort(
            arr, low, p, t_arrtrack,arrayAcess, comparison
            )

        t_arrtrack, arrayAcess,comparison = quicksort(
            arr, p+1, high, t_arrtrack, arrayAcess,comparison
            )

    return t_arrtrack, arrayAcess, comparison



#Choice & value interchange
def choices_value_interchange(choice,arr):
    if choice == 1:
        return (bubblesort(arr), "bubble sort")
    elif choice == 2:
        return (selection_sort(arr), "selection sort")
    elif choice == 3:
        track, _, _=quicksort(arr,0,len(arr)-1)
        return (track, "quick sort")
    elif choice == 4:
        exit()


# UI & UX setup 
def alert(text):
    print(len(text)*"-")
    print(text)
    print(len(text)*"-")



def menu_ui():
    alert("📶Welcome to the Algorithm Visualiser📶")
    texts = [
        "1. Bubble Sort",
        "2. Selection Sort",
        "3. Quick Sort",
        "4. Exit"
        ]
    for text in texts:
        print(text+"\n")
    alert("Please select the algorithm you want to visualize")



def selection():
    choice = int(input())
    return choice



def proceed():
    alert(f"Proceed?")
    input()



def menu(arr):
    menu_ui()
    choice = selection()
    return choices_value_interchange(choice,arr)


#Graph & Animations 
def graph(arr,name):
    fig, ax = plt.subplots(figsize=(20,10))
    bars = plt.bar(np.arange(0,len(arr)),arr, width=0.8)
    ax.set_title(f"VISUALIZING {name}")
    fig.suptitle("SORTING VISUALIZER", fontsize = 18)
    txt = ax.text(0,100,"")
    array = ax.text(30,100,"")
    comp = ax.text(60,100,"")
    
    return bars,fig,txt,array,comp 



def animations(bars,fig,txt,array,comp,arrtrack):

    fps = 60

    def update(frames):
        txt.set_text(f"FRAMES = {frames}")
        array.set_text(f"ARRAYACESSED = {arrtrack["Array Acesses"][frames]}")
        comp.set_text(f"COMPARISONS = {arrtrack["comparisons"][frames]}")
        
        for bar,height in zip(bars,arrtrack["snapshot"][frames]):
            bar.set_height(height)
            bar.set_color("#38BDF8")
        
        idx_a = arrtrack["write"][frames]
        if idx_a is not None:
            bars[idx_a].set_color("#EC4899")

        idx_b = arrtrack["access"][frames]
        if idx_b is not None:
            bars[idx_b].set_color("#F59E0B")

        idx_c = arrtrack["pivot"][frames]
        if idx_c is not None:
            bars[idx_c].set_color("#22C55E")
        
        return (*bars,txt,array,comp)
        
    ani = FuncAnimation(
        fig,
        update,
        frames=range(len(arrtrack["snapshot"])),
        interval=1000/fps,
        blit=True,
        repeat=False
    )

    plt.show()
    plt.close()



def main():
    while True:
        os.system("clear")
        arr = sort_me()
        arrtrack,name = menu(arr)
        bars,fig,txt,array,comp = graph(arr,name.upper())
        animations(bars,fig,txt,array,comp,arrtrack)



main()
