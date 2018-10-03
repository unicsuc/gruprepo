# -*- coding: utf-8 -*-
from resources.functions import *

base_url = 'https://filme-seriale.gold'

class filmeserialegratis:
    
    thumb = os.path.join(media, 'filmeserialegratis.jpg')
    nextimage = next_icon
    searchimage = search_icon
    name = 'Filme-Seriale.gratis'
    menu = [('Recente', base_url, 'recente', thumb),
            ('Genuri Filme', base_url, 'genuri', thumb),
            ('Genuri Seriale', 'seriale', 'genuri', thumb),
            ('Filme după ani', base_url, 'ani', thumb),
            ('Seriale după ani', base_url, 'aniseriale', thumb),
            ('Filme după calitate', base_url, 'calitate', thumb),
            ('Listă seriale', '%s/seriale-online' % base_url, 'recente', thumb),
            ('Episoade adăugate recent', '%s/episod' % base_url, 'recente', thumb),
            ('Căutare', base_url, 'cauta', searchimage)]
        
    def get_search_url(self, keyword):
        url = base_url + '/?s=' + quote(keyword)
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
                if ('%s/episod' % base_url) in url: 
                    link = fetchData(url)
                    regex_all = '''<td class="bb">.+?href=".+?>(.+?)<.+?href=".+?>(.+?)<.+?src="(.+?)".+?href="(.+?)".+?>(.+?)<.+?p>(.+?)</p.+?"dd"><center>(.+?)<.+?"ee"><center>(.+?)<.+?'''
                    match = re.findall(regex_all, link, re.IGNORECASE | re.DOTALL)
                    for serial, e_pisod, imagine, legatura, nume, descriere, add_data, traducator in match:
                        serial = htmlparser.HTMLParser().unescape(striphtml(serial).decode('utf-8')).encode('utf-8')
                        e_pisod = htmlparser.HTMLParser().unescape(striphtml(e_pisod).decode('utf-8')).encode('utf-8')
                        nume = htmlparser.HTMLParser().unescape(striphtml(nume).decode('utf-8')).encode('utf-8')
                        descriere = htmlparser.HTMLParser().unescape(striphtml(descriere).decode('utf-8')).encode('utf-8')
                        imagine = imagine.strip()
                        try: imagine = re.findall('url=(.+?)$', imagine)[0]
                        except: pass
                        pisod = re.findall('sezonul-(\d+)?.+?episodul-(\d+)?', e_pisod, re.IGNORECASE | re.DOTALL)
                        info = {
                            'Title': '%s S%s-E%s %s' % (serial.strip(), pisod[0][0], pisod[0][1], nume.strip()),
                            'Poster': imagine,
                            'Plot': descriere.strip(),
                            'TVShowTitle': serial.strip(),
                            'Season': pisod[0][0],
                            'Episode': pisod[0][1]
                            }
                        nume = '%s: %s : %s'% (serial.strip(), e_pisod, nume.strip())
                        lists.append((nume, legatura, imagine, 'get_links', info))
                else: 
                    link = fetchData(url)
                    regex_all = '''<div id="mt-(.+?year">.+?</span>)(?:.+?<span class="calidad2">(.+?)</span>)?'''
                    regex_info = '''src="(.+?)".+?boxinfo.+?href="(.+?)".+?"tt">(.+?)</.+?"ttx">(.+?)</.+?"year">(.+?)<'''
                    regex_n_v = '''(?:IMDB|TMDb):(.+?)</s.+?type.+?>(.+?)<'''
                    if link:
                        for bloc, tip in re.findall(regex_all, link, re.IGNORECASE | re.MULTILINE | re.DOTALL):
                            match = re.findall(regex_info, bloc, re.DOTALL)
                            voturi = re.findall(regex_n_v, bloc, re.IGNORECASE | re.DOTALL)
                            if voturi:
                                rating = striphtml(voturi[0][0]).split("/")[0].strip()
                                votes = striphtml(voturi[0][0]).split("/")[1].strip()
                                post = voturi[0][1]
                            else: rating = None; votes = None; post = ''
                            for imagine, legatura, nume, descriere, an in match:
                                imagine = imagine.strip()
                                try: imagine = re.findall('url=(.+?)$', imagine)[0]
                                except: pass
                                nume = htmlparser.HTMLParser().unescape(striphtml(nume).decode('utf-8')).encode('utf-8')
                                descriere = htmlparser.HTMLParser().unescape(striphtml(descriere).decode('utf-8')).encode('utf-8')
                                info = {
                                'Title': nume,
                                'Poster': imagine,
                                'Plot': descriere.strip(),
                                'Year': an,
                                'Rating': '%s' % rating,
                                'Votes': '%s' % votes,
                                'PlotOutline': '%s' % (descriere.strip())
                                }
                                nume = (nume + ' - ' + tip) if tip else nume
                                if 'eri' in tip or 'epis' in post or '/seriale/' in legatura:
                                    lists.append((nume, legatura, imagine, 'get_episoade', info))
                                else:
                                    lists.append((nume, legatura, imagine, 'get_links', info))
                match = re.search('"pagination"|"paginador"', link, flags=re.IGNORECASE)
                if match:
                    if '/page/' in url:
                        new = re.findall('/page/(\d+)', url)
                        nexturl = re.sub('/page/(\d+)', '/page/' + str(int(new[0]) + 1), url)
                    else:
                        if '/?s=' in url:
                            nextpage = re.findall('\?s=(.+?)$', url)
                            nexturl = '%s%s?s=%s' % (base_url, ('page/2/' if str(url).endswith('/') else '/page/2/'), nextpage[0])
                        else: nexturl = url + "/page/2"
                    lists.append(('Next', nexturl, self.nextimage, meniu, {}))
        elif meniu == 'get_episoade':
            link = fetchData(url)
            regex_all = '''numerando">(\d+ x \d+)<.+?href="(.+?)">(.+?)<.+?date">(.+?)<'''
            episod = re.compile(regex_all, re.IGNORECASE | re.MULTILINE | re.DOTALL).findall(link)
            info = eval(str(info))
            title = info['Title']
            for numero, legatura, nume, data in episod:
                nume = htmlparser.HTMLParser().unescape(nume.decode('utf-8')).encode('utf-8')
                ep_data = numero.split(' x ')
                info['TVShowTitle'] = title
                info['Title'] = '%s S%02dE%02d %s' % (title.decode('utf-8').encode('utf-8'), int(ep_data[0]), int(ep_data[1]), nume.strip())
                info['Season'] = ep_data[0]
                info['Episode'] = ep_data[1]
                lists.append((striphtml(str(numero) + ' ' + nume + ' - ' + data).replace("\n", ""), legatura, '', 'get_links', str(info)))
        elif meniu == 'get_links':
            link = fetchData(url)
            links = []
            regex_lnk = '''<(?:iframe.+?|script(?:\s)?)src=[\'"]((?:[htt]|[//]).+?(?!\.js))["\']'''
            regex_lnk2 = '''type=\'text/javascript\'>(?:\s)?str=['"](.+?)["']'''
            match_lnk2 = re.compile(regex_lnk2, re.IGNORECASE | re.DOTALL).findall(link)
            match_lnk = re.compile(regex_lnk, re.IGNORECASE | re.DOTALL).findall(link)
            for host, link1 in get_links(match_lnk):
                if not link1.endswith('.js'):
                    lists.append((host,link1,'','play', info, url))
            for coded in match_lnk2:
                try: 
                    link_script = re.findall(regex_lnk, unquote(coded.replace('@','%')), re.IGNORECASE | re.DOTALL)[0]
                    host = link_script.split('/')[2].replace('www.', '').capitalize()
                    lists.append((host,link_script,'','play', str(info), url))
                except: pass
        elif meniu == 'genuri':
            link = fetchData(base_url)
            regex_cats = '''"categorias">(.+?)</div'''
            regex_cat = '''href="(.+?)"(?:\s)?>(.+?)<.+?n>(.+?)<'''
            gen = re.findall(regex_cats, link, re.IGNORECASE | re.DOTALL)
            if url == 'seriale': match = re.findall(regex_cat, gen[1], re.DOTALL)
            else: match = re.findall(regex_cat, gen[0], re.DOTALL)
            for legatura, nume, cantitate in match:
                nume = clean_cat(htmlparser.HTMLParser().unescape(nume.decode('utf-8')).encode('utf-8')).capitalize()
                lists.append((nume,legatura,'','recente', info))
        elif meniu == 'ani' or meniu == 'aniseriale':
            link = fetchData(url)
            regex_cats = '''"filtro_y">.+?anul(.+?)</div'''
            regex_cat = '''href="(.+?)"(?:\s)?>(.+?)<.+?n>(.+?)<'''
            an = re.compile(regex_cats, re.IGNORECASE | re.MULTILINE | re.DOTALL).findall(link)
            if meniu == 'ani': match = re.compile(regex_cat, re.DOTALL).findall(an[0])
            else: match = re.compile(regex_cat, re.DOTALL).findall(an[1])
            for legatura, nume, cantitate in match:
                lists.append(('%s - %s' % (nume, cantitate),legatura,'','recente', info))
        elif meniu == 'calitate':
            link = fetchData(url)
            regex_cats = '''"filtro_y">.+?calita(.+?)</div'''
            regex_cat = '''href="(.+?)"(?:\s)?>(.+?)<.+?n>(.+?)<'''
            for cat in re.findall(regex_cats, link, re.IGNORECASE | re.DOTALL):
                match = re.findall(regex_cat, cat, re.DOTALL)
                for legatura, nume, cantitate in match:
                    nume = htmlparser.HTMLParser().unescape(striphtml(nume).decode('utf-8')).encode('utf-8')
                    lists.append(('%s - %s' % (nume, cantitate),legatura,'','recente', info))
                
        return lists
              
