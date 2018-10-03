# -*- coding: utf-8 -*-
from resources.functions import *

base_url = 'https://yesmovies.to'

CODE = '''def retA():
    class Infix:
        def __init__(self, function):
            self.function = function
        def __ror__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __or__(self, other):
            return self.function(other)
        def __rlshift__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __rshift__(self, other):
            return self.function(other)
        def __call__(self, value1, value2):
            return self.function(value1, value2)
    def my_add(x, y):
        try: return x + y
        except Exception: return str(x) + str(y)
    x = Infix(my_add)
    return %s
param = retA()'''

class ymovies:
    
    thumb = os.path.join(media, 'ymovies.jpg')
    nextimage = next_icon
    searchimage = search_icon
    name = 'YesMovies.to'
    menu = [('Recente', base_url, 'recente', thumb),
            ('Genuri', '0', 'genuri', thumb),
            ('Țări', '0', 'tari', thumb),
            ('Filme', '%s/movie/filter/movies.html' % base_url, 'recente', thumb),
            ('Seriale', '%s/movie/filter/series.html' % base_url, 'recente', thumb),
            ('Căutare', base_url, 'cauta', searchimage)
            ]
        
    def get_search_url(self, keyword):
        url = '%s/search/%s.html' % (base_url, quote(keyword))
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
                if url == base_url: url = '%s/yes.html' % base_url
                link = fetchData(url)
                regex_submenu = '''"ml-item".+?href="(.+?)".+?data-url="(.+?)".+?(?:eps">(.+?)</span.+?)?(?:quality"(?:[a-zA-Z\n\s#=":]+)?>(.+?)<.+?)?data-original="(.+?)".+?info">(.+?)</span'''
                if link:
                    match = re.compile(regex_submenu, re.DOTALL).findall(link)
                    for legatura, infolink, season, calitate, imagine, nume in match:
                        nume = (htmlparser.HTMLParser().unescape(striphtml(nume).decode('utf-8')).encode('utf-8')).strip()
                        info = {'Title': nume,'Plot': nume,'Poster': imagine}
                        sezon = re.search('season\s+(\d+)', nume, flags=re.IGNORECASE)
                        if sezon or season:
                            try: numea = re.sub('\s+-\s+season\s+\d+', '', nume, flags=re.IGNORECASE) if sezon else nume
                            except: numea = re.sub('(?i)\s+-\s+season\s+\d+', '', nume) if sezon else nume
                            info['Title'] = numea
                            info['TVShowTitle'] = numea
                            info['Season'] = str(sezon.group(1)) if sezon else '1'
                        lists.append(('%s - %s' % (nume, calitate if calitate else '%s' % ('Serial' if season else '')), legatura, imagine, 'get_all', info))
                    match = re.compile('"pagination', re.IGNORECASE).findall(link)
                    if len(match) > 0:
                        if '/page-' in url:
                            new = re.compile('/page-(\d+)').findall(url)
                            nexturl = re.sub('/page-(\d+)', '/page-' + str(int(new[0]) + 1), url)
                        else:
                            if '/genre/' in url or '/country/' in url or '/search/' in url:
                                nexturl = re.sub('.html', '/page-2.html', url)
                            else:
                                nexturl = re.sub('.html', '/latest/all/all/all/all/all/page-2.html', url)
                        lists.append(('Next', nexturl, self.nextimage, meniu, {}))
        elif meniu == 'get_all':
            lid = re.search('-(\d+)\.', url).group(1)
            oldurl = url
            url = re.sub('.html', '/watching.html', url)
            new_url = '%s/ajax/v4_movie_episodes/%s' % (base_url, lid)
            link = fetchData(new_url, rtype='json')
            #log(link)
            regex_embed = '''li id="sv.+?data-id="(.+?)".+?server-item(.+?)"'''
            regex = '''ep-item.+?data-index="(.+?)".+?data-server="(.+?)".+?data-id="(.+?)".+?id="(.+?)".+?title="(.+?)"'''
            if link:
                match = re.findall(regex, link.get('html'), re.DOTALL)
                check_embed = re.findall(regex_embed, link.get('html'), re.DOTALL)
                emb_server = ''
                for serv, typ in check_embed:
                        if typ.strip() == 'embed':
                            emb_server = serv
                            break    
                #log(link.get('html'))
                for dataindex, dataserver, dataid, episodeid, nume in match:
                    embed = 'no'
                    if dataserver == emb_server: embed = 'yes'
                    infos = json.loads(info)
                    try: nume = (htmlparser.HTMLParser().unescape(striphtml(nume).decode('utf-8')).encode('utf-8')).strip()
                    except: nume = nume.strip()
                    episod = re.search('episode\s+(\d+)', nume, flags=re.IGNORECASE)
                    if episod:
                        infos['Episode'] = str(episod.group(1))
                        infos['Title'] = '%s S%s E%s' % (infos['Title'], infos['Season'], infos['Episode'])
                        infos['Plot'] = '%s Episode %s' % (infos['Plot'], infos['Episode'])
                    else: infos['Episode'] = ''
                    lists.append(('Server %s - %s' % (dataserver, nume), '%ssplitthishere%ssplitthishere%ssplitthishere%ssplitthishere%ssplitthishere%s' % (dataindex, dataserver, dataid, lid, url, embed), '', 'get_links', str(infos), '1'))
                #log(lists)
        elif meniu == 'get_links':
            link_parts = url.split('splitthishere')
            if len(link_parts) > 5: embed = link_parts[5]
            else: embed = 'no'
            if embed == 'no':
                url_tokens = '%s/ajax/movie_token?eid=%s&mid=%s' % (base_url, link_parts[2], link_parts[3])
                headers = {'Host': 'yesmovies.to',
                        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'}
                tokens = fetchData(url_tokens, headers=headers)
                #log('tokens: ' + tokens)
                x = re.search('''_x=['"]([^"']+)''', tokens)
                if x: x = x.group(1)
                y = re.search('''_y=['"]([^"']+)''', tokens)
                if y: y = y.group(1)
                if not x or not y:
                    try:
                        script = '(' + tokens.split("(_$$)) ('_');")[0].split("/* `$$` */")[-1].strip()
                        script = script.replace('(__$)[$$$]', '\'"\'')
                        script = script.replace('(__$)[_$]', '"\\\\"')
                        script = script.replace('(o^_^o)', '3')
                        script = script.replace('(c^_^o)', '0')
                        script = script.replace('(_$$)', '1')
                        script = script.replace('($$_)', '4')
                        script = script.replace('+', '|x|')
                        vGlobals = {"__builtins__": None, '__name__': __name__, 'str': str, 'Exception': Exception}
                        vLocals = {'param': None}
                        exec(CODE % script) in vGlobals, vLocals
                        data = vLocals['param'].decode('string_escape')
                        x = re.search('''_x=['"]([^"']+)''', data).group(1)
                        y = re.search('''_y=['"]([^"']+)''', data).group(1)
                    except: x = ''; y = ''
                ip = re.search('''_ip(?:[\s+])?=(?:[\s+])?['"]([^"']+)''', tokens)
                ip = ip.group(1) if ip else ''
                z = re.search('''_z(?:[\s+])?=(?:[\s+])?['"]([^"']+)''', tokens)
                z = z.group(1) if z else ''
                url_source = '%s/ajax/movie_sources/%s?x=%s&y=%s' % (base_url, link_parts[2], x, y)
            elif embed == 'yes':
                url_source = '%s/ajax/movie_embed/%s' % (base_url, link_parts[2])
            #log('url_source; ' + url_source)
            one_urls = fetchData(url_source, link_parts[4], rtype='json', headers={'Host': 'yesmovies.to'})
            selm = -1
            if one_urls:
                try: 
                    embed = 'yes' if one_urls.get('embed') else embed
                except: pass
                if embed == 'yes':
                    try: 
                        playlink = one_urls.get('src')
                        sublink = None
                        selm = 0
                    except: pass
                else:
                    try: 
                        dialogb = xbmcgui.Dialog()
                        tracks = one_urls.get('playlist')[0].get('tracks')
                        if len(tracks) > 1:
                            sel = dialogb.select("Alege subtitrarea", [sel_s.get('label') for sel_s in tracks])
                        else: sel = 0
                        sublink = tracks[sel].get('file')
                        sublink = '%s%s' % (base_url, sublink) if sublink.startswith('/') else sublink
                    except: sublink = None
                    #try: 
                    dialogb = xbmcgui.Dialog()
                    msources = one_urls.get('playlist')[0].get('sources')
                    if msources:
                        if isinstance(msources, list):
                            if len(msources) > 1:
                                selm = dialogb.select("Alege varianta", [sel_m.get('label') for sel_m in msources])
                            else: selm = 0
                            playlink = msources[selm].get('file')
                        else: playlink = msources.get('file'); selm = 0
                        if playlink and not 'googleusercontent.com' in playlink:
                            playlink = playlink + '|User-Agent=%s&Referer=%s&Origin=%s' % (quote(randomagent()), quote(link_parts[4]), quote(base_url))
                    else: playlink = None
                data = json.loads(info)
                #log('episode: ' + data.get('Episode'))
                if data.get('TVShowTitle'):
                    viewmark = url
                    playname = '%s %s' % (data.get('TVShowTitle'), data.get('Title'))
                else:
                    viewmark = url
                    playname = data.get('Title')
                if not sublink: playname = playname + ' Fara subtitrare pe site'
                #log('playlink: ' + str(playlink))
                if playlink and selm <> -1: 
                    from resources import Core
                    core = Core.Core()
                    core.executeAction({'info': quote(info), 'favorite': 'check', 'site': 'filmeonlineto', 'landing': quote(viewmark), 'nume': playname, 'switch': 'play', 'link': quote(playlink), 'action': 'OpenSite', 'watched': 'check', 'subtitrare': quote(sublink) if sublink else ''})
                else: xbmc.executebuiltin('Notification(%s,%s)' % (xbmcaddon.Addon().getAddonInfo('name'), 'Nu s-a găsit link'))
                    #xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=False)
                #lists.append(('Play %s' % (playname),playlink,'','play', info, viewmark, sublink))
        elif meniu == 'genuri':
            link = fetchData('%s/yes.html' % base_url)
            regex = '''title="Genre"(.+?)</div'''
            regex_cats = '''href="(.+?)"(?:.+?)?>(.+?)<'''
            if link:
                for cats in re.findall(regex, link, re.DOTALL | re.IGNORECASE):
                    match = re.findall(regex_cats, cats)
                    if len(match) >= 0:
                        for legatura, nume in sorted(match, key=self.getKey):
                            lists.append((nume,legatura,'','recente', info))
        elif meniu == 'tari':
            link = fetchData('%s/yes.html' % base_url)
            regex = '''title="Country"(.+?)</div'''
            regex_cats = '''href="(.+?)"(?:.+?)?>(.+?)<'''
            if link:
                for cats in re.findall(regex, link, re.DOTALL | re.IGNORECASE):
                    match = re.findall(regex_cats, cats)
                    if len(match) >= 0:
                        for legatura, nume in sorted(match, key=self.getKey):
                            lists.append((nume,legatura,'','recente', info))
        return lists
              
