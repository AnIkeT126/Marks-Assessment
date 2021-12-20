# Project on Employee Management System
import mysql.connector as driver
import sys
def menu():
    loop="y"
    while loop=="y":
        print("\n........MENU.......")
        print("1. CREATE DATABASE")
        print("2. SHOW DATABASES")
        print("3. CREATE TABLE")
        print("4. SHOW TABLES")
        print("5. INSERT RECORD")
        print("6. UPDATE RECORD")
        print("7. DELETE RECORD")
        print("8. SEARCH RECORD")
        print("9. DISPLAY RECORD")
        print("10. QUIT")
        print()
        choice=int(input("Enter the choice (1-10) : "))
        if(choice==1):
            create_database()
        elif(choice==2):
            show_databases()
        elif(choice==3):
            create_table()
        elif(choice==4):
            show_tables()
        elif(choice==5):
            insert_record()
        elif(choice==6):
            update_record()
        elif(choice==7):
            delete_record()
        elif(choice==8):
            search_record()
        elif(choice==9):
            display_record()
        elif(choice==10):
            break
        else:
            print("Wrong Choice.")
        loop=input("\nDo you want to continue?(y or n)")
    else:
        sys.exit()
        
def create_database():
    con=driver.connect(host="localhost",user="root",passwd="12345",port="3307",charset='utf8')
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create database if not exists students')
    print()
    print("Database Created")
    con.close()
    
def show_databases():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',port="3307")
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show databases')
    for i in cur:
        print(i)
    con.close()
    
def create_table():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='students',port="3307")
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('create table if not exists stu(rollno integer primary key, name varchar(15), marks int)')
    print()
    print("Table Created -> STU")
    cur.execute('DESC stu')
    print("+-------------|--------------|-----------+")
    print("+Column Name  |DataType(Size)|NULL       |")
    print("+-------------|--------------|-----------+")
    
    for i in cur:
        print('|{0:12} | {1:12} | {2:10}|'.format(i[0],i[1].decode('UTF-8'),i[2]))
    print("+-------------|--------------|-----------+")
    con.close()
    
def show_tables():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='students',port="3307")
    if con.is_connected():
        print("Successfully Connected")
    cur=con.cursor()
    cur.execute('show tables')
    for i in cur:
        print(i)
    con.close()

def insert_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='students',port="3307")
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        rollno=int(input("ENTER student rollno : "))
        NAME=input("ENTER Name OF student : ")
        marks=int(input("ENTER Student Marks : "))
        query1="INSERT INTO stu(rollno,name,marks) VALUES({},'{}',{})".format(rollno,NAME,marks)
        cur.execute(query1)
        con.commit()
        print('Record Inserted')
        con.close()
    else:
        print("Error : Not Connected")

def update_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='students',port="3307")
    cur=con.cursor()
    d=int(input("Enter Student Rollno for update record : "))
    rollno=int(input("ENTER NEW Student rollno : "))
    name=input("ENTER NEW Name of student : ")
    marks=float(input("ENTER NEW marks of Student : "))
    query1="update stu set rollno=%s, name='%s', marks=%s where rollno=%s" %(rollno,name,marks,d)
    cur.execute(query1)
    con.commit()
    print("Record Updated")
    con.close()

def delete_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='students',port="3307")
    cur=con.cursor()
    d=int(input("Enter student rollno for deleting record : "))
    query1="delete from stu where rollno={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def search_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='students',port="3307")
    cur=con.cursor()
    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO SEARCH RECORD: ")
    print("1. ACCORDING TO Rollno")
    print("2. ACCORDING TO Name")
    print("3. ACCORDING TO MArks")
    print()
    choice=int(input("ENTER THE CHOICE (1-3) : "))
    if choice==1:
          d=int(input("Enter student rollno which you want to search : "))
          query1="select * from stu where rollno=%s" %(d)
    elif choice==2:
          name=input("Enter student Name which you want to search : ")
          query1="select * from stu where name='%s'" %(name)
    elif choice==3:
          mak=float(input("Enter student marks which you want to search : "))
          query1="select * from stu where marks=%s" %(mak)
    else:
          print("Wrong Choice")
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    for i in rec:
        print(i)
    print("Record Searched")
    con.close()

def display_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='students',port="3307")
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from stu')
        rec=cur.fetchall()
        count=cur.rowcount
        print("+----------|--------------|-----------+")
        print("+  stu ID  |   stu Name   |   Marks   |")
        print("+----------|--------------|-----------+")
        for i in rec:
            print('|{0:^9} | {1:^12} | {2:^10}|'.format(i[0],i[1],i[2])) 
        print("+----------|--------------|-----------+")
        print("|   Total no. of records are : ",count,"    |")
        print("+-------------------------------------+")
        con.close()
    else:
        print("Error : Database Connection is not success")

menu()
