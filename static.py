import requests
from bs4 import BeautifulSoup
import csv

#2330台積電

def stock_data(stock_num):

    url = "https://hk.finance.yahoo.com/quote/"+str(stock_num)+".TW/history/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # 找到歷史股價表格區塊
    rows = soup.select('table tbody tr')

    data = []
    for row in rows:
        cols = row.find_all("td")
        date = cols[0].text.strip()
        close = cols[4].text.strip()
        data.append([date, close])
        if len(data) >= 10:
            break

    # 存成 CSV
    with open("static.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["日期", "收盤價"])
        writer.writerows(data)

    print("已成功儲存為 static.csv")


stock_data(2330)