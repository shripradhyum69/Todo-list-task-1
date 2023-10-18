#usr/bin/python3

'''
task 1 : To Create a Todo List In Cli
Given Actions To Perform Are Create, View, Mark Tasks Complete, Delete a Task
Simple And Innovative Cli Application
'''

#importing the appropiate libraries
import mysql.connector
import random
from datetime import date
import time


class todolist:
    #constructor initialized for future purposes
    def __init__(self):
        pass

    #method to add a task
    def add_task(self):
        print("You have selected to add a task in your list")
        task_name=input("Enter the task name : ")
        task_description=input("Enter the task Description : ")
        current_time=time.strftime("%H:%M:%S")
        database_cursor.execute(f"insert into todolist1 values('{random.randint(100,1000)}','{task_name}','{task_description}','Not Completed','{date.today()}','{current_time}')")
        database_name.commit()
        print("Task Added")
        print("===============================================================================")



    #method to view all tasks
    def view_tasks(self):
        database_cursor.execute("select *from todolist1")
        task_list=database_cursor.fetchall()
        print("Task_ID\tTask_Date\tTask_time\tTask_name\tTask_description\tTask_status")
        for i in task_list:
            print(i[0],"\t",i[4],"\t",i[5],"\t",i[1],"\t",i[2],"\t",i[3])
        print("===============================================================================")


    #method to mark the task complete
    def marktask_complete(self):
        #to fetch all the tasks from the db
        database_cursor.execute("select task_id, task_name from todolist1")
        task_list=database_cursor.fetchall()
        print("Task_No.\tTask_name")
        #print(task_list)
        for i in range(len(task_list)):
            print(task_list[i][0], "\t", task_list[i][1])

        task_number=int(input("Enter the Task Number You Want To Mark Complete : "))
        #task_name2=task_list[task_number-1]
        database_cursor.execute(f"update todolist1 set task_status='Completed' where task_id='{task_number}'")
        database_name.commit()
        print("Task Successfully Marked As Completed")
        print("===============================================================================")



    #method to delete the task
    def delete_task(self):
        #to fetch all the tasks from the db
        database_cursor.execute("select task_id, task_name from todolist1")
        task_list = database_cursor.fetchall()
        print("Task_No.\tTask_name")
        # print(task_list)
        for i in range(len(task_list)):
            print(task_list[i][0], "\t", task_list[i][1])
        task_number=int(input("Enter the Task Number You Want To Delete : "))
        database_cursor.execute(f"delete from todolist1 where task_id='{task_number}'")
        database_name.commit()
        print("Task Successcully Deleted")
        print("===============================================================================")




if __name__ == '__main__':
    # creating a valid Mysql Connection (global vars declared)
    database_name = mysql.connector.connect(user="root", password="root123", host="127.0.0.1", database="todolist")
    database_cursor = database_name.cursor()
    #creating a menu bar where user has to choose the option
    userchoice_number=0
    todolist_object=todolist()
    print("===============================================================================")
    print("Welcome To The Todo List Application CLI Version")
    print("===============================================================================")
    while(1==1):
        print(" ")
        print("Enter the desired option from the drop down menu down below : ")
        print(" ")
        print("Press 1 to Add Tasks")
        print("Press 2 to View Tasks")
        print("Press 3 to Mark a Task as Completed")
        print("Press 4 to Delete a Task ")
        print("Press 5 to Exit the Application")
        print("===============================================================================")
        print(" ")
        userchoice_number=int(input("Enter a Valid Response : "))
        print(" ")
        if(userchoice_number==1):
            todolist_object.add_task()
        elif(userchoice_number==2):
            todolist_object.view_tasks()
        elif(userchoice_number==3):
            todolist_object.marktask_complete()
        elif(userchoice_number==4):
            todolist_object.delete_task()
        elif(userchoice_number==5):
            print("Thank You For Using the Task Manager")
            break
        else:
            print("The Response Is Invalid And Cannot Be Accepted Try Again")
            print(" ")
    print("Thank You For Using Task Management Application")
    database_name.close()



