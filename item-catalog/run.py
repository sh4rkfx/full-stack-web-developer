"""Project Entry Point."""
import sys
from src import app, db


if __name__ == '__main__':
    app.run(host='localhost', port=5000)

if __name__ == '__main__':
    if '--setup' in sys.argv:
        with app.app_context():
            db.create_all()
            db.session.commit()
            print("Database tables created")

    else:
        app.run(debug=True)