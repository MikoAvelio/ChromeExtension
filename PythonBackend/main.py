from flask import Flask, request, jsonify
import re

app = Flask(__name__)

datapool = "My Personal Project?" #Just an example string later on it will be pulled from my JSON file.

@app.route("/search", methods=['POST'])
def search_engine():
  payload = request.get_json()
  user_query = payload.get('query', '')
  advanced_search = payload.get('advanced', False)

  if not advanced_search:
    search = re.escape(user_query)
  else:
    search = user_query

  match_result = re.search(search, datapool, re.IGNORECASE)
  if match_result:
    return jsonify({"status": "found", "match": match_result.group()})
  else:
    return jsonify("No match found.")

if __name__ == '__main__':
  app.run(debug=True, port=5000)