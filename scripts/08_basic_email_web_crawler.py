import requests
from bs4 import BeautifulSoup


# get url
url = input('Enter a URL (include `http://`): ')

# connect to the url
responce = requests.get(url)
html = responce.text
soup = BeautifulSoup(html,"html.parser")
print(html)

links = []
for i in soup.find_all("a",href=True):
    links.append(i)
    print("leitud link: ", i)
# # print the number of links in the list
# print("\nFound {} links".format(len(links)))
# for email in emails:
#     print(email)
