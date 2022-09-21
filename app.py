import json
from logging import basicConfig
import os
from flask import Flask, flash, request, redirect, url_for, render_template, session, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import os
import mysql.connector
from mysql.connector import *
import random, string
from datetime import datetime
import pdfkit
import datetime
# from flask_wkhtmltopdf import Wkhtmltopdf

UPLOAD_FOLDER = 'static/images/'
WKHTMLTOPDF_PATH = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# wkhtmltopdf = Wkhtmltopdf(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET" , "POST"])
def home():
    if request.method == "POST":
        mail = request.form["email"]
        psw = request.form["password"]
        print("IN IF")
        if mail == "admin" and psw == "admin":
            print("IN IF2")
            return redirect(url_for('dashboard'))
        else:
            print("IN ELSE")
            flash(f'Wrong email and password', 'success')
            return redirect(url_for('login'))
            flash("Wrong Credentials")
            # return render_template("login.html")
    print("OUT IF")
    return render_template("login.html")
	# return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        mail = request.form["email"]
        psw = request.form["password"]
        if mail == 'admin' and psw == 'admin':
            flash(f'welcome {mail} you are logedin now','success')
            return redirect(url_for('dashboard'))
        else:
            flash(f'Wrong email and password', 'success')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route("/employee", methods=["GET" , "POST"])
