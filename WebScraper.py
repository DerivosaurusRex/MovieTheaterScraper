from bs4 import BeautifulSoup
import requests
import json

url='https://www.blitz-cinestar.hr/cinestar-zagreb'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

tweetArr=[]
for tweet in content.findAll('div', attrs={"class": "movie_box"}):
    tweetObject = {
        "movie": tweet.find('a', attrs={"class": "movieItemTitle"}).text,
    }
    print(tweetObject['movie'])
    tweetArr.append(tweetObject)

with open('movieData.json', 'w', encoding='utf-8') as outfile:
    json.dump(tweetArr, outfile)



