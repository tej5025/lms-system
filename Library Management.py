#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from datetime import *        
import re 
import random

class db:
    
    book_dict_list = [{'book_id': 101, 'name': 'wings of fire', 'author': 'wings ', 'pages': 35, 'quantity': 2, 'publish_year':1995, 'isbn': 9851193968372}, 
                        {'book_id': 102, 'name': 'sweet little chicken', 'author': 'john paul', 'pages': 50, 'quantity': 2, 'publish_year':2000, 'isbn': 2981185560161}, 
                        {'book_id': 103, 'name': 'chicken soup', 'author': 'lin tin sain', 'pages': 35, 'quantity': 2, 'publish_year':1975, 'isbn': 6791627927091},
                      {'book_id': 104, 'name': 'harry potter', 'author': 'j k rowling ', 'pages': 150, 'quantity': 5, 'publish_year': 1995, 'isbn': 2084378352673}]
    book_id = 105                
    admin_list = [{'name': 'tej', 'username': 'admin' , 'password': 'admin'},]
    users_list = [{'name': 'tejprakash uike', 'DoB': '08-07-1995', 'contact': 8055497594, 'email': 'tej5025@gmail.com', 'password': 'tejas'},]
    borrower_list = [{'book_id': 104, 'name': 'tejprakash uike', 'email': 'tej5025@gmail.com', 'contact': 8055497594, 'today': 'August 08, 2021', 'return_date': 'August 23, 2021', 'days_remaining': 15},
]
    users_borrowing_history = []
       
        