def employee():

    # Fetch Data

    if request.method == "POST" and request.form['action'] == 'search':
        eid = request.form["eid"]
        try:
            print("in Search")
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            query = "SELECT * FROM employee WHERE EmployeeID = %s"
            data = [eid]
            cursor.execute(query,data)
            emp_data = cursor.fetchall()
            salary = []
            print(emp_data)
            # print(emp_data[1])
            # for i in range(len(emp_data)):
            #     salary = ''.join(emp_data[i])
            #     print(salary)

            return render_template("employee.html", edata = emp_data)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")   

    # Save To Database

    if request.method == "POST" and request.form['action']== 'save':
        print("in Save")
        eid = request.form["eid"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        title = request.form["title"]
        dob = request.form["dob"]
        clocked = request.form["optradio"]
        address = request.form["add"]
        city = request.form["city"]
        country = request.form["con"]
        phone = request.form["phn"]
        mobile = request.form["mob"]
        fax = request.form["fax"]
        mail = request.form["mail"]
        if request.files["img"]:
            eimage = request.files["img"]
        else:
            eimage = ""
        nic = request.form["nic"]
        tax = request.form["tax"]
        bank = request.form["bank"]
        bank_ac = request.form["bac"]
        code = request.form["code"]
        # report = request.form["rpt"]
        report = ""
        nps = request.form["optradio2"]
        car = request.form["car"]
        hire = request.form["hire"]
        salary = request.form["sal"]
        position = request.form["pos"]
        dep = request.form["dep"]
        sdep = request.form["sdep"]
        paye = request.form["psch"]
        per = request.form["per"]
        lleave = request.form["lleave"]
        sleave = request.form["sleave"]
        fallow = request.form["falw"]
        tmode = request.form["tmode"]
        tallow = request.form["talw"]
        expatriate = request.form.get("chk1")
        edf = request.form["edf"]
        months = request.form["month"]  
        medf = request.form["medf"]
        house = request.form["hint"]
        erel = request.form["erel"]
        mrel = request.form["mrel"]
        payment = request.form["mop"]
        medical = request.form["med"]
        working = request.form["optradio3"]
        if working == "No":
            lwork = request.form["lwork"]
        else:
            lwork = "0000-00-00"
        spbonus = request.form["spbonus"]
        wdays = request.form["wday"]

        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            query2 =""" INSERT INTO employee (
                EmployeeID,
                FirstName,
                LastName,
                Title,
                DOB,
                clocked,
                address,
                city,
                country,
                phone,
                mobile,
                fax,
                email,
                image,
                NICno,
                TaxAC,
                Bank,
                BankAC,
                Bankcode,
                report,
                NPS,
                Carbenefit,
                hire,
                salary,
                position,
                department,
                Subdepartment,
                Payescheme,
                Payepercentage,
                Localleave,
                Sickleave,
                Fixedallow,
                Travelmode,
                Travelallow,
                expatriate,
                EDF,
                months,
                MonthlyEDF,
                Houseinterest,
                Educationrel,
                Medicalrel,
                Paymentmode,
                medical,
                working,
                Lastwork,
                Specialbonus,
                Workingdays
              )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
              );"""
            
            # print(eid)
            # print(fname)
            # print(lname)
            # print(title)
            # print(dob)
            # print(clocked)
            # print(address)
            # print(city)
            # print(country)
            # print(phone)
            # print(mobile)
            # print(fax)
            # print(mail)
            # print(nic)
            # print(tax)
            # print(bank)
            # print(bank_ac)
            # print(code)
            # print(report)
            # print(nps)
            # print(car)
            # print(hire)
            # print(salary)
            # print(position)
            # print(dep)
            # print(sdep)
            # print(paye)
            # print(per)
            # print(lleave)
            # print(sleave)
            # print(fallow)
            # print(tmode)
            # print(tallow)
            # print(expatriate)
            # print(edf)
            # print(months)
            # print(medf)
            # print(house)
            # print(erel)
            # print(mrel)
            # print(payment)
            # print(medical)
            # print(working)
            # print(lwork)
            # print(spbonus)
            # print(wdays)
            # print()
            if(eimage != ""):
                image = eimage.convert('RGB')    
                if image and allowed_file(image.filename):
                    print("In Image If")
                    filename = secure_filename(image.filename)
                    filename=''.join(random.choices(string.ascii_lowercase +string.digits, k=20))
                    picture = Image.open(image)
                    picture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename+'.jpeg'), "JPEG", optimize = True, quality = 30)
                    print(filename)
            else:
                filename = ""
            # data1 = [eid, fname, lname, title, dob, clocked, address, city, country, phone, mobile, fax, mail,filename, nic, tax, bank, bank_ac, code, report, nps, car, hire, salary, position, dep, sdep, paye, per, lleave, sleave, fallow, tmode, tallow, expatriate, edf, months, medf, house, erel, mrel, payment, medical, working, lwork, spbonus, wdays]
            data1 = [eid, fname, lname, title, dob, clocked, address, city, country, phone, mobile, fax, mail, filename, nic, tax, bank, bank_ac, code, report, nps, car, hire, salary, position, dep, sdep, paye, per, lleave, sleave, fallow, tmode, tallow, expatriate, edf, months, medf, house, erel, mrel, payment, medical, working, lwork, spbonus, wdays]
            print("Before Query")
            cursor.execute(query2, data1)
            print("Insert Query Successfully")
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("employee.html")         

    # if request.method == "POST":
    #     employee_id = request.form['eid']
    #     first_name = request.form["fname"]
    #     last_name = request.form["lname"]
    #     name_title = request.form["title"]
    #     print("title : " + name_title)
    #     dob = request.form["dob"]
    #     print("DOB : " +dob)
    #     print(type(dob))
    #     clocked = request.form["optradio"]
    #     print("Clock : " +clocked)
    #     # address = request.form["add"]
    #     # city = request.form["city"]
    #     # country = request.form["con"]
    #     # phone = request.form["phn"]
    #     # mobile = request.form["mob"]
    #     # fax = request.form["fax"]
    #     # mail = request.form["mail"]
    #     # image = request.files["img"]
    #     # print("Image : " + image)

    #     # nic_no = request.form["nic"]
    #     # tax = request.form["tax"]
    #     # bank = request.form["bank"]
    #     # print("Bank : " + bank)
    #     # bank_ac = request.form["bac"]
    #     # bank_code = request.form["code"]
    #     # # report = request.form["rpt"]
    #     # report = ""
    #     # nps = request.form["optradio2"]
    #     car_benefit = request.form["car"]

    #     # hire = request.form["hire"]
    #     salary = request.form["sal"]
    #     # position = request.form["pos"]
    #     department = request.form["dep"]
    #     # print("Department : " + department)
    #     sub_department = request.form["sdep"]
    #     # print("Sub Department : " + sub_department)
    #     paye_scheme = request.form["psch"]
    #     # print("Payscheme : " + paye_scheme)
    #     percentage = request.form["per"]
    #     lleave = request.form["lleave"]
    #     sleave = request.form["sleave"]
    #     fixed_allow = request.form["falw"]
    #     travel_mode = request.form["tmode"]
    #     # print("Travel Mode : " + travel_mode)
    #     travel_allow = request.form["talw"]
    #     expatriate = request.form.get("chk1")
    #     edf = request.form["edf"]
    #     months = request.form["month"]  
    #     medf = request.form["medf"]
    #     house_interest = request.form["hint"]
    #     education_rel = request.form["erel"]
    #     medical_rel = request.form["mrel"]
    #     payment = request.form["mop"]
    #     # print("Payment Mode : " + payment)
    #     medical = request.form["med"]
    #     working = request.form["optradio3"]
    #     # print(working)
    #     if working == "No":
    #         last_work = request.form["lwork"]
    #     else:
    #         last_work = None
    #     special_bonus = request.form["spbonus"]
    #     working_days = request.form["wday"]
    #     # print()
    #     filename = []
    #     # print(len(filename))
    #     try:
    #         connection = mysql.connector.connect(host='localhost',
    #                                             database='payroll',
    #                                             user='google',
    #                                             password='password') # @ZodiaX1013
    #         cursor = connection.cursor(buffered=True) 

    #         query1 = f"SELECT EmployeeID FROM employee"
    #         cursor.execute(query1)
    #         usernames = cursor.fetchall()

    #         print("Data : ", usernames)
    #         for i in range(len(usernames)):
    #             # for j in range(len(usernames)):
    #             data2 = ''.join(usernames[i])
    #             print(data2)
    #             if(data2 == employee_id):
    #                 print("Already Exist")
    #                 fquery = "SELECT * FROM employee WHERE EMployeeID = %s"
    #                 cursor.execute(fquery, data2)
    #                 data = cursor.fetchall()

    #                 return render_template("employee.html", data=data)
    #                 # fquery1 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(fquery1, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])
                    
    #                 # fquery2 = "SELECT FirstName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(fquery2, data2)
    #                 # fname = cursor.fetchall()
    #                 # for i in range(len(fname)):
    #                 #     first = ''.join(fname[i])

    #                 # fquery3 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery4 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery5 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery6 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery7 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery8 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery9 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery10 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery11 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery12 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])

    #                 # fquery13 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
    #                 # cursor.execute(query4, data2)
    #                 # lname = cursor.fetchall()
    #                 # for i in range(len(lname)):
    #                 #     last = ''.join(lname[i])
                        

    #         # if image and allowed_file(image.filename):
    #         #     print("In Image If")
    #         #     filename = secure_filename(image.filename)
    #         #     filename=''.join(random.choices(string.ascii_lowercase +string.digits, k=20))
    #         #     picture = Image.open(image)
    #         #     picture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename+'.jpg'), "JPEG", optimize = True, quality = 30)
    #         #     print(filename)

    #         if not usernames:
    #             print("In IF")
    #             query2 = """INSERT INTO employee (
    #                 EmployeeID,
    #                 FirstName,
    #                 LastName,
    #                 Title,
    #                 DOB,
    #                 clocked,
    #                 address,
    #                 city,
    #                 country,
    #                 phone,
    #                 mobile,
    #                 fax,
    #                 email,
    #                 image,
    #                 NICno,
    #                 TaxAC,
    #                 Bank,
    #                 BankAC,
    #                 Bankcode,
    #                 report,
    #                 NPS,
    #                 Carbenefit,
    #                 hire,
    #                 salary,
    #                 position,
    #                 department,
    #                 Subdepartment,
    #                 Payescheme,
    #                 Payepercentage,
    #                 Localleave,
    #                 Sickleave,
    #                 Fixedallow,
    #                 Travelmode,
    #                 Travelallow,
    #                 expatriate,
    #                 EDF,
    #                 months,
    #                 MonthlyEDF,
    #                 Houseinterest,
    #                 Educationrel,
    #                 Medicalrel,
    #                 Paymentmode,
    #                 medical,
    #                 working,
    #                 Lastwork,
    #                 Specialbonus,
    #                 Workingdays
    #               )
    #             VALUES (
    #                 %s,                    
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s
    #               );"""
    #             # data = [employee_id, first_name, last_name, name_title, dob, clocked, address, city, country, phone, mobile, fax, mail, filename, nic_no, tax, bank, bank_ac, bank_code, report,nps, car_benefit, hire, salary, position, department, sub_department, paye_scheme, percentage, lleave, sleave, fixed_allow, travel_mode, travel_allow, expatriate, edf, months, medf, house_interest, education_rel, medical_rel, payment, medical, working, last_work, special_bonus, working_days]
    #             # print(query2)
    #             # cursor.execute(query2, data)

    #         else:
    #             print("In Else")
    #             # for i in range(len(usernames)):
    #             #     data2 = ''.join(usernames[i])
    #             #     print("Data 2 :" + data2)
    #             #     # print(data2[i])
    #             #     if data2 == employee_id:
    #             #         print("Employee Exist")

    #                     # query3 = "SELECT * FROM employee WHERE EmployeeID = {data2} "

    #                     # return render_template("employee.html")
                        
    #                     # cursor.execute(query3)
    #                     # data3 = cursor.fetchall()
    #                     # for i in range(len(data3)):
    #                         # data4 = ''.join(data3[i])
    #             query4 = """INSERT INTO employee (
    #                 EmployeeID,
    #                 FirstName,
    #                 LastName,
    #                 Title,
    #                 DOB,
    #                 clocked,
    #                 address,
    #                 city,
    #                 country,
    #                 phone,
    #                 mobile,
    #                 fax,
    #                 email,
    #                 image,
    #                 NICno,
    #                 TaxAC,
    #                 Bank,
    #                 BankAC,
    #                 Bankcode,
    #                 report,
    #                 NPS,
    #                 Carbenefit,
    #                 hire,
    #                 salary,
    #                 position,
    #                 department,
    #                 Subdepartment,
    #                 Payescheme,
    #                 Payepercentage,
    #                 Localleave,
    #                 Sickleave,
    #                 Fixedallow,
    #                 Travelmode,
    #                 Travelallow,
    #                 expatriate,
    #                 EDF,
    #                 months,
    #                 MonthlyEDF,
    #                 Houseinterest,
    #                 Educationrel,
    #                 Medicalrel,
    #                 Paymentmode,
    #                 medical,
    #                 working,
    #                 Lastwork,
    #                 Specialbonus,
    #                 Workingdays
    #               )
    #             VALUES (
    #                 %s,                    
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s
    #               );"""
    #             # data5 = [employee_id, first_name, last_name, name_title, dob, clocked, address, city, country, phone, mobile, fax, mail, filename, nic_no, tax, bank, bank_ac, bank_code, report,nps, car_benefit, hire, salary, position, department, sub_department, paye_scheme, percentage, lleave, sleave, fixed_allow, travel_mode, travel_allow, expatriate, edf, months, medf, house_interest, education_rel, medical_rel, payment, medical, working, last_work, special_bonus, working_days]
    #             # print(query4)
    #             # cursor.execute(query4, data5)
            
    #         # length = len(data4)
    #         # print(data4)
    #         return render_template("employee.html")
    #     except Error as e:
    #         print("Error While connecting to MySQL : ", e)

    #     finally:
    #         connection.commit()
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")
    #     # return render_template() 
    # return render_template("employee.html")

