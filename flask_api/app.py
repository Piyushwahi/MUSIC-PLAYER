from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# ✅ Create Flask app and configure it
app = Flask(__name__, template_folder=os.path.abspath(os.path.join('..', 'player', 'templates')))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join('..', 'player', 'static', 'music'))
app.config['SECRET_KEY'] = 'your_secret_key'

# ✅ Extensions
db = SQLAlchemy(app)
CORS(app)

# ✅ Import routes after app and db
from api_routes import *

# ✅ Create DB tables
with app.app_context():
    db.create_all()

# ✅ Run app
if __name__ == '__main__':
    app.run(debug=True)