class admin(db):
    admin_session = False
    
    def __inint__(self, ):
        self.admin_session = admin_session
        self.admin_list = db.admin_list
        self.user_list = db.users_list
               
    def create_admin(self):
        admin = {}
        
        if self.admin_session :
            name = input('Ennter admin name : ')
            username = input('Enter admin username : ')
            passwd = input('Enter admin password : ')
            username_available = False
            for adm in self.admin_list:
                if adm['username'] != username:
                    username_available = True
            if username_available :
                admin['name'] = name
                admin['username'] = username
                admin['password'] = passwd
                db.admin_list.append(admin)
                print(admin)
                print('Admin has been created successfully')
                print(db.admin_list)
            else:
                print('Username Already exist..... Please try with another Username ')           
        else:
            print('Please login to create new admins')

    def create_user(self):
        isDOB = False
        dobReg = '^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
        isContact = False
        isEmail = False
        isExist = True
        emailReg = r'[\w\.-]+@[\w\.-]+(\.[\w]+)+'
        user = {}
        if self.admin_session :
            name = input("Enter User's full name : ")
            dob = input("Enter User's date of birth (dd-mm-yyyy format): ")
            if bool(re.search(dobReg, dob)):
                isDOB = True
            contact = input("Enter User's contact number (10 digit only): ")
            if contact.isdigit():
                if len(contact)==10:
                    isContact = True
            else:
                isContact = False
            email = input("Enter User's email : ")
            for i in range(len(db.users_list)):
                mail = db.users_list[i]['email']
                if mail==email:
                    isExist=True
                    break
            else:
                isExist=False
            if bool(re.search(emailReg, email)):
                isEmail = True
            password = input("Enter User's password : ")
            if isDOB==True and isContact==True and isEmail==True and isExist==False:
                contact = int(contact)
                user['name'] = name
                user['DoB'] = dob
                user['contact'] = contact
                user['email'] = email
                user['password'] = password

                db.users_list.append(user)
                print(db.users_list)
                if user:
                    print(user)
                    print('User account has been created successfully')
                else:
                    print('There is some error in creating user account')
            elif isDOB == False:
                print('Please enter dob in correct format!')

            elif isContact == False:
                print('Contact can only be of 10 digits!' )

            elif isEmail==False:
                print('Please enter a valid email!')

            elif isExist==True:
                print('This email already exists')
        else:
            print('Please login to create new users')
  

    def add_book(self):
        if self.admin_session:
            self.book_dict_list = db.book_dict_list
            self.book_dict = {}
            self.name = input("Enter book Title of book : " )
            self.author = input("Enter book Author : " )
            self.pages = int(input("Enter no pages book have : " ))
            self.quantity = int(input("Enter Quantity of books : " ))
            self.publish_year = int(input("Enter publish year of book : " ))
            self.isbn = random.randint(1111111111111,9999999999999)      
            self.bookid = db.book_id

            for book in self.book_dict_list:
                if book['name'] == self.name:
                    print("book with same title already Exist, \nfurther procces will only add quanity of book")
                    ip = input('Do you want to continue and add quantity, \nchoose y / n')
                    if ip == 'y':
                        book['quantity'] += self.quantity
                        break
                    elif ip != 'n' and ip != 'y':
                        print("please choose correct option next time")
                        break


            if self.pages <= 0:
                print('Pages can not be less than one , pls enter valid amount of pages')
            elif self.quantity <= 0:
                print('Quantity of Books must be one or more,\nPlease enter valid no of copies you want to add')
            else:
                self.book_dict['book_id'] = self.bookid
                self.book_dict['name'] = self.name
                self.book_dict['author'] = self.author
                self.book_dict['pages'] = self.pages
                self.book_dict['quantity'] = self.quantity
                self.book_dict['publish_year'] = self.publish_year
                self.book_dict['isbn'] = self.isbn
                print("New Book has been created As")
                print(self.book_dict)
                db.book_dict_list.append(self.book_dict)
                db.book_id += 1
                print("Now new book has been added to book_list")
                
            print(self.book_dict_list)
        else :
            print('Please Login to add book')

    def del_book(self):
        if self.admin_session:
            bkid = int(input("enter book  id to delet the book details"))
            for book in db.book_dict_list:
                if book['book_id'] == bkid:
                    print(book)
                    print("Do you really want to remove this book from book list,")
                    option = input("please say yes or no, \n yes will remove the book and no ")
                    if option == "yes":
                        db.book_dict_list.remove(book)
                        print("book has been rmoved successfully")
                        break
                    else:
                        print("Please enter valid yes to remove book")
                        break
            else:
                print("Book with given book_id is not present in database, \nPlease enter valid book_id present in Database ")
        else :
            print('Please Logit to delet book')
         
        
    def edit_book(self):
        if self.admin_session:
            bkid = int(input("enter book  id to edit book details"))
            for book in db.book_dict_list:
                if book['book_id'] == bkid:
                    print(book)
        
                    print ('\n1.name \n2.author, \n3.pages \n4.quantity ,\n5.publish_year')
                    entry = int(input("Enter number among above to change "))
                    for keys in book:
                        if entry == 1:
                            val = input("Enter new name to book id ")
                            book['name'] = val
                            print('Name of book to coresponding id has been changed to', val)
                            print(book)
                            break
                        elif entry == 2:
                            val = input("Update name of author to book id ")
                            book['author'] = val
                            print('Name of author to coresponding id has been changed to', val)
                            print(book)
                            break
                        elif entry == 3:
                            val = int(input("Enter new pages value to book id "))
                            book['pages'] = val
                            print('New value for pages of book to coresponding id has been changed to', val)
                            print(book)
                            break
                        elif entry == 4:
                            val = int(input("Update value of quantity to book id "))
                            book['quantity'] = val
                            print('Quantity of books to coresponding id has been changed to', val)
                            print(book)
                            break
                        elif entry == 5:
                            val = int(input("Update value of published_year to book id "))
                            book['publish_year'] = val
                            print('publish_year of books to coresponding id has been changed to', val)
                            print(book)
                            break
                    else :
                        print('book id is not found please enter correct book_id')
        else:
            print ('Please Login to edit book')
            
                   
    def issue_book(self):        
        if self.admin_session:
            books = db.book_dict_list
            users = db.users_list
            borrowing_history = db.users_borrowing_history
            borrower_dict = {}
            isSuccess = False
            valid_id = False
            is_available = False
            valid_email = False
            book_id = int(input('Enter book ID to issue book : '))
            for book in books :
                if book['book_id'] == book_id :
                    valid_id = True
                    if book['quantity'] > 0 :
                        is_available = True
                    else:
                        print('There are no available copies')  
                    break
            else : 
                print('Please enter valid book_id')
            
            email = input('Enter the email of user to issue book')
            for user in users :
                if user['email'] == email :
                    valid_email = True
                    break
            else :
                print('Email not Found , Please enter valid email')
                
            if valid_id and is_available and valid_email :
                for user in users :
                    if user['email'] == email :
                        name = user['name'] 
                        contact = user['contact'] 
                        
                        current_day = date.today()
                        returning_day = current_day+timedelta(15)
                        day = returning_day-current_day
                        days_remaining = day.days

                        today = current_day.strftime("%B %d, %Y")
                        new_date = datetime.today() + timedelta(15)
                        return_date = new_date.strftime("%B %d, %Y")

                        borrower_dict['book_id'] = book_id 
                        borrower_dict['name'] = name
                        borrower_dict['email'] = email 
                        borrower_dict['contact'] = contact
                        borrower_dict['today'] = today
                        borrower_dict['return_date'] = return_date
                        borrower_dict['days_remaining'] = days_remaining
                        db.borrower_list.append(borrower_dict)
                        
                        print(f'succesfully issued book with ID', {book_id} ,'To', {name}, sep= " ")
                        print(borrower_dict)
                        isSuccess = True
                        for i in books:
                                if i['book_id']==book_id:
                                    i['quantity']-=1
                                    print(i.items())

            if isSuccess:
                emailDict = {}
                booksDict = {}
                KEY = book_id
                borrowDate = 101
                dueDate = 131
                remaining = 10
                if borrowing_history:
                    for i in borrowing_history:
                        for keys in i.items():
                            mail = keys[0]
                            if mail==email:
                                for innerDict in keys[1]:
                                    for innerDictKey in innerDict:
                                        if innerDictKey=='books':
                                            innerDictList = innerDict[innerDictKey]
                                            if book_id not in innerDictList:
                                                innerDictList.append(book_id)
                                        innerDict[KEY]=[today, return_date, days_remaining]
                                        print(innerDict)
                                        break

                else:
                    booksDict['books'] = []
                    emailDict[email] = [booksDict]
                    borrowing_history.append(emailDict)
                    for i in borrowing_history:
                        for keys in i.items():
                            mail = keys[0]
                            if mail==email:
                                for innerDict in keys[1]:
                                    for innerDictKey in innerDict:
                                        if innerDictKey=='books':
                                            innerDictList = innerDict[innerDictKey]
                                            if book_id not in innerDictList:
                                                innerDictList.append(book_id)
                                        innerDict[KEY]=[today, return_date, days_remaining]
                                        print (innerDict)
                                        break     
                    print(borrowing_history)    
        else:
            print('You are not logged in to issue books')
            
    def accept_book(self):
        if self.admin_session:
            return_book = db.borrower_list
            books = db.users_borrowing_history
            fine = 0
            email = ""
            isValidID = False
            book_id = int(input('Enter book id to check : '))
            
            if return_book:
                for i in return_book:
                    if i['book_id']==book_id:
                        books.append(i)
                        email = i['email']
                        days = i['days_remaining']
                        if days<1:
                            fine+=100
                            print('boomm... 100 rs fine ')
                            for i in books:
                                    for keys in i.items():
                                        mail = keys[0]
                                        if mail==email:
                                            for innerDict in keys[1]:
                                                for innerDictKey in innerDict:
                                                    if innerDictKey==book_id:
                                                        book_key = innerDict[innerDictKey]
                                                        for value in book_key:
                                                            book_key.pop()
                                                            book_key.append(fine)
                                                            book_key.append('Returned')
                                                            print(i)
                                                            for i in range(len(return_book)):
                                                                if return_book[i][0]==book_id:
                                                                    print(return_book[i])
                                                                    del return_book[i]
                                                                    print('Book returned back successfully')
                                                            break
                            else:
                                for i in books:
                                    for keys in i.items():
                                        mail = keys[0]
                                        if mail==email:
                                            for innerDict in keys[1]:
                                                for innerDictKey in innerDict:
                                                    if innerDictKey==book_id:
                                                        book_key = innerDict[innerDictKey]
                                                        for value in book_key:
                                                            book_key.pop()
                                                            book_key.append('Returned')
                                                            print(i)
                                                            for i in range(len(return_book)):
                                                                if return_book[i][0]==book_id:
                                                                    print(return_book[1])
                                                                    del return_book[i]
                                                                    print('Book returned back successfully')
                                                            break
                else:            
                    print('Please check the id which you have entered!')
            else:
                print('There are no new returns')
        else:
            print('Please login to accept return books')
    
    
    def book_details(self):
        if self.admin_session :
            bkid = int(input("enter book  id to edit book details"))
            for book in db.book_dict_list:
                if book['book_id'] == bkid:
                    print(book)
        else:
            print('Please login, you are not logged in ')
    
    def list_borrowers(self):
        if self.admin_session:
            borrower_list = db.borrower_list
            if borrower_list:
                for borrower in borrower_list:
                    print(borrower)
            else:
                print('No pending borrowers in list')
        else:
            print('Please login to check borrowers list')

    
    
    def login(self):
        username = input("Enter username : ")
        password = input("Enter password : ")
        for admin in self.admin_list:
            if admin['username'] == username and admin['password'] == password:
                self.admin_session = True
                print('login success, welcome',admin['name'])

            else:
                print('Usename or Passeord is incorrect ,\nPlease check your username and password')

    def logout(self):
        if self.admin_session == True:
            self.admin_session = False
            print("logged out successfully")
        else:
            print("You are not logged in as admin")
        
        
