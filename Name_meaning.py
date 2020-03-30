import requests
from bs4 import BeautifulSoup as bs

print("Welcome to the program!\n")
loop = True
while loop:
    name = str(input("Enter the name of person to find its meaning :"))
    print("fetching data")
    url = "https://www.thenamemeaning.com/"
    url = url+name+"/"
    r = requests.get(url)
    data = r.content
    soup = bs(data,"lxml")
    out = "The meaning of the name {} is".format(name)
    data = soup.strong.next_sibling
    print(out+data)
    ch = str(input("\nDo you wanna enter again?(y/n)")).lower()
    if ch == 'y':
        continue
    else:
        loop = False
        print("Exiting")
