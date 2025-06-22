
## Adventure Camp Management System

This is a full-stack web application that allows users to book adventure camps by selecting their preferred location, meal plan, and entering necessary personal details.

## Technologies Used
- Backend: Python (Flask)
- Frontend: HTML, CSS
- Database: MySQL

## Features
- User-friendly camp booking interface
- Dynamic form inputs for:
  - Personal details (name, DOB, email, contact)
  - Destination and camp selection
  - Meal plan preferences
  - Medical condition input
- Responsive web design
- MySQL database integration for storing and retrieving camper and camp details

## Project Structure
project/
│
├── templates/
│   ├── welcome.html
│   ├── success.html
│   ├── booking_form.html
│
├── static/
│   └── styles.css
│
├── main.py
├── README.md
└── snapshots/ (Screenshots of database and output)

## Database Info
- Note: The `.sql` file is not included.
- Screenshots of the database schema and sample records are available in the `snapshots/` folder for reference.
- The database used is named `adventurecamp`, and it includes tables like:
  - camper
  - camp
  - location
  - mealplan
  - instructor
  - activity

## Output Preview
Refer to the `snapshots/` folder for:
- Web interface previews
- Booking form submissions
- Database table structures and entries

## How to Run
1. Install required Python packages:
   pip install flask mysql-connector-python

2. Run the app:
   python main.py

3. Open http://127.0.0.1:5000 in your browser
