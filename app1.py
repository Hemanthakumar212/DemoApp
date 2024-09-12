from flask import Flask,redirect,request,render_template,url_for
import mysql.connector
import templates
app=Flask(__name__)

app.config['SESSION_TYPE']='filesystem'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'name'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mydb=mysql.connector.connect(host='localhost',user='root',password='admin',db='name')
with mysql.connector.connect(host='localhost',user='root',password='admin',db='name') as conn:
    cursor=conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/state',methods=['GET','POST'])
def state():
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from state ')
    data=cursor.fetchall()
    cursor.close()
    return render_template('ram.html',data=data)

@app.route('/statedis',methods=['GET','POST'])
def statedis():
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from state_districtwise ')
    data1=cursor.fetchall()
    cursor.close()
    return render_template('statedis.html',data1=data1)
@app.route('/pincodewise',methods=['GET','POST'])
def pincodewise():
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from pincodewise ')
    data2=cursor.fetchall()
    cursor.close()
    return render_template('pincodewise.html',data2=data2)
@app.route('/from_pincodewise',methods=['GET','POST'])
def from_pincodewise():
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from from_to_pincodewise ')
    data3=cursor.fetchall()
    cursor.close()
    return render_template('from_to_pincodewise.html',data3=data3)
@app.route('/Company_Name',methods=['GET','POST'])
def Company_Name():
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from datasheet')
    data4=cursor.fetchall()
    cursor.close()
    return render_template('Company_Name.html',data4=data4)

@app.route('/overall',methods=['GET','POST'])
def overall():
    cursor=mydb.cursor(buffered=True)
    cursor.execute('select * from overall')
    data5=cursor.fetchall()
    cursor.close()
    return render_template('overall.html',data5=data5)



if __name__=="__main__":
    app.run(debug=True,use_reloader=True)



# from flask import Flask, render_template
# import mysql.connector

# app = Flask(__name__)

# # MySQL connection configuration
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="admin",
#     database="name"
# )

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # Create a cursor to execute SQL queries
#     cursor = mydb.cursor(dictionary=True)  # Use dictionary=True to return rows as dictionaries
#     cursor.execute('SELECT * FROM state')  # Modify this query to match your table structure
#     data = cursor.fetchall()  # Fetch all rows
#     cursor.close()  # Close the cursor after fetching data
    
#     # Pass the data to the template
#     return render_template('ram.html', data=data)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # Create a cursor to execute SQL queries
#     cursor = mydb.cursor(dictionary=True)  # Use dictionary=True to return rows as dictionaries
#     cursor.execute('SELECT * FROM state_districtwise')  # Modify this query to match your table structure
#     data = cursor.fetchall()  # Fetch all rows
#     cursor.close()  # Close the cursor after fetching data
    
#     # Pass the data to the template
#     return render_template('ram.html', data=data)

# if __name__ == "__main__":
#     app.run(debug=True, use_reloader=True)
