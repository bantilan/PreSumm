#pip install requests-html

from requests_html import HTMLSession
session = HTMLSession()

open("/content/PreSumm/bert_data/cnndm/python-data-stories.txt","w").close()

url = "https://gamingph.com/2019/10/super-mecha-champions-update-for-halloween-trick-or-treat-and-new-season-opener/"

with session.get(url) as r:

  selector=".post > div.entry"
  post = r.html.find(selector, first=True)

  text = post.text
  text = text.splitlines(True)

  text = text[1:-5]

  with open("/content/PreSumm/bert_data/cnndm/python-data-stories.txt","a") as f:
      f.writelines(text)
