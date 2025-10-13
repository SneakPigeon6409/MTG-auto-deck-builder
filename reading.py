import pandas as pd

cards = pd.read_csv('cards.csv', quotechar='"', skipinitialspace=True, encoding='utf-8-sig')
print(cards.head())
print(cards[cards["Type"] == "Land"].sort_values("Name"))