@app.route("/salary", methods=["GET" , "POST"])
def salary():

    # Search Data
    if request.method == "POST" and request.form['action'] == 'search':
        eid = request.form["eid"]
        month = request.form["mon"]
        year = request.form["year"]
        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True) 

            # query1 = "SELECT salary FROM employee WHERE EmployeeID = %s"
            # data = [eid]
            # cursor.execute(query1, data)
            # sal = cursor.fetchall()
            # for i in range(len(sal)):
            #     salary = ''.join(sal[i])

            # query2 = "SELECT Specialbonus FROM employee WHERE EmployeeID = %s"            
            # cursor.execute(query2, data)
            # bonus = cursor.fetchall()
            # for i in range(len(bonus)):
            #     bns = ''.join(bonus[i])

            # query3 = "SELECT Carbenefit FROM employee WHERE EmployeeID = %s"
            # cursor.execute(query3,data)
            # car = cursor.fetchall()
            # for i in range(len(car)):
            #     cars = ''.join(car[i])

            # query4 = "SELECT EDF FROM employee WHERE EmployeeID = %s"
            # cursor.execute(query4, data)
            # medf = cursor.fetchall()
            # for i in range(len(medf)):
            #     edf = ''.join(medf[i])

            # query5 = "SELECT medical FROM employee WHERE EmployeeID = %s"
            # cursor.execute(query5, data)
            # med = cursor.fetchall()
            # for i in range(len(med)):
            #     med = ''.join(med[i])
            
            # query6 = "SELECT Travelallow FROM employee WHERE EmployeeID = %s"
            # cursor.execute(query6, data)
            # travel = cursor.fetchall()
            # for i in range(len(travel)):
            #     talw = ''.join(travel[i])

            # query7 = "SELECT FirstName FROM employee WHERE EmployeeID = %s"
            # cursor.execute(query7, data)
            # fname = cursor.fetchall()
            # for i in range(len(fname)):
            #     first = ''.join(fname[i])

            # query8 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
            # cursor.execute(query8, data)
            # lname = cursor.fetchall()
            # for i in range(len(lname)):
            #     last = ''.join(lname[i])
            
            # query9 = "SELECT Educationrel FROM employee WHERE EmployeeID = %s"
            # cursor.execute(query9, data)
            # education = cursor.fetchall()
            # for i in range(len(education)):
            #     edu = ''.join(education[i])

            # query10 = "SELECT Medicalrel FROM employee WHERE EmployeeID = %s"
            # cursor.execute(query10, data)
            # mrel = cursor.fetchall()
            # for i in range(len(mrel)):
            #     mrel = ''.join(mrel[i])

            # today = datetime.date.today()
            # first_day = today.replace(day=1)
            # last_month = first_day - datetime.timedelta(days=1)
            # lfirst_day = last_month.replace(day=1)
            # llast_month = lfirst_day - datetime.timedelta(days=1)
            # req_month = llast_month.strftime("%m")
            # str_month = " "
            # if req_month == '1'.zfill(2):
            #     str_month = "January"
            # elif req_month == '2'.zfill(2):
            #     str_month = "February"
            # elif req_month == '3'.zfill(2):
            #     str_month = "March"
            # elif req_month == '4'.zfill(2):
            #     str_month = "April"
            # elif req_month == '5'.zfill(2):
            #     str_month = "May"
            # elif req_month == '6'.zfill(2):
            #     str_month = "June"
            # elif req_month == '7'.zfill(2):
            #     str_month = "July"
            # elif req_month == '8'.zfill(2):
            #     str_month = "August"
            # elif req_month == '9'.zfill(2):
            #     str_month = "September"
            # elif req_month == '10'.zfill(2):
            #     str_month = "October"
            # elif req_month == '11'.zfill(2):
            #     str_month = "November"
            # elif req_month == '12'.zfill(2):
            #     str_month = "December"

            # data1 = [eid , str_month ]
            # query11 = "SELECT PAYE FROM payable WHERE EmployeeID = %s AND Month = %s"
            # cursor.execute(query11, data1)
            # paye = cursor.fetchall()
            # for i in range(len(paye)):
            #     paye = ''.join(paye[i])
            
            # query12 = "SELECT gross FROM payable WHERE EmployeeID = %s AND Month = %s"
            # cursor.execute(query12, data1)
            # gross = cursor.fetchall()
            # for i in range(len(gross)):
            #     gross = ''.join(gross[i])
            
            # query13 = "SELECT IET FROM payable WHERE EmployeeID = %s AND Month = %s"
            # cursor.execute(query13, data1)
            # IET = cursor.fetchall()
            # for i in range(len(IET)):
            #     IET = ''.join(IET[i])
            
            data1 = [eid, month]
            data2 = [eid]
            query1 = "SELECT BasicSalary From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query1, data1)
            basic = cursor.fetchall()
            for i in range(len(basic)):
                basic = ''.join(basic[i])

            query2 = "SELECT FixedAllow From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query2, data1)
            falw = cursor.fetchall()
            for i in range(len(falw)):
                falw = ''.join(falw[i])

            query3 = "SELECT OtherDeduction From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query3, data1)
            otherded = cursor.fetchall()
            for i in range(len(otherded)):
                otherded = ''.join(otherded[i])

            query4 = "SELECT Overtime From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query4, data1)
            ot = cursor.fetchall()
            for i in range(len(ot)):
                ot = ''.join(ot[i])

            query5 = "SELECT DiscBonus From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query5, data1)
            disc = cursor.fetchall()
            for i in range(len(disc)):
                disc = ''.join(disc[i])

            query6 = "SELECT NSFEmpee From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query6, data1)
            nsf = cursor.fetchall()
            for i in range(len(nsf)):
                nsf = ''.join(nsf[i])

            query7 = "SELECT OtherAllow From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query7, data1)
            oalw = cursor.fetchall()
            for i in range(len(oalw)):
                oalw = ''.join(oalw[i])

            query8 = "SELECT TaxableAllow From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query8, data1)
            tax = cursor.fetchall()
            for i in range(len(tax)):
                tax = ''.join(tax[i])

            query9 = "SELECT Medical From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query9, data1)
            med = cursor.fetchall()
            for i in range(len(med)):
                med = ''.join(med[i])

            query10 = "SELECT Transport From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query10, data1)
            tran = cursor.fetchall()
            for i in range(len(tran)):
                tran = ''.join(tran[i])

            query11 = "SELECT NTaxableAllow From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query11, data1)
            ntax = cursor.fetchall()
            for i in range(len(ntax)):
                ntax = ''.join(ntax[i])

            query12 = "SELECT EDF From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query12, data1)
            edf = cursor.fetchall()
            for i in range(len(edf)):
                edf = ''.join(edf[i])

            query13 = "SELECT Arrears From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query13, data1)
            arr = cursor.fetchall()
            for i in range(len(arr)):
                arr = ''.join(arr[i])

            query14 = "SELECT AttendanceBns From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query14, data1)
            att = cursor.fetchall()
            for i in range(len(att)):
                att = ''.join(att[i])

            query15 = "SELECT TravelAllow From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query15, data1)
            travel = cursor.fetchall()
            for i in range(len(travel)):
                travel = ''.join(travel[i])

            query16 = "SELECT EOY From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query16, data1)
            eoy = cursor.fetchall()
            for i in range(len(eoy)):
                eoy = ''.join(eoy[i])

            query17 = "SELECT Loan From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query17, data1)
            loan = cursor.fetchall()
            for i in range(len(loan)):
                loan = ''.join(loan[i])

            query18 = "SELECT CarBenefit From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query18, data1)
            car = cursor.fetchall()
            for i in range(len(car)):
                car = ''.join(car[i])

            query19 = "SELECT LeaveRef From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query19, data1)
            leave = cursor.fetchall()
            for i in range(len(leave)):
                leave = ''.join(leave[i])

            query20 = "SELECT SLevy From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query20, data1)
            slevy = cursor.fetchall()
            for i in range(len(slevy)):
                slevy = ''.join(slevy[i])

            query21 = "SELECT SpecialBns From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query21, data1)
            spebns = cursor.fetchall()
            for i in range(len(spebns)):
                spebns = ''.join(spebns[i])

            query22 = "SELECT Lateness From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query22, data1)
            late = cursor.fetchall()
            for i in range(len(late)):
                late = ''.join(late[i])

            query23 = "SELECT EducationRel From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query23, data1)
            edurel = cursor.fetchall()
            for i in range(len(edurel)):
                edurel = ''.join(edurel[i])

            query24 = "SELECT SpeProBns From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query24, data1)
            speprobns = cursor.fetchall()
            for i in range(len(speprobns)):
                speprobns = ''.join(speprobns[i])

            query25 = "SELECT NPS From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query25, data1)
            nps = cursor.fetchall()
            for i in range(len(nps)):
                nps = ''.join(nps[i])

            query26 = "SELECT MedicalRel From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query26, data1)
            medrel = cursor.fetchall()
            for i in range(len(medrel)):
                medrel = ''.join(medrel[i])

            query27 = "SELECT Payable From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query27, data1)
            payable = cursor.fetchall()
            for i in range(len(payable)):
                payable = ''.join(payable[i])

            query28 = "SELECT Deduction From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query28, data1)
            ded = cursor.fetchall()
            for i in range(len(ded)):
                ded = ''.join(ded[i])

            query29 = "SELECT NetPay From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query29, data1)
            net = cursor.fetchall()
            for i in range(len(net)):
                net = ''.join(net[i])

            query31 = "SELECT CurrentGross From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query31, data1)
            cgross = cursor.fetchall()
            for i in range(len(cgross)):
                cgross = ''.join(cgross[i])

            query32 = "SELECT PrevGross From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query32, data1)
            pgross = cursor.fetchall()
            for i in range(len(pgross)):
                pgross = ''.join(pgross[i])

            query33 = "SELECT IET From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query33, data1)
            iet = cursor.fetchall()
            for i in range(len(iet)):
                iet = ''.join(iet[i])

            query34 = "SELECT NetCh From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query34, data1)
            netch = cursor.fetchall()
            for i in range(len(netch)):
                netch = ''.join(netch[i])

            query35 = "SELECT CurrentPAYE From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query35, data1)
            cpaye = cursor.fetchall()
            for i in range(len(cpaye)):
                cpaye = ''.join(cpaye[i])

            query36 = "SELECT PrevPAYE From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query36, data1)
            ppaye = cursor.fetchall()
            for i in range(len(ppaye)):
                ppaye = ''.join(ppaye[i])

            query37 = "SELECT PAYE From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query37, data1)
            paye = cursor.fetchall()
            for i in range(len(paye)):
                paye = ''.join(paye[i])

            query38 = "SELECT eCSG From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query38, data1)
            ecsg = cursor.fetchall()
            for i in range(len(ecsg)):
                ecsg = ''.join(ecsg[i])

            query39 = "SELECT eNSF From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query39, data1)
            ensf = cursor.fetchall()
            for i in range(len(ensf)):
                ensf = ''.join(ensf[i])

            query40 = "SELECT eLevy From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query40, data1)
            elevy = cursor.fetchall()
            for i in range(len(elevy)):
                elevy = ''.join(elevy[i])

            query41 = "SELECT Absences From salary WHERE EmployeeID = %s AND Month = %s"
            cursor.execute(query41, data1)
            absence = cursor.fetchall()
            for i in range(len(absence)):
                absence = ''.join(absence[i])

            query42 = "SELECT FirstName From employee WHERE EmployeeID = %s"
            cursor.execute(query42, data2)
            fname = cursor.fetchall()
            for i in range(len(fname)):
                fname = ''.join(fname[i])

            query43 = "SELECT LastName From employee WHERE EmployeeID = %s"
            cursor.execute(query43, data2)
            lname = cursor.fetchall()
            for i in range(len(lname)):
                lname = ''.join(lname[i])

            query44 = "SELECT position From employee WHERE EmployeeID = %s"
            cursor.execute(query44, data2)
            pos = cursor.fetchall()
            for i in range(len(pos)):
                pos = ''.join(pos[i])
            
            return render_template("salary.html", basic=basic, falw=falw, otherded=otherded, ot=ot, disc=disc, nsf=nsf, oalw=oalw, tax=tax, med=med, tran=tran, ntax=ntax, edf=edf, arr=arr, att=att, travel=travel, eoy=eoy, loan=loan, car=car, leave=leave, slevy=slevy, spebns=spebns, late=late, edurel=edurel, speprobns=speprobns, nps=nps, medrel=medrel, payable=payable, ded=ded, net=net, cgross=cgross, pgross=pgross, iet=iet, netch=netch, cpaye=cpaye, ppaye=ppaye, paye=paye, ecsg=ecsg, ensf=ensf, elevy=elevy, absence=absence, eid=eid, fname=fname, lname=lname, pos=pos, month=month, year=year)
            # return render_template("salary.html", sal=salary, bonus=bns, car=cars, edf=edf, med = med, travel = talw, eid = eid, fname=first, lname = last, edu=edu, paye=paye, gross=gross, IET=IET, mrel=mrel)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")   
    
    # Save To Database
    elif request.method == "POST" and request.form['action'] == 'save':
        
        fixedAlw = request.form["falw2"]
        otherDed = request.form["oded2"]
        overtime = request.form["ot2"]
        discBns = request.form["dbns2"]
        NSF = request.form["nsf"]
        otherAlw = request.form["oalw2"]
        tax = request.form["txdes2"]
        medical = request.form["med2"]
        transport = request.form["tran2"]
        ntax = request.form["ntxdes2"]
        edf = request.form["edf"]
        arrears = request.form["arr2"]
        attendance = request.form["atbns2"]
        travel = request.form["travel"]
        eoy = request.form["eoy"]
        loan = request.form["lrep"]
        car = request.form["car"]
        leaveRef = request.form["lref2"]
        paye = request.form["paye3"]
        slevy = request.form["levy"]
        speBns = request.form["spbonus2"]
        lateness = request.form["late"]
        educationRel = request.form["edu"]
        SpeProBns = request.form["spbonus3"]
        NPS = request.form["nps"]
        medicalRel = request.form["mrel"]
        Payable = request.form["pay"]
        Deduction = request.form["ded"]
        Net = request.form["npay"]
        cgross = request.form["cgrs"]
        pgross = request.form["pgrs"]
        iet = request.form["iet"]
        netch = request.form["netch"]
        cpaye = request.form["paye2"]
        ppaye = request.form["ppaye"]
        ecsg = request.form["nps2"]
        ensf = request.form["nsf2"]
        elevy = request.form["ivbt"]
        absence = request.form["abs"]
        month = request.form["mon"]
        fname = request.form["fname"]
        eid = request.form["eid"]
        UNQ = eid + " " + fname
        # lname = request.form["lname"]
        # print("Lname : ", lname)
        # print(lname)
        # fname = request.form["fname"]
        # flname = lname + " " + fname
        # print("Flname " , flname)
        # basic = request.form["bsal"]
        # arrears = request.form["arr2"]
        # tax = request.form["txdes2"]
        # ntax = request.form["ntxdes2"]
        # overseas = int(tax) + int(ntax)
        # travel = request.form["travel"]
        # other = request.form["oalw2"]
        # gross = request.form["cgrs"]
        # paye = request.form["paye"]
        # csg = request.form["nps"] 
        # nsf = request.form["nsf"] #nsf = nps = 213
        # medical = request.form["med2"]
        # levy = request.form["levy"]
        # tnet = request.form["npay"]
        # car = request.form["car"]
        # net = int(tnet) - int(levy)
        # net = int(tnet) + int(car)
        # print(net)
        # edf = request.form["edf"]
        # ot = request.form["ot2"]
        # travel = request.form["tran2"]
        # eoy = request.form["eoy"]
        # leaveRef = request.form["lref2"]
        # speBonus = request.form["spbonus2"]
        # speProBonus = request.form["spbonus3"]
        # fixedAlw = request.form["falw2"]
        # DiscBonus = request.form["dbns2"]
        # AttendanceBns = request.form["atbns2"]
        # loan = request.form["lrep"]
        # lateness = request.form["am4"]
        # otherDeduction = request.form["oded2"]
        # payable = request.form["pay"]
        # deduction = request.form["ded"]
        # ot1hour = request.form["hr1"]
        # ot1amt = request.form["am1"]
        # ot2hour = request.form["hr2"]
        # ot2amt = request.form["am2"]
        # ot3hour = request.form["hr3"]
        # ot3amt = request.form["am3"]
        # educationRel = request.form["edu"]
        # latehr = request.form["hr4"]

        # mon = request.form["mon"]
        # year = request.form["year"]
        # IET = request.form["iet"]
        # unqcode = lname + " " + mon

        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            query1 = """UPDATE salary
                        SET 
                        FixedAllow = %s,
                        OtherDeduction = %s,
                        Overtime = %s,
                        DiscBonus = %s,
                        NSFEmpee = %s,
                        OtherAllow = %s,
                        TaxableAllow = %s,
                        Medical = %s,
                        Transport = %s,
                        NTaxableAllow = %s,
                        EDF = %s,
                        Arrears = %s,
                        AttendanceBns = %s,
                        TravelAllow = %s,
                        EOY = %s,
                        Loan = %s,
                        CarBenefit = %s,
                        LeaveRef = %s,
                        SLevy = %s,
                        SpecialBns = %s,
                        Lateness = %s,
                        EducationRel = %s,
                        SpeProBns = %s,
                        NPS = %s,
                        MedicalRel = %s,
                        Payable = %s,
                        Deduction = %s,
                        NetPay = %s,
                        CurrentGross = %s,
                        PrevGross = %s,
                        IET = %s,
                        NetCh = %s,
                        CurrentPAYE = %s,
                        PrevPAYE = %s,
                        PAYE = %s,
                        eCSG = %s,
                        eNSF = %s,
                        eLevy = %s,
                        Absences = %s
                        WHERE 
                        UNQ = %s;"""
            data1 = [fixedAlw, otherDed, overtime, discBns, NSF, otherAlw, tax, medical, transport, ntax, edf, arrears, attendance, transport, eoy, loan, car, leaveRef, slevy, speBns, lateness, educationRel, SpeProBns, NPS, medicalRel, Payable, Deduction, Net, cgross, pgross, iet, netch, cpaye, ppaye, paye, ecsg, ensf, elevy, absence, UNQ ]
            
            cursor.execute(query1, data1)
            print("Database Updated Successfully")
            return render_template("paysheet.html")

            # query12 = "SELECT UNQ FROM payable"
            # cursor.execute(query12)

            # UNQ = cursor.fetchall()
            # print(UNQ)
            # for i in range(len(UNQ)):
            #     udata = ''.join(UNQ[i])
            # print(udata)
            # con = 0
            # for i in udata:
            #     if unqcode == i:
            #         con = 1
            #         break
            #     else:
            #         con = 0
                
            # Payable Table
            # if con == 0:
            #     query11 = """INSERT INTO payable (
            #         EmployeeID,
            #         BasicSalary,
            #         Overtime,
            #         OtherAllow,
            #         Transport,
            #         Arrears,
            #         EOY,
            #         LeaveRef,
            #         SpeBonus,
            #         SpeProBonus,
            #         FixedAllow,
            #         DiscBonus,
            #         TaxAllow,
            #         NTaxAllow,
            #         AttBonus,
            #         Loan,
            #         PAYE,
            #         Lateness,
            #         NPS,
            #         OtherDed,
            #         NSF,
            #         Medical,
            #         EDF,
            #         travel,
            #         car,
            #         SLevy,
            #         EducationRelief,
            #         gross,
            #         Payable,
            #         Deduction,
            #         NetPay,
            #         OT1hr,
            #         OT1amt,
            #         OT2hr,
            #         OT2amt,
            #         OT3hr,
            #         OT3amt,
            #         LatenessHr,
            #         Month,
            #         Year,
            #         IET,
            #         UNQ
            #     )
            #     VALUES (
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s,
            #         %s
            #     );"""
                
            #     data3 = [eid, basic, ot, other, travel, arrears, eoy, leaveRef, speBonus, speProBonus, fixedAlw, DiscBonus, tax, ntax, AttendanceBns, loan, paye, lateness, csg, otherDeduction, nsf, medical, edf, travel, car, levy, educationRel, gross, payable, deduction, net, ot1hour, ot1amt, ot2hour, ot2amt, ot3hour, ot3amt, latehr, mon, year, IET, unqcode]

            #     cursor.execute(query11 , data3)
            #     print("Payable Query Executed")

            # Paysheet Table
            # query10 = """INSERT INTO paysheet (
            #     EmployeeID,
            #     EmployeeName,
            #     BasicSalary,
            #     Arrears,
            #     Overseas,
            #     TravelAllow,
            #     OtherAllow,
            #     Gross,
            #     PAYE,
            #     CSG,
            #     NSF,
            #     Medical,
            #     SLevy,
            #     Net,
            #     Month,
            #     department
            #   )
            # VALUES (
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s,
            #     %s
            #   );"""
            
            # dep = "Demo"
            # data2 = [eid, flname, basic,arrears, overseas, travel, other, gross, paye, csg, nsf,medical, levy, net, mon, dep]
            # cursor.execute(query10, data2)
            # print("Insert Query Execute successfully")

        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("salary.html")
    

