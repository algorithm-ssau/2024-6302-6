from flask import Flask, request, jsonify
from .services import scrape_product

app = Flask(__name__)

@app.route("/api/scrape", methods=["POST"])
def scrape():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    product = scrape_product(url)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Failed to scrape product"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
