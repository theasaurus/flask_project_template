# flask_project_template
Setting up a basic flask app with a database (not using SQLAlchemy).

## Run the project
Type

    flask run
    
in the terminal to run the project.

The flask app will run in development mode, this can be changed in the .flaskenv file.

## Database
Define the database schema in schema.sql and run

    flask init-db

This will create a database called app.db (change name in config.py).

Make sure you change the secret key in config.py!

I didn't use SQLAlchemy because this was designed with my students in mind.
As I have to assess them on their ability to write SQL, I prefer not to use SQLAlchemy.

# References
Thanks to Miguel Grinberg's excellent [flask tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), it taught me so much about Flask.

db.py is based on the tutorial in the [flask documentation](https://flask.palletsprojects.com/en/2.0.x/tutorial/database/).
