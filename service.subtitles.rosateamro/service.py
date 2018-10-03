# -*- coding: utf-8 -*-

import os
import re
import shutil
import sys
import unicodedata
import urllib
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs
from resources.lib import requests
from resources.lib.requests.packages.urllib3.exceptions import InsecureRequestWarning

__addon__ = xbmcaddon.Addon()
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')

__cwd__        = xbmc.translatePath(__addon__.getAddonInfo('path')).decode("utf-8")
__profile__    = xbmc.translatePath(__addon__.getAddonInfo('profile')).decode("utf-8")
__resource__   = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib')).decode("utf-8")
__temp__       = xbmc.translatePath(os.path.join(__profile__, 'temp', ''))

base_url = 'https://rosa-team.ro'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.Session()

def Search(item):
    search_data = []
    epis = []
    search_data = searchsubtitles(item)
    if search_data != None:
        search_code = get_url(search_data[0]["ZipDownloadLink"], 'content')
        regex = '''"list-group"(.+?)</div'''
        regexb = '''href=['"](.+?)['"].+?>(.+?)(?:<.+?>)(.+?)<'''
        episoade = re.findall(regex, search_code, re.IGNORECASE | re.DOTALL)
        if len(episoade) > 0:
            for episod in episoade:
                for l_episod, nume_e, numar in re.findall(regexb, episod, re.IGNORECASE | re.DOTALL):
                    legatura = base_url + l_episod
                    epi = nume_e + numar
                    epis.append((legatura, epi))
            dialogb = xbmcgui.Dialog()
            if len(epis) > 1: sel = dialogb.select("Alege episodul", [sel_e[1].strip() for sel_e in epis])
            else: sel = 0
            try: search_code = get_url(epis[sel][0], 'content')
            except: search_code = get_url(search_data[0]["ZipDownloadLink"], 'content')
        else:
            search_code = get_url(search_data[0]["ZipDownloadLink"], 'content')
        regex_e = '''traducator['"]>(.+?)<.+?data.+?<td>(.+?)<.+?href=['"](.+?)['"]'''
        for traducator, numefisier, legatura in re.findall(regex_e, search_code, re.IGNORECASE | re.DOTALL):
            legatura = base_url + legatura
            listitem = xbmcgui.ListItem(label=traducator.strip(),
                                            label2=numefisier.strip(),
                                            iconImage='5',
                                            thumbnailImage="ro"
                                            )
            url = "plugin://%s/?action=setsub&link=%s&filename=%s" % (__scriptid__,
                                                                            urllib.quote_plus(legatura),
                                                                            numefisier
                                                                            )
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=listitem, isFolder=False)

