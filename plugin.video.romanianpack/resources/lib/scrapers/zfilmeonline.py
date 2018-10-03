# -*- coding: utf-8 -*-
from resources.functions import *

base_url = 'https://zfilmeonline.eu/'
    
class zfilmeonline:
    
    thumb = os.path.join(media, 'zfilmeonline.jpg')
    nextimage = next_icon
    searchimage = search_icon
    name = 'ZFilmeOnline.eu'
    menu = [('Recente', base_url, 'recente', thumb), 
            ('Genuri', base_url, 'genuri', thumb),
            ('Căutare', base_url, 'cauta', searchimage)]
                

    def cauta(self, keyword, result):
        result.append((self.__class__.__name__, self.name, self.parse_menu(self.get_search_url(keyword), 'recente')))
        
    def get_search_url(self, keyword):
        url = base_url + '/?s=' + quote(keyword)
        return url

    def parse_menu(self, url, meniu, info={}):
        lists = []
        link = fetchData(url)
        if meniu == 'recente' or meniu == 'cauta':
            if meniu == 'cauta':
                from resources.Core import Core
                Core().searchSites({'landsearch': self.__class__.__name__})
            else: 
                link = fetchData(url)
                regex_menu = '''class="item">(.+?(?:.+?calidad.+?</sp.+?|</div.+?)).+?</di'''
                regex_submenu = '''href=['"](.+?)['"].+?src=['"](.+?)['"](?:.+?star">(.+?)</sp.+?year">(.+?)<sp.+?"year">(\d+)<.+?| alt="(.+?)")'''
                if link:
                    for movie in re.compile(regex_menu, re.IGNORECASE | re.MULTILINE | re.DOTALL).findall(link):
                        match = re.compile(regex_submenu, re.DOTALL).findall(movie)
                        for legatura, imagine, rating, nume, an, numealt in match:
                            nume = htmlparser.HTMLParser().unescape(striphtml(nume).decode('utf-8')).encode('utf-8').strip()
                            if not numealt: info = {'Title': nume,'Plot': nume,'Poster': imagine,'Year':str(an), 'Rating': striphtml(rating).strip()}
                            else: 
                                nume = numealt
                                info = {'Title': nume,'Plot': nume,'Poster': imagine}
                            lists.append((nume, legatura, imagine, 'get_links', info))
                    match = re.compile('"paginado"', re.IGNORECASE).findall(link)
                    if len(match) > 0:
                        if '/page/' in url:
                            new = re.compile('/page/(\d+)').findall(url)
                            nexturl = re.sub('/page/(\d+)', '/page/' + str(int(new[0]) + 1), url)
                        else:
                            if '/?s=' in url:
                                nextpage = re.compile('\?s=(.+?)$').findall(url)
                                nexturl = '%s%s?s=%s' % (base_url, ('page/2/' if str(url).endswith('/') else '/page/2/'), nextpage[0])
                            else: nexturl = url + "/page/2"
                        lists.append(('Next', nexturl, self.nextimage, meniu, {}))
        elif meniu == 'get_links':
            link = fetchData(url)
            links = []
            nume = ''
            regex_base = '''var[\s*]s[\d\s=]+\'(.+?)\''''
            reg_coded = '''var s(?:\d+) = \'(.+?)\''''
            reg_server = '''<iframe.+?src=[\'"]((?:[htt]|[//]).+?)["\']'''
            regex_lnk = '''type=\'text/javascript\'> str=['"](.+?)["']'''
            regex_seriale = '''(?:<h3>.+?strong>(.+?)<.+?href=['"](.+?)['"].+?)'''
            regex_infos = '''<div itemprop="description".+?>(.+?)</div'''
            match_lnk = re.compile(regex_lnk, re.IGNORECASE | re.DOTALL).findall(link)
            match_nfo = re.findall(regex_infos, link, re.IGNORECASE | re.DOTALL)
            match2_lnk = re.compile(reg_server, re.IGNORECASE | re.DOTALL).findall(link)
            try:
                info = eval(str(info))
                info['Plot'] = (striphtml(match_nfo[0]).strip())
            except: pass
            for coded in match_lnk:
                try:
                    link_script = re.findall(reg_server, unquote(coded.replace('@','%')), re.IGNORECASE | re.DOTALL)[0]
                    host = link_script.split('/')[2].replace('www.', '').capitalize()
                    lists.append((host,link_script,'','play', str(info), url))
                except: pass
            for host, link1 in get_links(match2_lnk):
                lists.append((host,link1,'','play', str(info), url))
            
        elif meniu == 'genuri':
            link = fetchData(url)
            regex_cat = '''class="cat-item.+?href=['"](.+?)['"\s]>(.+?)<'''
            if link:
                match = re.findall(regex_cat, link, re.IGNORECASE | re.DOTALL)
                if len(match) > 0:
                    for legatura, nume in match:
                        lists.append((nume,legatura.replace('"', ''),'','recente', info))
        return lists
              