@app.route("/dashboard", methods=["GET" , "POST"])
def dashboard():
    try:
        connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
        cursor = connection.cursor(buffered=True) 

        # query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'employee'"
        # cursor.execute(query1)
        # column_name = cursor.fetchall()

        query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'employee' AND ORDINAL_POSITION between 2 AND 4;"
        cursor.execute(query1)
        column_name = cursor.fetchall()
        heading_data = []
        data = []
        print(len(column_name))
        for i in range(len(column_name)):
            print("i : " , i)
            # print("j : ", j)
            data = ''.join(column_name[i])
            print("Data :" + data)
            heading_data.append(data)
        
        print(column_name)
        print(heading_data)

        query2 = f"SELECT EmployeeID, FirstName, LastName FROM employee"
        cursor.execute(query2)
        table_data = cursor.fetchall()

        print(table_data)
        return render_template("dashboard.html", heading = heading_data, data = table_data)
    except Error as e:
            print("Error While connecting to MySQL : ", e)
    finally:
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

    return render_template("dashboard.html")

@app.route("/leave", methods=["GET" , "POST", "PUT"])
def leave():
    if request.method == 'POST':
        eid = request.form['eid']
        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True) 

            # query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'employee'"
            # cursor.execute(query1)
            # column_name = cursor.fetchall()

            query1 = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'LeaveData' AND ORDINAL_POSITION BETWEEN 3 AND 5;"
            cursor.execute(query1)
            column_name = cursor.fetchall()
            heading_data = []
            data = []
            print(len(column_name))
            for i in range(len(column_name)):
                print("i : " , i)
                # print("j : ", j)
                data = ''.join(column_name[i])
                print("Data :" + data)
                heading_data.append(data)
            
            print(column_name)
            print(heading_data)

            query2 = f"SELECT Date, LeaveType, LeaveDays FROM LeaveData;"
            cursor.execute(query2)
            table_data = cursor.fetchall()

            print(table_data)

            
            print(eid)
            query3 = f"SELECT Localleave, Sickleave FROM employee WHERE EmployeeID = '{eid}'"
            print(query3)
            cursor.execute(query3)
            leaves = cursor.fetchall()
            print(leaves)
            
            # leave_data = []
            # for i in range(len(leaves)):
            #     print("i : " , i)
            #     # print("j : ", j)
            #     data2 = ''.join(leaves[i])
            #     print("Data2 :" + data2)
            #     leave_data.append(data2)
            # print(leave_data[0])
            # print(leaves[0][0])

            query4 = f"SELECT EmployeeID, FirstName, LastName, Position FROM employee WHERE EmployeeID = '{eid}'"
            cursor.execute(query4)
            personal_data = cursor.fetchall()
            print(personal_data)
            print(personal_data[0][0])

            return render_template("leave.html", heading = heading_data, data = table_data, leaves = leaves, eid=eid,personal = personal_data )
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    print("Before")
    return render_template("leave.html")

