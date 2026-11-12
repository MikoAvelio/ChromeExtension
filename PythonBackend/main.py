from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import os
import json

app = Flask(__name__)

VAULT_FILE = "saved_assets.json"

if not os.path.exists(VAULT_FILE):
    
    with open(VAULT_FILE, 'w') as f:
        json.dump({"vault": []}, f)

@app.route("/search", methods=['POST'])
def search_engine():
  payload = request.get_json()
  user_query = payload.get('query', '')
  advanced_search = payload.get('advanced', False)

  if not advanced_search:
    if not advanced_search:
        search = rf"([^.]*?{re.escape(user_query)}[^.]*(?:\.|$|\?|!))"
    else:
        search = user_query

  with open(VAULT_FILE, 'r') as f:
    vault_data = json.load(f)

  active_search_text = " ".join(vault_data.get("vault", []))

  match_result = re.search(search, active_search_text, re.IGNORECASE)
  if match_result:
    return jsonify({"status": "found", "match": match_result.group(1).strip()})

  else:
    return jsonify({"status": "not_found", "message": "No match found."})

if __name__ == '__main__':
  CORS(app)
  app.run(debug=True, port=5000)