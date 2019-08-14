
#import numpy as we will use transpose funciton 
import numpy as np

#menu function that prints the menu
def menu():
    print("Menu:")
    print("(1)Enter 2D array as a list of lists")
    print("(2)Print the array in rectangular form")
    print("(3)Multiply an array row by a constant")
    print("(4)Add one row into another")
    print("(5)Add a multiple of one row to another")
    print("(6)Transpose the 2D array")
    print("(9)Quit")

#function that takes a string input
#and evaluate it as a python 2D array
def enterValues():
    print("Please type a 2D list of lists: ")
    array=eval(input())
    return array

#function for printing the array   
def printArray(a):
    #first loop traverses in rows
    for i in range(len(a)):
        #second loop traverses in columns
        for j in range(len(a[i])):
            print("{:8.3f}".format(a[i][j]), end = "")
        print()


#function that modifies the values of a row
#by multiplying with a given value
#it takes 3 arguments
def multiplyRow(a, row, multiplier):
    #for loop that traverses in the elements of the given row
    for i in range(len(a[row])):
        #updating the values of elements by multiplying them
        #with the multiplier
        a[row][i]=a[row][i]*multiplier

#function for adding elements of a row to corresponding elements
#of another row
def addSourceRowToDestinationRow(a, sourceRow, destRow):
    #traverse the elements of destination row only
    for i in range(len(a[destRow])):
        #update the values by adding corresponding values
        #from other row
        a[destRow][i]+=a[sourceRow][i]

#this function is almost the same as previous function
#the only difference is that ther is a multiplier involved
#while updating the values
def addMultipleOfSourceRowToDestRow(a, multiplier, sourceRow, destRow):
    for i in range(len(a[destRow])):
        #adds elements of a row to corresponding elements of other
        #row after multiplying with a given value
        a[destRow][i]+=(a[sourceRow][i])*multiplier

#function for transposing the matrix
def transpose(a):
    #convert the list to numpy array
    a=np.asarray(a)
    #use numpy's transpose function to transpose the array
    return a.transpose()


#matrix function with default value of a initialized
def matrix(a = [[2.0, 4.0, 5.0, 34.0], [2.0, 7.0, 4.0, 36.0], [3.0, 5.0, 4.0, 35.0]]):
    #infinite while loop
    while(True):
        print("=======================================")
        #print array always in the starting 
        printArray(a)
        #print the menu
        menu()
        #take user's input for option
        c=int(input())
        #use conditions according to the option selected by the user

        #choice 1 asks for an array input
        if(c==1):
            a=enterValues()
        #choice 2 for printing the array
        if(c==2):
            printArray(a)

        #choice 3 multiplying a row with a given constant
        if(c==3):
            #input for row number(starts from 0)
            print("Which row do you want to modify? ")
            row=int(input())
            #input for multiplier
            #can be int or float
            #so eval is used to convert into desired data type
            print("Enter mnultiplier: ")
            multiplier=eval(input())
            #Call the related function
            multiplyRow(a, row, multiplier)
        #choice 4 for adding elemnts of a row to another
        if(c==4):
            #input for source row
            print("Enter source row: ")
            sourceRow=int(input())
            #input for destination row(which will be modified)
            print("Enter destination row: ")
            destRow=int(input())
            #call the relevant function
            addSourceRowToDestinationRow(a, sourceRow, destRow)
        #choice 5 
        if(c==5):
            #input for multiplier value
            #cn be int or string thats why eval is used
            print("Enter multiplier: ")
            multiplier=eval(input())
            #input for source row
            print("Enter source Row: ")
            sourceRow=int(input())
            #input for destination row
            print("Enter destination row: ")
            destRow=int(input())
            #call the relevant function
            addMultipleOfSourceRowToDestRow(a, multiplier, sourceRow, destRow)
        #choice 6 for transpose
        if(c==6):
            #call the transpose function
            a=transpose(a)
        #entered 9 for terminating the program
        if(c==9):
            print("Quitting.")
            #break statement terminates the loop
            break


#call the matrix function to start execution
matrix()