def searchsubtitles(item):
    item['title'] = cleanhtml(item['title'])
    if len(item['tvshow']) > 0: search_string = item['tvshow'].replace(" ", "+")      
    else:
        if str(item['year']) == "": item['title'], item['year'] = xbmc.getCleanMovieTitle(item['title'])
    
        search_string = (re.sub('S(\d{1,2})E(\d{1,2})', '', item['title'])).replace(" ", "+")
        episodes = re.findall('S(\d{1,2})E(\d{1,2})', item['title'], re.IGNORECASE)
        if episodes:
            item['season'] = episodes[0][0]
            item['episode'] = episodes[0][1]
        else:
            episodes = re.findall('(\d)(\d{1,2})', item['title'], re.IGNORECASE)
            if episodes:
                search_string = (re.sub('(\d)(\d{1,2})', '', item['title']))
                item['season'] = episodes[0][0]
                item['episode'] = episodes[0][1]

    if item['mansearch']:
        search_string = urllib.unquote(item['mansearchstr']).replace(" ", "+")
        episodes = re.findall('S(\d{1,2})E(\d{1,2})', search_string, re.IGNORECASE)
        if episodes:
            item['season'] = episodes[0][0]
            item['episode'] = episodes[0][1]
        else: 
            item['season'] = ''
            item['episode'] = ''
    search_link = '%s/search.php?get=cautare&t=film&s=%s' % (base_url, search_string)
    search_link2 = '%s/search.php?get=cautare&t=serial&s=%s' % (base_url, search_string)
    search = get_url(search_link, 'json') + get_url(search_link2, 'json')
    match = []
    sezoane = []
    episoade = []
    for movie in search:
        legatura = base_url + movie['url']
        match.append((movie['titlu'],
                    'Rosa-Team',
                    legatura,
                    ))
    regex = '''"list-group"(.+?)</div'''
    regexb = '''href=['"](.+?)['"].+?>(.+?)(?:<.+?>)(.+?)<'''
    dialog = xbmcgui.Dialog()
    if len(match) > 1: sel = dialog.select("Alege filmul", ['%s %s' % ('Serial' if 'serial' in sel_m[2] else 'Film' ,sel_m[0]) for sel_m in match])
    else: sel = 0
    if sel >= 0 and match:
        if not item['season']:
            s_content = get_url(match[sel][2], 'content')
            s_serial = re.findall(regex, s_content, re.IGNORECASE | re.DOTALL)
            if len(s_serial) > 0:
                for s_serialb in s_serial:
                    for l_sezon, sezon, numar in re.findall(regexb, s_serialb, re.IGNORECASE | re.DOTALL):
                        legatura = base_url + l_sezon
                        sezon = sezon + numar
                        sezoane.append((legatura, sezon))
                dialogb = xbmcgui.Dialog()
                if len(sezoane) > 1: selb = dialogb.select("Alege sezonul", [sel_s[1].strip() for sel_s in sezoane])
                else: selb = 0
                if selb >= 0:
                    clean_search = []
                    clean_search.append({'SeriesSeason': '0', 'SeriesEpisode': '0', 'LanguageName': 'Romanian', 'episode': '0', 'SubFileName': sezoane[selb][1], 'SubRating': '5', 'ZipDownloadLink': sezoane[selb][0], 'ISO639': 'ro', 'SubFormat': 'srt', 'MatchedBy': 'fulltext', 'SubHearingImpaired': '0', 'Traducator': 'Rosa-Team', 'referer': base_url})
                    if clean_search: return clean_search 
                else: return None
            else:
                clean_search = []
                clean_search.append({'SeriesSeason': '0', 'SeriesEpisode': '0', 'LanguageName': 'Romanian', 'episode': '0', 'SubFileName': match[sel][0], 'SubRating': '5', 'ZipDownloadLink': match[sel][2], 'ISO639': 'ro', 'SubFormat': 'srt', 'MatchedBy': 'fulltext', 'SubHearingImpaired': '0', 'Traducator': 'Rosa-Team', 'referer': base_url})
                if clean_search: return clean_search
        else:
            clean_search = []
            clean_search.append({'SeriesSeason': '0', 'SeriesEpisode': '0', 'LanguageName': 'Romanian', 'episode': '0', 'SubFileName': match[sel][0], 'SubRating': '5', 'ZipDownloadLink': '%s/sezon:%s/episod:%s' % (match[sel][2], item['season'].lstrip('0'), item['episode'].lstrip('0')), 'ISO639': 'ro', 'SubFormat': 'srt', 'MatchedBy': 'fulltext', 'SubHearingImpaired': '0', 'Traducator': 'Rosa-Team', 'referer': base_url})
            if clean_search: return clean_search


def get_url(url, out):
    ua = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'
    headers = {'User-Agent': ua, 'Host': 'rosa-team.ro', 'Referer': '%s/' % base_url}
    if out == 'text': return s.get(url, headers=headers, verify=False).text
    elif out == 'json': return s.get(url, headers=headers, verify=False).json()
    else: return s.get(url, headers=headers, verify=False).content

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|\[.*?\]')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
      
