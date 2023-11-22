from functools import cache
import requests
import random
import time
from bs4 import BeautifulSoup
#print(tuples_to_string([("abc","aaaz"),("kkkkk","eeeee"),("xyz","iop")]))
result = requests.get("https://myanimelist.net/topanime.php")
src = result.content
soup = BeautifulSoup(src, 'lxml')
tags=soup.find_all('h3','hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3')
ratings=soup.find_all('div',class_="js-top-ranking-score-col di-ib al")
l=[]
l2=[]
for i in tags:
    a=i.text
    l.append(a)
for j in ratings:
    list=j.text
    l2.append(list)
l3=[]
@cache
def top_list(x,y):
# abc=" Anime".ljust(len(l[x])+3), "Rating"
 for output in range(x,y):
     abc=output+1,'.',l[output],"-",l2[output],"<a:star:833301009580425239>"
     l3.append(abc)
     result ='\n'.join('{} {} {} {} {} {}'.format(*pair) for pair in l3)
 l3.clear()
 return result
#top_list(0,10)

#  print(output+1,l[output],"-",l2[output])
#top_list(11,20)
#print(top_list(0,10))
la=['Lelouch', 'Luffy', 'L', 'Levi', 'Light', 'Zoro', 'Naruto', 'Edward', 'Rintarou', 'Killua', 'Kurisu', 'Itachi', 'Rem', 'Gintoki', 'Hachiman', 'Eren', 'Mikasa', 'Guts', 'Emilia', 'Saitama', 'Kazuto', 'Shouto', 'Kakashi', 'Ken', 'Spike', 'Sanji', 'Gokuu', 'Robin', 'Yato', 'Chika', 'Taiga', 'Hisoka', 'Asuna', 'Sasuke', 'Megumin', 'Hitagi', 'Zero', 'Kaguya', 'Roy', 'Tanjirou', 'Joseph', 'Saber', 'Kamina', 'Yuno', 'Ichigo', 'Shinobu', 'Yukino', 'Yuu', 'Mai', 'Ichigo']
lb=['Lamperouge', 'Monkey', 'Lawliet', 'Yagami', 'Roronoa', 'Uzumaki', 'Elric', 'Okabe', 'Zoldyck', 'Makise', 'Uchiha', 'Sakata', 'Hikigaya', 'Yeager', 'Ackerman', 'Kirigaya', 'Todoroki', 'Hatake', 'Kaneki', 'Spiegel', 'Son', 'Nico', 'Fujiwara', 'Aisaka', 'Morow', 'Yuuki', 'Uchiha', 'Senjougahara', 'Two', 'Shinomiya', 'Mustang', 'Kamado', 'Joestar', 'Gasai', 'Oshino', 'Yukinoshita', 'Ishigami', 'Sakurajima', 'Kurosaki']
def aniname2():
 first = random.randint(0, len(la))
 last = random.randint(0, len(lb))
 a=la[first], lb[last]
 str=' '.join(a)
 return str
