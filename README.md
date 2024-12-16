**README for User Management Flask Application**
**Project Overview**
This is a simple User Management application built using Django. It provides functionality for managing users, including viewing, editing, and creating new users. It connects to a MySQL database to store and retrieve user information.

**1. Setup Instructions**
Pre-requisites:
Before setting up the application, ensure you have the following installed:

**Python 3.x**: This application is built using Python 3.x.
**MySQL Database**: Ensure you have MySQL installed. 

**Setting Up the Project:**
Clone the repository: Clone the repository to your local machine using the following command:
git clone https://github.com/yourusername/user-management.git
cd user-management

**Install Required Dependencies:**
Install all necessary Python dependencies by running:
pip install -r requirements.txt
This will install Django, MySQL client, and other necessary packages.

**2. Database Schema and Setup**
Database Setup:
The application uses MySQL as the database backend. To set up the database:

Create the Database: First, log into MySQL:
mysql -u your_mysql_user -p

Create a database named users:
CREATE DATABASE users;

Create the users Table: In the users database, create a table to store user information:
USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL
);

Populate the Database with Sample Data: You can add some sample users to the users table using the following SQL queries:
INSERT INTO users (name, email, role) VALUES
('Payal', 'payalp1572@gmail.com', 'Admin'),
('Snehal', 'snehap28499@gmail.com', 'User'),

**3. Dependencies**
The application uses the following Python dependencies:

Django: Web framework for building the application.
mysqlclient: MySQL database adapter for Python.
Bootstrap : Used for frontend styling.

**4. How to Run the Application**
Start the Django Development Server: Run the following command to start the Django development server:
python manage.py runserver
By default, the application will run at http://127.0.0.1:8000/.

Accessing the Application:

Homepage: http://127.0.0.1:8000/
View Users: http://127.0.0.1:8000/users/
Create New User: http://127.0.0.1:8000/users/new_user/
Edit User: http://127.0.0.1:8000/users/edit_user/<id>/

**5. Git Workflow**
Cloning the Repository:
To contribute to this project, first clone the repository to your local machine:
git clone https://github.com/yourusername/user-management.git
cd user-management
Creating a Branch:
Create a new branch for your work:
git checkout -b feature/your-feature-name
git push origin feature/your-feature-name
Creating a Pull Request:
Once you've pushed your changes, open the repository on GitHub and create a pull request from your branch to the main branch.

Merging:
Once the pull request is reviewed and approved, merge it into the main branch.

Updating Your Local Repository:
After the pull request is merged, pull the latest changes into your local repository:
git checkout main
git pull origin main
