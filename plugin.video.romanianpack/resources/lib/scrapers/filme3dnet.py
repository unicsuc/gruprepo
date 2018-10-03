# -*- coding: utf-8 -*-
from resources.functions import *

base_url = 'http://www.filme3d.net'

class filme3dnet:
   
   thumb = os.path.join(media, 'filme3dnet.jpg')
   nextimage = next_icon
   searchimage = search_icon
   name = 'Filme3D.net'
   menu = [('Recente', base_url, 'recente', thumb), 
           ('Genuri', base_url, 'genuri', thumb),
           ('Căutare', base_url, 'cauta', searchimage)]

   def cauta(self, keyword, result):
       result.append((self.__class__.__name__, self.name, self.parse_menu('post', 'cauta', keyw=keyword)))

   def parse_menu(self, url, meniu, info={}, keyw=None):
       lists = []
       #log('link: ' + link)
       imagine = ''
       if meniu == 'recente':
           link = fetchData(url)
           regex_menu = r'''movie_box"(.+?)postbottom"'''
           rurl = r'''href=['"](.+?)?['"]'''
           rimagine = r'''src=['"](.+?)?['"]'''
           rnume = r'''movie-desc.+?alt.+?/>(.+?)?<sp'''
           rcategorii = r'''Cat.+?>(.+?)?<sp'''
           rdescriere = r'''line;">(.+?)?</div'''
           rcalitate = r'''class=['"](.+?)['"]>\1<'''
           if link:
               for movie in re.findall(regex_menu, link, re.IGNORECASE | re.MULTILINE | re.DOTALL):
                   if 'news-id' in movie:
                       legatura = re.findall(rurl, movie, re.DOTALL)[0]
                       imagine = re.findall(rimagine, movie, re.DOTALL)[0]
                       nume = re.findall(rnume, movie, re.DOTALL)[0]
                       nume = htmlparser.HTMLParser().unescape(striphtml(nume).decode('utf-8')).encode('utf-8').strip()
                       categorii = striphtml(re.findall(rcategorii, movie, re.DOTALL)[0]).strip()
                       try: calitate = re.findall(rcalitate, movie, re.DOTALL)[0]
                       except: calitate = ''
                       try: descriere = re.findall(rdescriere, movie, re.DOTALL)[0]
                       except: descriere = nume
                       descriere = htmlparser.HTMLParser().unescape(striphtml(descriere).decode('utf-8')).encode('utf-8').strip()
                       descriere = "-".join(descriere.split("\n"))
                       nume = '%s [COLOR yellow]%s[/COLOR]' % (nume, calitate)
                       info = {'Title': nume,'Plot': descriere,'Poster': imagine, 'Genre': categorii}
                       lists.append((nume, legatura, imagine, 'get_links', info))
               match = re.compile('pagenavi"', re.IGNORECASE).findall(link)
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
       elif meniu == 'by_genre' or meniu == 'cauta':
           if meniu == 'cauta':
               if url == 'post' and keyw:
                   data = {'do': 'search', 'subaction': 'search', 'story': keyw}
                   link = fetchData(base_url, base_url + '/?s=' + keyw, data)
               else:
                   link = None
                   from resources.Core import Core
                   Core().searchSites({'landsearch': self.__class__.__name__})
           else: link = fetchData(url)
           regex_menu = r'''short_post">(.+?)more"'''
           regex_movie = r'''href=['"](.+?)?['"\s*][\s]?>(.+?)<.+?src=['"](.+?)['"].+?calitate.+?>(.+?)<.+?cat.+?:(.+?)</div'''
           if link:
               for movie in re.findall(regex_menu, link, re.IGNORECASE | re.MULTILINE | re.DOTALL):
                   for legatura, nume, imagine, calitate, categorii in re.findall(regex_movie, movie, re.IGNORECASE | re.DOTALL):
                       nume = htmlparser.HTMLParser().unescape(striphtml(nume).decode('utf-8')).encode('utf-8').strip()
                       categorii = striphtml(categorii).strip()
                       calitate = calitate.rstrip()
                       nume = '%s [COLOR yellow]%s[/COLOR]' % (nume, calitate)
                       info = {'Title': nume,'Plot': nume + categorii,'Poster': imagine, 'Genre': categorii}
                       lists.append((nume, legatura, imagine, 'get_links', info))
               match = re.compile('pagenavi"', re.IGNORECASE).findall(link)
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
           regex_lnk = '''<iframe.+?src="((?:[htt]|[//]).+?)"'''
           regex_infos = '''"description">(.+?)</'''
           match_lnk = re.compile(regex_lnk, re.IGNORECASE | re.DOTALL).findall(link)
           match_nfo = re.compile(regex_infos, re.IGNORECASE | re.DOTALL).findall(link)
           try:
               info = eval(str(info))
               info['Plot'] = (striphtml(match_nfo[0]).strip())
           except: pass
           for host, link1 in get_links(match_lnk):
               lists.append((host,link1,'','play', info, url))
       elif meniu == 'genuri':
           link = fetchData(url)
           regex_cats = '''class="genres"(.+?)</ul'''
           regex_cat = '''href=['"](.+?)['"].+?">(.+?)<'''
           if link:
               for cat in re.findall(regex_cats, link, re.IGNORECASE | re.DOTALL):
                   match = re.findall(regex_cat, cat, re.DOTALL)
                   for legatura, nume in match:
                       if not nume == 'Diverse':
                        legatura = base_url + legatura
                        lists.append((nume, legatura, '', 'by_genre', info))
       return lists
             
