# Temporary file to copy data from data.txt into data.json

import json

with open("data.txt", "r") as file:
    data_list = file.readlines()

data_dic = {}
for row in data_list:
    row_data_bef = row.split("|")
    row_data = []
    for word in row_data_bef:
        row_data.append(word.strip())
    data_dic.update(
        {row_data[0]: {
             "email": row_data[1],
             "password": row_data[2]
         }})
with open("data.json", "w") as file:
    json.dump(data_dic, file, indent=4)
    print("# Successfully completed!")
