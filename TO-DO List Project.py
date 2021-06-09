# Bugs
# if readSavedFile function gets 'empty' string in list.txt it will say that the list is empty
# find alternative to enter key pressing of input function

# bookmark
# work on 1st option is partially done. start on 2nd option
# logic is to check if list.txt has any tasks that is if it has empty string then rewrite file and if it doesnt have empty string then append tasks

'''
To-Do List Project suggested by stonedtimelord from Python group 
t.me/c/1111136772/153296

Aim :Create a To-Do list app.
     After running program it should display options such as view to-do list, add new task, edit tasks, exit

Procedure :

Create loading screen after opening the py file with delay using sys library

create menu using print function and create a dictionary with numbers to access particular option

there will be 4 options 

view to-do list: access this option using number 1 in read only format

add new task: access this option using number 2 and once inside ask user to add task with time and date he wants it to be completed
and if he wants to save the task

edit task: access this option using number 3 and show all the list of tasks from view to-do list option but in read and write format
after selectin a particular task, ask if user wants to edit it, change date and time or delete it. when exiting ask if he is sure to
make the change

exit: access this option using number 4 and exit the py file

'''

import os
import time

# define clear function to clear screen when called 
# https://www.geeksforgeeks.org/clear-screen-python/
def clear():

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


# function to create the list.txt
def createSaveFile():
    
    # create the list.txt and write 'empty' string into it
    with open ('list.txt', 'a') as f:
        f.write('empty')    
    


# function to read saved file
def readSavedFile():
    
    # open the list.txt and read its content
    with open ('list.txt', 'r') as f:    
        readData = f.read()
        
        # if file contain 'empty' string, print the message
        if 'empty' in readData:
            print('No tasks added\n')
            
        # else print the file contents
        else:
            print(readData)


## function to create folder to save data of app. only used on fist time of opening app
#def saveFile():

    ## path to new folder to store list.txt
    #saveLocation = r'/home/andrio/Downloads/Not-To-Do List'
    
    ## if the path doesnt exist
    #if not os.path.exists(saveLocation):
        ## create a path
        #os.makedirs(saveLocation)
        ## create the list.txt inside the path
        #createSaveFile()  
    

def viewMenu():
    # function to print menu screen
    print('1. View To-Do List')
    print('2. Add new task')
    print('3. Edit tasks')
    print('4. Exit')
    
    
def viewList():
    while True:
        readSavedFile() 
        userSelectedOptionViewList = input("Press 'q' to exit to Main Menu\n")
        if userSelectedOptionViewList == 'q': 
            exit()
            
    
    
 
def addTask():
    print('adding task')


def editTask():
    print('editing task')


def exitApp():
    exit('Have a Good Day')


## called when running app for first time to create directory and list.txt
#saveFile()

createSaveFile()

# call viewMenu funtion to display the menu
viewMenu()


# dictionary to select options
menuOptions = {
    1 : 'View To-Do List',
    2 : 'Add new task',
    3 : 'Edit tasks',
    4 : 'Exit'
}

# dictionary to call funtion when selected number 
menuOptionsFuncions = {
    1 : viewList,
    2 : addTask,
    3 : editTask,
    4 : exitApp,
}



# asking user to select option and store it in a variable
userSelectedOption = int(input('Select your option: '))

# iterate through the dictionary keys to print corresponding option
for num in menuOptions.keys():
    
    # if the number selected by user match the key in dictionary, print the value and exit menuOptions iteration loop 
    if userSelectedOption == num:
        # added 2 second delay 
        time.sleep(2)
        # clear screen
        clear()        
        print(menuOptions[num])
    
        # iterate through dictionary keys to call function
        for numFunc in menuOptionsFuncions.keys():
        
            # if the number selected by user match the key in dictionary, call the corresponding function from the menuOptionsFuncions dictionary and exit   
            if userSelectedOption == numFunc:
                menuOptionsFuncions[numFunc]()

    # if userSelectedOption doesnt match the num or numFunc from dicts, throw error 
    elif userSelectedOption > 4:
        print('error invalid input') 
        break



