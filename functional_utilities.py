import requests

url = "https://mailsac.com/api/addresses/benjiboi214test@mailsac.com/messages"
headers = {'Mailsac-Key': 'F04YOjJk1Nr1tgCJK3V6xAsuuXFbU'}
response = requests.get(url, headers=headers)
# Print the status code of the response.
print(response.json())