"""
读取csv文件,并可视化
"""
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # 读第一行
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:     # 从第二行开始读
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')  # 最高气温数据

    plt.plot(dates, lows, c='blue')  # 最低气温数据

    # 为两条线之间着色
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 设置折线图的格式
    # plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.title("Daily high temperatures - 2014", fontsize=24)

    plt.xlabel('', fontsize=5)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    # 刻度
    plt.tick_params(axis='both', which='major', labelsize=20)

    plt.show()
