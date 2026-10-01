import os 
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, MultipleLocator

BASE_DIR = Path(__file__).resolve().parent 
STOCK_FILE = BASE_DIR/"grades.txt"

#utilities 
def get_grades():
    grades = []
    with open(STOCK_FILE,"r") as f:
        for line in f:
            if not line.strip():
                continue
            individual_grades = [int(i) for i in line.strip().split(',')]
            grades.append(individual_grades)
        return grades

def write_grades(grades):
    with open(STOCK_FILE, "w") as f:
        for grade in grades: 
            f.write(",".join(str(g) for g in grade))
            f.write("\n")

#menu
def menu_interface(grades):

    alert("💯 Welcome to CompSci the Student Grade Management System 💯")

    interface_choice = [
        "1. View All Individual Grades",
        "2. Add Individual Grades",
        "3. Individual Analyses",
        "4. Global Analyses",
        "5. Graph Averages",
        "Please select an option:"
    ]
    for range in interface_choice:
        print(range)
        print("\n")

def menu_choice():
    return input('')
    
def options(grades,choices):
    if choices == "1":
        os.system("clear")
        viewAll(grades)
    elif choices == "2":
        os.system("clear")
        add_individual_grades(grades)
    elif choices == "3":
        os.system("clear")
        individual_analyses(grades)
    elif choices == "4":
        os.system("clear")
        global_analyses(grades)
    elif choices == "5":
        os.system("clear")
        graph(grades)
    else:
        inavlid = input("Invaid input Please Try again(press any key to proceed):")

def menu(grades):
    while True:
        os.system("clear")
        menu_interface(grades)
        choices = menu_choice()
        options(grades,choices)

def proceed():
    alert(f"Proceed?")
    input()

def alert(x):
    print("-"*len(x))
    print(x)
    print("-"*len(x))
  

#Statistical analyses
def mean_cal(num):
    sum = 0
    for i in num:
        sum += i
    return sum/len(num)
        
def global_mean_cal(num):
    counter = 0
    sum = 0 
    for a in num:
        for b in a:
            sum += b
            counter += 1 
    return sum/counter

def mean(grades,t=None):
    mean = []
    if t == 1:
        for i in grades:
            mean.append(round(mean_cal(i)))
        return mean 
    else:
        return round(global_mean_cal(grades))

def bubblesort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i] 
                swapped = True
    return list

def break_all(grades):
    medlist = []
    for a in grades:
        for b in a:
            medlist.append(b)
    return medlist

def prep_global_med_cal(grades):
    grades = break_all(grades)
    grades = bubblesort(grades)
    return grades

def med_cal(grades):
    if len(grades) % 2 == 0:
        m1 = grades[int((len(grades)/2)-1)]
        m2 = grades[int((len(grades)/2))]
        return (m1+m2)/2
    else:
        return int((len(grades)+1)/2-1)

def med_global(grades):
    grades = prep_global_med_cal(grades)
    return med_cal(grades)

def med_individual(grades):
    individual_med = []
    for a in grades:
        a = bubblesort(a)
        individual_med.append(med_cal(a))
    return individual_med

def mod_cal(grades):
    mode = []
    highest = 0 
    for grade in grades:
        count = grades.count(grade)
        if count > highest:
            highest = count 
            modes = [grade]
        elif count == highest and grade not in modes:
            modes.append(grade)
    return modes

def mod_global(grades):
    grades = break_all(grades)
    return mod_cal(grades)

def mod_individual(grades):
    individual_mod = []
    for i in grades:
        individual_mod.append(mod_cal(i))
    return individual_mod

#min,max 
def max_Cal(max,i):
    if max < i:
        max = i
    return max 

def min_Cal(min,i):
    if min > i:
        min = i
    return min

#individual min,max
def get_individual_max(grades):
    max = grades[0]
    for i in grades:
        max = max_Cal(max,i)
    return max

def maximun(grades):
    max = []
    for i in grades:
        max.append(round(get_individual_max(i)))
    return max 
 
def get_individual_min(grades):
    min = grades[0]
    for i in grades:
        min = min_Cal(min,i)
    return min

def minimun(grades):
    min = []
    for i in grades:
        min.append(round(get_individual_min(i)))
    return min 
 
#global min,max
def get_global_max(grades):
    max = grades[0][0]
    for a in grades:
        for b in a:
            max = max_Cal(max,b)
    return max 

def get_global_min(grades):
    min = grades[0][0]
    for a in grades:
        for b in a:
            min = min_Cal(min,b)
    return min

#Core Functions
def viewAll(grades):
    counter = 1
    for grade in grades:
        print(f"student{counter}: {grade}")
        counter += 1
    proceed()

def add_individual_grades(grades):
    try:
        individual_grades = [int(i) for i in input("Please input a grade or grades seperated by(','):").strip().split(',')]
        individual_grades = bubblesort(individual_grades)
        grades.append(individual_grades)
        write_grades(grades)
    except:
        ValueError
        alert("Error Please Input a Number")
    finally:
        alert("Done")
        proceed()

def set_Xaxis():
    plt.xlabel("Grades")
    gradeScale = [0,10,20,30,40,50,60,70,80,90,100]
    plt.xticks(gradeScale)

def set_Yaxis():
    plt.ylabel("Number of Students")
    plt.rcParams["axes.autolimit_mode"] = "round_numbers"
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

def get_cordinates(average):
    cordinates = []
    avFreq = []
    for i in average: 
        freq = average.count(i)
        cordinates.append([i,freq])

    return cordinates

def plot(grades):    
    averages = mean(grades,1)
    cordinates = get_cordinates(averages)
    for a in cordinates:
        x,y = a
        plt.scatter(x,y)
    return cordinates

def graph(grades=None):
    plt.title("Student Grade Distrubution Scatter Plot")
    set_Xaxis()
    set_Yaxis()
    plot(grades)
    plt.ylim(bottom=0)
    plt.show()
    plt.close()

def individual_analyses(grades):
    average = mean(grades,1)
    median = med_individual(grades)
    mode = mod_individual(grades)
    max = maximun(grades)
    min = minimun(grades)
    for a,b,c,d,e,f in zip(range(1,len(average)+1),average,median,mode,max,min):
        alert(f"Student {a} |mean: {b} |med:{c} |mode:{d} | max:{e} |min: {f}")
    proceed()

def global_analyses(grades):
    average = mean(grades,2)
    median = med_global(grades)
    mode = mod_global(grades)
    max = get_global_max(grades)
    min = get_global_min(grades)
    alert(f"Average Student Score: {average} | Med Score: {median} | Mode Score: {mode}| Highest Score: {max}| Lowest Score: {min}")
    proceed()

#main
def main():
    grades = get_grades()
    menu(grades)

main()

