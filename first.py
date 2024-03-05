from flask import Flask, render_template, request
import mysql.connector



app = Flask(__name__)



# Replace with your MySQL database credentials
db_host = "localhost"
db_user = "root"
db_password = "!Sachinuh1234"
db_name = "mydatabase"

# Function to establish a database connection
def create_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

@app.route('/')
def index():
    return render_template('Home.html')

@app.route("/admin login" ,methods=["GET", "POST"])
def admin_login():
    return render_template("admin login.html")

@app.route("/login" ,methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/about" ,methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/contant" ,methods=["GET", "POST"])
def contant():
    return render_template("contact.html")

@app.route("/test report" ,methods=["GET", "POST"])
def test_report():
    return render_template("test report.html")

# Route for the form page
@app.route("/registration", methods=["GET", "POST"])
def form_page():
    if request.method == "POST":
        # Get form data
        Fname = request.form["First name"]
        Lname = request.form["Last name"]
        Aadhar = request.form["Aadhar"]
        email = request.form["email"]
        telephone = request.form["telephone"]
        gender = request.form["gender"]
        address = request.form["address"]
        diagnosed = request.form["Diagnosed"]
        symptomes = request.form["symptoms"]
        password = request.form["password"]
        # Convert the 'subscribe' checkbox value to BOOLEAN (0 or 1)
        #subscribe = 1 if "subscribe" in request.form else 0

        # Insert form data into the database
        connection = create_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO form_data (Fname, Lname, email, Aadhar, telephone, gender, address, diagnosed, symptomes, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (Fname, Lname, email, Aadhar, telephone, gender, address, diagnosed, symptomes, password)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()


        # return render_template("test report.html")
        return "Your information has been submitted successfully."

    return render_template("registration.html")




if __name__ == "__main__":

    
    app.run()

