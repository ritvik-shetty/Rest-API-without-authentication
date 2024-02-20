from flask import Flask, request, jsonify
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log",filemode='a' , format='%(asctime)s,%(name)s:%(levelname)s:%(message)s')



app = Flask(__name__)


def get_user(username):
    conn = sqlite3.connect('empdatabase.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user


# Route for listing all employees of the Database
@app.route('/list_employees', methods=['GET'])
def get():
    try:
        conn = sqlite3.connect('empdatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM emp')
        data = cursor.fetchall()
        conn.close()
        app.logger.info("Data fetched sucessfully from the database")
        result = [{'id': row[0], 'name': row[1], 'address':row[2], 'city':row[3], 'salary':row[4] } for row in data]
        return jsonify(result)
    except Exception as obj:
        logging.error("Exception Information",exc_info=True)

# Route for adding employees of the Database
@app.route('/create_employee', methods=['POST'])
def posts():
    app.logger.info("User requested a POST request")
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')
    city= data.get('city')
    salary=data.get('salary')
    if not name or not address or not city or not salary:
        return jsonify({'error': 'name address city and salary are required'}), 400
    try:
        connection = sqlite3.connect('empdatabase.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO emp (name, addr, city, salary) VALUES (?, ?, ?, ?)', (name, address, city, salary))
        connection.commit()
        connection.close()
        app.logger.info("Data put sucessfully into the database")
        return jsonify({'message': 'Employee created successfully, '+ name}), 201
    
    except Exception as obj:
        logging.error("Exception Information",exc_info=True)


@app.route('/insert_using_rams_address', methods=['POST'])
def insert_shams_using_rams_address():
    # Get the JSON data from the request body
    data = request.get_json()

    # Extract name, address, city, and salary from the JSON data
    name = data.get('name')
    address = data.get('address')
    city = data.get('city')
    salary = data.get('salary')

    # Connect to the SQLite database
    conn = sqlite3.connect('empdatabase.db')
    cursor = conn.cursor()

    try:
        # Execute the SQL query to insert Shams' data using Rams' address
        cursor.execute("""
            INSERT INTO emp (name, addr, city, salary)
            SELECT ?, addr, city, salary
            FROM emp
            WHERE name = 'Ram'
        """, (name,))

        conn.commit()

        return jsonify({'message': 'Data inserted successfully.'}), 200
    
    except Exception as e:
        # Rollback the transaction if an error occurs
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    
    finally:
        # Close the database connection
        conn.close()


# Route for updating employees of the Database
@app.route('/update_employee/<int:emp_id>', methods=['PUT'])
def putdata(emp_id):
    app.logger.info(f"User requested a PUT request")
    data = request.get_json()
  
    name = data.get('name')
    address = data.get('address')
    city = data.get('city')
    salary = data.get('salary')

    if not name or not address or not city or not salary:
        return jsonify({'error': 'name address city and salary are required'}), 400

    try:
        connection = sqlite3.connect('empdatabase.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
        existing_emp = cursor.fetchone()

        if existing_emp is None:
            cursor.execute('INSERT INTO emp (id, name, addr, city, salary) VALUES (?, ?, ?, ?, ?)',
                           (emp_id, name, address, city, salary))
            connection.commit()
            connection.close()
            app.logger.info("New employee created successfully")
            return jsonify({'message': 'Employee created successfully ' + name}), 201  # 201 Created status code

        else:
            cursor.execute('UPDATE emp SET name = ?, addr = ?, city=?, salary=? WHERE id = ?',
                           (name, address, city, salary, emp_id))
            connection.commit()
            connection.close()
            app.logger.info("Employee data updated successfully")
            return jsonify({'message': 'Employee updated successfully ' + name}), 200  # 200 OK status code

    except Exception as e:
        logging.error("An error occurred while updating/creating employee data", exc_info=True)
        return jsonify({'error': 'An error occurred while updating/creating employee data'}), 500  # 500 Internal Server Error status code


@app.route('/update_employee', methods=['PATCH'])
def patch():
    app.logger.info(f"User requested a PATCH request for employee-id:")
    data = request.get_json()
    app.logger.info(data)
    emp_id = data.get('id')

    try:
        connection = sqlite3.connect('empdatabase.db')
        cursor = connection.cursor()

        
        cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
        existing_emp = cursor.fetchone()
        # app.logger.info(existing_emp)
        if existing_emp is None:
            app.logger.info("Employee not found in the database")
            return jsonify({'error': 'Employee not found'}), 404

        existing_emp = list(existing_emp)

        # Update only the fields that are present in the request
        for key, value in data.items():
            if key == 'name':
                existing_emp[1] = value
            elif key == 'address':
                existing_emp[2] = value
            elif key == 'city':
                existing_emp[3] = value
            elif key == 'salary':
                existing_emp[4] = value

        cursor.execute('UPDATE emp SET name = ?, addr = ?, city = ?, salary = ? WHERE id = ?', 
                       (existing_emp[1], existing_emp[2], existing_emp[3], existing_emp[4], emp_id))
        connection.commit()
        connection.close()

        app.logger.info("Employee data updated successfully")
        return jsonify({'message': 'Employee data updated successfully'}), 200

    except Exception as e:
        logging.error("An error occurred while updating employee data", exc_info=True)
        return jsonify({'error': 'An error occurred while updating employee data'}), 500



# Route for deleting employees from the Database
@app.route('/remove_employee/<int:emp_id>', methods=['DELETE'])
def delete_emp_route(emp_id):
    app.logger.info(f"User requested a DELETE request for employee-id:{emp_id}")
    try:
        connection = sqlite3.connect('empdatabase.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
        data = cursor.fetchone()

        if data:
            cursor.execute('DELETE FROM emp WHERE id = ?', (emp_id,))
            connection.commit()
            connection.close()
            app.logger.info("Data deleted sucessfully from the database")
            return jsonify({'message': 'Employee deleted successfully'})
        else:
            connection.close()
            app.logger.info("Data is not present in the database")
            return jsonify({'message': 'Improper ID'}), 404
    
    except Exception as obj:
            logging.error("Exception Information",exc_info=True)

# Route for listing specific employees of the Database
@app.route('/employee/<int:emp_id>',methods=['GET'])
def get_spec_emp(emp_id):
    app.logger.info(f"User requested a GET request for employee-id:{emp_id} ")
    try:
        conn = sqlite3.connect('empdatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM emp WHERE id = ?', (emp_id,))
        data = cursor.fetchall()
        conn.close()

        result = [{'id': row[0], 'name': row[1], 'address':row[2], 'city':row[3], 'salary':row[4] } for row in data]

        if not result:
            app.logger.info("Employee not found in the database")
            return jsonify({'error': 'Employee not found'}), 404

        app.logger.info("Data fetched sucessfully from the database")
        return jsonify(result)
    
    except Exception as obj:
            logging.error("Exception Information",exc_info=True)


if __name__ == '__main__':
    app.run(debug=True)

