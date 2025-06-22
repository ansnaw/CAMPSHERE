from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='AdventureCamp'
)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/booking_form', methods=['GET', 'POST'])
def booking_form():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT LocationID, City FROM location")
    locations = cursor.fetchall()
    
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        dob = request.form.get('dob')
        email = request.form.get('email')
        phone = request.form.get('phone')
        medical_info = request.form.get('medical_info')
        meal_type = request.form.get('meal_type')
        dietary_preference = request.form.get('dietary_preference')

        cursor.execute(""" 
            INSERT INTO camper (FirstName, LastName, DOB, Email, PhoneNumber, MedicalInfo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, dob, email, phone, medical_info))
        db.commit()
        camper_id = cursor.lastrowid

        cursor.execute(""" 
            INSERT INTO MealPlan (CamperID, MealType, DietaryPreference)
            VALUES (%s, %s, %s)
        """, (camper_id, meal_type, dietary_preference))
        db.commit()
        cursor.close()
        
        return redirect(url_for('success'))

    return render_template('booking_form.html', locations=locations)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/get_camps')
def get_camps():
    locationID = request.args.get('locationID')
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT CampID, CampName FROM camp WHERE LocationID = %s", (locationID,))
    camps = cursor.fetchall()
    cursor.close()
    return jsonify(camps=camps)

@app.route('/get_camp_details')
def get_camp_details():
    campID = request.args.get('campID')
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT Duration, Pricers AS Price FROM camp WHERE CampID = %s", (campID,))
    camp_details = cursor.fetchone()
    cursor.close()
    return jsonify(duration=camp_details['Duration'], price=camp_details['Price'])

if __name__ == '__main__':
    app.run(debug=True)
