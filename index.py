import bs4 as bs
import urllib.request
import matplotlib.pyplot as plt
import regex as re


sauce = urllib.request.urlopen("http://www.cricbuzz.com/live-cricket-scorecard/18613/nz-vs-eng-1st-odi-england-tour-of-new-zealand-2018").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

status = soup.find('div', class_='cb-scrcrd-status')
innings_1 = soup.find(id='innings_2')
text_gray = innings_1.find_all('span', class_= 'text-gray')
sbitems = innings_1.find_all('a', class_='cb-text-link')
items = innings_1.find_all
# for i, j in zip(sbitems, text_gray):
#     print(i.text+"      "+j.text)
#     #print(j.text)

cbscrditems = innings_1.find_all('div', class_='cb-scrd-itms')

labels = []
sizes =[]
outs=[]

for i in cbscrditems:
    sbitems = i.find('a', class_='cb-text-link')
    if sbitems:
        labels.append(sbitems.text)
    text_gray = i.find('span', class_ = 'text-gray')
    if text_gray:
        outs.append(text_gray.text)
    bold = i.find('div', class_='text-bold')
    if bold:
        sizes.append(int(bold.text))
# for i in text_gray:
#     print(i.text)
# print(innings_1.text)
# print(status.text)
    #print(i.text)
print(len(labels), len(sizes))
fig1, ax1 = plt.subplots()

ax1.pie(sizes[:len(outs)],explode=None, labels=None, autopct='%0.1f%%', shadow=True, startangle=90)
ax1.legend(labels= labels[:len(outs)])
ax1.axis('equal')
plt.show()
