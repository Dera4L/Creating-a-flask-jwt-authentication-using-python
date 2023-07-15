A simple JWT (JSON Web Token) authentication program written in Python. This program helps protect user passwords by implementing JWT-based authentication. It provides a secure and reliable method for user authentication and authorization.

Features
* User registration: Allows users to create an account by providing their username and password.
* User login: Validates the user's credentials and generates a JWT upon successful authentication.
* Protected routes: Implements JWT-based authentication for protecting routes and resources. Only authenticated users with valid JWTs can access these routes.
* Password hashing: Safely stores user passwords using hashing techniques to enhance security.


Requirements
* Python 3.6+
* Flask
* PyJWT
* Bcrypt

  Usage
* Set the required environment variables:
* export FLASK_APP=app.py
* export FLASK_ENV=development
* Start the Flask development server
* flask run
* Access the application in your browser at http://localhost:5000.
 Configuration
* The configuration for the application can be found in the config.py file. You can modify the configuration options according to your needs.
