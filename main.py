import pymysql
from app import app
from tables import Customer, Employee, Deliverable
from connection import mysql
from flask import flash, session, render_template, request, redirect

@app.route('/table_list')
def show_tables():
    return render_template('table_list.html')



@app.route('/')
def index():
    if 'email' in session:
        username = session['email']
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to logout</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + "click here to login</b></a>"


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')


@app.route('/submit', methods=['POST'])
def login_submit():
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    # validate the received values
    if _email and _password and request.method == 'POST':
        # check user exists
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM tbl_user WHERE user_email=%s"
        sql_where = (_email,)
        cursor.execute(sql, sql_where)
        row = cursor.fetchone()
        if row:
            if row[3] == _password:
                session['email'] = row[1]
                cursor.close()
                conn.close()
                return redirect('/table_list')
            else:
                flash('Invalid password!')
                return redirect('/login')
        else:
            flash('Invalid email/password!')
            return redirect('/login')


@app.route('/new_customer')
def add_customer_view():
    return render_template('add_customer.html')


@app.route('/add_customer', methods=['POST'])
def add_customer():
    try:
        _customer_id = request.form['inputCustomerID']
        _customer_name = request.form['inputCustomerName']
        _street_name = request.form['inputStreet']
        _city = request.form['inputCity']
        _zipcode = request.form['inputZipcode']
        _phone_number = request.form['inputPhoneNumber']
        _employee_id = request.form['inputEmployeeID']
        # validate the received values
        if _customer_id and _customer_name and _street_name and _city and _zipcode and _phone_number and _employee_id and request.method == 'POST':
            sql = "INSERT INTO customer(customer_id, customer_name, street_name, city, zipcode, phone_number, employee_id) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            data = (_customer_id, _customer_name, _street_name, _city, _zipcode, _phone_number, _employee_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Completed: Customer added.')
            return redirect('/customers')
        else:
            return 'Error while adding customer'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/customers')
def customers():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM customer")
        rows = cursor.fetchall()
        table = Customer(rows)
        table.border = True
        return render_template('customer.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit_customer/<int:id>')
