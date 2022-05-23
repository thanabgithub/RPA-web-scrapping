# %%
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

URL = "https://www.sanno.ac.jp/tukyo/process/examination.html"
match = "試験日"
def get_current_date():

    msg = ''
    from datetime import datetime
    from datetime import timedelta
    today = datetime.today().strftime('%Y-%m-%d')
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')


    return today, yesterday

def get_today_data(URL, match, today):
    tables = pd.read_html(URL,match=match)


    today_df = tables[0]
    today_df.to_csv('data/'+today+'.csv', index = False)

    return today_df

def confirm_no_update(today_df, yesterday):
    
    yesterday_df = pd.read_csv('data/'+yesterday+'.csv')
    
    is_no_update = (today_df!=yesterday_df).sum().sum() < 1.0

    return is_no_update, today_df, yesterday_df

def df_to_file(df):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.axis('tight')
    ax.table(cellText=df.values,
            colLabels=df.columns,
            loc='center',
            bbox=[0,0,1,1])
    plt.savefig('temp_table.png')

    return open('temp_table.png','rb')

def create_contents(is_no_update, today, yesterday, today_df, yesterday_df):
    if (is_no_update):
        MSG = today + " 変更なし"
        file = {'imageFile':None}
        data = {'message': MSG}
    else:
        MSG = today + " 変更あり ！！ 注意！！"
        file = {'imageFile':df_to_file(today_df)}
        data = {'message': MSG} 
    return data, file

# %%
import requests



def send_line_notify(notification_message, file):
    """
    LINE
    """
    line_notify_token = 'OkmgRkoVYsHOkpmrHaJkskI1Og9oT645m0EnbcNNvZD'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}

    requests.post(line_notify_api, headers = headers, data = data, files = file)

if __name__ == "__main__":
    today, yesterday = get_current_date()
    today_df = get_today_data(URL, match, today)
    is_no_update, today_df, yesterday_df = confirm_no_update(today_df, yesterday)
    data, file = create_contents(is_no_update, today, yesterday, today_df, yesterday_df)

    send_line_notify(data, file)