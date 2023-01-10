import requests

# Replace USERNAME and REPOSITORY with your GitHub username and repository name
url = "https://raw.githubusercontent.com/dadaqi/CMPUT404/main/printversion.py?token=GHSAT0AAAAAAB5FMOI6VIFFF5BF53AGXDXSY546PYA"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    # If the request is successful, get the content of the file
    content = response.json()["content"]
    # Decode the content from base64
    source_code = content.decode("base64")
    # Print the source code
    print(source_code)
else:
    # If the request is not successful, print an error message
    print("Failed to retrieve source code")


import requests

print(requests.__version__)