# Movie Recommendation System

This is a Django-based web application that provides movie recommendations based on the MovieLens dataset. The application allows users to input a user ID to fetch personalized recommendations.

## Features
- **Page 1:** Allows the user to enter a MovieLens user ID.
- **Page 2:** Displays the top 20 recommended movies for the entered user, including details like title, genre, synopsis, and cover image.
- **Navigation:** Easy navigation between recommendation results and selecting another user.

## Requirements
- **Python version:** 3.12.0 (or another compatible version)
- **Dependencies:** Specified in `requirements.txt`

## Installation and Setup

### 1. Clone or Extract the Project
- Clone this repository or extract the `.zip` file containing the project.

### 2. Create and Activate Virtual Environment
- **Windows:**
  ```bash
$  python -m venv venv
$  venv\Scripts\activate

- **Mac/Linux:**
$  python3 -m venv venv
$  source venv/bin/activate


### 3. Install Dependencies

Install the required packages:
$   pip install -r requirements.txt

### 4. Apply Migrations

Ensure that the database is properly configured by running migrations:
$   python manage.py makemigrations
$   python manage.py migrate


### 5. Run the Server
Start the development server:
$  python manage.py runserver


### 6. Access the Application
Visit http://127.0.0.1:8000/ to access the application.


######### Usage
Page 1: Enter a valid MovieLens user ID to fetch recommendations.
Page 2: View the top 20 recommendations and use the "Select Another User" button to enter another user ID.