def log(module, msg):
    xbmc.log((u"### [%s] - %s" % (module, msg,)).encode('utf-8'), level=xbmc.LOGDEBUG)
  
def safeFilename(filename):
    keepcharacters = (' ', '.', '_', '-')
    return "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip()

def natcasesort(arr):
    if isinstance(arr, list):
        arr = sorted(arr, key=lambda x:str(x).lower())
    elif isinstance(arr, dict):
        arr = sorted(arr.iteritems(), key=lambda x:str(x[0]).lower())
    return arr

def natural_key(string_):
    return [int(k) if k.isdigit() else k for k in re.split(r'(\d+)', string_)]

def normalizeString(obj):
    try:
        return unicodedata.normalize(
                                     'NFKD', unicode(unicode(obj, 'utf-8'))
                                     ).encode('ascii', 'ignore')
    except:
        return unicode(str(obj).encode('string_escape'))

def get_params(string=""):
    param = []
    if string == "":
        paramstring = sys.argv[2]
    else:
        paramstring = string
    if len(paramstring) >= 2:
        params = paramstring
        cleanedparams = params.replace('?', '')
        if (params[len(params)-1] == '/'):
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param

params = get_params()

if params['action'] == 'search' or params['action'] == 'manualsearch':
    log(__name__, "action '%s' called" % params['action'])
    item = {}
    item['temp']               = False
    item['rar']                = False
    item['mansearch']          = False
    item['year']               = xbmc.getInfoLabel("VideoPlayer.Year")                         # Year
    item['season']             = str(xbmc.getInfoLabel("VideoPlayer.Season"))                  # Season
    item['episode']            = str(xbmc.getInfoLabel("VideoPlayer.Episode"))                 # Episode
    item['tvshow']             = normalizeString(xbmc.getInfoLabel("VideoPlayer.TVshowtitle"))  # Show
    item['title']              = normalizeString(xbmc.getInfoLabel("VideoPlayer.OriginalTitle"))# try to get original title
    item['file_original_path'] = xbmc.Player().getPlayingFile().decode('utf-8')                 # Full path of a playing file
    item['3let_language']      = [] #['scc','eng']

    if 'searchstring' in params:
        item['mansearch'] = True
        item['mansearchstr'] = params['searchstring']

    for lang in urllib.unquote(params['languages']).decode('utf-8').split(","):
        if lang == "Portuguese (Brazil)":
            lan = "pob"
        elif lang == "Greek":
            lan = "ell"
        else:
            lan = xbmc.convertLanguage(lang, xbmc.ISO_639_2)

        item['3let_language'].append(lan)

    if item['title'] == "":
        log(__name__, "VideoPlayer.OriginalTitle not found")
        item['title']  = normalizeString(xbmc.getInfoLabel("VideoPlayer.Title"))      # no original title, get just Title

    if item['episode'].lower().find("s") > -1:                                      # Check if season is "Special"
        item['season'] = "0"                                                          #
        item['episode'] = item['episode'][-1:]

    if (item['file_original_path'].find("http") > -1):
        item['temp'] = True

    elif (item['file_original_path'].find("rar://") > -1):
        item['rar']  = True
        item['file_original_path'] = os.path.dirname(item['file_original_path'][6:])

    elif (item['file_original_path'].find("stack://") > -1):
        stackPath = item['file_original_path'].split(" , ")
        item['file_original_path'] = stackPath[0][8:]

    Search(item)

elif params['action'] == 'setsub':
    if xbmcvfs.exists(__temp__):
        shutil.rmtree(__temp__)
    xbmcvfs.mkdirs(__temp__)
    files = os.path.join(__temp__, "rosa-team.srt")
    r = get_url(urllib.unquote_plus(params['link']), 'content')
    with open(files, 'wb') as f: f.write(r)
    try: xbmc.Player().setSubtitles(files)
    except: pass
    listitem = xbmcgui.ListItem(label=files)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=files, listitem=listitem, isFolder=False)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
