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
CREATE SCHEMA IF NOT EXISTS `smart_star` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `smart_star` ;

-- -----------------------------------------------------
-- Table `smart_star`.`employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`employee` (
  `employee_id` INT NOT NULL,
  `ssn` VARCHAR(9) NOT NULL,
  `employee_name` VARCHAR(20) NOT NULL,
  `department` VARCHAR(15) NOT NULL,
  `dept_position` VARCHAR(15) NULL DEFAULT NULL,
  `date_of_entry` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`employee_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `smart_star`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`customer` (
  `customer_id` INT NOT NULL,
  `customer_name` VARCHAR(20) NOT NULL,
  `street_name` VARCHAR(50) NOT NULL,
  `city` VARCHAR(20) NOT NULL,
  `zipcode` VARCHAR(5) NOT NULL,
  `phone_number` VARCHAR(10) NOT NULL,
  `employee_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  INDEX `customer_ibfk_1` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `customer_ibfk_1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `smart_star`.`employee` (`employee_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `smart_star`.`deliverable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`deliverable` (
  `deliverable_id` INT NOT NULL,
  `order_date` DATE NULL DEFAULT NULL,
  `delivery_date` DATETIME NULL DEFAULT NULL,
  `customer_id` INT NOT NULL,
  `employee_id` INT NOT NULL,
  PRIMARY KEY (`deliverable_id`),
  INDEX `deliverable_ibfk_1_idx` (`customer_id` ASC) VISIBLE,
  INDEX `deliverable_ibfk_2_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `deliverable_ibfk_1`
    FOREIGN KEY (`customer_id`)
    REFERENCES `smart_star`.`customer` (`customer_id`),
  CONSTRAINT `deliverable_ibfk_2`
    FOREIGN KEY (`employee_id`)
    REFERENCES `smart_star`.`employee` (`employee_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `smart_star`.`delivery`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`delivery` (
  `tracking_number` VARCHAR(20) NOT NULL,
  `carrier_name` VARCHAR(10) NOT NULL,
  `contact` VARCHAR(10) NULL DEFAULT NULL,
  `deliverable_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`tracking_number`),
  INDEX `delivery_ibfk_1_idx` (`deliverable_id` ASC) VISIBLE,
  CONSTRAINT `delivery_ibfk_1`
    FOREIGN KEY (`deliverable_id`)
    REFERENCES `smart_star`.`deliverable` (`deliverable_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `smart_star`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`product` (
  `product_id` INT NOT NULL,
  `product_name` VARCHAR(20) NOT NULL,
  `classification` VARCHAR(15) NOT NULL,
  `price` DECIMAL(10,2) NULL DEFAULT NULL,
  `inventory` INT NOT NULL,
  PRIMARY KEY (`product_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `smart_star`.`order_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`order_list` (
  `deliverable_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`deliverable_id`, `product_id`),
  INDEX `order_list_ibkf_2` (`product_id` ASC) VISIBLE,
  CONSTRAINT `order_list_ibfk_1`
    FOREIGN KEY (`deliverable_id`)
    REFERENCES `smart_star`.`deliverable` (`deliverable_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `order_list_ibkf_2`
    FOREIGN KEY (`product_id`)
    REFERENCES `smart_star`.`product` (`product_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `smart_star`.`tbl_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`tbl_user` (
  `user_id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `user_email` VARCHAR(45) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `user_password` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

USE `smart_star` ;

-- -----------------------------------------------------
-- Placeholder table for view `smart_star`.`customer_delivery`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`customer_delivery` (`customer_name` INT, `employee_id` INT, `carrier_name` INT);

-- -----------------------------------------------------
-- Placeholder table for view `smart_star`.`customer_transactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`customer_transactions` (`customer_name` INT, `address` INT, `product_name` INT, `price` INT, `quantity` INT, `total` INT);

-- -----------------------------------------------------
-- Placeholder table for view `smart_star`.`long_term_workers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `smart_star`.`long_term_workers` (`employee_id` INT, `ssn` INT, `employee_name` INT, `department` INT, `dept_position` INT, `date_of_entry` INT);

-- -----------------------------------------------------
-- View `smart_star`.`customer_delivery`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smart_star`.`customer_delivery`;
USE `smart_star`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`ckoh`@`localhost` SQL SECURITY DEFINER VIEW `smart_star`.`customer_delivery` AS select `smart_star`.`customer`.`customer_name` AS `customer_name`,`smart_star`.`deliverable`.`employee_id` AS `employee_id`,`smart_star`.`delivery`.`carrier_name` AS `carrier_name` from ((`smart_star`.`customer` join `smart_star`.`deliverable` on((`smart_star`.`customer`.`customer_id` = `smart_star`.`deliverable`.`customer_id`))) join `smart_star`.`delivery` on((`smart_star`.`deliverable`.`deliverable_id` = `smart_star`.`delivery`.`deliverable_id`)));

-- -----------------------------------------------------
-- View `smart_star`.`customer_transactions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smart_star`.`customer_transactions`;
USE `smart_star`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`ckoh`@`localhost` SQL SECURITY DEFINER VIEW `smart_star`.`customer_transactions` AS select `smart_star`.`customer`.`customer_name` AS `customer_name`,concat(`smart_star`.`customer`.`street_name`,', ',`smart_star`.`customer`.`city`,', ',`smart_star`.`customer`.`zipcode`) AS `address`,`smart_star`.`product`.`product_name` AS `product_name`,`smart_star`.`product`.`price` AS `price`,`smart_star`.`order_list`.`quantity` AS `quantity`,(`smart_star`.`product`.`price` * `smart_star`.`order_list`.`quantity`) AS `total` from (((`smart_star`.`customer` join `smart_star`.`deliverable` on((`smart_star`.`customer`.`customer_id` = `smart_star`.`deliverable`.`customer_id`))) join `smart_star`.`order_list` on((`smart_star`.`deliverable`.`deliverable_id` = `smart_star`.`order_list`.`deliverable_id`))) join `smart_star`.`product` on((`smart_star`.`order_list`.`product_id` = `smart_star`.`product`.`product_id`)));

-- -----------------------------------------------------
-- View `smart_star`.`long_term_workers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smart_star`.`long_term_workers`;
USE `smart_star`;
CREATE  OR REPLACE ALGORITHM=UNDEFINED DEFINER=`ckoh`@`localhost` SQL SECURITY DEFINER VIEW `smart_star`.`long_term_workers` AS select `smart_star`.`employee`.`employee_id` AS `employee_id`,`smart_star`.`employee`.`ssn` AS `ssn`,`smart_star`.`employee`.`employee_name` AS `employee_name`,`smart_star`.`employee`.`department` AS `department`,`smart_star`.`employee`.`dept_position` AS `dept_position`,`smart_star`.`employee`.`date_of_entry` AS `date_of_entry` from `smart_star`.`employee` where (`smart_star`.`employee`.`date_of_entry` < '2010-01-01 00:00:00');

```
4. Run the code to start the server:
```
python main.py
```

5. Access the URL on the browser:
```
http://localhost:5000/
```
