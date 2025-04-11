import yfinance as yf
import pandas as pd

# 建立 TSMC 台積電的 Ticker 物件（Yahoo Finance 代碼為 2330.TW）
tsmc = yf.Ticker("2330.TW")

# 取得最近 10 天的歷史資料（含開盤、最高、最低、收盤等）
hist = tsmc.history(period="10d")

# 取出最近 10 筆的收盤價資料
recent_closes = hist['Close'].tail(10)


# 儲存成 CSV 檔案（含日期欄位）
recent_closes.to_csv("api1.csv", encoding="utf-8-sig", header=True)

print("已儲存為 api.csv")
