# -*- coding: utf-8 -*-

'''
    Masterani Redux add-on

    this program is free software: you can redistribute it and/or modify
    it under the terms of the gnu general public license as published by
    the free software foundation, either version 3 of the license, or
    (at your option) any later version.

    this program is distributed in the hope that it will be useful,
    but without any warranty; without even the implied warranty of
    merchantability or fitness for a particular purpose.  see the
    gnu general public license for more details.

    you should have received a copy of the gnu general public license
    along with this program.  if not, see <http://www.gnu.org/licenses/>.
'''

import base64
import json
import re
import requests
import xbmc
import xbmcgui
import re
from resources.lib.modules import cache
from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import masterani
from resources.lib.modules.control import progressDialog
from resources.lib.modules.watched import Watched
from resources.lib.modules import kitsu
import resolveurl

count = 0

#GETLINKS
def getlinks(url):
    link_list = []	
    link_list_id = []
    with requests.session() as s:
        p = s.get(url)
        print (p.text).encode('utf-8')
        ep_id = (p.text).encode('utf-8').split('var args = { anime: {"info":{', 1)[1]
        ep_id = ep_id.encode('utf-8').split('"id":', 2)[2]
        ep_id = ep_id.encode('utf-8').split(',', 1)[0]
        print ep_id
        try:
            videos = re.findall(r'videos = (\[.*?\])', p.text)[0]
            print videos
            videos = json.loads(videos)
            for i in videos:
                type = ''
                if type == '':
                    type = 1
                embed_id = 'None Required' #Literally only got this part to fix an error
                link_list.append({'url': i['src'], 'name': 'Aika', 'quality': i['res'], 'type': type, 'embed_id': embed_id})
        except:
            #mirrors = re.findall(r"mirrors= (.*?), auto_update", p.text)[0]
            mirrors = (p.text).split("<video-mirrors :mirrors='", 1)[1]
            mirrors = mirrors.split("'></video-mirrors>", 1)[0]
            mirrors = json.loads(mirrors)
            for i in mirrors:
                link_list.append({'embed_id':i['embed_id'],'url': i['host']['embed_prefix'] + i['embed_id'], 'name': i['host']['name'], 'quality': i['quality'], 'type': i['type']})
    print link_list
    link_list_id.append(link_list)
    link_list_id.append(ep_id)
    return link_list_id

def getid(url):
    with requests.session() as s:
        p = s.get(url)
        id = p.text
        id = id.split('"id":', 2)[2]
        print id
        id = id.split(',', 1)[0]
        print id        
    return id
	
def getdirect(hostname, url, quality, embed_id):
    if 'Stream.moe' in hostname:
        mp4 = resolveurl.resolve(url)
    if 'MP4Upload' in hostname:
        mp4 = resolveurl.resolve(url)     
    if 'Vidstreaming' in hostname:
        mp4 = resolveurl.resolve(url)
    if 'Openload' in hostname:
        mp4 = resolveurl.resolve(url)
    if 'Drive.g' in hostname:
        mp4 = resolveurl.resolve(url)
    if 'Rapidvideo' in hostname:
        rv = requests.get(url + '&q=%sp' % quality)
        link = (rv.text).encode('utf-8')
        link = link.split('<source src="', 1)[1]
        link = link.split('" type="video/mp4"', 1)[0]
        mp4 = link
    #AIKA TO BE REMOVED SOON
    if 'Aika' in hostname:
        mp4 = url
    if 'Streamango' in hostname:
        mp4 = resolveurl.resolve(url)
    if 'Mystream' in hostname:
        link = requests.get(url)
        link = (link.text).encode('utf-8')
        link = link.split('<source src="', 1)[1]
        link = link.split('" type="video/mp4"', 1)[0]
        mp4 = link
    if 'Tiwi.kiwi' in hostname:
        viewpage = client.request("https://tiwi.kiwi/" + embed_id + "#")
        hashsnip = re.compile("(?<=\,\\')(.*)(?=\\')").findall(viewpage)[0] # find hash
        qualitynum = "o" # original
        if quality is 720:
            qualitynum = "n" # normal (720p)
        elif quality is 480:
            qualitynum = "l" # low (480p)
        urlsnip = "dl?op=download_orig&id=" + embed_id + "&mode=" + qualitynum + "&hash=" + hashsnip
        downloadpage = client.request("https://tiwi.kiwi/" +urlsnip)
        mp4Raw = re.compile("href=\"(.+?mp4)").findall(downloadpage)[0]
        try: from urllib import quote
        except: pass
        mp4 = quote(mp4Raw, safe="%/:=&?~#+!$,;'@()*[]")
    mp4 = str(mp4)
    return mp4

