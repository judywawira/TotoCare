import os 

# Import the main Flask app
from app import app

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5001)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)