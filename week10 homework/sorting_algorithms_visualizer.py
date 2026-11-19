#Imported libaries 
import sounddevice as sd
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np 
from arrtrack import ArrTrack,ArrTrackForPivots

def sort_me():
    n = 100
    arr = np.arange(1,n+1)
    np.random.shuffle(arr)

    return arr 

#Bubble sort algorithm with tracked arrayacesses and comparisons
def bubblesort(arr):

    swapped = True
    while swapped == True:
        swapped = False 
        for i in range(len(arr.arr)-1):
            if arr.greater(i,arr.arr[i+1]):
                t = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = t 
                swapped = True


#Selection sort algorithm with tracked arrayacesses and comparisons
def selection_sort(arr):

    highestIndex = len(arr)-1
    insertIndex = 0 
    
    while insertIndex < highestIndex:
        minPosition = insertIndex 
        for i in range(insertIndex+1,highestIndex+1):
            if arr.less(i,arr.arr[minPosition]):
                minPosition = i

        c = arr[minPosition]
        arr[minPosition] = arr[insertIndex]
        arr[insertIndex] = c

        insertIndex = insertIndex + 1


#Quick sort algorithm with tracked arrayacesses and comparisons
def parition(arr, low, high):
    
    pivot = arr.p(low)

    i = low
    j = high

    while True:

        while arr.less(i,pivot):
            i += 1
            
        while arr.greater(j,pivot):
            j -= 1 
        
        if i >= j:
            return j
        
        c = arr[i]
        arr[i] = arr[j]
        arr[j] = c

        i += 1
        j -= 1 
        
def quicksort(arr, low, high):

    if low < high:
        p = parition(arr, low, high)
        quicksort(arr, low, p)
        quicksort(arr, p+1, high)




#Choice & value interchange
def cls(choice,arr):
    if choice == 1:
        arr = ArrTrack(arr)
        bubblesort(arr)
        return  arr,"bubble sort"
    elif choice == 2:
        arr = ArrTrack(arr)
        selection_sort(arr)
        return arr,"selection sort"
    elif choice == 3:
        arr = ArrTrackForPivots(arr)
        quicksort(arr,0,len(arr)-1)
        return arr,"quick sort"
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



def launcher(arr):
    menu_ui()
    choice = selection()
    return cls(choice,arr)


#Graph & Animations 
def graph(arr,name):
    fig, ax = plt.subplots(figsize=(20,10))
    bars = plt.bar(np.arange(0,len(arr)),arr.arr, width=0.8)
    ax.set_title(f"VISUALIZING {name}")
    fig.suptitle("SORTING VISUALIZER", fontsize = 18)
    txt = ax.text(0,100,"")
    array = ax.text(30,100,"")
    comp = ax.text(60,100,"")
    
    return bars,fig,txt,array,comp 

def animations(arr,bars,fig,txt,array,comp):

    fps = 360

    def update(frames):
        txt.set_text(f"FRAMES = {frames}")
        array.set_text(f"ARRAYACESSED = {arr.arrayAccesses[frames]}")
        comp.set_text(f"COMPARISONS = {arr.comparisons[frames]}")
        
        for bar,height in zip(bars,arr.snapshots[frames]):
            bar.set_height(height)
            bar.set_color("#38BDF8")
    
        idx_a = arr.write[frames]
        if idx_a is not None:
            bars[idx_a].set_color("#EC4899")
           

        idx_b = arr.access[frames]
        if idx_b is not None:
            bars[idx_b].set_color("#F59E0B")
        
        if isinstance(arr, ArrTrackForPivots):
            idx_c = arr.pivot[frames]
            if idx_c is not None:
                bars[idx_c].set_color("#22C55E")
        
        return (*bars,txt,array,comp)
        
    ani = FuncAnimation(
        fig,
        update,
        frames=range(len(arr.snapshots)),
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
        arr,name = launcher(arr)
        bars,fig,txt,array,comp = graph(arr,name.upper())
        animations(arr,bars,fig,txt,array,comp)



main()