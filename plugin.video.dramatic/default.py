import sys
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmc
import urllib
import urlparse
import requests
from bs4 import BeautifulSoup
import resolveurl

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
xbmcplugin.setContent(addon_handle, 'movies')

scrape_base = "https://www3.watchasian.co/"
mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

mostpopulardrama = "most-popular-drama"
mostpopularstars = "list-star.html"
searchdrama = "search?type=movies&keyword="
searchstar = "search?type=stars&keyword="
page = "?page="

base_page = 1

def usersearch():
    kb = xbmc.Keyboard('default', 'heading')
    kb.setDefault('')
    kb.setHeading('Search')
    kb.setHiddenInput(False)
    kb.doModal()
    if (kb.isConfirmed()):
        searched  = kb.getText()
        search_term = searched.replace(" ", "+")
        return(search_term)
    else:
        return

def bsmenu(url):
    menuitem = []    
    allmenu = []
    get = requests.get(url, headers = mozhdr)
    soupeddata = BeautifulSoup(get.content, "html.parser")
    links = soupeddata.find_all("div", class_ = "tab-content left-tab-1 selected")
    for a in links:
        img = a.find_all("li")
        for b in img:
            link = b.find_all("a")
            for c in link:
                href = c.get("href")
            imgs = b.find_all("img")
            for c in imgs:
                image = c.get("data-original")
                title = c.get("alt") 
                title = title.replace("&#039;", "'")
            menuitem = [title, href, image]
            allmenu.append(menuitem)
	return allmenu
	
def bsstars(url):
    menuitem = []    
    allmenu = []
    get = requests.get(url, headers = mozhdr)
    soupeddata = BeautifulSoup(get.content, "html.parser")
    links = soupeddata.find_all("ul", class_ = "list-star")
    for a in links:
        link = a.find_all("a", class_ = "img")
        for c in link:
            href = c.get("href")
            imgs = c.find_all("img")
            for d in imgs:
                image = d.get("data-original")
                title = d.get("alt")
            menuitem = [title, href, image]
            allmenu.append(menuitem)
        menuitem = []
	return allmenu

def bsstars2(url):
    menuitem = []    
    allmenu = []
    get = requests.get(url, headers = mozhdr)
    soupeddata = BeautifulSoup(get.content, "html.parser")
    links = soupeddata.find_all("ul", class_ = "switch-block list-episode-item")
    for a in links:
        img = a.find_all("li")
        for b in img:
            link = b.find_all("a", class_ = "img")
            for c in link:
                href = c.get("href")
                imgs = c.find_all("img")
                for d in imgs:
                    image = d.get("data-original")
                    title = d.get("alt")
            menuitem = [title, href, image]
            allmenu.append(menuitem)
            menuitem = []
	return allmenu
	
def bsepisodes(url):
    epinfo = []    
    alleps = []
    get = requests.get(url, headers = mozhdr)
    soupeddata = BeautifulSoup(get.content, "html.parser")
    links = soupeddata.find_all("div", class_ = "tab-content left-tab-1 selected")
    for a in links:
        episode = a.find_all("a")
        for b in episode:
            types = b.find_all("span", class_ = "type SUB")
            types2 = b.find_all("span", class_ = "type RAW")
            for c in types:
                type = c.text
                type = type.replace(" ", "")
            for c in types2:
                type = c.text
                type = type.replace(" ", "")
            href = b.get("href")
            title = href.replace("/", "")
            title = title.replace("-", " ")
            title = title.replace(".html", "")
            title = title.title()		
            title = title + " - " + type			
            epinfo = [title, href]
            alleps.insert(0, epinfo)
            epinfo = []
    return alleps

def resolve_url(url):
    duration=7500   #in milliseconds
    message = "Cannot Play URL"
    stream_url = resolveurl.HostedMediaFile(url=url).resolve()
    # If urlresolver returns false then the video url was not resolved.
    if not stream_url:
        dialog = xbmcgui.Dialog()
        dialog.notification("ResolveURL Error", message, xbmcgui.NOTIFICATION_INFO, duration)
        return False
    else:        
        return stream_url

