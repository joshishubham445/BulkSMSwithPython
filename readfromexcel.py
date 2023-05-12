import pandas as pd
import requests
from datetime import date

url = "https://www.fast2sms.com/dev/bulkV2"
headers = {
    'cache-control': "no-cache"
}

workbook = pd.read_excel('Add your File Path')

filteredWB = workbook.filter(items=["Name","Mobile Number","Reminder Date"])
filteredWB["Reminder Date"] = pd.to_datetime(filteredWB["Reminder Date"], format='%Y-%m-%d')
filteredWB = filteredWB.loc[(filteredWB["Reminder Date"].dt.date == date.today())]

for data in filteredWB.index:
    mobileNo = int(filteredWB["Mobile Number"][data])
    querystring = {"authorization":"Add your API Key",
               "sender_id":"TXTIND",
               "message":"Add your message",
               "route":"v3",
               "numbers":mobileNo}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