@app.route("/lock_salary", methods=["GET" , "POST"])
def lock_salary():
    month_data = request.form.get('year')
    if month_data == '2022-10':
        print("Success")
    print(month_data)
    return render_template("lock-salary.html")

@app.route("/process_salary", methods=["GET" , "POST"])
def process_salary():
    if request.method == "POST":
        eid = request.form["eid"]
        month = request.form["mon"]
        year = request.form["year"]
        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)
            if eid == "PP01":
                # print("Do Somthing")
                # query1 = "SELECT Carbenefit, salary, Fixedallow, Travelallow, EDF, MonthlyEDF, Houseinterest, Educationrel, Medicalrel, medical, Specialbonus FROM employee"
                # query1 = "SELECT EmployeeID FROM employee"
                # cursor.execute(query1)
                # data1 = cursor.fetchall()

                # tdata1 = []
                # employee_id = []
                # for i in range(len(data1)):
                #     tdata1 = ''.join(data1[i])
                #     employee_id.append(tdata1)
                # print(employee_id)
                # print(data1)
                query1 = "SELECT FirstName FROM employee WHERE EmployeeID = %s"
                data = [eid]
                cursor.execute(query1,data)
                fname = cursor.fetchall()
                for i in range(len(fname)):
                    fname = ''.join(fname[i])

                query2 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
                cursor.execute(query2,data)
                lname = cursor.fetchall()
                for i in range(len(lname)):
                    lname = ''.join(lname[i])

                flname = lname + " " + fname
                UNQ = eid + " " + fname

                query3 = "SELECT Carbenefit, salary, Fixedallow, Travelallow, EDF, Houseinterest, Educationrel, Medicalrel, medical, Specialbonus FROM employee WHERE EmployeeID = %s "
                
                cursor.execute(query3, data)
                emp_data = cursor.fetchall()
                # print("Employee Data : \n " , emp_data)

                # print("\n", emp_data[0])
                emp_data2 = list(emp_data[0])

                # print("\n", emp_data2)

                car = int(emp_data2[0])
                basic = int(emp_data2[1])
                fixAllow = int(emp_data2[2])
                travel = int(emp_data2[3])
                edf = int(emp_data2[4])
                house = int(emp_data2[5])
                education = int(emp_data2[6])
                Medicalrel = int(emp_data2[7])
                medical = int(emp_data2[8])
                SpeProBns = int(emp_data2[9])

                # Not Defined Values
                arrears = 0
                OT = 0
                otherAllow = 0
                tax = 0
                ntax = 0
                overseas = tax + ntax
                pgross = 0
                # Calculation Of All Salary
                # Get Elements


                # Calcutations
                gross = basic + arrears + OT + travel + otherAllow + tax + car + fixAllow + SpeProBns + travel
                tgross = basic + arrears + OT + travel + otherAllow + overseas + fixAllow + SpeProBns

                temp = basic * 0.06

                if temp > overseas:
                    payable = round(gross - car)
                else:
                    payable = round(gross - car + ntax)
                
                # For IET
                IET = round( (edf + education + Medicalrel) / 13)

                # For PAYE and CSG

                if basic > 50000:
                    PAYE = round( (tgross - IET) * 0.15)
                    CSG = round( basic * 0.03)
                else:
                    PAYE = round((tgross - IET) * 0.1)
                    CSG = round(basic * 0.015)
                
                # For NSF
                nsf = round(basic * 0.01)
                IVBT = round(basic * 0.015)

                if nsf > 213:
                    nsf = 213
                else:
                    nsf = round(nsf)
                
                # NSF For employer

                ensf = round(basic * 0.025)
                if ensf > 531:
                    ensf = 531
                else:
                    ensf = round(ensf)
                
                # S.Levy
                # emo = emolument
                emo = round(tgross * 13)
                if emo > 3000000:
                    levy = round((tgross - IET - (3000000/13)) * 0.25)

                    emo2 = round(emo * 0.1)
                    if emo2 > levy:
                        slevy = round(levy)
                    else:
                        slevy = round(emo2)
                else:
                    slevy = 0
                
                # Deduction
                deduction = round(PAYE + CSG + nsf + medical)
                net = round(payable - deduction)

                # NetCh in PAYE
                netch = round(tgross + pgross - IET)

                # NPS
                if basic > 50000:
                    nps = round(basic * 0.06)
                else:
                    nps = round(basic * 0.03)
                
                insert_query = """
                    INSERT INTO salary(
                    EmployeeID,
                    EmployeeName,
                    BasicSalary,
                    FixedAllow,
                    OtherDeduction,
                    Overtime,
                    DiscBonus,
                    NSFEmpee,
                    OtherAllow,
                    TaxableAllow,
                    Medical,
                    Transport,
                    NTaxableAllow,
                    EDF,
                    Arrears,
                    AttendanceBns,
                    TravelAllow,
                    EOY,
                    Loan,
                    CarBenefit,
                    LeaveRef,
                    SLevy,
                    SpecialBns,
                    Lateness,
                    EducationRel,                    
                    SpeProBns,
                    NPS,
                    MedicalRel,
                    Payable,
                    Deduction,
                    NetPay,
                    CurrentGross,
                    PrevGross,
                    IET,
                    NetCh,
                    CurrentPAYE,
                    PrevPAYE,
                    PAYE,
                    eCSG,
                    eNSF,
                    eLevy,
                    Absences,
                    Month,
                    Year,
                    UNQ
                    )

                    VALUES(
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                    );
                    """
                data1 = [eid, flname, basic , fixAllow, 0, OT, 0, nsf, otherAllow, tax, medical, 0, ntax, edf, arrears, 0, travel, 0, 0, car, 0, slevy, 0, 0, education, SpeProBns, CSG, Medicalrel, payable, deduction, net, tgross, pgross, IET, netch, PAYE, 0, PAYE, nps ,ensf, IVBT, 0, month, year, UNQ]
                
                cursor.execute(insert_query, data1)
                print("Insert Query Run Successfully")
                # return render_template("salary.html",sal = basic ,falw = fixAllow, ot = OT, nsf = nsf, olaw = otherAllow, tax = tax, med = medical, ntax = ntax, edf = edf, arr = arrears, travel = travel, car = car, slevy = slevy, edu = education, bonus = SpeProBns, csg = CSG, mrel = Medicalrel, pay = payable, ded = deduction, net = net, cgrs = tgross, pgrs = pgross, iet = IET, nch = netch, paye = PAYE, ensf = ensf, levy = IVBT)
                print(data1)
                str1 = json.dumps(data1)

                # return str1
                msg = "Processing Complete"
                return render_template("process.html", msg = msg)
            else:
                print("Do Something Else")
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")    
    return render_template("process.html")