class user(db):
    session = False
    def __init__(self, ):
        self.session = session
        self.email = username
        
    def register(self):
        isDOB = False
        dobReg = '^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
        isContact = False
        isEmail = False
        isExist = True
        emailReg = r'[\w\.-]+@[\w\.-]+(\.[\w]+)+'
        user = {} 
        name = input('Enter your full name : ')
        dob = input('Enter your date of birth (dd-mm-yyyy format): ')
        if bool(re.search(dobReg, dob)):
            isDOB = True
        contact = input('Enter your contact number (10 digit only): ')
        if contact.isdigit():
            if len(contact)==10:
                isContact = True
        else:
            isContact = False
        email = input('Enter your email : ')
        for i in range(len(db.users_list)):
            mail = db.users_list[i]['email']
            if mail==email:
                isExist=True
                break
        else:
            isExist=False
        if bool(re.search(emailReg, email)):
            isEmail = True
            
        password = input('Enter your password : ')
        if isDOB==True and isContact==True and isEmail==True and isExist==False:
            contact = int(contact)
            user['name'] = name
            user['DoB'] = dob
            user['contact'] = contact
            user['email'] = email
            user['password'] = password

            db.users_list.append(user)
            #print(db.users_list)
            if user:
                print(user)
                print('Your account has been created successfully')
            else:
                print('There is some error in creating user account')
        elif isDOB == False:
            print('Please enter dob in correct format!')

        elif isContact == False:
            print('Contact can only be of 10 digits!' )

        elif isEmail==False:
            print('Please enter a valid email!')

        elif isExist==True:
            print('This email already exists')
            
    def login(self):
        users = db.users_list
        username = input('Enter your email : ')
        password = input('Enter your password : ')
        if len(users)>0:
            for i in range(len(users)):
                if users[i]['email']==username and users[i]['password']==password:
                    # breakpoint()
                    self.session = True
                    self.email = username
                    books = db.users_borrowing_history
                    email=username
                    book_id_for_submitting = 0
                    month = 0
                    Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

                    for i in books:
                        for keys in i.items():
                            mail = keys[0]
                            if mail==email:
                                for innerDict in keys[1]:
                                    for innerDictKey in innerDict:
                                        if innerDictKey=='books':
                                            book_id_for_submitting = innerDict[innerDictKey]
                                        for book_ids in book_id_for_submitting:
                                            if innerDictKey==book_ids:
                                                book_key = innerDict[innerDictKey]
                                                for value in book_key:
                                                    length_of_book_key = len(book_key)-1
                                                    remaining_days = book_key[2]
                                                    current_day = date.today()
                                                    date_convertor = str(book_key[1]).split()
                                                    for i in range(1, len(Months)):
                                                        if date_convertor[0]==Months[i]:
                                                            month = i+1
                                                    day = int(date_convertor[1].replace(',', ""))
                                                    year = int(date_convertor[2])

                                                    returning_date = date(year, month, day)

                                                    day = returning_date-current_day
                                                    days_remaining = day.days

                                                    if book_key[length_of_book_key]=='Pending':
                                                        book_key.pop(length_of_book_key-1)
                                                        book_key.insert(length_of_book_key-1, days_remaining)

                                                    elif book_key[length_of_book_key]=='Returned':
                                                        pass

                                                    else:
                                                        book_key.pop()
                                                        book_key.append(days_remaining)
                                                    break
                    print('Welcome to Library', end=" ")
                    break
                else:
                    pass
            else:
                print('Password or username is incorrrect')
        else:
            print('No users')
            
    def my_borrowed_list(self):
        if self.session:
            email = self.email
            books = db.users_borrowing_history
            book_history = []
            custom_dict = {}
            seperate_book_history = []
            for i in books:
                for keys in i.items():
                    mail = keys[0]
                    if mail==email:
                        for innerDict in keys[1]:
                            for innerDictKey in innerDict:
                                if innerDictKey=='books':
                                    book_key = innerDict[innerDictKey]
                                    for value in book_key:
                                        book_history.append(value)
                                if innerDictKey in book_history:
                                    for book_id in book_history:
                                        books_id = innerDict[book_id]
                                        custom_dict[book_id]=innerDict[book_id]
                                    seperate_book_history.append(custom_dict)
                                    print(seperate_book_history)
                                    print(custom_dict)
                                    break
            for i in range(len(seperate_book_history)):
                for book_id in book_history:
                    values = seperate_book_history[i][book_id]
                    for individual_value in values:
                        print(book_id, individual_value, sep=" ")
                    
        else:
            print('You are not logged in to view books')
    
    def details_of_book(self):
        if self.session :
            bkid = input("enter the book_id of your borrowed book :  ")
            for book in db.book_dict_list:
                if book['book_id'] == bkid:
                    print(book)
                    break            
            else:
                print(" please enter correct book_id")
        else:
            print("Please Log in to see book details")
            
    
    def logout(self):
        if self.session:
            self.session=False
            print('Thank you for visiting Library')
        else:
            print("You are not logged in as user")


