from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DATABASE = 'coffee_ratings.db'

# Database helper functions
def get_db_connection():
    """Create a connection to the SQLite database"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with coffee items table"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS coffee_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            votes INTEGER DEFAULT 0
        )
    ''')
    
    # Check if table is empty, then add sample data
    cursor.execute('SELECT COUNT(*) FROM coffee_items')
    count = cursor.fetchone()[0]
    
    if count == 0:
        # Add sample coffee items
        sample_coffees = [
            ('Espresso', 'Strong and concentrated coffee shot'),
            ('Cappuccino', 'Espresso with steamed milk and foam'),
            ('Latte', 'Espresso with lots of steamed milk'),
            ('Americano', 'Espresso diluted with hot water'),
            ('Mocha', 'Chocolate-flavored coffee drink')
        ]
        
        cursor.executemany(
            'INSERT INTO coffee_items (name, description, votes) VALUES (?, ?, 0)',
            sample_coffees
        )
    
    conn.commit()
    conn.close()

# API Routes
@app.route('/api/coffees', methods=['GET'])
def get_coffees():
    """Get all coffee items with their vote counts"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM coffee_items ORDER BY votes DESC')
    coffees = cursor.fetchall()
    conn.close()
    
    # Convert to list of dictionaries
    coffee_list = []
    for coffee in coffees:
        coffee_list.append({
            'id': coffee['id'],
            'name': coffee['name'],
            'description': coffee['description'],
            'votes': coffee['votes']
        })
    
    return jsonify(coffee_list)

@app.route('/api/vote', methods=['POST'])
def vote_coffee():
    """Increment the vote count for a coffee item"""
    data = request.get_json()
    coffee_id = data.get('id')
    
    if not coffee_id:
        return jsonify({'error': 'Coffee ID is required'}), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Update vote count
    cursor.execute('UPDATE coffee_items SET votes = votes + 1 WHERE id = ?', (coffee_id,))
    conn.commit()
    
    # Get updated coffee item
    cursor.execute('SELECT * FROM coffee_items WHERE id = ?', (coffee_id,))
    coffee = cursor.fetchone()
    conn.close()
    
    if coffee:
        return jsonify({
            'id': coffee['id'],
            'name': coffee['name'],
            'votes': coffee['votes']
        })
    else:
        return jsonify({'error': 'Coffee not found'}), 404

@app.route('/')
def index():
    """Serve the frontend HTML page"""
    return app.send_static_file('index.html')

if __name__ == '__main__':
    init_db()  # Initialize database on startup
    app.run(debug=True, port=5000)
