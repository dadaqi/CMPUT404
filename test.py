import urllib.request

url = "https://raw.githubusercontent.com/dadaqi/CMPUT404/main/test.py"
response = urllib.request.urlopen(url)
source_code = response.read().decode("utf-8")

print(source_code)