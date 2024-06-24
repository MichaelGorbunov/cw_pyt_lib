#git branch develop
import pandas as pd
excel_data = pd.read_excel("data\\operations.xls")
print(excel_data.shape)
print(excel_data.head())
print(len(excel_data))
cat_list = []
# print(excel_data["Категория"].unique())
for items in excel_data["Категория"].unique():
    cat_list.append(items)
print(cat_list)
for item in cat_list:
    selected_reviews = excel_data.loc[excel_data["Категория"] == item]
    print(len(selected_reviews))
    print(selected_reviews["Сумма операции"].sum())
card_list = []
for items in excel_data["Номер карты"].unique():
    card_list.append(items)
print(card_list)

