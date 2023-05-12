import pandas as pd
import requests
from datetime import date

url = "https://www.fast2sms.com/dev/bulkV2"
headers = {
    'cache-control': "no-cache"
}

workbook = pd.read_excel('D:\Other\Programs\Bulk SMS Trial project\Bulk SMS Trial project\participants.csv')

filteredWB = workbook.filter(items=["Name","Mobile Number","Reminder Date"])
filteredWB["Reminder Date"] = pd.to_datetime(filteredWB["Reminder Date"], format='%Y-%m-%d')
filteredWB = filteredWB.loc[(filteredWB["Reminder Date"].dt.date == date.today())]

for data in filteredWB.index:
    mobileNo = int(filteredWB["Mobile Number"][data])
    querystring = {"authorization":"F2oabSBHZgE5ylRAer1x0Gf3msjuPwIvn7MNz6DLUt8dKQWVq9b1RZSypNOX8oBd7qn9WM0xQwrhULuv",
               "sender_id":"TXTIND",
               "message":"""Dear Customer, Thank you for your visit. 
Your next wheel alignment is due in today. 
Regards. OM Tyres - MRF Tyres and Services""",
               "route":"v3",
               "numbers":mobileNo}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)