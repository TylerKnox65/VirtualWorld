#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""
import dataBaseCreator as db
import json
import sqlite3
from types import DynamicClassAttribute
import os


class main():
    def __init__(self) -> None:
       self.dataEntry()
    
    def dataEntry(self): #Enter selection mode
        while True:
            try:
                choice = int(input(("\nWelcome to assignment helper!\nWith this program you can (1) Create assigment, (2) Edit assignment scores, (3) Delete data, (4) View current assignments, (5) Quit Program:  ")))
                break
            except:
                print("Enter a valid integer.")
        if choice == 1:
            self.createAssignment()

        elif choice == 2:
            self.editData()
        elif choice == 3:
            try:
                sure = str(input("Are you sure? Enter YES to confirm: "))
                if sure != "YES":
                    raise ValueError('A very specific bad thing was avoided.')
                else:
                    self.delete()
            except:
                self.dataEntry()
                    
            #self.delete()
        elif choice  == 4:
            self.getData()
        elif choice == 5:
            os._exit(0)
        self.dataEntry()
    def writeData(self): #Write Data to file, unused
        pass
    def editData(self): #Edit current data
        name = input("Enter the assignment name: ")
        studentname = input("Enter the student name: ")
        newmark = input(f"Enter new mark that {studentname} has: ")
        db.main().update(filename="marks.db",Basename=name,updatename=studentname,updateTo=newmark,params=None)
    def getData(self): #Finds the data
        name = input("Enter the assignment name: ")
        studentname = input("Enter student name: ")
        data = db.main().retrieveEntries(filename="marks.db", Basename=name, entries=studentname)
        data = str(data).replace("'",'').replace(",",'').replace("(",'').replace(")",'').strip("[]")
        print(f"{studentname} has a current mark of {data} for the assignment: {name}")
    
    def createAssignment(self):
        #teachername = str(input("Enter teacher name: "))
        name = str(input("Enter the assignment name: "))

        #value = str(input("Enter the assignment value: "))
        while True:
            try:
                numStudent = int(input("Enter the amount of students that have a mark: "))
                break
            except:
                print("Enter a valid amount of students")
        
        
        prev={}
        for i in range(numStudent):
                studentName = str(input("Enter the student's name: "))
                studentMark = str(input(f"Enter the student: {studentName}'s mark: "))
                prev[studentName] = studentMark
        entries = str([i for i in prev]).strip("[]").replace("'","")
        
        print(entries, type(entries))
        values = [prev[i] for i in prev]
        
        db.main().createDataBase(filename="marks.db", Basename=name, entries=entries)
        db.main().insertInto(filename="marks.db", Basename=name, entries=entries, values=values)


    def delete(self): #THIS DELETES ALL DATA SAVED
       os.remove("marks.db")
       
           



if __name__ == "__main__":
    main()