# @app.route("/paysheet", methods=["GET" , "POST"])
# def paysheet():
#     rendered = render_template('payslip.html',filename='css/style.css')
#     options = {
#     'page-size': 'A3',
#     'margin-top': '0.75in',
#     'margin-right': '0.2in',
#     'margin-bottom': '0.75in',
#     'margin-left': '0.2in',
#     'encoding': "UTF-8",
#     'custom-header': [
#         ('Accept-Encoding', 'gzip')
#     ],
#     'no-outline': None
# }
#     pdf = pdfkit.from_string(rendered,options=options,verbose=True)

    
#     responses = make_response(pdf)
#     responses.headers['Content-Type'] = 'application/pdf'
#     responses.headers['Content-Disposition'] = 'inline; filename=download.pdf'

#     # # pdfkit.from_url('', 'out.pdf')

#     # return render_template_to_pdf('test.html', download=True, save=False, param='hello')
#     return responses
    # return render_template("paysheet.html")

@app.route("/payslip", methods=["GET" , "POST"])
def payslip():
    if request.method == "POST":
        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            # query1 = "SELECT * FROM paysheet"
            # print("Before Query1")
            # query1 = "SELECT FirstName, LastName, NICno, position, department FROM employee"

            query1 = "SELECT FirstName FROM employee"
            cursor.execute(query1)
            data1 = cursor.fetchall()
            print(data1)
            tdata1 = []
            fname = []
            for i in range(len(data1)):
                print("i : " , i)
                # print("j : ", j)
                tdata1 = ''.join(data1[i])
                print("Data :" + tdata1)
                fname.append(tdata1)

            query2 = "SELECT LastName FROM employee"
            cursor.execute(query2)
            data2 = cursor.fetchall()
            print(data2)
            tdata2 = []
            lname = []
            for i in range(len(data2)):
                print("i : " , i)
                # print("j : ", j)
                tdata2 = ''.join(data2[i])
                print("Data :" + tdata2)
                lname.append(tdata2)

            flname = [i +j for i,j in zip(lname,fname)]
            print(flname)
            # for i in range(len(fname)):
            #     tdata = ' '.join()

            # for i in range(len(data1)):
            #     tdata1 = ''.join(data1[i])
            #     data2.append(data1)
            #     # print(data1)

            # print(fname)            
            # print("After Query1")


            # print("Before Query2")
            

            #     print("After Join \n" , data1)

            # query2 = "SELECT BasicSalary, OtherAllow, EOY, travel, OT1hr, OT1amt, OT2hr, OT2amt, OT3hr, OT3amt, Arrears, LeaveRef, SpeProBonus, Lateness, PAYE, Loan, OtherDed, NPS, NSF, Medical, LatenessHr, Lateness, SLevy FROM payable "
            # cursor.execute(query2)
            # data2 = cursor.fetchall()
            
            # print("After Query2")

            # print(data2)
            # for i in range(len(data2)):
            #     print("i : " , i)
            #     # print("j : ", j)
            #     data2 = ''.join(data2[i])

            # print("After Join \n" , data2)

            # session["data1"] = data1
            # session["data2"] = data2
            return "Ready"
            # return render_template("payslip2.html", data1=data1, data2=data2)
            # return render_template("payslip2.html")
        except Error as e:
            print("Error While connecting to MySQL : ", e )
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("payslip2.html")

