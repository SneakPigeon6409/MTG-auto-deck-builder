import pandas as pd
#with open('cards.csv', 'r', encoding='utf-8-sig') as f:
#    content = f.read()
#    print("File contents:\n", content)
cards = pd.read_csv('cards.csv', quotechar='"', skipinitialspace=True, encoding='utf-8-sig', engine='python')
print(cards.head())
print(cards[cards["Type"] == "Land"].sort_values("Name"))