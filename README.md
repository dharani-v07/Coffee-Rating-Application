# Coffee Rating Application ☕

A beginner-friendly web application where users can vote for their favorite coffee drinks. Each vote is stored in a database and the rankings update in real-time.

## Features

- Display a list of coffee items with descriptions
- Vote for your favorite coffee with a single click
- Real-time vote count updates
- Persistent storage using SQLite database
- Beautiful, responsive UI with gradient design

## Tech Stack

- **Backend**: Python Flask (simple web framework)
- **Database**: SQLite (built-in, no setup required)
- **Frontend**: HTML, CSS, JavaScript (vanilla, no frameworks)

## Project Structure

```
coffee-rating-app/
├── app.py                 # Flask backend with API endpoints
├── requirements.txt       # Python dependencies
├── coffee_ratings.db      # SQLite database (created automatically)
└── static/
    ├── index.html        # Frontend HTML page
    ├── style.css         # Styling
    └── script.js         # JavaScript for API calls
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher installed on your system

### Installation Steps

1. **Navigate to the project directory**
   ```bash
   cd "d:/VirtualWorksIntern/Coffee Rating Application"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   - The application will start at `http://localhost:5000`
   - Open this URL in your web browser

## How It Works

### Backend (app.py)

- **Flask Server**: Runs on port 5000 and serves the application
- **Database**: SQLite database with a `coffee_items` table
- **API Endpoints**:
  - `GET /api/coffees` - Returns all coffee items with vote counts
  - `POST /api/vote` - Increments the vote count for a coffee item
- **Auto-initialization**: Creates the database and adds sample coffee data on first run

### Frontend

- **HTML**: Displays the coffee list with voting buttons
- **CSS**: Beautiful gradient design with hover effects
- **JavaScript**: Makes API calls to fetch data and submit votes

### Database Schema

```sql
CREATE TABLE coffee_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    votes INTEGER DEFAULT 0
);
```

## Sample Coffee Items

The app comes pre-loaded with 5 coffee items:
1. Espresso - Strong and concentrated coffee shot
2. Cappuccino - Espresso with steamed milk and foam
3. Latte - Espresso with lots of steamed milk
4. Americano - Espresso diluted with hot water
5. Mocha - Chocolate-flavored coffee drink

## API Usage Examples

### Get all coffees
```bash
curl http://localhost:5000/api/coffees
```

### Vote for a coffee (ID: 1)
```bash
curl -X POST http://localhost:5000/api/vote \
  -H "Content-Type: application/json" \
  -d '{"id": 1}'
```

## Customization

### Adding new coffee items

Edit the `sample_coffees` list in `app.py`:
```python
sample_coffees = [
    ('Your Coffee Name', 'Description'),
    # Add more items...
]
```

Then delete the existing database file and restart the app:
```bash
del coffee_ratings.db
python app.py
```

### Changing the design

Edit `static/style.css` to customize colors, fonts, and layout.

## Troubleshooting

**Port already in use?**
- Change the port in `app.py`: `app.run(debug=True, port=5001)`

**Database errors?**
- Delete `coffee_ratings.db` and restart the app to recreate it

**Dependencies not installing?**
- Ensure you have Python 3.7+ and pip is working: `pip --version`

## Learning Resources

This project is designed for beginners. Key concepts to explore:
- **Flask**: https://flask.palletsprojects.com/
- **SQLite**: https://www.sqlite.org/docs.html
- **Fetch API**: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

## License

This is a learning project. Feel free to modify and use it for educational purposes.
