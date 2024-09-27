from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
articles = soup.find_all(class_ = "titleline")

article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.find(name="a").get("href")
    article_links.append(article_link)

article_upvotes = soup.find_all(class_ = "score")

all_upvotes = []

for upvote in article_upvotes:
    all_upvotes.append(int(upvote.getText().split()[0]))

max_upvotes = max(all_upvotes)
position = all_upvotes.index(max_upvotes)
print(article_texts[position])
print(article_links[position])










#with open ("bs4-start/website.html", "r") as file:
    #contents = file.read()

#soup = BeautifulSoup(contents, "html.parser")

#print(soup.title.string)

#print(soup.prettify())

#allanchors = soup.find_all(name="a")

#for anchors in allanchors:
    #print(anchors.getText())
    #print(anchors.get("href"))

#heading = soup.find(name="h1", id="name")
#(heading)

#section_heading = soup.find(name="h3", class_ = "heading")

#print(section_heading.getText())

#company_url=soup.select_one(selector="p a")

#print(company_url)

#name=soup.select_one(selector="#name")

#print(name)

#headings=soup.select(".heading")

#print(headings)


