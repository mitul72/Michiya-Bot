import requests
from bs4 import BeautifulSoup

def desc(a):
 b=a.split()
 if len(b)==1:
  url="https://myanimelist.net/anime.php?cat=anime&q="+b[0]+"%20&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=f&gx=0"
 elif len(b)==2:
  url="https://myanimelist.net/anime.php?cat=anime&q="+b[0]+"%20"+b[1]+"&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=f&gx=0"
 elif len(b)==3:
  url="https://myanimelist.net/anime.php?cat=anime&q="+b[0]+"%20"+b[1]+"%20"+b[2]+"%20&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=f&gx=0"
 elif len(b)==4:
  url="https://myanimelist.net/anime.php?cat=anime&q="+b[0]+"%20"+b[1]+"%20"+b[2]+"%20"+b[3]+"&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=f&gx=0"
 elif len(b)==5:
  url="https://myanimelist.net/anime.php?cat=anime&q="+b[0]+"%20"+b[1]+"%20"+b[2]+"%20"+b[3]+"%20"+b[4]+"&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=f&gx=0"
 elif len(b)==6:
  url="https://myanimelist.net/anime.php?cat=anime&q="+b[0]+"%20"+b[1]+"%20"+b[2]+"%20"+b[3]+"%20"+b[4]+"%20"+b[5]+"&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=f&gx=0"
 elif len(b)==7:
  url="https://myanimelist.net/anime.php?cat=anime&q="+b[0]+"%20"+b[1]+"%20"+b[2]+"%20"+b[3]+"%20"+b[4]+"%20"+b[5]+"%20"+b[6]+"&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=f&gx=0"

 l=[]
 l2=[]
 response = requests.get(url)
 html = response.text
 soup = BeautifulSoup(html, "html5lib")
 links = soup.findAll("a","hoverinfo_trigger fw-b fl-l")
 for link in links:
     anime=link.strong
     l2.append(anime)
     f=l2[0]
     href = link.get('href')
     l.append(href)
     x=l[0]

 name=f.text
 result=requests.get(x)
 html2=result.text
 soup2 = BeautifulSoup(html2, "html5lib")
 def rating():
  for i in range(0,10):
   rating = soup2.find("div", class_="score-label score-" + str(i))
#  rating=soup2.find("div",class_="score-label score-"+str(i))
#  rating=soup2.find("div",class_="score-label score-"+str(i))
   s=str(rating)
   if s.find("<div")!=-1:
  # rating=rating.text
    rating=str(rating.text)
    return rating
 rating=rating()
# rating=rating.text
 xyz=soup2.findAll("p",itemprop="description")

 for para in xyz:
    anidesc=str(para.text)
 anidesc=anidesc.replace("[Written by MAL Rewrite]","")
 return (anidesc,rating,name)


