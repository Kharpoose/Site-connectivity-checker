import urllib.request
request_url = urllib.request.urlopen('https://www.twitch.com/')
print(request_url.read())

from urllib.parse import * parse_url = urlparse('https://www.geeksforgeeks.org / python-langtons-ant/')
print(parse_url)
print("\n")
unparse_url = urlunparse(parse_url)
print(unparse_url)
