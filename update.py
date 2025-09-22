from flask import Blueprint, request, redirect, url_for, flash
import mysql.connector

update_bp = Blueprint('update_bp', __name__)

db_config = {
    'user': 'root',
    'password': '0p;/9ol.',
    'host': 'localhost',
    'database': '1141-database'
}

@update_bp.route('/update/<int:post_id>', methods=['POST'])
def update_post(post_id):
    conn = None
    cursor = None
    try:
        # Get data from the form
        username = request.form['username']
        email = request.form['email']
        
        # Establish database connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # SQL query to update data based on the post ID
        update_query = "UPDATE users SET username = %s, email = %s WHERE id = %s"
        
        # Execute the query with the data and the post ID
        cursor.execute(update_query, (username, email, post_id))
        
        # Commit the changes to the database
        conn.commit()

        flash(f"User with ID {post_id} updated successfully!")
        
    except mysql.connector.Error as e:
        flash(f"Error updating user: {e}", 'error')
        print(f"Database Error: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

    # Redirect to the main page to show the updated data
    return redirect(url_for('read_bp.index'))
