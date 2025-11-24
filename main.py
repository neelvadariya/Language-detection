from flask import Flask, request, jsonify
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/detect-language', methods=['POST'])
def detect_language():
    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400

    url = data['url']
    parsed = urlparse(url)

    # Get the path from URL
    path = parsed.path.strip("/")

    # If path contains "/", get the first segment
    prefix = path.split("/")[0] if path else ""

    # Check for language-like patterns
    if prefix and (prefix.lower() == "en" or "_" in prefix or "-" in prefix):
        language = prefix
    else:
        language = "default"

    return jsonify({"language": language})


if __name__ == '__main__':
    app.run(debug=True)
