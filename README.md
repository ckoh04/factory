# Smart Star Glass Company 

Steps:

1. Install Python.

2. Install dependencies.

```
pip3 install flask_table
pip3 install pymysql
pip3 install flask-mysql
```
3. Run these SQL lines to create necessary tables.

```
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(20) NOT NULL,
  `street_name` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `zipcode` varchar(5) NOT NULL,
  `phone_number` varchar(10) NOT NULL,
  `employee_id` int DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `customer_ibfk_1` (`employee_id`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

```
CREATE TABLE `deliverable` (
  `deliverable_id` int NOT NULL,
  `order_date` date DEFAULT NULL,
  `delivery_date` datetime DEFAULT NULL,
  `customer_id` int NOT NULL,
  `employee_id` int NOT NULL,
  PRIMARY KEY (`deliverable_id`),
  KEY `deliverable_ibfk_2` (`employee_id`),
  KEY `deliverable_ibfk_1` (`customer_id`),
  CONSTRAINT `deliverable_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE,
  CONSTRAINT `deliverable_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

```
CREATE TABLE `employee` (
  `employee_id` int NOT NULL,
  `ssn` varchar(9) NOT NULL,
  `employee_name` varchar(20) NOT NULL,
  `department` varchar(15) NOT NULL,
  `dept_position` varchar(15) DEFAULT NULL,
  `date_of_entry` datetime DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

4. Run the code to start the server:
```
python main.py
```

5. Access the URL on the browser:
```
http://localhost:5000/
```
