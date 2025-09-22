from flask import Flask, redirect, url_for, render_template

# Import your blueprints
from create import create_bp
from read import read_bp
from update import update_bp
from delete import delete_bp

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for session management.
# This is required for using features like flash messages.
# NOTE: For a production environment, this should be a complex, random string
# stored securely (e.g., in an environment variable).
app.secret_key = 'your_super_secret_and_unique_key_here'

# Register the blueprints with the application
app.register_blueprint(create_bp)
app.register_blueprint(read_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)

# A simple index route to show the user data and forms
@app.route('/')
def index():
    # Redirect to the main 'read' route
    return redirect(url_for('read_bp.index'))

if __name__ == '__main__':
    app.run(debug=True)
