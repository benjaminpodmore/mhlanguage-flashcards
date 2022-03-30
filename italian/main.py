import requests
import csv
import time

START = 87906
END = 89000

card_sets = []
word_count = 0

for i in range(START, END + 1):
    if i % 2 != 0:
        continue
    r = requests.get(f'https://mhe-language-lab.azurewebsites.net/api/GetFlashCards?menuID={i}')
    card_sets.append(r.json())
    word_count += len(r.json())
    time.sleep(2)

for idx, card_set in enumerate(card_sets):
    with open(f'data/complete/{idx}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for card in card_set:
            writer.writerow([card['SideA'], card['SideB']])

