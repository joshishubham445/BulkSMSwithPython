import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"F2oabSBHZgE5ylRAer1x0Gf3msjuPwIvn7MNz6DLUt8dKQWVq9b1RZSypNOX8oBd7qn9WM0xQwrhULuv",
               "sender_id":"TXTIND",
               "message":"This is a test message",
               "route":"v3",
               "numbers":"9767227771"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)