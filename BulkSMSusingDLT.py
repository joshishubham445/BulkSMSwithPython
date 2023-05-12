import pandas as pd
import requests
from datetime import date

url = "https://www.fast2sms.com/dev/bulkV2"

workbook = pd.read_excel('Add your File Path')

filteredWB = workbook.filter(items=["Name","Mobile Number","Reminder Date"])
filteredWB["Reminder Date"] = pd.to_datetime(filteredWB["Reminder Date"], format='%Y-%m-%d')
filteredWB = filteredWB.loc[(filteredWB["Reminder Date"].dt.date == date.today())]


for data in filteredWB.index:
    mobileNo = int(filteredWB["Mobile Number"][data])
    querystring = {"authorization":"YOUR_API_KEY",
                   "sender_id":"DLT_SENDER_ID",
                   "message":"YOUR_MESSAGE_ID",
                   "variables_values":" Optional",
                   "route":"dlt",
                   "numbers":mobileNo}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
