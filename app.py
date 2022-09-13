
import os


from flask import Flask, flash, request, redirect, url_for, render_template, session, send_file
from sqlalchemy import true
from werkzeug.utils import secure_filename
from PIL import Image
import os
import mysql.connector
from mysql.connector import *
import random, string
from datetime import date
import pdfkit

UPLOAD_FOLDER = 'static/images/'
WKHTMLTOPDF_PATH = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# wkhtmltopdf = Wkhtmltopdf(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','pdf'])
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf')

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
        image = request.files["img"]
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

            if image and allowed_file(image.filename):
                print("In Image If")
                filename = secure_filename(image.filename)
                filename=''.join(random.choices(string.ascii_lowercase +string.digits, k=20))
                picture = Image.open(image)
                picture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename+'.jpeg'), "JPEG", optimize = True, quality = 30)
                print(filename)
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
        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True) 

            query1 = "SELECT salary FROM employee WHERE EmployeeID = %s"
            data = [eid]
            cursor.execute(query1, data)
            sal = cursor.fetchall()
            for i in range(len(sal)):
                salary = ''.join(sal[i])

            query2 = "SELECT Specialbonus FROM employee WHERE EmployeeID = %s"            
            cursor.execute(query2, data)
            bonus = cursor.fetchall()
            for i in range(len(bonus)):
                bns = ''.join(bonus[i])

            query3 = "SELECT Carbenefit FROM employee WHERE EmployeeID = %s"
            cursor.execute(query3,data)
            car = cursor.fetchall()
            for i in range(len(car)):
                cars = ''.join(car[i])

            query4 = "SELECT EDF FROM employee WHERE EmployeeID = %s"
            cursor.execute(query4, data)
            medf = cursor.fetchall()
            for i in range(len(medf)):
                edf = ''.join(medf[i])

            query5 = "SELECT Medicalrel FROM employee WHERE EmployeeID = %s"
            cursor.execute(query5, data)
            med = cursor.fetchall()
            for i in range(len(med)):
                med2 = ''.join(med[i])
            
            query6 = "SELECT Travelallow FROM employee WHERE EmployeeID = %s"
            cursor.execute(query6, data)
            travel = cursor.fetchall()
            for i in range(len(travel)):
                talw = ''.join(travel[i])

            query7 = "SELECT FirstName FROM employee WHERE EmployeeID = %s"
            cursor.execute(query7, data)
            fname = cursor.fetchall()
            for i in range(len(fname)):
                first = ''.join(fname[i])

            query8 = "SELECT LastName FROM employee WHERE EmployeeID = %s"
            cursor.execute(query8, data)
            lname = cursor.fetchall()
            for i in range(len(lname)):
                last = ''.join(lname[i])
            
            query9 = "SELECT Educationrel FROM employee WHERE EmployeeID = %s"
            cursor.execute(query9, data)
            education = cursor.fetchall()
            for i in range(len(education)):
                edu = ''.join(education[i])

            return render_template("salary.html", sal=salary, bonus=bns, car=cars, edf=edf, med = med2, travel = talw, eid = eid, fname=first, lname = last, edu=edu)
        except Error as e:
                print("Error While connecting to MySQL : ", e)
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")   
    
    # Save To Database
    elif request.method == "POST" and request.form['action'] == 'save':
        eid = request.form["eid"]
        lname = request.form["lname"]
        # print("Lname : ", lname)
        # print(lname)
        fname = request.form["fname"]
        flname = lname + " " + fname
        # print("Flname " , flname)
        basic = request.form["bsal"]
        arrears = request.form["arr2"]
        tax = request.form["txdes2"]
        ntax = request.form["ntxdes2"]
        overseas = int(tax) + int(ntax)
        travel = request.form["travel"]
        other = request.form["oalw2"]
        gross = request.form["grs"]
        paye = request.form["paye"]
        csg = request.form["nps"] 
        nsf = request.form["nsf"] #nsf = nps = 213
        medical = request.form["med2"]
        levy = request.form["levy"]
        net = request.form["npay"]
        car = request.form["car"]
        # net = int(tnet) + int(car)
        # print(net)
        edf = request.form["edf"]
        ot = request.form["ot2"]
        transport = request.form["tran2"]
        eoy = request.form["eoy"]
        leaveRef = request.form["lref2"]
        speBonus = request.form["spbonus2"]
        speProBonus = request.form["spbonus3"]
        fixedAlw = request.form["falw2"]
        DiscBonus = request.form["dbns2"]
        AttendanceBns = request.form["atbns2"]
        loan = request.form["lrep"]
        lateness = request.form["am4"]
        otherDeduction = request.form["oded2"]
        payable = request.form["pay"]
        deduction = request.form["ded"]
        ot1hour = request.form["hr1"]
        ot1amt = request.form["am1"]
        ot2hour = request.form["hr2"]
        ot2amt = request.form["am2"]
        ot3hour = request.form["hr3"]
        ot3amt = request.form["am3"]
        educationRel = request.form["edu"]
        latehr = request.form["hr4"]

        try:
            connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                                database='heroku_dbb5a8d2e1d2fbf',
                                                user='b58f7064154253',
                                                password='32de4f18') # @ZodiaX1013
            cursor = connection.cursor(buffered=True)

            # Payable Table
            query11 = """INSERT INTO payable (
                EmployeeID,
                BasicSalary,
                Overtime,
                OtherAllow,
                Transport,
                Arrears,
                EOY,
                LeaveRef,
                SpeBonus,
                SpeProBonus,
                FixedAllow,
                DiscBonus,
                TaxAllow,
                NTaxAllow,
                AttBonus,
                Loan,
                PAYE,
                Lateness,
                NPS,
                OtherDed,
                NSF,
                Medical,
                EDF,
                travel,
                car,
                SLevy,
                EducationRelief,
                gross,
                Payable,
                Deduction,
                NetPay,
                OT1hr,
                OT1amt,
                OT2hr,
                OT2amt,
                OT3hr,
                OT3amt,
                LatenessHr
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
                %s
              );"""
            
            data3 = [eid, basic, ot, other, transport, arrears, eoy, leaveRef, speBonus, speProBonus, fixedAlw, DiscBonus, tax, ntax, AttendanceBns, loan, paye, lateness, csg, otherDeduction, nsf, medical, edf, travel, car, levy, educationRel, gross, payable, deduction, net, ot1hour, ot1amt, ot2hour, ot2amt, ot3hour, ot3amt, latehr]

            cursor.execute(query11 , data3)
            print("Payable Query Executed")

            # Paysheet Table
            query10 = """INSERT INTO paysheet (
                EmployeeID,
                EmployeeName,
                BasicSalary,
                Arrears,
                Overseas,
                TravelAllow,
                OtherAllow,
                Gross,
                PAYE,
                CSG,
                NSF,
                Medical,
                SLevy,
                Net,
                Date,
                department
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
                %s
              );"""
            
            cdate = date.today()
            dep = "Demo"
            data2 = [eid, flname, basic,arrears, overseas, travel, other, gross, paye, csg, nsf,medical, levy, net, cdate, dep]
            cursor.execute(query10, data2)
            print("Insert Query Execute successfully")

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
            print("Before Query1")
            query1 = "SELECT FirstName, LastName, NICno, position, department FROM employee WHERE EmployeeID = 'AB002' AND EmployeeID = 'AB003'"
            cursor.execute(query1)
            data1 = cursor.fetchall()
            print("After Query1")

            print(data1)

            print("Before Query2")
            for i in range(len(data1)):
                print("i : " , i)
                # print("j : ", j)
                data = ''.join(data1[i])

                print("After Join \n" , data1)

            query2 = "SELECT BasicSalary, OtherAllow, EOY, travel, OT1hr, OT1amt, OT2hr, OT2amt, OT3hr, OT3amt, Arrears, LeaveRef, SpeProBonus, Lateness, PAYE, Loan, OtherDed, NPS, NSF, Medical, LatenessHr, Lateness, SLevy FROM payable "
            cursor.execute(query2)
            data2 = cursor.fetchall()
            
            print("After Query2")

            print(data2)
            for i in range(len(data2)):
                print("i : " , i)
                # print("j : ", j)
                data = ''.join(data2[i])

            print("After Join \n" , data2)

            session["data1"] = data1
            session["data2"] = data2
            return "Successful"
            # return render_template("payslip2.html", data1=data1, data2=data2)
        except Error as e:
            print("Error While connecting to MySQL : ", e )
        finally:
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template("payslip.html")

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
            query1 = "SELECT EmployeeName, BasicSalary, Arrears, Overseas, TravelAllow, OtherAllow, Gross, PAYE, CSG, NSF, Medical, SLevy, Net FROM paysheet"
            cursor.execute(query1)
            data = cursor.fetchall()
            print(data)
            session["data"] = data
            return redirect(url_for('download', data = data))
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
    app.run(debug=true)