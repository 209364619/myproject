# -*- coding: UTF-8 -*-
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


def connect_test():
    '''
    数据库连接
    :return:
    '''
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='203.57.226.56',
                                  database='new')
    return cnx


def tables():
    '''
    数据库表创建语句
    :return:
    '''
    TABLES = {}
    TABLES['employees'] = (
        "CREATE TABLE `employees` ("
        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `birth_date` date NOT NULL,"
        "  `first_name` varchar(14) NOT NULL,"
        "  `last_name` varchar(16) NOT NULL,"
        "  `gender` enum('M','F') NOT NULL,"
        "  `hire_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`)"
        ") ENGINE=InnoDB")

    TABLES['departments'] = (
        "CREATE TABLE `departments` ("
        "  `dept_no` char(4) NOT NULL,"
        "  `dept_name` varchar(40) NOT NULL,"
        "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
        ") ENGINE=InnoDB")

    TABLES['salaries'] = (
        "CREATE TABLE `salaries` ("
        "  `emp_no` int(11) NOT NULL,"
        "  `salary` int(11) NOT NULL,"
        "  `from_date` date NOT NULL,"
        "  `to_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
        "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
        "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB")

    TABLES['dept_emp'] = (
        "CREATE TABLE `dept_emp` ("
        "  `emp_no` int(11) NOT NULL,"
        "  `dept_no` char(4) NOT NULL,"
        "  `from_date` date NOT NULL,"
        "  `to_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
        "  KEY `dept_no` (`dept_no`),"
        "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
        "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
        "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
        "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB")

    TABLES['dept_manager'] = (
        "  CREATE TABLE `dept_manager` ("
        "  `dept_no` char(4) NOT NULL,"
        "  `emp_no` int(11) NOT NULL,"
        "  `from_date` date NOT NULL,"
        "  `to_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`,`dept_no`),"
        "  KEY `emp_no` (`emp_no`),"
        "  KEY `dept_no` (`dept_no`),"
        "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
        "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
        "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
        "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB")

    TABLES['titles'] = (
        "CREATE TABLE `titles` ("
        "  `emp_no` int(11) NOT NULL,"
        "  `title` varchar(50) NOT NULL,"
        "  `from_date` date NOT NULL,"
        "  `to_date` date DEFAULT NULL,"
        "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
        "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
        "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
        ") ENGINE=InnoDB")
    return TABLES


def create_database(cnx, DB_NAME):
    '''
    创建数据库
    :param cursor:
    :return:
    '''
    # 创建数据库
    cursor = cnx.cursor()
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    # 切换到数据库
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)


def insert_test():
    cnx = mysql.connector.connect(user='root', password='123456',
                                  host='203.57.226.56', database='python_test')
    cursor = cnx.cursor()

    tomorrow = datetime.now().date() + timedelta(days=1)

    add_employee = ("INSERT INTO employees "
                    "(first_name, last_name, hire_date, gender, birth_date) "
                    "VALUES (%s, %s, %s, %s, %s)")
    add_salary = ("INSERT INTO salaries "
                  "(emp_no, salary, from_date, to_date) "
                  "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

    data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

    # Insert new employee
    cursor.execute(add_employee, data_employee)
    emp_no = cursor.lastrowid

    # Insert salary information
    data_salary = {
        'emp_no': emp_no,
        'salary': 50000,
        'from_date': tomorrow,
        'to_date': date(9999, 1, 1),
    }
    cursor.execute(add_salary, data_salary)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()


if __name__ == '__main__':
    '''
    #创建数据库连接
    cnx = connect_test()

    cursor = cnx.cursor()
    #创建数据库，并切使用该数据库
    create_database(cnx, 'python_test')

    tables = tables()

    for table_name in tables:
        table_description = tables[table_name]
        try:
            print("Creating table {}: ".format(table_name),)
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    cursor.close()
    cnx.close()
    '''
    insert_test()
