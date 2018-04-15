"""
读取csv文件,并可视化
"""
import csv

import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #读第一行
    #print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    highs = []
    for row in reader:     #从第二行开始读
        highs.append(int(row[1]))

    # print(highs)
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')

    #设置折线图的格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    #刻度
    plt.tick_params(axis='both', which='major', labelsize=20)

    plt.show()