def sug():
 g=['Fullmetal Alchemist: Brotherhood (TV)', 'Steins;Gate (TV)', 'Clannad After Story (TV)', 'your name. (movie)', 'Rurouni Kenshin: Trust & Betrayal (OAV)', 'Code Geass: Lelouch of the Rebellion R2 (TV)', 'Spirited Away (movie)', 'Mushishi: The Next Chapter (TV)', 'Cowboy Bebop (TV)', 'Princess Mononoke (movie)', '(The) Disappearance of Haruhi Suzumiya (movie)', 'A Silent Voice (movie)', '(The) Legend of the Galactic Heroes (OAV)', 'Mushi-Shi (TV)', 'Death Note (TV)', 'Maria Watches Over Us 3rd Season (OAV)', 'Maria Watches Over Us Season 2: Printemps (TV)', 'Code Geass: Lelouch of the Rebellion (TV)', 'Made in Abyss (TV)', 'anohana: The Flower We Saw That Day (TV)', 'Maria Watches Over Us 4th Season (TV)', 'Bunny Drop (TV)', 'Monster (TV)', 'Gintama (TV 2/2011)', 'Evangelion: 2.0 You Can (Not) Advance (movie)', 'Gintama (TV 4/2015)', 'Descending Stories: Showa Genroku Rakugo Shinju (TV)', "Gintama' (TV 3/2012)", 'Ghost in the Shell: Stand Alone Complex 2nd GIG (TV)', 'Grave of the Fireflies (movie)', 'Cross Game (TV)', 'Fullmetal Alchemist (TV)', 'Fighting Spirit (TV)', 'Summer Wars (movie)', 'Nausicaä of the Valley of the Wind (movie)', '(The) Girl Who Leapt Through Time (movie)', 'Nodame Cantabile (TV)', '5 Centimeters Per Second (movie)', 'Gurren Lagann (TV)', '(The) Garden of Sinners (movie series)', 'Hunter × Hunter (TV 2011)', 'My Neighbor Totoro (movie)', 'Wolf Children (movie)', 'Baccano! (TV)', 'Gintama: The Final Movie', 'Honey and Clover II (TV)', 'Attack on Titan (TV 4/2019)', "Natsume's Book of Friends (TV 4)", 'Star Blazers 2199 (TV)', 'Hajime no Ippo: New Challenger (TV)', "Howl's Moving Castle (movie)", 'GTO: Great Teacher Onizuka (TV)', 'Kanon (TV 2/2006)', "Kino's Journey (TV)", 'Puella Magi Madoka Magica (TV)', 'Mushishi Tokubetsu-hen: Hihamukage (special)', 'Time of Eve (ONA)', 'Millennium Actress (movie)', 'Monogatari Series Second Season (TV)', "Natsume's Book of Friends (TV 2)", 'Kaleido Star (TV)', 'Kids on the Slope (TV)', 'Mushishi: Zoku-Shō: Suzu no Shizuku (movie)', 'Time of Eve (movie)', 'Mononoke (TV)', 'Gankutsuou: The Count of Monte Cristo (TV)', '(The) Melancholy of Haruhi Suzumiya (TV)', "Natsume's Book of Friends (TV 3)", 'Clannad (TV)', 'Planetes (TV)', 'NANA (TV)', 'Your Lie in April (TV)', 'Made in Abyss: Dawn of the Deep Soul (movie)', 'Castle in the Sky (movie)', 'Looking Up At The Half-Moon (TV)', 'Samurai Champloo (TV)', 'Whisper of the Heart (movie)', 'Ouran High School Host Club (TV)', 'Ghost in the Shell: Stand Alone Complex (TV)', 'Aria the Origination (TV)', 'Maria Watches Over Us (TV)', 'Gurren Lagann the Movie – The Lights in the Sky Are Stars', 'Moribito - Guardian of the Spirit (TV)', 'Mushishi Zoku-Shō Tokubetsu-hen: Odoro no Michi (special)', 'Spice and Wolf II (TV)', 'A Place Further Than the Universe (TV)', 'Angel Beats! (TV)', 'ef: a tale of memories (TV)', '(The) Beast Player Erin (TV)', 'Legend of the Galactic Heroes: Overture to a New War (movie)', 'Black Lagoon: The Second Barrage (TV)', 'Welcome to the NHK (TV)', 'ef: a tale of melodies (TV)', 'Violet Evergarden (TV)', 'March comes in like a lion (TV 2)', 'My Hero Academia (TV 3)', 'Bloom Into You (TV)', 'Haibane Renmei (TV)', '(The) Tale of the Princess Kaguya (movie)', 'Sword of the Stranger (movie)', 'Cowboy Bebop: The Movie', 'Haikyu!! Second Season (TV)', 'Shōwa Genroku Rakugo Shinjū (TV)', 'Honey and Clover (TV)', 'Hunter X Hunter (OAV)', 'My Hero Academia (TV 2)', '(The) Twelve Kingdoms (TV)', 'Gintama. (TV 5/2017)', 'Tokyo Godfathers (movie)', 'Haikyu!! (TV 3)', 'Owarimonogatari (specials)', 'Mobile Suit Gundam UC (OAV)', 'Romeo × Juliet (TV)', 'Maison Ikkoku (TV)', 'Major (TV)', 'Toradora! (TV)', 'Shirobako (TV)', 'Tsubasa Tokyo Revelations (OAV)', 'ERASED (TV)', 'Evangelion: 1.0 You Are (Not) Alone (movie)', 'Re:ZERO -Starting Life in Another World- (TV)', 'Full Metal Panic! The Second Raid (TV)', 'Hellsing Ultimate (OAV)', 'BECK: Mongolian Chop Squad (TV)', 'Hunter X Hunter (TV)', 'Chihayafuru (TV)', 'Fate/Zero (TV 2)', 'Kimi ni Todoke - From Me to You (TV)', 'Haikyu!! To The Top (TV 5)', 'Mob Psycho 100 II (TV)', 'Maquia - When the Promised Flower Blooms (movie)', 'Katanagatari (TV)', 'Ping Pong (TV)', 'Berserk (TV)', 'Brave King GaoGaiGar Final (OAV)', 'Attack on Titan (TV 2/2017)', 'Bakuman. 2 (TV)', 'Den-noh Coil (TV)', 'Nodame Cantabile: Paris (TV)', "Natsume's Book of Friends (TV)", 'One Piece Episode of Nami: Kōkaishi no Namida to Nakama no Kizuna (special)', '(The) Rose of Versailles (TV)', 'Natsume Yūjin-Chō Roku (TV 6)', 'Princess Tutu (TV)', '(La) Maison en Petits Cubes (movie)', 'Vinland Saga (TV)', 'Made in Abyss (movies)', 'Kaiba (TV)', 'Liz and the Blue Bird (movie)', 'Conan, the Boy in Future (TV)', 'Azumanga Daioh (TV)', 'Full Metal Panic? Fumoffu (TV)', 'Ascendance of a Bookworm (TV 2)', 'Hunter X Hunter: G I Final (OAV)', 'Sound! Euphonium 2 (TV)', 'Eden of the East (TV)', 'Yuri!!! on Ice (TV)', 'Nodame Cantabile: Finale (TV)', '(The) Garden of Words (movie)', 'Hotarubi no Mori e (movie)', 'Trigun (TV)', 'Paprika (movie)', 'Ghost in the Shell: Stand Alone Complex: Solid State Society (movie)', 'Kimi ni Todoke 2nd Season (TV)', 'Violet Evergarden I: Eternity and the Auto Memory Doll (movie)', 'R.O.D -The TV-', 'Hanasaku Iroha - Blossoms for Tomorrow (TV)', 'Legend of the Galactic Heroes: My Conquest is the Sea of Stars (movie)', 'School Rumble: 2nd Semester (TV)', 'Haikyu!! (TV)', 'Berserk: The Golden Age Arc III - The Advent (movie)', 'Gungrave (TV)', 'Magnetic Rose (movie)', 'Spice and Wolf (TV)', 'Natsume Yūjin-Chō Go (TV 5)', 'Mob Psycho 100 (TV)', '(The) Eccentric Family 2 (TV)', 'Last Exile (TV)', 'Rurouni Kenshin (TV)', 'Bakuman. 3 (TV)', 'Kono Oto Tomare!: Sounds of Life (TV 2)', 'Assassination Classroom (TV 2)', 'Chihayafuru 3 (TV)', 'Comedy (OAV)', 'Fruits Basket 2nd Season (TV)', 'Lupin the Third: Part 5 (TV)', 'Fruits Basket (TV 2/2019)', 'xxxHOLiC: Kei (TV)', 'Attack on Titan (TV)', 'Neon Genesis Evangelion: The End of Evangelion (movie)', 'Master Keaton (OAV)', 'Skip Beat! (TV)', '(The) Super Dimension Fortress Macross: Do You Remember Love? (movie)', "Kiki's Delivery Service (movie)", 'Kizumonogatari Part 3: Reiketsu (movie)', 'Romeo and the Black Brothers (TV)', 'Hunter X Hunter: Greed Island (OAV)', 'Ghost in the Shell: Stand Alone Complex - Individual Eleven (OAV)', '(The) Super Dimension Fortress Macross (TV)', 'Bakemonogatari (TV)']
 rand=random.randint(0,len(g))
 i=g[rand]
 return i
def topic_rand():
 topic_url="https://www.conversationstarters.com/generator.php"
 topic_response=requests.get(topic_url)
 topic_html = topic_response.text
 topic_soup = BeautifulSoup(topic_html, "html5lib")
 topic_link = topic_soup.findAll("div",id="random")
 for topic_i in topic_link:
     topic_rand=topic_i.text
 return topic_rand