def play_video(path):
    """
    Play a video by the provided path.
    :param path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    vid_url = play_item.getfilename()
    stream_url = resolve_url(vid_url)
    if stream_url:
        play_item.setPath(stream_url)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

	
def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
    url = build_url({'mode': 'mostpopulardrama', 'foldername': mostpopulardrama, 'pagenum' : base_page})
    li = xbmcgui.ListItem('Most Popular Drama', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    url = build_url({'mode': 'mostpopularstar', 'foldername': mostpopularstars, 'pagenum' : base_page})
    li = xbmcgui.ListItem('Most Popular Stars', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    url = build_url({'mode': 'searchdrama', 'foldername': searchdrama})
    li = xbmcgui.ListItem('Drama Search', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    url = build_url({'mode': 'searchstar', 'foldername': searchstar})
    li = xbmcgui.ListItem('Star Search', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)
	
elif mode[0] == 'mostpopulardrama':
    scrape_add = args['foldername'][0]    
    pagenum = args['pagenum'][0]
    scrape_link = scrape_base + scrape_add + page + str(pagenum)
    info = bsmenu(scrape_link)
    count = 0
    for a in info:
        url = build_url({'mode': 'serieschoice', 'foldername': info[count][1]})
        li = xbmcgui.ListItem(info[count][0], iconImage=info[count][2])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)        
        count = count + 1 
    nextpage = int(pagenum) + 1
    prevpage = int(pagenum) - 1
    if pagenum == 1:
        url = build_url({'mode': 'mostpopulardrama', 'foldername': mostpopulardrama, 'pagenum' : newpage})
        li = xbmcgui.ListItem('Next Page', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)	
    elif pagenum <> 1:
        url = build_url({'mode': 'mostpopulardrama', 'foldername': mostpopulardrama, 'pagenum' : nextpage})
        li = xbmcgui.ListItem('Next Page', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
        url = build_url({'mode': 'mostpopulardrama', 'foldername': mostpopulardrama, 'pagenum' : prevpage})
        li = xbmcgui.ListItem('Previous Page', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)		
    xbmcplugin.endOfDirectory(addon_handle)	

elif mode[0] == 'mostpopularstar':
    scrape_add = args['foldername'][0]    
    pagenum = args['pagenum'][0]
    scrape_link = scrape_base + scrape_add + page + str(pagenum)
    info = bsstars(scrape_link)
    count = 0
    for a in info:
        url = build_url({'mode': 'starchoice', 'foldername': info[count][1]})
        li = xbmcgui.ListItem(info[count][0], iconImage=info[count][2])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)        
        count = count + 1 
    nextpage = int(pagenum) + 1
    prevpage = int(pagenum) - 1
    if pagenum == 1:
        url = build_url({'mode': 'mostpopularstar', 'foldername': mostpopularstars, 'pagenum' : nextpage})
        li = xbmcgui.ListItem('Next Page', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)	
    elif pagenum <> 1:
        url = build_url({'mode': 'mostpopularstar', 'foldername': mostpopularstars, 'pagenum' : nextpage})
        li = xbmcgui.ListItem('Next Page', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
        url = build_url({'mode': 'mostpopularstar', 'foldername': mostpopularstars, 'pagenum' : prevpage})
        li = xbmcgui.ListItem('Previous Page', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)		
    xbmcplugin.endOfDirectory(addon_handle)	

elif mode[0] == 'searchdrama':
    scrape_add = args['foldername'][0]
    search_add = usersearch()
    scrape_link = scrape_base + scrape_add + search_add
    info = bsmenu(scrape_link)
    count = 0
    for a in info:
        url = build_url({'mode': 'serieschoice', 'foldername': info[count][1]})
        li = xbmcgui.ListItem(info[count][0], iconImage=info[count][2])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)        
        count = count + 1 
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'searchstar':
    scrape_add = args['foldername'][0]
    search_add = usersearch()
    scrape_link = scrape_base + scrape_add + search_add
    info = bsstars2(scrape_link)
    count = 0
    for a in info:
        url = build_url({'mode': 'starchoice', 'foldername': info[count][1]})
        li = xbmcgui.ListItem(info[count][0], iconImage=info[count][2])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)        
        count = count + 1 
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'serieschoice':
    scrape_add = args['foldername'][0]
    scrape_link = scrape_base + scrape_add
    episodes = bsepisodes(scrape_link)
    count = 0
    for a in episodes:
        linkcentral = scrape_base + episodes[count][1]
        get = requests.get(linkcentral, headers = mozhdr)
        soupeddata = BeautifulSoup(get.content, "html.parser")
        serveranime = soupeddata.find_all("li", class_ = "Standard Server selected")
        serverkvid = soupeddata.find_all("li", class_ = "kvid")
        serverstreamango = soupeddata.find_all("li", class_ = "streamango")
        serverestram = soupeddata.find_all("li", class_ = "estram")
        serverrapidvideo = soupeddata.find_all("li", class_ = "rapidvideo")
        serveropen = soupeddata.find_all("li", class_ = "openload")
        serverthevideo = soupeddata.find_all("li", class_ = "thevideo")	
        for a in serveranime:
            anime = a.get("data-video") 
        for a in serverkvid:
            kvid = a.get("data-video") 
        for a in serverstreamango:
            streamango = a.get("data-video")
        for a in serverestram:
            estram = a.get("data-video")
        for a in serverrapidvideo:
            rapidvideo = a.get("data-video")
        for a in serveropen:
            open = a.get("data-video")
        for a in serverthevideo:
            thevideo = a.get("data-video")	
        url = build_url({'mode': 'episodechoice', 'foldername': streamango})
        li = xbmcgui.ListItem(episodes[count][0], iconImage='DefaultVideo.png')
        li.setProperty('IsPlayable' , 'true')		
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)  
        count = count + 1 
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'starchoice':
    scrape_add = args['foldername'][0]
    scrape_link = scrape_base + scrape_add
    info = bsmenu(scrape_link)
    count = 0
    for a in info:
        url = build_url({'mode': 'serieschoice', 'foldername': info[count][1]})
        li = xbmcgui.ListItem(info[count][0], iconImage=info[count][2])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)        
        count = count + 1 
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'episodechoice':
    scrape = args['foldername'][0]
    play_video(scrape)


