# %%
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib


URL = "https://www.sanno.ac.jp/tukyo/process/examination.html"
tables = pd.read_html(URL,match="試験日")
df = tables[0]
print("There are : ",len(tables)," tables")
print("Take look at table 0")
print(df)

import dataframe_image as dfi
        
dfi.export(df,"temp_table.png")

prefile = open('temp_table.png','rb')
file = {'imageFile':prefile}
data = ({
'message': df
})

from datetime import datetime
print(datetime.today().strftime('%Y-%m-%d'))

# %%
import requests
import pdb; pdb.set_trace();raise
def main(msg, file=None):
    send_line_notify(msg, file)

def send_line_notify(notification_message, file):
    """
    LINE
    """
    line_notify_token = 'OkmgRkoVYsHOkpmrHaJkskI1Og9oT645m0EnbcNNvZD'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'\n {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data, file = file)

if __name__ == "__main__":
    main(df, file)