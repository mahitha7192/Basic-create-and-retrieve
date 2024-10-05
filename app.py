from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['employee']  
collection = db['testemployee']

@app.route('/')
def home():
    hold = list(collection.find())  # Fetch all from MongoDB
    return render_template('home.html', hold=hold)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':  # If the form is submitted
        # Get form data
        name = request.form.get('name')
        dob = request.form.get('dob')
        work = request.form.get('work')

        # Insert into MongoDB
        collection.insert_one({'name': name, 'dob': dob, 'work': work})
        
        return redirect(url_for('home'))  # Redirect back to home page

    return render_template('add.html')  # If it's a GET request, show the add page

if __name__ == "__main__":
    app.run(debug=True)