def edit_customer(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM customer WHERE customer_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('edit_customer.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_customer', methods=['POST'])
def update_customer():
    try:
        _customer_id = request.form['inputCustomerID']
        _customer_name = request.form['inputCustomerName']
        _street_name = request.form['inputStreet']
        _city = request.form['inputCity']
        _zipcode = request.form['inputZipcode']
        _phone_number = request.form['inputPhoneNumber']
        _employee_id = request.form['inputEmployeeID']
        # validate the received values
        if _customer_id and _customer_name and _street_name and _city and _zipcode and _phone_number and _employee_id and request.method == 'POST':
            sql = "UPDATE customer SET customer_name=%s, street_name=%s, city=%s, zipcode=%s, phone_number%s, employee_id=%s WHERE customer_id=%s"
            data = (_customer_id, _customer_name, _street_name, _city, _zipcode, _phone_number, _employee_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Customer information updated successfully!')
            return redirect('/customers')
        else:
            return 'Error while updating customer'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_customer/<int:id>')
def delete_customer(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customer WHERE customer_id=%s", (id,))
        conn.commit()
        flash('Customer deleted successfully!')
        return redirect('/customers')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


'''
##################################################################################################################
'''
@app.route('/new_employee')
def add_employee_view():
    return render_template('add_employee.html')


@app.route('/add_employee', methods=['POST'])
def add_employee():
    try:
        _employee_id = request.form['inputEmployeeID']
        _ssn = request.form['inputSSN']
        _employee_name = request.form['inputEmployeeName']
        _department = request.form['inputDepartment']
        _dept_position = request.form['inputDeptPosition']
        _date_of_entry = request.form['inputDateOfEntry']

        if _employee_id and _ssn and _employee_name and _department and _dept_position and _date_of_entry and request.method == 'POST':
            sql = "INSERT INTO employee(employee_id, ssn, employee_name, department, dept_position, date_of_entry) VALUES(%s, %s, %s, %s, %s, %s)"
            data = (_employee_id, _ssn, _employee_name, _department, _dept_position, _date_of_entry)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Completed: Employee added.')
            return redirect('/employees')
        else:
            return 'Error while adding employee'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/employees')
def employees():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()
        table = Employee(rows)
        table.border = True
        return render_template('employee.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit_employee/<int:id>')
def edit_employee(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employee WHERE employee_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('edit_employee.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_employee', methods=['POST'])
def update_employee():
    try:
        _employee_id = request.form['inputEmployeeID']
        _ssn = request.form['inputSSN']
        _employee_name = request.form['inputEmployeeName']
        _department = request.form['inputDepartment']
        _dept_position = request.form['inputDeptPosition']
        _date_of_entry = request.form['inputDateOfEntry']
        # validate the received values
        if _employee_id and _ssn and _employee_name and _dept_position and _date_of_entry and request.method == 'POST':
            sql = "UPDATE employee SET employee_id=%s, ssn=%s, employee_name=%s, dept_position=%s, phone_number%s, employee_id=%s WHERE employee_id=%s"
            data = (_employee_id, _ssn, _employee_name, _department, _dept_position, _date_of_entry)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Employee information updated successfully!')
            return redirect('/employees')
        else:
            return 'Error while updating employee'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_employee/<int:id>')
def delete_employee(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employee WHERE employee_id=%s", (id,))
        conn.commit()
        flash('Employee deleted successfully!')
        return redirect('/employees')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



'''
##################################################################################################################
'''

@app.route('/new_deliverable')
def add_deliverable_view():
    return render_template('add_deliverable.html')


@app.route('/add_deliverable', methods=['POST'])
def add_deliverable():
    try:
        _deliverable_id = request.form['inputDeliverableID']
        _order_date = request.form['inputOrderDate']
        _delivery_date = request.form['inputDeliveryDate']
        _customer_id = request.form['inputCustomerID']
        _employee_id = request.form['inputEmployeeID']


        if _deliverable_id and _order_date and _delivery_date and _customer_id and _employee_id and request.method == 'POST':
            sql = "INSERT INTO deliverable(deliverable_id, order_date, delivery_date, customer_id, employee_id) VALUES(%s, %s, %s, %s, %s)"
            data = (_deliverable_id, _order_date, _delivery_date, _customer_id, _employee_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Completed: Deliverable added.')
            return redirect('/deliverables')
        else:
            return 'Error while adding deliverable'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/deliverables')
def deliverables():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM deliverable")
        rows = cursor.fetchall()
        table = Deliverable(rows)
        table.border = True
        return render_template('deliverable.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit_deliverable/<int:id>')
def edit_deliverable(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM deliverable WHERE deliverable_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('edit_deliverable.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update_deliverable', methods=['POST'])
def update_deliverable():
    try:
        _deliverable_id = request.form['inputDeliverableID']
        _order_date = request.form['inputOrderDate']
        _delivery_date = request.form['inputDeliveryDate']
        _customer_id = request.form['inputCustomerID']
        _employee_id = request.form['inputEmployeeID']


        if _deliverable_id and _order_date and _delivery_date and _customer_id and _employee_id and request.method == 'POST':
            sql = "UPDATE deliverable SET deliverable_id=%s, order_date=%s, delivery_date=%s, customer_id=%s, employee_id%s WHERE deliverable_id=%s"
            data = (_deliverable_id, _order_date, _delivery_date, _customer_id, _employee_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('Deliverable information updated successfully!')
            return redirect('/deliverables')
        else:
            return 'Error while updating deliverable'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete_deliverable/<int:id>')
def delete_deliverable(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM deliverable WHERE deliverable_id=%s", (id,))
        conn.commit()
        flash('Deliverable deleted successfully!')
        return redirect('/deliverables')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

'''
############################################Special Queries###########################################################
'''
@app.route('/long_term_employees')
def long_term_employees():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM smart_star.employee WHERE date_of_entry < '2010-01-01 00:00:00'")
        rows = cursor.fetchall()
        table = Employee(rows)
        table.border = True
        return render_template('special_queries.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    app.run()
