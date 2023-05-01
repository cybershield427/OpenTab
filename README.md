# OpenTab

## Created by Team: CyberShield

### Complete
1. main frame window
2. menu bar
3. toolbar
4. status bar
5. login button


### Pending
1. after login main window
2. databases for user and customer
3. authentication process
4. ...


### List of members
Hangbo Zhang: main frame, menu, toolbar, status bar, login window, buttons

Kristine Rivera: databases for use and customer (in progress)

Josh Constantino: Add functionality to settings and help

Joshua Rio

## For Assignment 3

### Progress

After last time when the frame of the application has been created, there are couple new progresses were made.
1. The functionality of the Login button (open login window) and cancel button (close the app)
2. The new window after login button was clicked have been created to take the username and password
3. create the database to hold the users' information such as username, password, first last name, phone number
4. The user login credential has been implemented that will check if username, password pair is in the database
5. The windows after login have been created. If it's admin(manager/owner), it will give the window to sign up for new
    user (more function such as delete will be added later on). If it's a normal user, then the main window will display.
6. Sign up window has been implemented which have field to take user input. It will check if the username has been taken
    and password met the security requirement (length, complexity). If all good, new user will be added into the database.
    If not, then an error message will be display accordingly.
7. Created restaurant database to hold customer information such as name, credit card number and table number
8. Created authorized users: waiter1 & waiter2
9. Added functionality to the help button to create a pop-up window and give a message.

### Link

Link to the repository
https://github.com/cybershield427/OpenTab

### Pending

1. The main window after login is still ongoing. It still needs to implement the function of add table, etc
2. more functions for each element such as help, setting etc
3. Implement function to assign to tables and create customers
4. Update table window to indicate unassigned tables from assigned tables

### Roles and responsibilities

| Members          | New completion | Current   | Next       |
|------------------|----------------|-----------|------------|
| Hangbo Zhang     | Progress 1-6   | Pending 1 | Pending 2  |
| Kristine Rivera  | Progress 7-8   | Pending 3 | Pending 4  |
| Josh Constantino | Progress 9     | Pending 2 | -          |
| Joshua Rio       | -              | -         | -          |


## For Assignment 4

### Done since Last submit (Progress)
1. The main window after login with the implement function of add table
2. have added more functionality into other elements such as help, setting
3. function to assign to tables and create customer database
4. fuzz testing, SQL injection, DoS, Buffer overflow
5. static analyze
6. dynamic analyze

### Pending now
1. more testing cases
2. functionality of all the buttons
3. better UI
4. set limitation of user privilege to database


### Roles and responsibilities

| Members          | New completion | Current   | Next         |
|------------------|----------------|-----------|--------------|
| Hangbo Zhang     | progress 4,5,6 | pending 1 | pending 4, 3 |
| Kristine Rivera  | progress 1, 3  | pending 3 | pending 2, 3 |
| Josh Constantino |                |           | -            |
| Joshua Rio       | -              | -         | -            |

### Link

Link to the repository

https://github.com/cybershield427/OpenTab

## For Assignment 5


| Members          | New completion                                                                                      |
|------------------|-----------------------------------------------------------------------------------------------------|
| Hangbo Zhang     | set limitation of user privilege, penetration tests, test cases, Wiki page, Release the application |
| Kristine Rivera  | better UI, adding more functionality, test cases                                                    |
| Josh Constantino | -                                                                                                   |
| Joshua Rio       | -                                                                                                   |

### Technical notes
- install Pyside6 by `pip install pyside6` or `pip install -r requirements.txt`
- With the PySide6 installed in your local machine. You can start the program by running: 
`python3 main.py`
- The login window will pop up. You can log in with admin and changeme. 
From then, you can sign up for all your waiters/waitress.
- For waiters/waitress, after the sign-up finished by the manager/admin, 
they can log in with their own username and password.
- After login, they can add table, assign customer, store or delete customers' information of the tables. 
However, they will only be able to see the name and orders of the customer not any other information of the customers.
- After initial login with admin, please make sure to sign up a new manager account and delete the `admin` account 
as it was default and open to everyone.
- The 2 database that stores the information of the waiters/waitress and customers are currently created 
in the local machine. They are also included in the project. You might want to change the name of the database 
and also maybe stored in somewhere else.
- There are couple test/default waiters/waitress accounts. You might want to delete them as well.

### Brief thoughts
- there are a lot of UI libraries available in python, finding an easy to learn and use is not that easy
- the connection between all the buttons to the actions and between windows to windows 
are at first was hard to establish.
- UI design is definitely another very different field. Our application's UI is very basic.
- able to create the database, set different constrains and communicate with the database from our application
was a great achievements.


### Link to Repository
https://github.com/cybershield427/OpenTab

### Link to Final Report
https://github.com/cybershield427/OpenTab/blob/main/ICS427-Final-Report.pdf

### Link to Release Version
https://github.com/cybershield427/OpenTab/releases/tag/v1.0.0

### Link to Wiki Page
https://github.com/cybershield427/OpenTab/wiki