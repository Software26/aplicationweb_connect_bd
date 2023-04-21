from flask import Flask,render_template,request,url_for,redirect,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'# view the app this security

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (Fullname, phone, email) VALUES (%s,%s,%s)',(fullname, phone, email))
        mysql.connection.commit()
        flash('Contact added successfully')# realice
        return redirect (url_for('index'))
    
@app.route('/edit')
def edit():
    return "edit contact"

@app.route("/delete")
def delete():
    return "delete"



if __name__ == '__main__':
    app.run(debug=True)