class Library(user, admin):
    def __init__(self) :
        
        j=1
        try:
            while j!=0:
                print('\n***********************************')
                print('|| Select any one of the options ||')
                print('***********************************')
                print('** | 1.| User                    **')
                print('** | 2.| Admin                   **') 
                print('** | 3.| Exit                    **') 
                print('***********************************')
                req = int(input('Enter input : '))

                if req==1:
                    i = 1
                    try:
                        while i!=0:
                            print('\n***********************************')
                            print('|| Select any one of the options ||'  )
                            print('*************************************')
                            print('** | 1.| Login to Library          **')
                            print('** | 2.| Register to Library       **') 
                            print('** | 3.| My Books                  **')
                            print('** | 4.| View Book detail          **')
                            print('** | 5.| Logout                    **')
                            print('*************************************')
                            req = int(input('Enter input : '))

                            if req==1:
                                user.login(self)
                            elif req==2:
                                user.register(self)
                            elif req==3:
                                user.my_borrowed_list(self)
                            elif req==4:
                                user.details_of_book(self)
                            elif req==5:
                                user.logout(self)
                                i=0
                            else:
                                print('Invalid input')
                    except:
                        print('No option selected! Program exiting users...........', end=" ")
                elif req==2:
                    i = 1
                    try:
                        while i!=0:
                            print('\n**************************************')
                            print('||   Select any one of the options   ||')
                            print('***************************************')
                            print('** | 1.| Admin Login                 **')
                            print('** | 2.| Create Admins               **') 
                            print('** | 3.| Create User                 **') 
                            print('** | 4.| Add Books                   **')
                            print('** | 5.| Edit Books                  **')
                            print('** | 6.| Delete Books                **')
                            print('** | 7.| view Books by book Id       **')
                            print('** | 8.| issue Book to User          **')
                            print('** | 9.| List Borrowers              **')
                            print('** | 10.| Accept Books               **')
                            print('** | 11.| Logout                     **')
                            print('***************************************')
                            req = int(input('Enter input : '))

                            if req==1:
                                admin.login(self)
                            elif req==2:
                                admin.create_admin(self)
                            elif req==3:
                                admin.create_user(self)
                            elif req==4:
                                admin.add_book(self)
                            elif req==5:
                                admin.edit_book(self)
                            elif req==6:
                                admin.del_book(self)
                            elif req==7:
                                admin.book_details(self)
                            elif req==8:
                                admin.issue_book(self)
                            elif req==9:
                                admin.list_borrowers(self)
                            elif req==10:
                                admin.accept_book(self)
                            elif req==11:
                                admin.logout(self)
                                i=0
                                print('Thank you')
                            else:
                                print('Invalid input')
                    except:
                        print('No option selected! Program exiting admin...........', end=" ")

                elif req==3:
                    print('Thank you for visiting uLibrary')
                    break
                else:
                    print('Invalid input')
        except:
            print('No option selected! Program stopping...........', end=" ")

lib = Library()


# In[ ]:




