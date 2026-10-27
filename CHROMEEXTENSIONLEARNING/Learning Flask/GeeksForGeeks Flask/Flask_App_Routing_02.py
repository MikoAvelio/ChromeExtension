#Flask App Routing is the process of 
#defining how different URLs in a web application are handled by the Flask framework.
# In Flask, routing is achieved using the @app.route() decorator,
# which maps a specific URL to a corresponding view function. 
# This allows you to create dynamic web applications by defining different routes for various endpoints.

# - Create different routes for different URLs in your Flask application.
# - Build dynamic URLs for your application by using route parameters.
# - Handle different HTTP methods (GET, POST, etc.) in web applications and APIs.
# - Organize URL mappings and view functions for better code structure and maintainability.

# Example of Flask App Routing:
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello, Miko (Home Page Version)!"

# @app.route('/hello')
# def hello():
#     return "Hello, Miko!"

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

# Explanation of the code:
# - The code imports the Flask class from the flask module.
# - An instance of the Flask class is created and assigned to the variable app.
# - The @app.route('/') decorator is used to define a route for the root URL ('/'). When this URL is accessed, the index() function is called, which returns the string "Hello, Miko (Home Page Version)!".
# - The @app.route('/hello') decorator defines a route for the URL '/hello'. When this URL is accessed, the hello() function is called, which returns the string "Hello, Miko!".
# - The if __name__ == '__main__': block checks if the script is being run directly (as opposed to being imported as a module). If it is, app.run(debug=True, port=5000) starts the Flask development server with debugging enabled and listens on port 5000.

#Creating Basic Routes in Flask:
# An application is able to contain multiple rotues as seen from the example above with each route connected to its own view function.

# Example:
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello, Miko (Home Page Version)!"

# @app.route('/hello')
# def hello():
#     return "Hello, Miko!"

# @app.route('/about')
# def about():
#     return "This is the About Personal Project."

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

#Dynamic URLs
#Static routes work when the URL is known beforehand, but dynamic routes are 
# useful when part of the URL changes for different users or resources

#Example
# from flask import Flask
# app = Flask(__name__)
# @app.route("/user/<username>")
# def user_profile(username):
#     return f"Welcome, {username}!"

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

# Explanation:
# <username> is a variable part of the URL.
# Flask sends the value that was typed into the view function as a keyword argument
# Different usernamed can use the same route
# A single route can handle many URLs.

#Multiple Dynamic Parts in a Route
# A route can contain more than one variable section
# from flask import Flask
# app = Flask(__name__)
# @app.route("/user/<username>/post/<post_id>")
# def post(username, post_id):
#     return f"User: {username}, Post: {post_id}"

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

# URL Converters in Flask
# By default, a variable route part accepts text without a slash. Flask can also prive converters to
# restrict the type of value accepted by the route

# Flask provides these built in converters:
# string: Accepts tect without a slash. This is default.
# int: accepts integers
# float: accepts floating point values
# path: accept text including slashes
# any: matches one value in a predefined set
# uuid: accepts UUID values

# Example of using a URL converter in Flask:
# from flask import Flask
# app = Flask(__name__)
# @app.route("/post/<int:post_id>")
# def post(post_id):
#     return f"Post ID: {post_id}"

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

# Trailing Slashes
# Flask treats trailing slashes as part of the route definition.

# from flask import Flask
# app = Flask(__name__)

# @app.route("/PersonalProjects/")
# def PersonalProjects():
#     return "This is your personal project notes"
# if __name__ == "__main__":
#     app.run(debug=True, port = 5000)

# Explanation
# route has /PersonalProjects/ as its "real" form
# Acessing /PersonalProjects redirects to /PersonalProjects/
# But a route defined without a trailing slash generally does not accept the slash added form automatically.

# Building URLs with url_for()
# Hardcoding URLs throughout an application could make route changes difficult to maintain.
# Flask provides url_for() to generate a URL from an endopoint name.

# from flask import Flask, url_for

# app = Flask(__name__)
# @app.route("/")
# def home():
#     return url_for("profile", username = "Miko")

# @app.route("/user/<username>")
# def profile(username):
#     return f"Profile: {username}"
# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

# Explanation:
# First argument of url_for() is the endpoint which matches the view function name
# the other keyword arguments fill the url variables
# URL generation avoids hardcoding paths
# Flask handles escaping and application URL prefixes when constructing URLs

# Mapping URLs with add_url_rule()
# Routes can also be registed without using the route() decorating by adding add_url_rule().
# The route () decorator is essnetially a convenient way to register a view function with Flask's URL routing system.

# from flask import Flask
# app = Flask(__name__)
# def profile(username):
#     return f"ProfileL {username}"
# app.add_url_rule("user/<usernames>", "profile", profile)
# if __name__ == "__main__":
#     app.run()

# Explanation:
# /user/<username> defines the URL rule
# profile is the endpoint name
# profile is also the function hanfling the request
# this approach is useful when route registrationa nd function definitions are seperated.