def play(anime_id, episode_id):

    #global count
    #count = count + 1
    
    episode_link = episode_id
    episode_number = episode_link.split("/", 6)[6]
	
    l1 = "Fetching video."
    progressDialog.create(heading="Masterani Redux", line1="Fetching video.")
    progressDialog.update(0, line1=l1, line3="Loading hosts.")
    
    hosts = getlinks(episode_link)[0]   
    ep_id = getlinks(episode_link)[1]
    #linkforcover = getcover(episode_link)

    if hosts is None:
        xbmcgui.Dialog().ok("Masterani Redux", "Something went wrong.", "Please try again later.")
        return

    #Remove Disabled Hosts

    if control.setting("host.mystream") == "false":
            for e in hosts:
                if 'Mystream' in e['name']:
                    hosts.remove(e)

    if control.setting("host.mp4upload") == "false":
            for e in hosts:
                if 'MP4Upload' in e['name']:
                    hosts.remove(e)

    if control.setting("host.youtube") == "false":
        for e in hosts:
            if 'YouTube' in e['name']:
                hosts.remove(e)
        
    if control.setting("host.stream.moe") == "false":
        for e in hosts:
            if 'Stream.moe' in e['name']:
                hosts.remove(e)

    if control.setting("host.drive.g") == "false":
        for e in hosts:
            if 'Drive.g' in e['name']:
                hosts.remove(e)
                
    if control.setting("host.vidstreaming") == "false":
        for e in hosts:
            if 'Vidstreaming' in e['name']:
                hosts.remove(e)
            
    if control.setting("host.rapidvideo") == "false":
        for e in hosts:
            if 'Rapidvideo' in e['name']:
                hosts.remove(e)

    if control.setting("host.aika") == "false":
        for e in hosts:
            if 'Aika' in e['name']:
                hosts.remove(e)

    if control.setting("host.streamango") == "false":
        for e in hosts:
            if 'Streamango' in e['name']:
                hosts.remove(e)
        
    if control.setting("host.openload") == "false":
        for e in hosts:
            if 'Openload' in e['name']:
                hosts.remove(e)
                
    if control.setting("host.tiwikiwi") == "false":
        for e in hosts:
            if 'Streamango' in e['name']:
                hosts.remove(e)

    progressDialog.update(25, line1=l1, line3="Loading episodes urls.")
    progressDialog.update(50, line1=l1, line3="Picking nose.")

    hostlist = []

    videos = sorted(hosts, key=lambda k: (-int(k['type']), int(k['quality'])), reverse=True)
    print videos

    autoplay = control.setting("autoplay.enabled")
    maxq = control.setting("autoplay.maxquality")
    subdub = control.setting("autoplay.subdub")

    videoCounter = 0
    autoplayHost = 0
    hostCounter = 0
    
    autovids = []
    

#    while videoCounter < len(videos):
#        try:
#            hostname = videos[videoCounter]['name']
#            subs = 'Sub' if videos[videoCounter]['type'] is 1 else 'Dub'
#            quality = videos[videoCounter]['quality']
#            if 'true' in autoplay:
#                if subdub == subs and int(quality) <= int(maxq):
#                    hostlist.append("%s | %s | %s" % (quality, subs, hostname))
#                    autoplayHost = hostCounter
#                    break
#                hostCounter += 1
#            else:
#                hostlist.append("%s | %s | %s" % (quality, subs, hostname))
#            videoCounter += 1
#        except:
#            videos.remove(videos[videoCounter])


    while videoCounter < len(videos):      
        try:
            hostname = videos[videoCounter]['name']
            subs = 'Sub' if videos[videoCounter]['type'] is 1 else 'Dub'
            quality = videos[videoCounter]['quality']
            if 'true' in autoplay:
                if subdub == subs and int(quality) <= int(maxq):
                    hostlist.append("%s | %s | %s" % (quality, subs, hostname))    
                    autovids.append(videos[videoCounter])                
            else:
                hostlist.append("%s | %s | %s" % (quality, subs, hostname))
            videoCounter += 1
        except:
            videos.remove(videos[videoCounter])


            
    if len(hostlist) is 0:
        progressDialog.close()
        xbmcgui.Dialog().notification("Masterani Redux", "No supported hosts found.")
        return

    if 'false' in autoplay:
        hostDialog = control.dialog.select("Select host.", hostlist)
    else:
        if len(hostlist) is 0:
            progressDialog.close()
            xbmcgui.Dialog().notification("Masterani Redux", "No hosts found for autoplay. Change addon settings and try again.")
            hostDialog = -1
        else:
            hostDialog = autoplayHost
			
    if hostDialog == -1:
        progressDialog.close()
        control.execute('dialog.close(okdialog)')
        return

    if 'true' in autoplay:
        try:
            hostname = autovids[hostDialog]['name']		
            hostlink = autovids[hostDialog]['url']
            hostquality = autovids[hostDialog]['quality']
            embed_id = autovids[hostDialog]['embed_id']   
        except:
            xbmcgui.Dialog().notification("Masterani Redux", "You have attempted all the hosts")
    else:        
        hostname = videos[hostDialog]['name']		
        hostlink = videos[hostDialog]['url']
        hostquality = videos[hostDialog]['quality']
        embed_id = videos[hostDialog]['embed_id']
	
    c = cache.get(masterani.get_anime_details, 3, anime_id)
    syn = c['plot'].encode('utf-8')
    print syn
    start_date = c['premiered']
    print start_date 
    sty = c['premiered'].split("-", 1)[0]
    print sty
    gen = str(c['genre'])
    print gen
    epcount = c['episode_count']

    progressDialog.update(75, line1=l1, line3="Loading video.")
	
    #Resolve Links
    mp4 = getdirect(hostname, hostlink, hostquality, embed_id)
    progressDialog.close()
    MAPlayer().run(anime_id, ep_id, mp4, syn, start_date, sty, gen, episode_number, epcount, episode_link)

