import xbmc,urlparse,xbmcplugin,xbmcgui,json,sys
from functions import *




def Index():
	Add("Search",mode="Search",folder=True)
	Add("Genres",mode="Genres",folder=True)
	Add("Latest Episodes",mode="Latest",folder=True)

def Search():
	Input = Keyboard()
	if Input:
		Searchterm(Input)

def Searchterm(term):
	Data = GetURL("https://ww5.dubbedanime.net/search?term={term}".format(term=term))
	bs = Soup(Data[0].read())
	Content = bs.find_all("li","w-100 list-view-link py-1 px-2 my-1 border-secondary d-inline-block")
	for item in Content:
		try:
			URL = item.a.get("href")
			Name = item.a.string
			Add(Name,URL,"Series",folder=True)
		except:
			pass

def Genres():
	Data = GetURL("https://dubbedanime.net/genres")
	bs = Soup(Data[0].read())
	Content = bs.find_all("div","form-check form-check-inline")
	for genre in Content:
		try:
			String = genre.label.string
			Add(String[0].upper()+String[1:],mode="Genre",folder=True)
		except:
			pass

def Genre(genre):
	Data = GetURL("https://dubbedanime.net/genres",data={"genres[]":genre.lower()})
	JSON = json.loads(Data[0].read())
	for item in sorted(JSON,key=lambda k: k['english']):
		try:
			# Name = item["title"]
			Name = item["english"]
			Image = item["image"]
			Description = item["synopsis"]
			URL = item["url"]
			Add(Name,URL,"Series",Image,folder=True)
		except:
			pass
	xbmcplugin.setContent(int(sys.argv[1]), 'movies')

def Series(url):
	Data = GetURL(url)
	bs = Soup(Data[0].read())
	Episodes = bs.find_all("div","fig-cont position-relative pr-2 w-25")
	for item in reversed(Episodes):
		try:
			Image = "http:"+item.figure.img.get("src")
			Name = item.figure.img.get("title")
			URL = item.figure.a.get("href")
			Add(Name,URL,"Playlist",Image,folder=True)
		except:
			pass
	xbmcplugin.setContent(int(sys.argv[1]), 'episodes')


def NewEpisodes():
	Data = GetURL("https://dubbedanime.net/")
	bs = Soup(Data[0].read())
	NewEpisodes = bs.find_all("div","fig-cont d-inline-block position-relative pr-2")
	for item in NewEpisodes:
		try:
			Link = item.a.get("href")
			Name = item.a.string
			Img = "http:"+item.img.get("src")
			Add(Name,Link,"Playlist",Img,folder=True)
		except:
			pass
	xbmcplugin.setContent(int(sys.argv[1]), 'episodes')

def Playlist(name,url,icon):
	VideoLinks = GetVideoLinks(url)
	for item in VideoLinks:
		try:
			Add("{Host} - {Type}".format(Host=item["host"],Type=item["type"]),item["id"],"Play",icon,playable=True)
		except:
			pass

def Play(name,url):
	newurl = GetLink(name,url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, xbmcgui.ListItem(path=newurl))
###############################################################################################################
mode = None
###############################################################################################################
for x in urlparse.parse_qsl(sys.argv[2][1:]):globals()[x[0]] = x[1]
###############################################################################################################
if	  mode		==	  "Play":		Play(name,url)
elif  mode		==	  "Playlist":	Playlist(name,url,iconimage)
elif  mode 		== 	  "Series":		Series(url)
elif  mode 		== 	  "Genres":		Genres()
elif  mode 		== 	  "Genre":		Genre(name)
elif  mode 		== 	  "Latest": 	NewEpisodes()
elif  mode 		== 	  "Search": 	Search()
else:Index()
EndOfDirectory()