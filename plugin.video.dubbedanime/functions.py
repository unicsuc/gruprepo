import re,xbmc,json,xbmcaddon,urlparse,xbmcgui,sys,xbmcplugin
from urllib import urlencode,unquote
from os.path import join,exists
from os import listdir
AddonInfo 			= xbmcaddon.Addon().getAddonInfo
Translate 			= xbmc.translatePath
Compile 			= lambda x,y: re.compile(x).findall(y)
EndOfDirectory 		= lambda: xbmcplugin.endOfDirectory(int(sys.argv[1]))

Addon_Path = Translate(AddonInfo("path"))

Join = lambda x:join(Addon_Path,"resources","images",x)

def Image(x):
	contents = listdir(join(Addon_Path,"resources","images"))
	for item in contents:
		find = re.findall("{x}\..*".format(x=x),item,re.IGNORECASE)
		if len(find) == 1:
			xbmc.log(Join(find[0]),2)
			return Join(find[0])
	return False

def Add(name, url='', mode='', iconimage=AddonInfo('icon'), fanart=AddonInfo('fanart'), description='',folder=False,playable=False,mime=False):
	#This Is Where The Params Are Defined. Were Creating The Following Params ['url','mode','name','iconimage']
	if Image(name) and iconimage == AddonInfo("icon"):
		iconimage = Image(name)
	u=urlparse.urlunparse(['plugin', AddonInfo('id'), '/', '', urlencode({'url':url,'mode':mode,'name':name,'iconimage':iconimage}), ''])
	liz = xbmcgui.ListItem(name)
	handle=sys.argv[1]
	if playable:
		liz.setProperty('isPlayable', 'true')
		liz.setInfo(type='video', infoLabels={'title':name,'mediatype':'video'})
	liz.setArt({ 'fanart': fanart,'thumb': iconimage,"poster":iconimage,"icon":iconimage})
	ok = xbmcplugin.addDirectoryItem(handle=int(handle), url=u, listitem=liz, isFolder=folder)
	return ok

def GetURL(url,cookie="dubbedanime.cookie",data=None):
	import cookielib
	import urllib2
	import os
	if data:data = urlencode(data)
	Profile = Translate(AddonInfo("profile"))
	if not os.path.exists(Profile):
		os.makedirs(Profile)
	cookies = cookielib.LWPCookieJar()
	cookies_location = os.path.join(Profile,cookie)
	if os.path.exists(cookies_location):
		cookies.load(cookies_location)
	handlers = [
	    urllib2.HTTPHandler(),
	    urllib2.HTTPSHandler(),
	    urllib2.HTTPCookieProcessor(cookies)
	    ]
	opener = urllib2.build_opener(*handlers)

	def fetch(uri):
	    req = urllib2.Request(uri,data=data)
	    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
	    return opener.open(req)

	def dump():
	    for cookie in cookies:
	        print cookie.name, cookie.value
	res = fetch(url)
	cookies.save(cookies_location)
	return [res,cookies]

def GetVideoLinks(url):
	req = GetURL(url)
	Data = Compile(r"var episode_videos = (\[.*\])",req[0].read())[0]
	JSON = json.loads(Data)
	return JSON

def GetLink(host,id):
	if "trollvid" in host:
		Data = GetURL("https://trollvid.net/embed/{id}".format(id=id),"trollvid.cookie")
		URL = Compile(r"unescape\(\'(.*)\'\)",Data[0].read())[0]
		return unquote(URL)
	elif "mp4upload" in host:
		Data = GetURL("https://mp4upload.com/embed-{id}.html".format(id=id),"mp4upload.cookie")
		ID = Compile(r"mp4\|video\|(.*)\|\d{1,4}\|setup",Data[0].read())[0]
		return "https://www1.mp4upload.com:282/d/{ID}/video.mp4".format(ID=ID)

def Keyboard(heading=AddonInfo("name")):
	kb = xbmc.Keyboard ('', heading)
	kb.doModal()
	if (kb.isConfirmed()):
		return kb.getText()
	else:
		return None

def Soup(content):
	from bs4 import BeautifulSoup as BS
	return BS(content,"html.parser")