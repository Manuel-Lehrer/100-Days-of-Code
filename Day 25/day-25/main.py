# # with open(file="weather_data.csv", mode="r") as weather_data:
# #     data = weather_data.readlines()
#
# # import csv
# #
# # with open(file="weather_data.csv", mode="r") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temp = int(row[1])
# #             temperatures.append(temp)
# #
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# #print(data["temp"])
#
# data_dict = data.to_dict()
# #(data_dict)
#
# temp_list = data["temp"].to_list()
# #print(temp_list)
#
# # average = sum(temp_list)/len(temp_list)
# average = data["temp"].mean()
# #print(average)
#
# maximum = data["temp"].max()
# #print(maximum)
#
# #print(data[data.day == "Monday"])
#
# #print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp*9/5+32)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_list = data["Primary Fur Color"].to_list()


color_counts = []

gray_count = fur_list.count("Gray")
color_counts.append(gray_count)
cinnamon_count = fur_list.count("Cinnamon")
color_counts.append(cinnamon_count)
black_count = fur_list.count("Black")
color_counts.append(black_count)

squirrel_dict = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "counts": color_counts
}

squirrel_data = pandas.DataFrame(squirrel_dict)
print(squirrel_data)
squirrel_data.to_csv("squirrel_data.csv")




