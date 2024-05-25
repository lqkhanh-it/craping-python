from flask import Flask, request, jsonify
from scrape import scrape_data

app = Flask(__name__)

@app.route('/api/v1/scrape', methods=['POST'])
def receive_data():
    url = request.get_json()["url"]
    
    try:
        scraped_data = scrape_data(url)
        return scraped_data
    except Exception as e:
        return jsonify({'error': str(e)}), 500 

if __name__ == '__main__':
    app.run(debug=True)