class MAPlayer(xbmc.Player):
    def __init__(self):
        xbmc.Player.__init__(self)
        self.anime_id = 0
        self.episode_id = 0

    def run(self, anime_id, ep_id, url, synop, start_date, start_year, gen, epnum, epcount, eplink):
        control.sleep(200)

        self.anime_id = int(anime_id)
        self.episode_id = int(ep_id)

        item = control.item(path=url)

        try:
            c = cache.get(masterani.get_anime_details, 3, self.anime_id)

            ctype = c['type']
            ctype = 'movie' if int(ctype) is 2 else 'episode'

            tvshowtitle = c['title']
            poster = c['poster']
            coverlink = "http://cdn.masterani.me/poster/" + poster
            print coverlink

            item.setArt({'icon': coverlink, 'thumb': coverlink, 'poster': coverlink, 'tvshow.poster': coverlink, 'season.poster': coverlink})

            e = c['episodes'][self.episode_id]
            title = e['info']['title']
            season2options = [': Season 2', ' Season 2', ': 2nd Season', ': Second Season', ' 2nd Season', ' Second Season', ': Part 2', ' Part 2', ': Part II', ' Part II']
            season3options = [': Season 3', ' Season 3', ': 3rd Season', ': Third Season', ' 3rd Season', ' Third Season', ': Part 3', ' Part 3', ': Part III', ' Part III']
            season4options = [': Season 4', ' Season 4', ': 4th Season', ': Fourth Season', ' 4th Season', ' Fourth Season', ': Part 4', ' Part 4', ': Part IV', ' Part IV']
            season5options = [': Season 5', ' Season 5', ': 5th Season', ': Fifth Season', ' 5th Season', ' Fifth Season', ': Part 5', ' Part 5', ': Part V', ' Part V']
            season = 1
            for option in season2options:
                if option in tvshowtitle:
                    tvshowtitle = tvshowtitle.replace(option, "")
                    season = 2
            for option in season3options:
                if option in tvshowtitle:
                    tvshowtitle = tvshowtitle.replace(option, "")
                    season = 3
            for option in season4options:
                if option in tvshowtitle:
                    tvshowtitle = tvshowtitle.replace(option, "")
                    season = 4
            for option in season5options:
                if option in tvshowtitle:
                    tvshowtitle = tvshowtitle.replace(option, "")
                    season = 5
            episode = e['info']['episode']
            if ctype is 'video': title = c['title']
            if title is None: title = "Episode %s" % episode

            item.setInfo(type="video",
                         infoLabels={'tvshowtitle': title, 'title': tvshowtitle, 'episode': int(episode),
                                     'season': int(season), 'mediatype': ctype})
									 
            #year = e['info']['aired'].split("-", 1)[0]
            #plot = e['info']['description']

            if 'movie' in ctype:
                year = start_year
                plot = synop
                genre = gen
                item.setInfo(type="video",
                             infoLabels={'year': year, 'plot': plot, 'genre': genre})
            else:   
                year = e['info']['aired'].split("-", 1)[0]
                plot = e['info']['description']			
                item.setInfo(type="video",
                             infoLabels={'year': year, 'plot': plot, 'genre': gen})

        except:
            pass

        item.setProperty('Video', 'true')
        item.setProperty('IsPlayable', 'true')

        trackyesno = control.getSetting("track.yesno")
        tracktype = control.getSetting("track.type")

        if trackyesno == "true" and tracktype == 'Kitsu':
                kitsu.KitsuScrobbler().kitsu_initScrobble(tvshowtitle, start_date, epnum, epcount)
        else:
            pass

        self.play(url, item)

        self.playback_checker(self.anime_id, eplink)

        pass

    def playback_checker(self, ani, ep):
        #xbmc.sleep(1500)
        #if self.isPlaying():
            #pass
        #else:
            #play(ani, ep)
        
        for i in range(0, 300):
            if self.isPlaying():
                break
            xbmc.sleep(100)

        while self.isPlaying():
            try:
                if (self.getTime() / self.getTotalTime()) >= .8:
                    Watched().mark(self.anime_id, self.episode_id)
            except:
                pass
            xbmc.sleep(1000)

    def onPlayBackStarted(self):
        control.execute('Dialog.Close(all,true)')
        control.setSetting("anime.lastvisited", str(self.anime_id))
        pass

    def onPlayBackEnded(self):
        self.onPlayBackStopped()
        pass

    def onPlayBackStopped(self):
        control.refresh()
        pass
