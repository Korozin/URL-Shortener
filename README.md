# URL-Shortener
Simple Flask localhost app to make my own URL Shortener

## How to use
first run
```
python Flask-App.py
```
to hook the backend into a localhost  

then run
```
python URL-Shorten.py
```
to create a shortend URL

## Note!
I'm too lazy to create an actual host for this app myself. As such I'm just releasing the script so you can make it your own localhost. Just run `Flask-App.py` and it'll automatically start a localhost at either `http://localhost:5000` or `http://127.0.0.1:5000`  

Keep the `Flask-App.py` script running, and while it's still running, execute `URL-Shorten.py`. This will create the link at `http://localhost:5000/hash` and post the JSON dictionary to the server allowing it to redirect you to the URL you posted. Note: the generated URLs will only work while the server is running.  

## Example Usage

Flask-App Output
```
┬─[peppermint@arch-core:~/Desktop]─[07:05:14 PM]
╰─>$ python Flask-App.py
 * Serving Flask app 'Flask-App'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

URL-Shorten Output
```
┬─[peppermint@arch-core:~/Desktop]─[07:06:19 PM]
╰─>$ python URL-Shorten.py
URL to shorten: example.com
http://localhost:5000/EAaArVRs
```

after running URL-Shorten, Flask-App should output something similar to this
```
127.0.0.1 - - [08/Apr/2023 19:06:22] "POST /map HTTP/1.1" 200 -
```

then put `http://localhost:5000/EAaArVRs` into your browser, and it should redirect to `https://example.com`
