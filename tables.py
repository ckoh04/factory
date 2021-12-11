from flask_table import Table, Col, LinkCol


class Customer(Table):
    customer_id = Col('customer_id')
    customer_name = Col('customer_name')
    street_name = Col('street_name')
    city = Col('city')
    zipcode = Col('zipcode')
    phone_number = Col('phone_number')
    employee_id = Col('employee_id')
    edit = LinkCol('Edit', 'edit_customer', url_kwargs=dict(id='customer_id'))
    delete = LinkCol('Delete', 'delete_customer', url_kwargs=dict(id='customer_id'))


class _Customer(Table):
    customer_id = Col('customer_id')
    customer_name = Col('customer_name')
    street_name = Col('street_name')
    city = Col('city')
    zipcode = Col('zipcode')
    phone_number = Col('phone_number')
    employee_id = Col('employee_id')


class Deliverable(Table):
    deliverable_id = Col('deliverable_id')
    order_date = Col('order_date')
    delivery_date = Col('delivery_date')
    customer_id = Col('customer_id')
    employee_id = Col('employee_id')
    edit = LinkCol('Edit', 'edit_deliverable', url_kwargs=dict(id='deliverable_id'))
    delete = LinkCol('Delete', 'delete_deliverable', url_kwargs=dict(id='deliverable_id'))


class _Deliverable(Table):
    deliverable_id = Col('deliverable_id')
    order_date = Col('order_date')
    delivery_date = Col('delivery_date')
    customer_id = Col('customer_id')
    employee_id = Col('employee_id')


class Employee(Table):
    employee_id = Col('employee_id')
    ssn = Col('ssn')
    employee_name = Col('employee_name')
    department = Col('department')
    dept_position = Col('dept_position')
    date_of_entry = Col('date_of_entry')
    edit = LinkCol('Edit', 'edit_employee', url_kwargs=dict(id='employee_id'))
    delete = LinkCol('Delete', 'delete_employee', url_kwargs=dict(id='employee_id'))


class _Employee(Table):
    employee_id = Col('Employee ID')
    employee_name = Col('Employee Name')
    department = Col('Department')
    dept_position = Col('Department Position')
    date_of_entry = Col('Date of Entry')


class Product(Table):
    product_id = Col('product_id')
    product_name = Col('product_name')
    classification = Col('classification')
    price = Col('price')
    inventory = Col('inventory ')
    edit = LinkCol('Edit', 'edit_product', url_kwargs=dict(id='product_id'))
    delete = LinkCol('Delete', 'delete_product', url_kwargs=dict(id='product_id'))


class _Product(Table):
    product_id = Col('product_id')
    product_name = Col('product_name')
    classification = Col('classification')
    price = Col('price')
    inventory = Col('inventory ')


class Delivery(Table):
    tracking_number = Col('tracking_number')
    carrier_name = Col('carrier_name')
    contact = Col('contact')
    deliverable_id = Col('deliverable_id')
    edit = LinkCol('Edit', 'edit_delivery', url_kwargs=dict(id=('tracking_number')))
    delete = LinkCol('Delete', 'delete_delivery', url_kwargs=dict(id=('tracking_number')))


class _Delivery(Table):
    tracking_number = Col('Tracking Number')
    carrier_name = Col('Carrier Name')
    contact = Col('Contact')
    deliverable_id = Col('Deliverable ID')

class _Customer_Delivery(Table):
    customer_name = Col('Customer Name')
    employee_id = Col('Employee ID')
    carrier_name = Col('Carrier Name')

class OrderList(Table):
    deliverable_id = Col('Deliverable ID' )
    product_id = Col('Product ID')
    quantity = Col('Quantity')
    delete = LinkCol('Edit', 'edit_order', url_kwargs=dict(id='deliverable_id'))

class _Customer_Transactions(Table):
    customer_name = Col("Customer Name")
    address = Col("Address")
    product_name = Col("Product Name")
    price = Col("Price")
    quantity = Col("Quantity")
    total = Col("Total (USD)")