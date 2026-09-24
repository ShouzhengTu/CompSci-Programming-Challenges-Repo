import os 
from pathlib import Path


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

def median(grades):
    length = len(grades)
    if length % 2 == 0:
        m1 = int(grades[(len(grades)/2)-1])
        m2 = int(grades[(len(grades)/2)])
        med = (m1+m2)/2
        return med 
    else:
        index = int((len(grades)+1)/2-1)
        med = grades[index]
        return med

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
        individual_grades = [int(i) for i in input("Please input a grade:").strip().split(',')]
        grades.append(individual_grades)
        write_grades(grades)
    except:
        ValueError
        alert("Error Please Input a Number")
    finally:
        alert("Done")
        proceed()

def individual_analyses(grades):
    average = mean(grades,1)
    max = maximun(grades)
    min = minimun(grades)
    for a,b,c,d in zip(range(1,len(average)+1),average,max,min,):
        alert(f"Student {a} |mean: {b} | max:{c}| min: {d}")
    proceed()

def global_analyses(grades):
    average = mean(grades,2)
    max = get_global_max(grades)
    min = get_global_min(grades)
    alert(f"Average Student Score: {average} | Highest Score: {max}| Lowest Score: {min}")
    proceed()

#main
def main():
    grades = get_grades()
    menu(grades)

main()


         