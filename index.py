import bs4 as bs
import urllib.request
import regex as re


sauce = urllib.request.urlopen("http://www.cricbuzz.com/live-cricket-scorecard/18613/nz-vs-eng-1st-odi-england-tour-of-new-zealand-2018").read()

soup = bs.BeautifulSoup(sauce, 'lxml')

status = soup.find('div', class_='cb-scrcrd-status')
innings_1 = soup.find(id='innings_2')
print(innings_1.text)
print(status.text)