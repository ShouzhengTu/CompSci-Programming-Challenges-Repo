import time as t
import os
from tracemalloc import Snapshot
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random as r 
import numpy as np 

def sort_me():
    n = 100
    arr = np.round(np.linspace(0,1000,n), 0)
    np.random.shuffle(arr)
    return arr

def bubblesort(arr):
    snapshot = [arr.copy()]
    swapped = True
    while swapped == True:
        swapped = False 
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
                snapshot.append(arr.copy())
    return snapshot

def selection_sort(arr):
    snapshot = [arr.copy()]
    highestIndex = len(arr)-1
    insertIndex = 0 
    while insertIndex < highestIndex:
        minPosition = insertIndex 
        for i in range(insertIndex,highestIndex+1):
            if arr[i] < arr[minPosition]:
                minPosition = i
        c = arr[minPosition]
        arr[minPosition] = arr[insertIndex]
        arr[insertIndex] = c
        snapshot.append(arr.copy())
        insertIndex = insertIndex + 1
    return snapshot

def parition(arr, low, high):
    snapshot = [arr.copy()]
    pivot = arr[low]
    i = low
    j = high

    while True:

        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1 
        
        if i >= j:
            return j, snapshot
        
        c = arr[i]
        arr[i] = arr[j]
        arr[j] = c 
        snapshot.append(arr.copy())
        
def quicksort(sort_me, low, high):
    total_snapshots = []
    if low < high:
        p,snapshot = parition(sort_me, low, high)
        for snap in snapshot:
            total_snapshots.append(snap)
        total_snapshots.extend(quicksort(sort_me, low, p))
        total_snapshots.extend(quicksort(sort_me, p+1, high))
    return total_snapshots



def alert(text):
    print(len(text)*"-")
    print(text)
    print(len(text)*"-")

def choices(choice,arr):
    if choice == 1:
        snapshot = bubblesort(arr)
        return snapshot, "bubble sort"
    elif choice == 2:
        snapshot = selection_sort(arr)
        return snapshot, "selection sort"
    elif choice == 3:
        snapshot = quicksort(arr,0,len(arr)-1)
        return snapshot, "quick sort"
    elif choice == 4:
        exit()

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
    snapshot = choices(choice,arr)
    return snapshot

def graph(arr,name):
    fig, ax = plt.subplots()
    bars = plt.bar(np.arange(0,len(arr)),arr)
    ax.set_title(f"VISUALIZING {name}")
    fig.suptitle("SORTING VISUALIZER", fontsize = 18)
    txt = ax.text(0,1000,"")
    return bars,fig,ax,txt

def animations(snapshot,bars,fig,ax,txt):

    fps = 120

    def update(frames):
        txt.set_text(f"ARRAYACESSED = {frames}")
        for bar,height in zip(bars,snapshot[frames]):
            bar.set_height(height)
        return (*bars,txt)
        
    ani = FuncAnimation(
        fig,
        update,
        frames=range(len(snapshot)),
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
        snapshot,name = menu(arr)
        bars,fig,ax,txt = graph(arr,name.upper())
        animations(snapshot,bars,fig,ax,txt)
        
main()