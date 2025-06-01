##Younderbots_TASKASSIGMENT-1

OVERVIEW:
This is a basic CRUD (Create, Read, Update, Delete) web application for managing student records. I created the frontend using HTML and developed the backend using Python with Flask. The data is stored in a MySQL database, and I used WAMP server to run MySQL and phpMyAdmin to view and manage the database records.


FEATURES:
Add new student details
View the list of all students
Update student information
Delete student records


HOW TO RUN THIS PROJECT:

Step 1: Clone the Project
git clone https://github.com/aashi984/Younderbots_TASKASSIGMENT-1.git
cd Younderbots_TASKASSIGMENT-1

Step 2: Start WAMP Server
Make sure the WAMP server is running.
Open phpMyAdmin by visiting:
http://localhost/phpmyadmin/

Step 3: Set Up MySQL Database
In phpMyAdmin,I have created a new database named:"task1" and
Inside that database, I have created a table named:"A1"

Step 4: Create Virtual Environment
python -m venv venv

Step 5: Activate Virtual Environment
On Windows:
venv\Scripts\activate

Step 6: Install Requirements
pip install -r requirements.txt

Step 7: Start Flask Backend Server
python backend.py

Step 8: Open in Browser
Visit http://127.0.0.1:5000


TOOLS USED:
Python (Flask)
HTML (for frontend)
MySQL (via WAMP server)
phpMyAdmin (to view/manage database)

Note:
Ensure WAMP server is running before starting the Flask server.

