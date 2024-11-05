from flask import Flask, jsonify, request, render_template
from database import connect_db, create_tables, add_seasonal_flavor, add_ingredient, add_customer_suggestion, view_seasonal_flavors, view_ingredients

app = Flask(__name__)

# Connect to the database and initialize tables
conn = connect_db()
create_tables(conn)

# Health check route
@app.route('/health')
def health_check():
    return jsonify({"status": "running"}), 200

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API routes for flavors, ingredients, and suggestions as in the previous code
# ...

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
