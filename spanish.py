import requests


i = 19496
f = 19602

a = open("spanish_vocab.txt","w")

r = requests.get(f"https://mhe-language-lab.azurewebsites.net/api/GetFlashCards?menuID={i}")

for x in range(i,f+1):
    r = requests.get(f"https://mhe-language-lab.azurewebsites.net/api/GetFlashCards?menuID={x}")
    l = r.json()
    for card in l:
        a.write(f"{card['SideA']}\t{card['SideB']}\n")


a.close()
