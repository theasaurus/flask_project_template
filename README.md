# flask_project_template
Setting up a basic flask app with an SQLite database (not using SQLAlchemy/ORM).

## Run the project
Type

    flask run
    
in the terminal to run the project.

The flask app will run in development (debug) mode, this can be changed in the .flaskenv file.

## Database
Define the database schema in schema.sql and run

    flask init-db

This will create a database called app.db (change name in config.py).

Make sure you change the secret key in config.py!

If you want to use an existing database, put the database file (.db) in the root directory and modify the name in config.py.

## Routes
Define the different routes (URLs) in routes.py. 
Flask will look for html pages in app/templates.

If you want to use the database, first import from app.db.

    from app.db import get_db

Then we can start executing SQL statements:

    db = get_db()
    db.execute("INSERT INTO table VALUES ('a', 'b');")
    db.commit()

To get results:

    results = db.execute("SELECT * FROM table")
    rows = results.fetchall()

Take a look at the [python sqlite3 docs](https://docs.python.org/3/library/sqlite3.html) for more examples. 

## References
Thanks to Miguel Grinberg's excellent [flask tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), it taught me so much about Flask.

db.py is based on the tutorial in the [flask documentation](https://flask.palletsprojects.com/en/2.3.x/tutorial/database/).
