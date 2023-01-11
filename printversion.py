# import requests

# # Replace USERNAME and REPOSITORY with your GitHub username and repository name
# url = "https://api.github.com/repos/dadaqi/CMPUT404/contents/printversion.py"

# # Send an HTTP GET request to the URL
# response = requests.get(url)

# # Check the status code of the response
# if response.status_code == 200:
#     script_text = response.text
#     # Print the source code
#     print(script_text)
# else:
#     # If the request is not successful, print an error message
#     print("Failed to retrieve source code")

import requests

script_url = "https://api.github.com/repos/dadaqi/CMPUT404/contents/printversion.py"
response = requests.get(script_url)

if response.status_code == 200:
    script_text = response.text
    print(script_text)
    with open("script.py", "w") as file:
        file.write(script_text)


import requests

print(requests.__version__)