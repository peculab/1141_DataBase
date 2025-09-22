from flask import Blueprint, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

create_bp = Blueprint('create_bp', __name__)

db_config = {
    'user': 'root',
    'password': '0p;/9ol.',
    'host': 'localhost',
    'database': '1141-database'
}

@create_bp.route('/add', methods=['POST'])
def add_post():
    conn = None
    cursor = None
    try:
        # Get data from the form
        username = request.form['username']
        email = request.form['email']

        # Get the current time for the 'created_at' column
        created_at = datetime.now() 

        # Establish database connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SQL query to insert data
        insert_query = "INSERT INTO users (username, email, created_at) VALUES (%s, %s, %s)"

        # Execute the query with the data
        cursor.execute(insert_query, (username, email, created_at))
        
        # Commit the changes to the database
        conn.commit()

        # Use Flask's `flash` to show a success message to the user
        flash(f"User '{username}' added successfully!")
        
    except mysql.connector.errors.IntegrityError as e:
        # Handle "Duplicate entry" errors gracefully
        flash(f"Error: A user with that username or email already exists. {e}", 'error')
        print(f"Database IntegrityError: {e}") # Log the error for debugging
        
    except mysql.connector.Error as e:
        # Handle other database-related errors (e.g., connection failure)
        flash("An error occurred with the database. Please try again later.", 'error')
        print(f"Database Error: {e}") # Log the error for debugging
        
    finally:
        # Always close the cursor and connection, regardless of success or failure
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

    # Redirect to the main page
    return redirect(url_for('read_bp.index'))