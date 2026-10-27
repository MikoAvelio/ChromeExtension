# GET Version
# from flask import Flask, request, render_template, app
# app = Flask(__name__)

# @app.route('/square', methods=['GET'])
# def squarenumber():
#     num = request.args.get('num')

#     if num is None:
#         return render_template('squarenum.html')
#     elif num.strip() == '':
#         return "<h1>Invalid input. Please enter a valid number.</h1>"
#     else:
#         try:
#             square = int(num) ** 2
#             return render_template("answer.html", squareofnum=square, num=num)
#         except ValueError:
#             return "<h1>Invalid input. Please enter a valid number.</h1>"


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

    #Explanation:
    #request.args.get('num') retrieves the number form the URL parameters.
    # if num is None the user is visiting the page for the first time otherwise an error message is displayed.
    # the square of the number is calculated and passed to the answer.html template.

# POST Version
# Post methos is used to send data for the server for processing
# Unlike GET, it does not append data to the URL. Instead, it sends data in the request body, making it a better choice for sensitive or large data.
# from flask import Flask, request, render_template
# app = Flask(__name__)

# @app.route('/square', methods=['GET', 'POST'])
# def squarenumber():
#     if request.method == 'POST':
#         num = request.form.get('num')
#         if num.strip() == '':
#             return "<hi>Invalid number</hi>"
#         square = int(num) ** 2
#         return render_template('answer.html', squareofnum=square, num=num)
#     return render_template('squarenum.html')
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

# Explanation:
# Supports both GET and POST route now accepths both GET (to render the form) and POST (to process the input).
# Data is sent in the request body instead of request.args.get('num'), use request.form.get('num') to retrieve the number from the form.
# More secure since data is not appended to the URL, its not visible in browser history or logs.
# Same logic for processing input app still checks if the numver is provided, its square and renders the result using answer.html