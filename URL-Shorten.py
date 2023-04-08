import hashlib
import base64
import requests
import urllib

def format_link(link):
    # check if link starts with http:// or https://
    parsed = urllib.parse.urlparse(link)
    if parsed.scheme == "":
        # Determine the URL scheme by making a request to the URL
        try:
            response = requests.get("https://" + link)
            if response.status_code == 200:
                link = "https://" + link
            else:
                link = "http://" + link
        except requests.exceptions.RequestException:
            link = "http://" + link
    return link

# the URL to shorten
url = format_link(input("URL to shorten: "))

# create a hash of the URL using SHA-256
hash_object = hashlib.sha256(url.encode())

# encode the hash as base64
short_hash = base64.urlsafe_b64encode(hash_object.digest()[:6]).decode()

# construct the shortened URL
short_url = f"http://localhost:5000/{short_hash}"

# add the mapping to the url_map dictionary
response = requests.post('http://localhost:5000/map', json={'short': short_hash, 'url': url})

print(short_url)
