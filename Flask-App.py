from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

# map shortened URLs to their original URLs
url_map = {}

@app.route('/<short_hash>')
def redirect_url(short_hash):
    if short_hash in url_map:
        return redirect(url_map[short_hash])
    else:
        return "Error: Shortened URL not found."

@app.route('/map', methods=['POST'])
def map_url():
    data = request.json
    url_map[data['short']] = data['url']
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # start the web server
    app.run()
