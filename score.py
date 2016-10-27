# workaround for windows console encoding error (http://stackoverflow.com/questions/16346914/python-3-2-unicodeencodeerror-charmap-codec-cant-encode-character-u2013-i)
# chcp 65001
# set PYTHONIOENCODING=utf-8

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.cricbuzz.com/cricket-match/live-scores")

soup = BeautifulSoup(r.text, "lxml")
for match in soup.find_all("a",{"class":"cb-lv-scrs-well-live"}):
	print("\t" + match.text)