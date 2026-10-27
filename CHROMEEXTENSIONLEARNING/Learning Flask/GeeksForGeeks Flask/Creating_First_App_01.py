# Creating app.py (or main.py) file

# You should import this code:
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
# if __name__ == '__main__':
#     app.run()

# Explanation of the code:
# Flash is imported from the flask module
# Flask(__name__) is used to create an instance of the Flask class. 
# The __name__ variable is a special Python variable that gets
# its value depending on how we execute the containing script. If we execute the script directly, it will be set to __main__. 
# If we import the script from another module, it will be set to the name of that module.
# The @app.route('/') decorator is used to bind the hello_world() function to the root URL ('/').
# The hello_world() function returns the string 'Hello World!' when the root URL is accessed.
# if __name__ == '__main__': checks if the script is being run directly (as opposed to being imported as a module). 
# If it is, app.run() starts the Flask development server, allowing us to access the application in a web browser.