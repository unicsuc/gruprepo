# -*- coding: utf-8 -*-
from resources.functions import *

base_url = 'http://www.clicksud.org'

class clicksudorg:
    
    thumb = os.path.join(media, 'clicksud.jpg')
    nextimage = next_icon
    searchimage = search_icon
    name = 'ClickSud.org'
    menu = [('Recente', base_url, 'recente', thumb), 
            ('Seriale românești', base_url + '/2012/06/seriale-romanesti-online.html', 'liste', thumb),
            ('Emisiuni online', base_url + '/2012/11/emisiuni-tv-online.html', 'liste', thumb),
            ('Seriale online', base_url + '/2014/08/seriale-online.html', 'online', thumb),
            ('Las Fierbinti', base_url + '/p/las-fierbinti-online.html', 'online', thumb),
            ('Căutare', base_url, 'cauta', searchimage)]
        
    def get_search_url(self, keyword):
        url = base_url + '/search/?q=' + quote(keyword)
        return url

    def getKey(self, item):
        return item[1]

    def cauta(self, keyword, result):
        result.append((self.__class__.__name__, self.name, self.parse_menu(self.get_search_url(keyword), 'recente')))

    def parse_menu(self, url, meniu, info={}):
        lists = []
        imagine = ''
        if meniu == 'recente' or meniu == 'cauta':
            if meniu == 'cauta':
                from resources.Core import Core
                Core().searchSites({'landsearch': self.__class__.__name__})
            else: 
                link = fetchData(url)
                regex_menu = '''<article(.+?)</article'''
                regex_submenu = '''href=['"](.+?)['"].+?title=['"](.+?)['"].+?content=['"]([htp].+?)['"]'''
                regex_search = '''<span class='pager-older-link.+?href=['"](.+?)['"].+?</span'''
                if link:
                    for meniu in re.compile(regex_menu, re.DOTALL).findall(link):
                        match = re.findall(regex_submenu, meniu, re.DOTALL)
                        for legatura, nume, imagine in match:
                            nume = htmlparser.HTMLParser().unescape(nume.decode('utf-8')).encode('utf-8')
                            info = {'Title': nume,'Plot': nume,'Poster': imagine}
                            szep = re.findall('(?:sezo[a-zA-Z\s]+(\d+).+?)?epi[a-zA-Z\s]+(\d+)', nume, re.IGNORECASE | re.DOTALL)
                            if szep:
                                try:
                                    if re.search('–|-|~', nume):
                                        all_name = re.split(r'–|-|:|~', nume,1)
                                        title = all_name[0]
                                        title2 = all_name[1]
                                    else: 
                                        title = nume
                                        title2 = ''
                                    title, year = xbmc.getCleanMovieTitle(title)
                                    title2, year2 = xbmc.getCleanMovieTitle(title2)
                                    title = title if title else title2
                                    year = year if year else year2
                                    if year: info['Year'] = year
                                    if szep[0][1] and not szep[0][0]: info['Season'] = '01'
                                    else: info['Season'] = str(szep[0][0])
                                    info['Episode'] = str(szep[0][1])
                                    info['TvShowTitle'] = (re.sub('(?:sezo[a-zA-Z\s]+\d+.+?)?epi[a-zA-Z\s]+\d+.+?$', '', title, flags=re.IGNORECASE | re.DOTALL)).strip()
                                except: pass
                            lists.append((nume, legatura, imagine, 'get_links', info))
                    match = re.compile(regex_search, re.DOTALL).findall(link)
                    if match:
                        nexturl = match[0]
                        lists.append(('Next', nexturl, self.nextimage, meniu, {}))
        elif meniu == 'get_links':
            sources = []
            link = fetchData(url)
            regex_lnk = '''(?:item title="(.+?)".+?)?<iframe.+?src="((?:[htt]|[//]).+?)"'''
            match_lnk = re.findall(regex_lnk, link, re.IGNORECASE | re.DOTALL)
            for nume, match in match_lnk:
                if not '+f.id+' in match: sources.append((nume, match))
            for host, link1 in get_links(sources):
                lists.append((host,link1,'','play', info, url))#addLink(host, link1, thumb, name, 10, striphtml(match_nfo[0]))
        elif meniu == 'liste':
            link = fetchData(url)
            regex_menu = '''(?s)<table (.+?)</table'''
            regex_submenu = '''(?:(?s)<li.+?href="(.+?)">(.+?)<(?:.+?src="(.+?)")?|td>.+?href="(.+?)">(.+?)<)'''
            regex2_submenu = '''(?s)data-label="(.+?)"><a.+?href="(.+?)"(?:.+?src="(.+?)")?'''
            for meniu in re.compile(regex_menu, re.DOTALL).findall(link):
                match = re.compile(regex_submenu).findall(meniu)
                for legatura, nume, imagine, legatura2, nume2 in match:
                    if not imagine: imagine = self.thumb
                    if not legatura and not nume:
                        legatura = legatura2
                        nume = nume2
                    nume = htmlparser.HTMLParser().unescape(striphtml(nume.decode('utf-8'))).encode('utf-8')
                    if legatura.endswith(".html"): switch = 'get_links'
                    elif re.search('/search/', legatura): switch = 'recente'
                    else: switch = 'liste'
                    if nume and not nume.isspace():
                        lists.append((nume,legatura.replace('"', ''),imagine,switch,info))
            for meniu in re.compile(regex_menu, re.DOTALL).findall(link):
                match = re.compile(regex2_submenu).findall(meniu)
                for nume, legatura, imagine in match:
                    if not imagine: imagine = self.thumb
                    nume = htmlparser.HTMLParser().unescape(striphtml(nume.decode('utf-8'))).encode('utf-8')
                    if legatura.endswith(".html"): switch = 'get_links'
                    elif re.search('/search/', legatura): switch = 'recente'
                    else: switch = 'liste'
                    if not nume.isspace():
                        lists.append((nume,legatura.replace('"', ''),imagine,switch,info))
        elif meniu == 'online':
            link = fetchData(url)
            regex_menu = '''(?s)<table (.+?)</table'''
            regex_submenu = '''(?s)<li.+?href="(.+?)">(.+?)<'''
            for meniu in re.compile(regex_menu, re.DOTALL).findall(link):
                match = re.compile(regex_submenu).findall(meniu)
                for legatura, nume in match:
                    nume = htmlparser.HTMLParser().unescape(striphtml(nume.decode('utf-8'))).encode('utf-8')
                    if re.search('sezonul|episodul', legatura): switch = 'get_links'
                    elif re.search('/search/', legatura): switch = 'recente'
                    else: switch = 'liste'
                    lists.append((nume,legatura.replace('"', ''),self.thumb,switch,info))
        return lists