@app.route("/paysheet", methods=["GET" , "POST"])
def paysheet():

    # For Pdf Generate
    if request.method == "POST" and request.form['action'] == 'pdf':
        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            # query1 = "SELECT * FROM paysheet"
            # query1 = "SELECT EmployeeName, BasicSalary, Arrears, Overseas, TravelAllow, OtherAllow, Gross, PAYE, CSG, NSF, Medical, SLevy, Net FROM paysheet"
            query1 = "SELECT EmployeeName, BasicSalary, Arrears, Overtime, LeaveRef, EOY, TravelAllow, OtherAllow, Payable, Absences, CurrentPAYE, NPS, NSFEmpee, Medical, SLevy, Lateness, Deduction, NetPay FROM salary"
            cursor.execute(query1)
            data = cursor.fetchall()
            print(data)
            session["data"] = data
            return render_template("paysheet2.html", data=data)
            # return redirect(url_for('download', data = data))
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        

    # For Excel Generate

    if request.method == "POST" and request.form['action'] == 'excel':
        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            # query1 = "SELECT * FROM paysheet"
            query1 = "SELECT EmployeeName, BasicSalary, Arrears, Overseas, TravelAllow, OtherAllow, Gross, PAYE, CSG, NSF, Medical, SLevy, Net FROM paysheet"
            cursor.execute(query1)
            data = cursor.fetchall()
            print(data)
            session["data"] = data
            return render_template("paysheet2.html", data=data)
        except Error as e:
            print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




    # if request.method == 'POST':
    #     print("Paysheet")

    #     eid = request.form["eid"]
    #     fname = request.form["fname"]
    #     lname = request.form["lname"]
    #     flname = fname + lname
    #     basic = request.form["basic"]
    #     arr = request.form["arr"]
    #     overseas = request.form["over"]
    #     travel = request.form["travel"]
    #     other = request.form["other"]
    #     gross = request.form["med"]
    #     paye = request.form["gross"]
    #     csg = request.form["paye"]
    #     nsf = request.form["csg"]
    #     med = request.form["nsf"]
    #     levy = request.form["levy"]
    #     net = request.form["net"]

    #     try:
    #         connection = mysql.connector.connect(host='localhost',
    #                                             database='payroll',
    #                                             user='google',
    #                                             password='password') # @ZodiaX1013
    #         cursor = connection.cursor(buffered=True)

    #         query1 = """INSERT INTO paysheet (
    #                     EmployeeID,
    #                     EmployeeName,
    #                     BasicSalary,
    #                     Arrears,
    #                     Overseas,
    #                     TravelAllow,
    #                     OtherAllow,
    #                     Gross,
    #                     PAYE,
    #                     CSG,
    #                     NSF,
    #                     Medical,
    #                     SLevy,
    #                     Net
    #                 )
    #                 VALUES (%s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s,
    #                 %s
    #                 );"""
    #         data = [eid, flname, basic, arr, overseas, travel, other, gross, paye, csg, nsf, med, levy, net]
    #         print("Before Query Executed")
    #         cursor.execute(query1,data)
    #         print("Query Executed")
    #     except Error as e:
    #             print("Error While connecting to MySQL : ", e)
    #     finally:
    #         connection.commit()
    #         cursor.close()
    #         connection.close()
    #         print("MySQL connection is closed")   
    
    return render_template("paysheet.html") 

@app.route('/download')
def download():
    if "data" in session:
        data = session["data"]
    rendered = render_template('paysheet2.html',filename='css/style.css', data=data)
    options = {
        'page-size': 'A3',
        'margin-top': '0.75in',
        'margin-right': '0.5in',
        'margin-bottom': '0.75in',
        'margin-left': '0.1in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'no-outline': None
    }
    
    pdfkit.from_string(rendered,'paysheet.pdf',options=options,verbose=True)
    # return render_template('paysheet2.html',filename='css/style.css', data=data)
    p = "./paysheet.pdf"
    return send_file(p, as_attachment=True)

    
if __name__ == "__main__":
    app.run(debug=True)