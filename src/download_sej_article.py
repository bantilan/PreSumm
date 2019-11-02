#pip install requests-html

from requests_html import HTMLSession
session = HTMLSession()

url = "https://gamingph.com/2019/09/chess-rush-patch-review-new-hero-headreaper-and-guild-system/"

with session.get(url) as r:

  selector="#post-21527 > div.entry"
  post = r.html.find(selector, first=True)

  text = post.text
  text = text.splitlines(True)

  text = text[1:-5]

  with open("python-data-stories.txt","a") as f:
      f.writelines(text)
