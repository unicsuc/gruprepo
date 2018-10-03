# -*- coding: utf-8 -*-
import urllib
import urllib2
import datetime
import re
import os
import base64
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib
from modules . jsunpack import unpack as packets
from modules . common import random_agent
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
try :
 import json
except :
 import simplejson as json
import time
import requests
import _Edit
if 64 - 64: i11iIiiIii
OO0o = [ 'alldebrid.com' , 'allmyvideos.net' , 'allvid.ch' , 'auengine.com' , 'beststreams.net' , 'briskfile.com' , 'castamp.com' , 'clicknupload.com' , 'clicknupload.me' , 'clicknupload.link' , 'cloudy.ec' , 'cloudzilla.to' , 'neodrive.co' , 'crunchyroll.com' , 'daclips.in' , 'daclips.com' , 'dailymotion.com' , 'divxstage.eu' , 'divxstage.net' , 'divxstage.to' , 'couldtime.to' , 'ecostream.tv' , 'exashare.com' , 'estream.to' , 'facebook.com' , 'fastplay.cc' , 'fastplay.to' , 'fastplay.sx' , 'filehoot.com' , 'filenuke.com' , 'filepup.net' , 'filmshowonline.net' , 'flashx.tv' , 'plus.google.com' , 'googlevideo.com' , 'picasaweb.google.com' , 'googleusercontent.com' , 'googledrive.com' , 'gorillavid.in' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'hdvid.tv' , 'idowatch.net' , 'indavideo.hu' , 'ishared.eu' , 'jetload.tv' , 'kingfiles.net' , 'letwatch.us' , 'letwatch.to' , 'vidshare.us' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'api.video.mail.ru' , 'mega-debrid.eu' , 'megamp4.net' , 'mersalaayitten.com' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movshare.net' , 'wholecloud.net' , 'mp4engine.com' , 'mp4stream.com' , 'mp4upload.com' , 'myvidstream.net' , 'nosvideo.com' , 'nxload.com' , 'noslocker.com' , 'auroravid.to' , 'novamov.com' , 'nowvideo.sx' , 'nowvideo.eu' , 'nowvideo.ch' , 'nowvideo.sx' , 'nowvideo.co' , 'nowvideo.li' , 'nowvideo.ec' , 'nowvideo.at' , 'nowvideo.fo' , 'ok.ru' , 'odnoklassniki.ru' , 'openload.io' , 'openload.co' , 'play44.net' , 'played.to' , 'playhd.video' , 'playhd.fo' , 'playu.net' , 'playu.me' , 'playwire.com' , 'Premiumize.me' , 'primeshare.tv' , 'promptfile.com' , 'purevid.com' , 'rapidvideo.ws' , 'rapidvideo.com' , 'api.real-debrid.com' , 'premium.rpnet.biz' , 'rutube.ru' , 'shared2.me' , 'shared.sx' , 'sharerepo.com' , 'sharesix.com' , 'simply-debrid.com' , 'speedplay.xyz' , 'speedplay.us' , 'speedplay3.pw' , 'speedvideo.net' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'stream.moe' , 'streamango.com' , 'streamcherry.com' , 'teramixer.com' , 'thevideo.me' , 'thevideos.tv' , 'toltsd-fel.tk' , 'trollvid.net' , 'tune.pk' , 'tusfiles.net' , 'twitch.tv' , 'up2stream.com' , 'upload.af' , 'uploadc.com' , 'uploadc.ch' , 'zalaa.com' , 'uploadx.org' , 'uptobox.com' , 'uptostream.com' , 'userfiles.com' , 'userscloud.com' , 'veehd.com' , 'veoh.com' , 'vid.ag' , 'vidbull.com' , 'vidcrazy.net' , 'uploadcrazy.net' , 'thevideobee.to' , 'videoboxer.co' , 'vidgg.to' , 'vid.gg' , 'videohut.to' , 'videomega.tv' , 'videoraj.to' , 'videorev.cc' , 'videosky.to' , 'video.tt' , 'videoweed.es' , 'bitvid.sx' , 'videoweed.com' , 'videowood.tv' , 'byzoo.org' , 'playpanda.net' , 'videozoo.me' , 'videowing.me' , 'videowing.me' , 'easyvideo.me' , 'play44.net' , 'playbb.me' , 'video44.net' , 'vidio.sx' , 'vidlox.tv' , 'vid.me' , 'vidspot.net' , 'vidto.me' , 'vidup.me' , 'vidup.org' , 'vidzi.tv' , 'vimeo.com' , 'vivo.sx' , 'vk.com' , 'vkpass.com' , 'vodlocker.com' , 'vshare.io' , 'vshare.eu' , 'watchers.to' , 'watchonline.to' , 'watchvideo.us' , 'watchvideo2.us' , 'watchvideo3.us' , 'watchvideo4.us' , 'watchvideo5.us' , 'watchvideo6.us' , 'watchvideo7.us' , 'watchvideo8.us' , 'watchvideo9.us' , 'weshare.me' , 'xvidstage.com' , 'youlol.biz' , 'shitmovie.com' , 'yourupload.com' , 'youtube.com' , 'youtu.be' , 'youwatch.org' , 'api.zevera.com' , 'zettahost.tv' , 'zstream.to' ]
Oo0Ooo = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' ]
if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
class I1IiiI ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 27 - 27: iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o
I1IiI = _Edit . addon
o0OOO = I1IiI . getAddonInfo ( 'version' )
iIiiiI = xbmc . translatePath ( I1IiI . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
Iii1ii1II11i = xbmc . translatePath ( I1IiI . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
iI111iI = os . path . join ( iIiiiI , 'favorites' )
IiII = os . path . join ( iIiiiI , 'history' )
iI1Ii11111iIi = base64 . decodestring
i1i1II = os . path . join ( iIiiiI , 'list_revision' )
O0oo0OO0 = os . path . join ( Iii1ii1II11i , 'icon.png' )
I1i1iiI1 = os . path . join ( Iii1ii1II11i , 'fanart.jpg' )
iiIIIII1i1iI = os . path . join ( iIiiiI , 'source_file' )
o0oO0 = iIiiiI
oo00 = I1IiI . getSetting ( 'Adult' )
o00 = I1IiI . getSetting ( 'Porn_Pass' )
Oo0oO0ooo = I1IiI . getSetting ( 'debug' )
if os . path . exists ( iI111iI ) == True :
 o0oOoO00o = open ( iI111iI ) . read ( )
else : o0oOoO00o = [ ]
if os . path . exists ( iiIIIII1i1iI ) == True :
 i1 = open ( iiIIIII1i1iI ) . read ( )
else : i1 = [ ]
oOOoo00O0O = 'plugin.video.supremacy'
if 15 - 15: I11iii11IIi
def O00o0o0000o0o ( string ) :
 if Oo0oO0ooo == 'true' :
  xbmc . log ( "[addon.live.Supremacy Lists-%s]: %s" % ( o0OOO , string ) )
  if 88 - 88: o0ooo / OOO0O / I1ii * oOOOo0o0O + OoOoo0 % oOOoo
  if 43 - 43: OOooO % ooO00oo - o00ooooO0oO - IiIi11i - II1 + IiIi11i
def o0O0 ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0' }
  O00O0O0O0 = urllib2 . Request ( url , None , headers )
  ooO0O = urllib2 . urlopen ( O00O0O0O0 )
  oo = ooO0O . read ( )
  ooO0O . close ( )
  return oo
 except urllib2 . URLError , iii11iII :
  O00o0o0000o0o ( 'URL: ' + url )
  if hasattr ( iii11iII , 'code' ) :
   O00o0o0000o0o ( 'We failed with error code - %s.' % iii11iII . code )
   xbmc . executebuiltin ( "XBMC.Notification(Supremacy,We failed with error code - " + str ( iii11iII . code ) + ",10000," + O0oo0OO0 + ")" )
  elif hasattr ( iii11iII , 'reason' ) :
   O00o0o0000o0o ( 'We failed to reach a server.' )
   O00o0o0000o0o ( 'Reason: %s' % iii11iII . reason )
   xbmc . executebuiltin ( "XBMC.Notification(Supremacy,We failed to reach a server. - " + str ( iii11iII . reason ) + ",10000," + O0oo0OO0 + ")" )
   if 42 - 42: o00ooooO0oO + OOO0O
   if 70 - 70: IiIIi1I1Iiii % IiIIi1I1Iiii . ooO00oo % Ooo00oOo00o * o0ooo % I1ii
def iiI1IiI ( ) :
 if oOOoo00O0O == _Edit . name :
  O00o0o0000o0o ( "SKindex" )
  II ( '[COLOR blue]======[/COLOR][COLOR red]WELCOME TO SUPREMACY ADD-ON[/COLOR][COLOR blue]======[/COLOR]' , '' , '' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLOR red]Supremacy Movie Search[/COLOR]' , 'http://stephen-builds.uk/supremacy/Search%20Supremacy%20Movies/home.txt' , 41 , 'http://stephen-builds.uk/art/icon111.jpg' , I1i1iiI1 , '' , '' , '' , '' )
  II ( '[COLOR aqua]24/7 Shows[/COLOR]' , '' , 905 , 'http://stephen-builds.uk/art/24%207%20shows.png' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
  II ( '[COLORaqua]Scraper Movies[/COLOR]' , '' , 999997 , 'http://stephen-builds.uk/art/MOVIE%20SCRAPPER.png' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLORaqua]Scraper Tv Shows[/COLOR]' , '' , 400 , 'http://stephen-builds.uk/art/TV%20SHOWS%20SCRAPPER.png' , I1i1iiI1 , '' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLORaqua]Freeview[/COLOR]' , 'https://tvcatchup.com/channels' , 301 , 'http://stephen-builds.uk/art/FREEVEW.png' , I1i1iiI1 , '' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLORaqua]Sport Replays[/COLOR]' , 'http://fullmatchsports.com/' , 500 , 'http://stephen-builds.uk/art/football.png' , I1i1iiI1 , '' , '' , '' , '' , '' )
  ooOoOoo0O ( '[COLORaqua]Acestream Channels Scraper[/COLOR]' , '' , 504 , 'http://stephen-builds.uk/art/lo.png' , I1i1iiI1 , '' , '' , '' , '' , '' )
  if 76 - 76: OOO0O0O0ooooo / o0ooo . IIiIiII11i * oOOoo - oOOOo0o0O
  Oooo ( _Edit . MainBase , '' )
  if oo00 == o00 :
   ooOoOoo0O ( '[COLOR red]18 only[/COLOR]' , '' , 69 , 'http://stephen-builds.uk/art/18%20only.png' , I1i1iiI1 , '' , '' , '' , '' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 67 - 67: oOOOo0o0O / II1 % OoOoo0 - IIii1I
def Ooo ( ) :
 O0o0Oo = { 'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0' }
 Oo00OOOOO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 O0O = 'https://proxyportal.net'
 O00o0OO = 'http://unblocked.lol/views/tv.php'
 I11i1 = requests . get ( O0O , headers = O0o0Oo ) . content
 iIi1ii1I1 = re . compile ( '<h2 id="livesport"(.+?)<h2 class="text-center">' , re . DOTALL ) . findall ( I11i1 )
 o0 = re . compile ( '<div class="panel-body">.+?href="(.+?)".+?"true"></i>(.+?)<' , re . DOTALL ) . findall ( str ( iIi1ii1I1 ) )
 for I11II1i , IIIII in o0 :
  IIIII = IIIII . encode ( 'utf8' ) . replace ( '&nbsp;' , '' )
  ooooooO0oo ( IIIII , Oo00OOOOO + I11II1i , 906 , '' , I1i1iiI1 , '' , '' )
  if 49 - 49: o0ooo * IIii1I / O00ooooo00 / i11iIiiIii / o0ooo
  if 28 - 28: oOOOo0o0O - ooO00oo . ooO00oo + I11iii11IIi - II1 + OOO0O0O0ooooo
  if 95 - 95: Ooo00oOo00o % I1ii . OOO0O0O0ooooo
  if 15 - 15: IiIi11i / oOOoo . oOOoo - O00ooooo00
  if 53 - 53: ooO00oo + IIiIiII11i * I1ii
  if 61 - 61: O00ooooo00 * oOOOo0o0O / II1 . i11iIiiIii . I11iii11IIi
  if 60 - 60: OoOoo0 / OoOoo0
  if 46 - 46: oOOoo * oOOOo0o0O - Ooo00oOo00o * I1ii - o00ooooO0oO
  if 83 - 83: II1
  if 31 - 31: iIiiiI1IiI1I1 - oOOOo0o0O . o00ooooO0oO % I11iii11IIi - OOO0O0O0ooooo
  if 4 - 4: iIiiiI1IiI1I1 / IiIi11i . OOooO
  if 58 - 58: oOOOo0o0O * i11iIiiIii / I11iii11IIi % o00ooooO0oO - OOO0O / I1ii
def ii11i1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 if iconimage == '' :
  iconimage = O0oo0OO0
 if fanart == '' :
  fanart = I1i1iiI1
 if not 'http' in url :
  ooooooO0oo ( name , url , mode , iconimage , fanart , description , extra )
 elif 'watchseries' in url :
  ooooooO0oo ( name , url , mode , iconimage , fanart , description , extra )
 elif 'm3u' in url :
  ooooooO0oo ( name , url , mode , iconimage , fanart , description , extra )
 else :
  IIIii1II1II ( url , name , iconimage , fanart , description , '' , '' , True , '' , '' , 1 , '' )
def i1I1iI ( url ) :
 oo0OooOOo0 = [ 'How To Download' , 'Contact' , 'DMCA/Privacy Policy' , 'Sitemap' , 'Home' , 'Index' ]
 I11i1 = requests . get ( url ) . content
 o0O = BeautifulSoup ( I11i1 )
 O00oO = o0O . findAll ( 'nav' , attrs = { 'id' : 'site-navigation' } )
 for I11i1I1I in O00oO :
  oO0Oo = I11i1I1I . findAll ( 'li' )
  if 54 - 54: o0ooo - IIiIiII11i + II1
  for O0o0 in oO0Oo :
   if 71 - 71: oOOOo0o0O + IiIi11i % i11iIiiIii + OOO0O - ooO00oo
   oO0OOoO0 = O0o0 . findAll ( 'a' )
   for I11II1i in oO0OOoO0 :
    if I11II1i . has_key ( 'href' ) :
     if I11II1i . has_key ( 'itemprop' ) :
      I111Ii111 = I11II1i [ 'href' ]
      i111IiI1I = I11II1i . findAll ( 'span' )
      for IIIII in i111IiI1I :
       O0 = IIIII . text
       if not O0 in oo0OooOOo0 :
        O0 = O0 . replace ( 'Full Match' , 'Recent Games' )
        if I111Ii111 == '#' :
         ooOoOoo0O ( '[COLORred]' + O0 + '[/COLOR]' , '' , '' , '' , I1i1iiI1 , '' , '' , '' , '' , '' )
        else :
         ooOoOoo0O ( '[COLORaqua]' + O0 + '[/COLOR]' , I111Ii111 , 501 , '' , I1i1iiI1 , '' , '' , '' , '' , '' )
         if 30 - 30: o0ooo . oOOoo - II1
         if 8 - 8: O00ooooo00 - IIii1I * iIiiiI1IiI1I1 + i11iIiiIii / o00ooooO0oO % oOOOo0o0O
def iIIIi1 ( url ) :
 I11i1 = requests . get ( url ) . content
 o0O = BeautifulSoup ( I11i1 )
 O00oO = o0O . findAll ( 'div' , attrs = { 'class' : 'content-thumbnail' } )
 for I11i1I1I in O00oO :
  oO0OOoO0 = I11i1I1I . findAll ( 'a' )
  for I11II1i in oO0OOoO0 :
   if I11II1i . has_key ( 'href' ) :
    I111Ii111 = I11II1i [ 'href' ]
   iiII1i1 = I11II1i . findAll ( 'img' )
   for o00oOO0o in iiII1i1 :
    O0oo0OO0 = o00oOO0o [ 'src' ]
    O0 = o00oOO0o [ 'alt' ]
    ooOoOoo0O ( '[COLORaqua]' + O0 + '[/COLOR]' , I111Ii111 , 502 , O0oo0OO0 , O0oo0OO0 , '' , '' , '' , '' , '' )
    if 80 - 80: I1ii + oOOOo0o0O - oOOOo0o0O % OOooO
def OoOO0oo0o ( url ) :
 I11i1 = requests . get ( url ) . content
 o0 = re . compile ( '<div class="streaming">(.+?)<div class="tab-content">' , re . DOTALL ) . findall ( I11i1 )
 if 14 - 14: o0ooo * OOooO * OOooO / I11iii11IIi
 for I11II1i in o0 :
  Oo0o00 = re . compile ( 'href="(.+?)">(.+?)<' , re . DOTALL ) . findall ( str ( I11II1i ) )
  for O0O0oOO00O00o , iI1ii11iIi1i in Oo0o00 :
   ooOoOoo0O ( '[COLORaqua]' + iI1ii11iIi1i + '[/COLOR]' , url + O0O0oOO00O00o , 503 , '' , '' , '' , '' , '' , '' , '' )
   if 50 - 50: ooO00oo
   if 14 - 14: OoOoo0 % Ooo00oOo00o * OoOoo0
def iII ( url ) :
 I11i1 = requests . get ( url ) . content
 oO00o0 = re . compile ( '<iframe.+?src="(.+?)"' , re . DOTALL ) . findall ( I11i1 )
 for I11II1i in oO00o0 :
  if not "facebook" in I11II1i :
   if not 'http' in I11II1i :
    I11II1i = 'https:' + I11II1i
   OOoo0O = requests . get ( I11II1i ) . content
   Oo0ooOo0o = re . compile ( '<source src="(.+?)".+?label=\'(.+?)\'' , re . DOTALL ) . findall ( OOoo0O )
   for Ii1i1 , iiIii in Oo0ooOo0o :
    ooooooO0oo ( '[COLORaqua] link 1' + iiIii + '[/COLOR]' , Ii1i1 , 906 , '' , '' , '' , '' )
   ooo0O = I11II1i . replace ( 'mirror=1' , 'mirror=2' )
   OOoo0O = requests . get ( ooo0O ) . content
   Oo0ooOo0o = re . compile ( '<iframe.+?src="(.+?)"' , re . DOTALL ) . findall ( OOoo0O )
   for oOoO0o00OO0 in Oo0ooOo0o :
    ooooooO0oo ( '[COLORaqua] link 2 [/COLOR]' , oOoO0o00OO0 , 906 , '' , '' , '' , '' )
    if 7 - 7: oOOOo0o0O + o00ooooO0oO + OOO0O0O0ooooo
    if 9 - 9: iIiiiI1IiI1I1 . o0ooo - IiIi11i / o0ooo
    if 46 - 46: OoOoo0 . oOOOo0o0O * OoOoo0 % O00ooooo00
    if 46 - 46: I11iii11IIi + Ooo00oOo00o
    if 10 - 10: IiIIi1I1Iiii - o00ooooO0oO . OOO0O0O0ooooo
    if 84 - 84: OOO0O0O0ooooo
def OOOooOO0 ( url ) :
 O00o0o0000o0o ( "get_porn_data" )
 Oooo ( _Edit . PornBase , '' )
def OOOOoOoo0O0O0 ( url ) :
 O00O0O0O0 = urllib2 . Request ( url )
 O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 ooO0O = ''
 I11II1i = ''
 try :
  ooO0O = urllib2 . urlopen ( O00O0O0O0 )
  I11II1i = ooO0O . read ( )
  ooO0O . close ( )
 except : pass
 if I11II1i != '' :
  return I11II1i
 else :
  I11II1i = 'Opened'
  return I11II1i
if 85 - 85: I1ii % i11iIiiIii - OOooO * II1 / IIiIiII11i % IIiIiII11i
if 1 - 1: Ooo00oOo00o - I1ii . OoOoo0 . Ooo00oOo00o / IiIIi1I1Iiii + OoOoo0
if 78 - 78: OOO0O0O0ooooo . I1ii . iIiiiI1IiI1I1 % oOOOo0o0O
if 49 - 49: oOOoo / Ooo00oOo00o . iIiiiI1IiI1I1
if 68 - 68: i11iIiiIii % OOO0O + i11iIiiIii
if 31 - 31: iIiiiI1IiI1I1 . IIiIiII11i
if 1 - 1: IiIIi1I1Iiii / o0ooo % OOooO * ooO00oo . i11iIiiIii
def III1Iiii1I11 ( ) :
 II ( '[COLORaqua]NEW MOVIES[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/SCRAP%20MOVIES.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]PEOPLE WATCHING[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/people%20watching.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]FULL LIST MOVIES[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/full.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]MOVIES A - Z[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/A-Z/A-Z.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]MOVIES GENRE[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/Genre/Genre.txt' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]MOST POPULAR[/COLOR]' , 'http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8' , 999996 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 II ( '[COLORaqua]Kids Movies[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/Kids%20movies.xml' , 999999 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' )
 if 9 - 9: OOO0O / IiIIi1I1Iiii - IIiIiII11i / II1 / IIii1I - o0ooo
def o00oooO0Oo ( url ) :
 I11i1 = requests . get ( url ) . text
 o0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( I11i1 )
 for O0 , o0O0OOO0Ooo , iiIiI , I1 , OOO00O0O , iii , oOooOOOoOo in o0 :
  if oOooOOOoOo == ' ' :
   oOooOOOoOo = I1i1iiI1
  if I1 == ' ' :
   I1 = O0oo0OO0
  OOO00O0O = OOO00O0O . replace ( '\\n' , ' ' )
  if o0O0OOO0Ooo == 'Movie Search' :
   ooooooO0oo ( O0 , iii , 999998 , I1 , oOooOOOoOo , OOO00O0O , '' )
  elif o0O0OOO0Ooo == 'Menu' :
   II ( O0 , iiIiI , 999999 , I1 , oOooOOOoOo , OOO00O0O , '' )
   if 41 - 41: oOOoo - OOO0O0O0ooooo - OOO0O0O0ooooo
def oO00OOoO00 ( url ) :
 I11i1 = requests . get ( url ) . text
 o0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<season>(.+?)</season>.+?<episode>(.+?)</episode>.+?<season_year>(.+?)</season_year>.+?<fanart>(.+?)</fanart>.+?</item>' , re . DOTALL ) . findall ( I11i1 )
 for O0 , o0O0OOO0Ooo , iiIiI , I1 , OOO00O0O , IiI111111IIII , i1Ii , ii111iI1iIi1 , oOooOOOoOo in o0 :
  if oOooOOOoOo == ' ' :
   oOooOOOoOo = I1i1iiI1
  if I1 == ' ' :
   I1 = O0oo0OO0
  OOO00O0O = OOO00O0O . replace ( '\\n' , ' ' )
  if o0O0OOO0Ooo == 'tv search' :
   II ( O0 + ' - SEASON -' + IiI111111IIII + '- EPISODE-' + i1Ii + '-' + ii111iI1iIi1 , '' , 404 , I1 , oOooOOOoOo , '' , O0 )
  elif o0O0OOO0Ooo == 'Menu' :
   II ( O0 , iiIiI , 410 , I1 , oOooOOOoOo , OOO00O0O , '' )
   if 78 - 78: Ooo00oOo00o . oOOOo0o0O + Ooo00oOo00o / OoOoo0 / Ooo00oOo00o
def oO0O00OoOO0 ( url ) :
 II ( '[COLORaqua]Most Popular By Genre[/COLOR]' , 'http://www.imdb.com/genre/?ref_=nv_ch_gr_3' , 999995 , '' , '' , '' , '' , '' , '' )
 OoO = 'http://imdb.com'
 I11i1 = requests . get ( 'http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8' ) . content
 o0 = re . compile ( '<td class="posterColumn">.+?title=.+?>(.+?)</a>.+?<span class="secondaryInfo">(.+?)</span>' , re . DOTALL ) . findall ( I11i1 )
 for IIIII , iii in o0 :
  O00 = iii . replace ( '(' , '' ) . replace ( ')' , '' )
  ooooooO0oo ( IIIII + '  [COLORred]' + iii + '[/COLOR]' , O00 , 999998 , '' , '' , iii , IIIII )
  if 29 - 29: o00ooooO0oO / Ooo00oOo00o . O00ooooo00 * IIiIiII11i + i11iIiiIii
def I1Ii ( url ) :
 I11i1 = requests . get ( url ) . content
 o0 = re . compile ( '<tr class=".+?".+?<h3>.+?href="(.+?)">(.+?)<.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( I11i1 )
 for O0oo00o0O , i1I1I , iiI1I in o0 :
  II ( '[COLORaqua]' + i1I1I . upper ( ) + '[/COLOR]' , O0oo00o0O , 999994 , '' , '' , '' , '' , '' , '' )
  if 12 - 12: i11iIiiIii - O00ooooo00 - Ooo00oOo00o . O00ooooo00 - oOOOo0o0O + OOO0O0O0ooooo
def oO0OOOO0 ( url ) :
 if 26 - 26: oOOoo
 I11i1 = requests . get ( url ) . content
 o0 = re . compile ( '<td class="image">.+?title="(.+?)".+?<span class="year_type">(.+?)<' , re . DOTALL ) . findall ( I11i1 )
 for I11iiI1i1 , I1i1Iiiii in o0 :
  I11iiI1i1 = I11iiI1i1 . replace ( '&#x26;#x27;' , '' ) . replace ( '&#x26;' , '' ) . replace ( '&#x27;' , '' )
  O00 = I1i1Iiiii [ 1 : 5 ]
  ooooooO0oo ( I11iiI1i1 + '  [COLORred]' + I1i1Iiiii + '[/COLOR]' , O00 , 999998 , '' , '' , I1i1Iiiii , I11iiI1i1 )
  if 94 - 94: o0ooo * oOOoo / IiIIi1I1Iiii / oOOoo
def oO0 ( url ) :
 if 75 - 75: IiIi11i + I11iii11IIi + o0ooo * OoOoo0 % I1ii . OOooO
 I11i1 = requests . get ( url ) . content
 o0O = BeautifulSoup ( I11i1 )
 if 55 - 55: oOOOo0o0O . IIiIiII11i
 if 61 - 61: IiIIi1I1Iiii % ooO00oo . IiIIi1I1Iiii
 O00oO = o0O . findAll ( 'p' , attrs = { 'class' : "channelsicon" } )
 for I11i1I1I in O00oO :
  if 100 - 100: o00ooooO0oO * OOO0O0O0ooooo
  oO0OOoO0 = I11i1I1I . findAll ( 'a' )
  for I11II1i in oO0OOoO0 :
   if I11II1i . has_key ( 'href' ) :
    o00oO0oo0OO = 'https://tvcatchup.com' + I11II1i [ 'href' ]
   O0O0OOOOoo = I11II1i . findAll ( 'img' , attrs = { 'style' : "" } )
   if 74 - 74: OOO0O + iIiiiI1IiI1I1 / Ooo00oOo00o
   for oOo0O0Oo00oO in O0O0OOOOoo :
    if 7 - 7: ooO00oo * o00ooooO0oO % oOOoo - o0ooo
    i1i = oOo0O0Oo00oO [ 'alt' ]
    i1i = i1i . encode ( 'utf8' )
   o0 = re . compile ( '<br />(.+?)</a>' ) . findall ( str ( I11II1i ) )
   for oOOoo00O00o in o0 :
    oOOoo00O00o = oOOoo00O00o . encode ( 'utf8' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , 'and' )
    import base64
    iI1Ii11111iIi = base64 . decodestring
    I11i1 = requests . get ( o00oO0oo0OO ) . content
    o0 = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( I11i1 )
    for iI1ii11iIi1i in o0 :
     if not 'text' in iI1ii11iIi1i :
      url = iI1Ii11111iIi ( iI1Ii11111iIi ( iI1ii11iIi1i ) )
      ii11i1 ( '[COLORgold]' + i1i + '[/COLOR][COLORwhite] - [COLORsteelblue]' + oOOoo00O00o + '[/COLOR]' , url , 906 , '' , '' , '' , '' , '' , '' )
      if 98 - 98: oOOOo0o0O + ooO00oo + I1ii % II1
def oooooo0O000o ( ) :
 if 64 - 64: IIiIiII11i . o0ooo - o00ooooO0oO / II1
 ooOoOoo0O ( '[COLORaqua][B]Tv Shows List[/COLOR][/B]' , 'http://www.tvmaze.com/shows' , 402 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' , '' )
 ooOoOoo0O ( '[COLORred]SEARCH Tv Shows[/COLOR]' , '' , 405 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' , '' )
 ooOoOoo0O ( '[COLORaqua]Popular Tv Shows[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/tv%20shows/gotmain.txt' , 410 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' , '' )
 ooOoOoo0O ( '[COLORaqua]Netflix Original Tv Shows[/COLOR]' , 'http://stephen-builds.uk/supremacy/scrap%20movies/Netflix%20Original%20Tv%20Shows/Netflix%20Original%20Tv%20Shows.txt' , 410 , 'http://stephen-builds.uk/art/add.jpg' , 'http://stephen-builds.uk/art/dark-power-button-psd.jpg' , '' , '' , '' , '' , '' )
 if 66 - 66: OOooO - OOooO - i11iIiiIii . OOO0O - oOOOo0o0O
 if 77 - 77: I11iii11IIi - iIiiiI1IiI1I1 - IiIi11i
def IiiiIIiIi1 ( url ) :
 II ( '[COLORsteelblue]SEARCH[/COLOR]' , '' , 405 , '' , I1i1iiI1 , '' , '' )
 I11i1 = requests . get ( url ) . content
 o0 = re . compile ( '<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( I11i1 )
 OoOOoOooooOOo = re . compile ( '<li class="next"><a href="(.+?)"' ) . findall ( I11i1 )
 for url , o00oOO0o , IIIII in o0 :
  oOo0O = 'http://www.tvmaze.com' + url . replace ( '"' , '' )
  OOoo0O = requests . get ( oOo0O ) . content
  o0 = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OOoo0O )
  for oo0O0 in o0 :
   if not '<div>' in oo0O0 :
    iI = oo0O0 . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   o00oOO0o = 'http:' + o00oOO0o
   IIIII = IIIII . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if IIIII == '' :
    OO0O000 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( url ) )
    for IIIII in OO0O000 :
     IIIII = IIIII . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  II ( IIIII , oOo0O , 403 , o00oOO0o , oOooOOOoOo , iI , '' )
  if 37 - 37: II1 - OOO0O0O0ooooo - o0ooo
 for o0o0O0O00oOOo in OoOOoOooooOOo :
  url = 'http://www.tvmaze.com' + o0o0O0O00oOOo
  II ( 'NEXT' , url , 402 , o00oOO0o , oOooOOOoOo , '' , '' )
  if 14 - 14: I11iii11IIi + I1ii
def oo00oO0O0 ( url , name , iconimage ) :
 O0 = name . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
 o00oOO0o = iconimage
 I11i1 = requests . get ( url + '/episodes' ) . content
 OOoo0O = requests . get ( url ) . content
 iIi1ii1I1 = re . compile ( "<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>" , re . DOTALL ) . findall ( I11i1 )
 o0 = re . compile ( '<span id="year">\((.+?)-' , re . DOTALL ) . findall ( OOoo0O )
 for ii111iI1iIi1 in o0 :
  ii111iI1iIi1 = ii111iI1iIi1 . replace ( ' ' , '' )
 for IiI111111IIII , iiI1I in iIi1ii1I1 :
  if not 'special' in IiI111111IIII . lower ( ) :
   IiI111111IIII = IiI111111IIII . replace ( 'S' , '' ) . replace ( 's' , '' )
  I11I11 = re . compile ( '<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( str ( iiI1I ) )
  for i1Ii , o000O0O , I1i1i1iii in I11I11 :
   if not 'special' in i1Ii . lower ( ) :
    II ( O0 + ' - SEASON -' + IiI111111IIII + '- EPISODE-' + i1Ii + '-' + ii111iI1iIi1 , '' , 404 , o00oOO0o , oOooOOOoOo , '' , O0 )
    if 16 - 16: oOOoo + ooO00oo * OOO0O0O0ooooo % O00ooooo00 . IIiIiII11i
def Oo0OO ( ) :
 O0OooOo0o = xbmcgui . Dialog ( )
 iiI11ii1I1 = O0OooOo0o . input ( 'Searching...' , type = xbmcgui . INPUT_ALPHANUM )
 Ooo0OOoOoO0 = 'http://www.tvmaze.com/search?q=' + ( iiI11ii1I1 ) . replace ( ' ' , '+' )
 oOo0OOoO0 = Ooo0OOoOoO0 . lower ( )
 IIo0Oo0oO0oOO00 = requests . get ( oOo0OOoO0 ) . content
 o0 = re . compile ( '<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>' , re . DOTALL ) . findall ( IIo0Oo0oO0oOO00 )
 for O0O , o00oOO0o , IIIII in o0 :
  oOo0O = 'http://www.tvmaze.com' + O0O . replace ( '"' , '' )
  OOoo0O = requests . get ( oOo0O ) . content
  o0 = re . compile ( '<article>.+?<p>(.+?)</p>' , re . DOTALL ) . findall ( OOoo0O )
  for oo0O0 in o0 :
   if not '<div>' in oo0O0 :
    iI = oo0O0 . replace ( '<b>' , '' ) . replace ( '</b>' , '' ) . replace ( '<i>' , '' ) . replace ( '</i>' , '' )
   o00oOO0o = 'http:' + o00oOO0o
   IIIII = IIIII . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
   if IIIII == '' :
    OO0O000 = re . compile ( '/shows/.+?/([^"]*)"' ) . findall ( str ( O0O ) )
    for IIIII in OO0O000 :
     IIIII = IIIII . replace ( '-' , ' ' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' )
  II ( IIIII , oOo0O , 403 , o00oOO0o , oOooOOOoOo , iI , '' )
  if 92 - 92: II1 * o00ooooO0oO
def o0000oO ( name , extra ) :
 if 11 - 11: IiIi11i / I11iii11IIi - ooO00oo * II1 + II1 . I11iii11IIi
 i1I1i111Ii = xbmcgui . DialogProgress ( )
 i1I1i111Ii . create ( 'Checking for stream' )
 from modules import Scrape_Nan
 ooo = name + '<>'
 i1i1iI1iiiI = re . compile ( '(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>' ) . findall ( str ( ooo ) )
 for O0 , Ooo0oOooo0 , oOOOoo00 , ii111iI1iIi1 in i1i1iI1iiiI :
  O0 = O0
  Ooo0oOooo0 = Ooo0oOooo0
  oOOOoo00 = oOOOoo00
  iiIiIIIiiI = ''
  Scrape_Nan . scrape_episode ( O0 , ii111iI1iIi1 , '' , Ooo0oOooo0 , oOOOoo00 , '' )
  if 12 - 12: OOO0O0O0ooooo - o0ooo
def oOoO00O0 ( url ) :
 import base64
 iI1Ii11111iIi = base64 . decodestring
 I11i1 = requests . get ( url ) . content
 o0 = re . compile ( 'var.+?=.+?"(.+?)"' , re . DOTALL ) . findall ( I11i1 )
 for iI1ii11iIi1i in o0 :
  if not 'text' in iI1ii11iIi1i :
   url = iI1Ii11111iIi ( iI1Ii11111iIi ( iI1ii11iIi1i ) )
   OO ( '' , url )
   if 7 - 7: OOO0O0O0ooooo * i11iIiiIii * oOOoo + IiIi11i % Ooo00oOo00o - IiIi11i
def II1IIIIiII1i ( url ) :
 import resolveurl
 try :
  i1II1 = resolveurl . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( i1II1 , xbmcgui . ListItem ( IIIII ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( IIIII ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "ERROR" , "unplayable stream" )
   sys . exit ( )
   if 25 - 25: o00ooooO0oO / IIii1I % OOooO
def IiiiiI1i1Iii ( extra , url ) :
 from modules import Scrape_Nan
 IIIII = str ( extra )
 iii = str ( url )
 i1I1i111Ii = xbmcgui . DialogProgress ( )
 i1I1i111Ii . create ( 'Checking for stream' )
 Scrape_Nan . scrape_movie ( IIIII , iii , '' )
 if 87 - 87: o0ooo
def IiI1iiiIii ( url ) :
 O0OooOo0o = xbmcgui . Dialog ( )
 I1III1111iIi = O0OooOo0o . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1i111I = I1III1111iIi . lower ( )
 if I1i111I == '' :
  pass
 else :
  OooOo0oo0O0o00O ( I1i111I , url )
  if 48 - 48: IiIi11i / o00ooooO0oO . IIii1I * I11iii11IIi * I1ii / O00ooooo00
def OooOo0oo0O0o00O ( Search_name , url ) :
 IIo0Oo0oO0oOO00 = OOOOoOoo0O0O0 ( url )
 if IIo0Oo0oO0oOO00 != 'Failed' :
  o0 = re . compile ( '<channel>.+?<name>(.+?)</name>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>.+?<fanart>(.+?)</fanart>.+?</channel>' , re . DOTALL ) . findall ( IIo0Oo0oO0oOO00 )
  for IIIII , iiII1i1 , url , oOooOOOoOo in o0 :
   if not 'http:' in url :
    pass
   else :
    OooOo0oo0O0o00O ( Search_name , url )
  oO00o0 = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( IIo0Oo0oO0oOO00 )
  for IIIII , url , iiII1i1 , oOooOOOoOo in oO00o0 :
   if 'http:' in url :
    if Search_name . lower ( ) in IIIII . lower ( ) :
     IIIii1II1II ( url , IIIII , iiII1i1 , oOooOOOoOo , '' , '' , '' , '' , None , '' , 1 )
     if 92 - 92: IiIIi1I1Iiii % IiIIi1I1Iiii - o0ooo / I11iii11IIi
     if 10 - 10: OOooO + IiIIi1I1Iiii * OOO0O + IIii1I / o00ooooO0oO / OOO0O
def iI1II ( ) :
 if os . path . exists ( iI111iI ) == True :
  ooOoOoo0O ( 'Favorites' , 'url' , 4 , os . path . join ( Iii1ii1II11i , 'resources' , 'favorite.png' ) , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "browse_xml_database" ) == "true" :
  ooOoOoo0O ( 'XML Database' , 'http://xbmcplus.xb.funpic.de/www-data/filesystem/' , 15 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "browse_community" ) == "true" :
  ooOoOoo0O ( 'Community Files' , 'community_files' , 16 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if os . path . exists ( IiII ) == True :
  ooOoOoo0O ( 'Search History' , 'history' , 25 , os . path . join ( Iii1ii1II11i , 'resources' , 'favorite.png' ) , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "searchyt" ) == "true" :
  ooOoOoo0O ( 'Search:Youtube' , 'youtube' , 25 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "searchDM" ) == "true" :
  ooOoOoo0O ( 'Search:dailymotion' , 'dmotion' , 25 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if I1IiI . getSetting ( "PulsarM" ) == "true" :
  ooOoOoo0O ( 'Pulsar:IMDB' , 'IMDBidplay' , 27 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if os . path . exists ( iiIIIII1i1iI ) == True :
  o0OOo0o0O0O = json . loads ( open ( iiIIIII1i1iI , "r" ) . read ( ) )
  if 65 - 65: i11iIiiIii
  if len ( o0OOo0o0O0O ) > 1 :
   for O0O0o0oOOO in o0OOo0o0O0O :
    if 67 - 67: I11iii11IIi + OOO0O . o0ooo . iIiiiI1IiI1I1
    if isinstance ( O0O0o0oOOO , list ) :
     ooOoOoo0O ( O0O0o0oOOO [ 0 ] . encode ( 'utf-8' ) , O0O0o0oOOO [ 1 ] . encode ( 'utf-8' ) , 1 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' , 'source' )
    else :
     o000ooooO0o = O0oo0OO0
     oOooOOOoOo = I1i1iiI1
     oo0O0 = ''
     iI1i11 = ''
     credits = ''
     OoOOoooOO0O = ''
     if O0O0o0oOOO . has_key ( 'thumbnail' ) :
      o000ooooO0o = O0O0o0oOOO [ 'thumbnail' ]
     if O0O0o0oOOO . has_key ( 'fanart' ) :
      oOooOOOoOo = O0O0o0oOOO [ 'fanart' ]
     if O0O0o0oOOO . has_key ( 'description' ) :
      oo0O0 = O0O0o0oOOO [ 'description' ]
     if O0O0o0oOOO . has_key ( 'date' ) :
      iI1i11 = O0O0o0oOOO [ 'date' ]
     if O0O0o0oOOO . has_key ( 'genre' ) :
      OoOOoooOO0O = O0O0o0oOOO [ 'genre' ]
     if O0O0o0oOOO . has_key ( 'credits' ) :
      credits = O0O0o0oOOO [ 'credits' ]
     ooOoOoo0O ( O0O0o0oOOO [ 'title' ] . encode ( 'utf-8' ) , O0O0o0oOOO [ 'url' ] . encode ( 'utf-8' ) , 1 , o000ooooO0o , oOooOOOoOo , oo0O0 , OoOOoooOO0O , iI1i11 , credits , 'source' )
     if 86 - 86: o0ooo
  else :
   if len ( o0OOo0o0O0O ) == 1 :
    if isinstance ( o0OOo0o0O0O [ 0 ] , list ) :
     Oooo ( o0OOo0o0O0O [ 0 ] [ 1 ] . encode ( 'utf-8' ) , I1i1iiI1 )
    else :
     Oooo ( o0OOo0o0O0O [ 0 ] [ 'url' ] , o0OOo0o0O0O [ 0 ] [ 'fanart' ] )
     if 5 - 5: ooO00oo * I11iii11IIi
     if 5 - 5: o00ooooO0oO
def O0I11Iiii1I ( url = None ) :
 if url is None :
  if not I1IiI . getSetting ( "new_file_source" ) == "" :
   oo00O0oO0O0 = I1IiI . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not I1IiI . getSetting ( "new_url_source" ) == "" :
   oo00O0oO0O0 = I1IiI . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  oo00O0oO0O0 = url
 if oo00O0oO0O0 == '' or oo00O0oO0O0 is None :
  return
 O00o0o0000o0o ( 'Adding New Source: ' + oo00O0oO0O0 . encode ( 'utf-8' ) )
 if 96 - 96: i11iIiiIii % IiIi11i / I11iii11IIi
 I1IiI11 = None
 if 9 - 9: OoOoo0
 oo = OoooO ( oo00O0oO0O0 )
 print 'source_url' , oo00O0oO0O0
 if isinstance ( oo , BeautifulSOAP ) :
  if oo . find ( 'channels_info' ) :
   I1IiI11 = oo . channels_info
  elif oo . find ( 'items_info' ) :
   I1IiI11 = oo . items_info
 if I1IiI11 :
  iIII = { }
  iIII [ 'url' ] = oo00O0oO0O0
  try : iIII [ 'title' ] = I1IiI11 . title . string
  except : pass
  try : iIII [ 'thumbnail' ] = I1IiI11 . thumbnail . string
  except : pass
  try : iIII [ 'fanart' ] = I1IiI11 . fanart . string
  except : pass
  try : iIII [ 'genre' ] = I1IiI11 . genre . string
  except : pass
  try : iIII [ 'description' ] = I1IiI11 . description . string
  except : pass
  try : iIII [ 'date' ] = I1IiI11 . date . string
  except : pass
  try : iIII [ 'credits' ] = I1IiI11 . credits . string
  except : pass
 else :
  if '/' in oo00O0oO0O0 :
   iIi = oo00O0oO0O0 . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in oo00O0oO0O0 :
   iIi = oo00O0oO0O0 . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in iIi :
   iIi = urllib . unquote_plus ( iIi )
  ii111I = xbmc . Keyboard ( iIi , 'Displayed Name, Rename?' )
  ii111I . doModal ( )
  if ( ii111I . isConfirmed ( ) == False ) :
   return
  iiI = ii111I . getText ( )
  if len ( iiI ) == 0 :
   return
  iIII = { }
  iIII [ 'title' ] = iiI
  iIII [ 'url' ] = oo00O0oO0O0
  iIII [ 'fanart' ] = oOooOOOoOo
  if 7 - 7: I11iii11IIi + iIiiiI1IiI1I1 . O00ooooo00
 if os . path . exists ( iiIIIII1i1iI ) == False :
  Ooo0 = [ ]
  Ooo0 . append ( iIII )
  i1I1I = open ( iiIIIII1i1iI , "w" )
  i1I1I . write ( json . dumps ( Ooo0 ) )
  i1I1I . close ( )
 else :
  o0OOo0o0O0O = json . loads ( open ( iiIIIII1i1iI , "r" ) . read ( ) )
  o0OOo0o0O0O . append ( iIII )
  i1I1I = open ( iiIIIII1i1iI , "w" )
  i1I1I . write ( json . dumps ( o0OOo0o0O0O ) )
  i1I1I . close ( )
 I1IiI . setSetting ( 'new_url_source' , "" )
 I1IiI . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(Supremacy,New source added.,5000," + O0oo0OO0 + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : I1IiI . openSettings ( )
 if 34 - 34: IIiIiII11i % OOooO + IiIi11i * IIii1I
 if 33 - 33: IIiIiII11i / IiIi11i * oOOOo0o0O / OOO0O + IiIIi1I1Iiii / OOooO
def iII1I1I1 ( name ) :
 o0OOo0o0O0O = json . loads ( open ( iiIIIII1i1iI , "r" ) . read ( ) )
 for i11IIIiI11 in range ( len ( o0OOo0o0O0O ) ) :
  if isinstance ( o0OOo0o0O0O [ i11IIIiI11 ] , list ) :
   if o0OOo0o0O0O [ i11IIIiI11 ] [ 0 ] == name :
    del o0OOo0o0O0O [ i11IIIiI11 ]
    i1I1I = open ( iiIIIII1i1iI , "w" )
    i1I1I . write ( json . dumps ( o0OOo0o0O0O ) )
    i1I1I . close ( )
    break
  else :
   if o0OOo0o0O0O [ i11IIIiI11 ] [ 'title' ] == name :
    del o0OOo0o0O0O [ i11IIIiI11 ]
    i1I1I = open ( iiIIIII1i1iI , "w" )
    i1I1I . write ( json . dumps ( o0OOo0o0O0O ) )
    i1I1I . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 8 - 8: Ooo00oOo00o + o00ooooO0oO - o0ooo % IiIIi1I1Iiii % o0ooo * I1ii
 if 9 - 9: IiIIi1I1Iiii - i11iIiiIii - oOOOo0o0O * oOOoo + IiIi11i
 if 44 - 44: iIiiiI1IiI1I1
def OOOO0OOO ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
 o0O = BeautifulSoup ( o0O0 ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for O0O0o0oOOO in o0O ( 'a' ) :
  o00oO0oo0OO = O0O0o0oOOO [ 'href' ]
  if not o00oO0oo0OO . startswith ( '?' ) :
   IIIII = O0O0o0oOOO . string
   if IIIII not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if o00oO0oo0OO . endswith ( '/' ) :
     if browse :
      ooOoOoo0O ( IIIII , url + o00oO0oo0OO , 15 , O0oo0OO0 , oOooOOOoOo , '' , '' , '' )
     else :
      ooOoOoo0O ( IIIII , url + o00oO0oo0OO , 14 , O0oo0OO0 , oOooOOOoOo , '' , '' , '' )
    elif o00oO0oo0OO . endswith ( '.xml' ) :
     if browse :
      ooOoOoo0O ( IIIII , url + o00oO0oo0OO , 1 , O0oo0OO0 , oOooOOOoOo , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( iiIIIII1i1iI ) == True :
       if IIIII in i1 :
        ooOoOoo0O ( IIIII + ' (in use)' , url + o00oO0oo0OO , 11 , O0oo0OO0 , oOooOOOoOo , '' , '' , '' , '' , 'download' )
       else :
        ooOoOoo0O ( IIIII , url + o00oO0oo0OO , 11 , O0oo0OO0 , oOooOOOoOo , '' , '' , '' , '' , 'download' )
      else :
       ooOoOoo0O ( IIIII , url + o00oO0oo0OO , 11 , O0oo0OO0 , oOooOOOoOo , '' , '' , '' , '' , 'download' )
       if 3 - 3: Ooo00oOo00o
       if 97 - 97: o00ooooO0oO
def iiIII1i ( browse = False ) :
 O0O = 'http://community-links.googlecode.com/svn/trunk/'
 o0O = BeautifulSoup ( o0O0 ( O0O ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 I1I = o0O ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for O0O0o0oOOO in I1I :
  IIIII = O0O0o0oOOO ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   ooOoOoo0O ( IIIII , O0O + IIIII , 1 , O0oo0OO0 , oOooOOOoOo , '' , '' , '' , '' , 'download' )
  else :
   ooOoOoo0O ( IIIII , O0O + IIIII , 11 , O0oo0OO0 , oOooOOOoOo , '' , '' , '' , '' , 'download' )
   if 68 - 68: IiIi11i
   if 25 - 25: OOO0O . IiIi11i
def OoooO ( url , data = None ) :
 print 'getsoup' , url , data
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  data = o0O0 ( url )
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   print 'found m3u data' , data
   return data
   if 24 - 24: I1ii / i11iIiiIii + I1ii
 elif data == None :
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    I1i11i = xbmcvfs . copy ( url , os . path . join ( iIiiiI , 'temp' , 'sorce_temp.txt' ) )
    if I1i11i :
     data = open ( os . path . join ( iIiiiI , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( iIiiiI , 'temp' , 'sorce_temp.txt' ) )
    else :
     O00o0o0000o0o ( "failed to copy from smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     print 'found m3u data' , data
     return data
  else :
   O00o0o0000o0o ( "Soup Data not found!" )
   return
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 11 - 11: IIiIiII11i / iIiiiI1IiI1I1 + o0ooo * OOO0O - OOO0O - IIiIiII11i
 if 85 - 85: OoOoo0 % I1ii / IIii1I . IIii1I
def Oooo ( url , fanart ) :
 print 'url-getData' , url
 iIIiIiI1I1 = "List"
 if 56 - 56: IIiIiII11i . OOO0O0O0ooooo + IiIIi1I1Iiii
 o0O = OoooO ( url )
 if 1 - 1: OOooO
 if isinstance ( o0O , BeautifulSOAP ) :
  if len ( o0O ( 'layoutype' ) ) > 0 :
   iIIiIiI1I1 = "Thumbnail"
   if 97 - 97: oOOOo0o0O + OOooO + OOO0O0O0ooooo + i11iIiiIii
  if len ( o0O ( 'channels' ) ) > 0 :
   oOoO0 = o0O ( 'channel' )
   for Oo0 in oOoO0 :
    if 83 - 83: i11iIiiIii % o0ooo % IiIi11i
    if 11 - 11: iIiiiI1IiI1I1 % Ooo00oOo00o * OOooO + IiIi11i + oOOoo
    II1Iiiiii = ''
    ii1ii111 = 0
    try :
     II1Iiiiii = Oo0 ( 'externallink' ) [ 0 ] . string
     ii1ii111 = len ( Oo0 ( 'externallink' ) )
    except : pass
    if 10 - 10: o00ooooO0oO % ooO00oo * ooO00oo . OoOoo0 / oOOoo % oOOOo0o0O
    if ii1ii111 > 1 : II1Iiiiii = ''
    if 49 - 49: Ooo00oOo00o / I1ii + OOO0O0O0ooooo * o0ooo
    IIIII = Oo0 ( 'name' ) [ 0 ] . string
    I1ii11 = Oo0 ( 'thumbnail' ) [ 0 ] . string
    if I1ii11 == None :
     I1ii11 = ''
     if 74 - 74: IiIIi1I1Iiii - o0ooo . O00ooooo00
    try :
     if not Oo0 ( 'fanart' ) :
      if I1IiI . getSetting ( 'use_thumb' ) == "true" :
       i1III = I1ii11
      else :
       i1III = fanart
     else :
      i1III = Oo0 ( 'fanart' ) [ 0 ] . string
     if i1III == None :
      raise
    except :
     i1III = fanart
     if 49 - 49: i11iIiiIii % oOOoo . I11iii11IIi
    try :
     oo0O0 = Oo0 ( 'info' ) [ 0 ] . string
     if oo0O0 == None :
      raise
    except :
     oo0O0 = ''
     if 13 - 13: i11iIiiIii + O00ooooo00 * IIii1I % II1 - iIiiiI1IiI1I1 * oOOOo0o0O
    try :
     OoOOoooOO0O = Oo0 ( 'genre' ) [ 0 ] . string
     if OoOOoooOO0O == None :
      raise
    except :
     OoOOoooOO0O = ''
     if 26 - 26: II1 * IIiIiII11i + oOOOo0o0O
    try :
     iI1i11 = Oo0 ( 'date' ) [ 0 ] . string
     if iI1i11 == None :
      raise
    except :
     iI1i11 = ''
     if 24 - 24: i11iIiiIii % IIii1I + oOOOo0o0O / i11iIiiIii
    try :
     credits = Oo0 ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 70 - 70: Ooo00oOo00o * OOO0O0O0ooooo . OoOoo0 + IIiIiII11i . ooO00oo
    try :
     if II1Iiiiii == '' :
      ooOoOoo0O ( IIIII . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , I1ii11 , i1III , oo0O0 , OoOOoooOO0O , iI1i11 , credits , True )
     else :
      if 14 - 14: IIii1I % IIii1I * i11iIiiIii - Ooo00oOo00o - OoOoo0
      ooOoOoo0O ( IIIII . encode ( 'utf-8' ) , II1Iiiiii . encode ( 'utf-8' ) , 1 , I1ii11 , i1III , oo0O0 , OoOOoooOO0O , iI1i11 , None , 'source' )
    except :
     O00o0o0000o0o ( 'There was a problem adding directory from getData(): ' + IIIII . encode ( 'utf-8' , 'ignore' ) )
  else :
   O00o0o0000o0o ( 'No Channels: getItems' )
   o00oo0 ( o0O ( 'item' ) , fanart )
 else :
  oooooOOO000Oo ( o0O )
  if 52 - 52: iIiiiI1IiI1I1 % ooO00oo . I11iii11IIi * IIii1I
 if iIIiIiI1I1 == "Thumbnail" :
  I111i1II ( )
  if 69 - 69: oOOoo * OOO0O0O0ooooo . i11iIiiIii / oOOoo . o0ooo
  if 63 - 63: OoOoo0 + o0ooo . iIiiiI1IiI1I1 - IIiIiII11i
  if 52 - 52: o0ooo % IiIIi1I1Iiii
  if 64 - 64: OOO0O0O0ooooo % OoOoo0 % OOO0O0O0ooooo * Ooo00oOo00o . I1ii + IIiIiII11i
  if 75 - 75: OoOoo0 . II1 % o0ooo * OoOoo0 % II1
def oooooOOO000Oo ( data ) :
 I11i1iIiIIIIIii = data . rstrip ( )
 o0 = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)' ) . findall ( I11i1iIiIIIIIii )
 OOo0 = len ( o0 )
 print 'total m3u links' , OOo0
 for ii11I1 , oO0oo , Ii111iIi1iIi in o0 :
  if 'tvg-logo' in ii11I1 :
   I1ii11 = IIIIIo0ooOoO000oO ( ii11I1 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if I1ii11 :
    if I1ii11 . startswith ( 'http' ) :
     I1ii11 = I1ii11
     if 85 - 85: o0ooo . I11iii11IIi / IiIi11i . OOO0O0O0ooooo % o00ooooO0oO
    elif not I1IiI . getSetting ( 'logo-folderPath' ) == "" :
     OO0ooo0oOO = I1IiI . getSetting ( 'logo-folderPath' )
     I1ii11 = OO0ooo0oOO + I1ii11
     if 97 - 97: IIiIiII11i / OOooO
    else :
     I1ii11 = I1ii11
     if 71 - 71: iIiiiI1IiI1I1 / O00ooooo00 . OOO0O % II1 . I11iii11IIi
     if 41 - 41: O00ooooo00 * iIiiiI1IiI1I1 / II1 . oOOOo0o0O
  else :
   I1ii11 = ''
  if 'type' in ii11I1 :
   O0iII1 = IIIIIo0ooOoO000oO ( ii11I1 , 'type=[\'"](.*?)[\'"]' )
   if O0iII1 == 'yt-dl' :
    Ii111iIi1iIi = Ii111iIi1iIi + "&mode=18"
   elif O0iII1 == 'regex' :
    O0O = Ii111iIi1iIi . split ( '&regexs=' )
    if 27 - 27: Ooo00oOo00o . OoOoo0 + I11iii11IIi / IIii1I % OOooO . IiIi11i
    IIIIi1 = iIi11iiIiI1I ( OoooO ( '' , data = O0O [ 1 ] ) )
    if 3 - 3: O00ooooo00 / iIiiiI1IiI1I1 / i11iIiiIii * O00ooooo00 - iIiiiI1IiI1I1
    IIIii1II1II ( O0O [ 0 ] , oO0oo , I1ii11 , '' , '' , '' , '' , '' , None , IIIIi1 , OOo0 )
    continue
  IIIii1II1II ( Ii111iIi1iIi , oO0oo , I1ii11 , '' , '' , '' , '' , '' , None , '' , OOo0 )
  if 42 - 42: iIiiiI1IiI1I1 . II1 . o0ooo * I1ii
 xbmc . executebuiltin ( "Container.SetViewMode(50)" )
 if 81 - 81: oOOoo * o0ooo + o00ooooO0oO + IiIIi1I1Iiii - II1
def i1i1I111iIi1 ( name , url , fanart ) :
 o0O = OoooO ( url )
 oo00O00oO000o = o0O . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 OOo00OoO = oo00O00oO000o ( 'item' )
 try :
  i1III = oo00O00oO000o ( 'fanart' ) [ 0 ] . string
  if i1III == None :
   raise
 except :
  i1III = fanart
 for Oo0 in oo00O00oO000o ( 'subchannel' ) :
  name = Oo0 ( 'name' ) [ 0 ] . string
  try :
   I1ii11 = Oo0 ( 'thumbnail' ) [ 0 ] . string
   if I1ii11 == None :
    raise
  except :
   I1ii11 = ''
  try :
   if not Oo0 ( 'fanart' ) :
    if I1IiI . getSetting ( 'use_thumb' ) == "true" :
     i1III = I1ii11
   else :
    i1III = Oo0 ( 'fanart' ) [ 0 ] . string
   if i1III == None :
    raise
  except :
   pass
  try :
   oo0O0 = Oo0 ( 'info' ) [ 0 ] . string
   if oo0O0 == None :
    raise
  except :
   oo0O0 = ''
   if 10 - 10: o0ooo / i11iIiiIii
  try :
   OoOOoooOO0O = Oo0 ( 'genre' ) [ 0 ] . string
   if OoOOoooOO0O == None :
    raise
  except :
   OoOOoooOO0O = ''
   if 92 - 92: OoOoo0 . o00ooooO0oO
  try :
   iI1i11 = Oo0 ( 'date' ) [ 0 ] . string
   if iI1i11 == None :
    raise
  except :
   iI1i11 = ''
   if 85 - 85: OOO0O . o00ooooO0oO
  try :
   credits = Oo0 ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 78 - 78: IiIi11i * o00ooooO0oO + IIii1I + IIii1I / o00ooooO0oO . oOOoo
  try :
   ooOoOoo0O ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , I1ii11 , i1III , oo0O0 , OoOOoooOO0O , credits , iI1i11 )
  except :
   O00o0o0000o0o ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 o00oo0 ( OOo00OoO , i1III )
 if 97 - 97: IiIi11i / o00ooooO0oO % O00ooooo00 % OOO0O
 if 18 - 18: IIii1I % OoOoo0
def O00oO0 ( name , url , fanart ) :
 o0O = OoooO ( url )
 oo00O00oO000o = o0O . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 OOo00OoO = oo00O00oO000o ( 'subitem' )
 o00oo0 ( OOo00OoO , fanart )
 if 97 - 97: o00ooooO0oO - IIii1I
 if 75 - 75: II1 * ooO00oo
def I1Iiiiiii ( name , url , iconimage , fanart ) :
 oo0OooOOo0 = [ ] ; I1IIIiI1I1ii1 = [ ] ; iiiI1I1iIIIi1 = 0
 Iii = I1iiiiI1iI ( url , 'sublink:' , '#' )
 for O0oo00o0O in Iii :
  if 'LISTSOURCE:' in O0oo00o0O :
   iIiiiii1i = iiIi1IIiI ( O0oo00o0O , 'LISTSOURCE:' , '::' )
   i1oO0OO0 = iiIi1IIiI ( O0oo00o0O , 'LISTNAME:' , '::' )
  else :
   iIiiiii1i = O0oo00o0O . replace ( 'sublink:' , '' ) . replace ( '#' , '' )
   i1oO0OO0 = name
  if len ( iIiiiii1i ) > 10 :
   iiiI1I1iIIIi1 = iiiI1I1iIIIi1 + 1 ; oo0OooOOo0 . append ( i1oO0OO0 ) ; I1IIIiI1I1ii1 . append ( iIiiiii1i )
   if 82 - 82: ooO00oo - ooO00oo + I11iii11IIi
 if iiiI1I1iIIIi1 == 1 :
  try :
   if 8 - 8: o0ooo % OOooO * I1ii % oOOoo . IiIi11i / IiIi11i
   o0O0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
   OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1IIIiI1I1ii1 [ 0 ] , listitem = o0O0O0o )
   xbmc . Player ( ) . play ( ooO000 ( I1IIIiI1I1ii1 [ 0 ] ) , o0O0O0o )
  except :
   pass
 else :
  oOOOO = xbmcgui . Dialog ( )
  Ii = oOOOO . select ( 'Supremacy Select A Source' , oo0OooOOo0 )
  if Ii >= 0 :
   Ii1ii111i1 = name
   i1i1i1I = str ( I1IIIiI1I1ii1 [ Ii ] )
   if 83 - 83: I1ii + II1
   try :
    o0O0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
    OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1i1I , listitem = o0O0O0o )
    xbmc . Player ( ) . play ( ooO000 ( i1i1i1I ) , o0O0O0o )
   except :
    pass
    if 22 - 22: oOOoo % OOooO * II1 - o0ooo / IIii1I
    if 86 - 86: II1 . OOooO % I11iii11IIi / OoOoo0 * OOooO / o0ooo
def oO ( ) :
 if 60 - 60: OOO0O * IIiIiII11i
 I1iIiI11I1 = 'Name of channel show or movie'
 i1oOOoo0o0OOOO = ''
 ii111I = xbmc . Keyboard ( i1oOOoo0o0OOOO , I1iIiI11I1 )
 ii111I . doModal ( )
 if ii111I . isConfirmed ( ) :
  i1oOOoo0o0OOOO = ii111I . getText ( ) . replace ( '\n' , '' ) . strip ( )
  if len ( i1oOOoo0o0OOOO ) == 0 :
   xbmcgui . Dialog ( ) . ok ( 'RobinHood' , 'Nothing Entered' )
   return
   if 26 - 26: OOooO % IIii1I + o0ooo
 i1oOOoo0o0OOOO = i1oOOoo0o0OOOO . lower ( )
 oo0OooOOo0 = [ ]
 oo0OooOOo0 . append ( _Edit . MainBase )
 OOOooo = 0
 Oo00oo0000OO = 1
 O0oOOo0Oo = 0
 o000O000 = 0
 ii1 = xbmcgui . DialogProgress ( )
 ii1 . create ( 'Supremacy Searching Please wait' , ' ' )
 if 77 - 77: IIiIiII11i % OOO0O0O0ooooo
 while Oo00oo0000OO <> O0oOOo0Oo :
  I1iii = oo0OooOOo0 [ O0oOOo0Oo ] . strip ( )
  print 'read this one from file list (' + str ( O0oOOo0Oo ) + ')'
  O0oOOo0Oo = O0oOOo0Oo + 1
  if 86 - 86: OOO0O * OOO0O0O0ooooo * ooO00oo
  Ooo0oo = ''
  try :
   Ooo0oo = net . http_GET ( I1iii ) . content
   Ooo0oo = Ooo0oo . encode ( 'ascii' , 'ignore' ) . decode ( 'ascii' )
   if 41 - 41: I11iii11IIi * OoOoo0 / I11iii11IIi % I1ii
  except :
   pass
   if 18 - 18: iIiiiI1IiI1I1 . II1 % I11iii11IIi % oOOoo
  if len ( Ooo0oo ) < 10 :
   Ooo0oo = ''
   OOOooo = OOOooo + 1
   print '*** PASSED ****' + I1iii + '  ************* Total Passed Urls: ' + str ( OOOooo )
   time . sleep ( .5 )
   if 9 - 9: Ooo00oOo00o - IiIIi1I1Iiii * II1 . IiIIi1I1Iiii
  ii1Ii1IiIIi = int ( ( O0oOOo0Oo / 300 ) * 100 )
  o0OO0 = '     Pages Read: ' + str ( O0oOOo0Oo ) + '        Matches Found: ' + str ( o000O000 )
  ii1 . update ( ii1Ii1IiIIi , "" , o0OO0 , "" )
  if 100 - 100: IiIIi1I1Iiii * o00ooooO0oO / o00ooooO0oO
  if ii1 . iscanceled ( ) :
   return
   if 41 - 41: IIii1I % OoOoo0
  if len ( Ooo0oo ) > 10 :
   oOo0oO = I1iiiiI1iI ( Ooo0oo , '<channel>' , '</channel>' )
   for O0oo00o0O in oOo0oO :
    iIiiiii1i = iiIi1IIiI ( O0oo00o0O , '<externallink>' , '</externallink>' )
    if 5 - 5: oOOOo0o0O - oOOOo0o0O . IiIIi1I1Iiii + I11iii11IIi - oOOOo0o0O . I1ii
    if 31 - 31: iIiiiI1IiI1I1 - IIii1I - IIii1I % OoOoo0
    if len ( iIiiiii1i ) > 5 :
     Oo00oo0000OO = Oo00oo0000OO + 1
     oo0OooOOo0 . append ( iIiiiii1i )
     if 12 - 12: IIii1I
     if 20 - 20: o0ooo / O00ooooo00
   oOIi111 = I1iiiiI1iI ( Ooo0oo , '<item>' , '</item>' )
   for O0oo00o0O in oOIi111 :
    iIiiiii1i = iiIi1IIiI ( O0oo00o0O , '<link>' , '</link>' )
    IIIII = iiIi1IIiI ( O0oo00o0O , '<title>' , '</title>' )
    oO0i1iI = '  ' + IIIII . lower ( ) + '  '
    if 10 - 10: iIiiiI1IiI1I1 . OOooO
    if len ( iIiiiii1i ) > 5 and oO0i1iI . find ( i1oOOoo0o0OOOO ) > 0 :
     o000O000 = o000O000 + 1
     oOooOOOoOo = ''
     I1ii11 = iiIi1IIiI ( O0oo00o0O , '<thumbnail>' , '</thumbnail>' )
     oOooOOOoOo = iiIi1IIiI ( O0oo00o0O , '<fanart>' , '</fanart>' )
     if len ( oOooOOOoOo ) < 5 :
      oOooOOOoOo = O0oo0OO0
     if iIiiiii1i . find ( 'sublink' ) > 0 :
      ooOoOoo0O ( IIIII , iIiiiii1i , 30 , I1ii11 , oOooOOOoOo , '' , '' , '' , '' )
     else :
      IIIii1II1II ( str ( iIiiiii1i ) , IIIII , I1ii11 , oOooOOOoOo , '' , '' , '' , True , None , '' , 1 )
      if 32 - 32: oOOoo . ooO00oo . II1 - Ooo00oOo00o + I1ii
      if 88 - 88: OOooO
 ii1 . close ( )
 xbmc . executebuiltin ( "Container.SetViewMode(50)" )
 if 19 - 19: iIiiiI1IiI1I1 * ooO00oo + oOOoo
def O0o ( data , Searchkey ) :
 I11i1iIiIIIIIii = data . rstrip ( )
 o0 = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\n]+)' ) . findall ( I11i1iIiIIIIIii )
 OOo0 = len ( o0 )
 print 'total m3u links' , OOo0
 for ii11I1 , oO0oo , Ii111iIi1iIi in o0 :
  if 'tvg-logo' in ii11I1 :
   I1ii11 = IIIIIo0ooOoO000oO ( ii11I1 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if I1ii11 :
    if I1ii11 . startswith ( 'http' ) :
     I1ii11 = I1ii11
     if 95 - 95: Ooo00oOo00o
    elif not I1IiI . getSetting ( 'logo-folderPath' ) == "" :
     OO0ooo0oOO = I1IiI . getSetting ( 'logo-folderPath' )
     I1ii11 = OO0ooo0oOO + I1ii11
     if 60 - 60: II1 % IiIIi1I1Iiii + oOOOo0o0O . IiIi11i * IIii1I
    else :
     I1ii11 = I1ii11
     if 93 - 93: Ooo00oOo00o
     if 5 - 5: OoOoo0 / oOOOo0o0O
  else :
   I1ii11 = ''
  if 'type' in ii11I1 :
   O0iII1 = IIIIIo0ooOoO000oO ( ii11I1 , 'type=[\'"](.*?)[\'"]' )
   if O0iII1 == 'yt-dl' :
    Ii111iIi1iIi = Ii111iIi1iIi + "&mode=18"
   elif O0iII1 == 'regex' :
    O0O = Ii111iIi1iIi . split ( '&regexs=' )
    if 77 - 77: IiIi11i - IIiIiII11i % OoOoo0 - OOO0O0O0ooooo
    IIIIi1 = iIi11iiIiI1I ( OoooO ( '' , data = O0O [ 1 ] ) )
    if 67 - 67: oOOOo0o0O + IiIIi1I1Iiii
    IIIii1II1II ( O0O [ 0 ] , oO0oo , I1ii11 , '' , '' , '' , '' , '' , None , IIIIi1 , OOo0 )
    continue
  IIIii1II1II ( Ii111iIi1iIi , oO0oo , I1ii11 , '' , '' , '' , '' , '' , None , '' , OOo0 )
  if 84 - 84: OOO0O0O0ooooo * II1 - ooO00oo * ooO00oo
def i1ii ( text , pattern ) :
 oO0O = ""
 try :
  oOO = re . findall ( pattern , text , flags = re . DOTALL )
  oO0O = oOO [ 0 ]
 except :
  oO0O = ""
  if 11 - 11: i11iIiiIii - I1ii . I1ii
 return oO0O
 if 31 - 31: oOOOo0o0O / IiIIi1I1Iiii * O00ooooo00 . I11iii11IIi
def I1iiiiI1iI ( text , start_with , end_with ) :
 OO0o0oO = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return OO0o0oO
 if 83 - 83: o0ooo / i11iIiiIii % IIii1I . OoOoo0 % I1ii . II1
def iiIi1IIiI ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : OO0o0oO = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : OO0o0oO = ''
 else :
  try : OO0o0oO = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : OO0o0oO = ''
 return OO0o0oO
 if 94 - 94: oOOoo + IIii1I % Ooo00oOo00o
def o00oo0 ( items , fanart ) :
 OOo0 = len ( items )
 print 'START GET ITEMS *****'
 O00o0o0000o0o ( 'Total Items: %s' % OOo0 )
 for O0OO0oOOo in items :
  OO0oO0o = False
  III111i11IiI = False
  try :
   IIIII = O0OO0oOOo ( 'title' ) [ 0 ] . string
   if IIIII is None :
    IIIII = 'unknown?'
  except :
   O00o0o0000o0o ( 'Name Error' )
   IIIII = ''
   if 71 - 71: OoOoo0 / OoOoo0 * I1ii * I1ii / iIiiiI1IiI1I1
   if 35 - 35: oOOOo0o0O * o0ooo * IIiIiII11i % IiIIi1I1Iiii . I11iii11IIi
  try :
   if O0OO0oOOo ( 'epg' ) :
    if O0OO0oOOo . epg_url :
     O00o0o0000o0o ( 'Get EPG Regex' )
     O00o00O = O0OO0oOOo . epg_url . string
     ii1iii11i1 = O0OO0oOOo . epg_regex . string
     I11 = Oo00oO0O ( O00o00O , ii1iii11i1 )
     if I11 :
      IIIII += ' - ' + I11
    elif O0OO0oOOo ( 'epg' ) [ 0 ] . string > 1 :
     IIIII += OOooOO00O0OO00oo ( O0OO0oOOo ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   O00o0o0000o0o ( 'EPG Error' )
  try :
   O0O = [ ]
   if len ( O0OO0oOOo ( 'link' ) ) > 0 :
    if 69 - 69: o0ooo / IiIIi1I1Iiii
    for O0O0o0oOOO in O0OO0oOOo ( 'link' ) :
     if not O0O0o0oOOO . string == None :
      O0O . append ( O0O0o0oOOO . string )
      if 43 - 43: OOO0O . IIiIiII11i / II1 % II1
   elif len ( O0OO0oOOo ( 'sportsdevil' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'sportsdevil' ) :
     if not O0O0o0oOOO . string == None :
      iIIIII1iiiiII = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + O0O0o0oOOO . string
      oooO = O0OO0oOOo ( 'referer' ) [ 0 ] . string
      if oooO :
       if 22 - 22: IiIi11i - IiIi11i % oOOOo0o0O . o00ooooO0oO + I1ii
       iIIIII1iiiiII = iIIIII1iiiiII + '%26referer=' + oooO
      O0O . append ( iIIIII1iiiiII )
   elif len ( O0OO0oOOo ( 'p2p' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'p2p' ) :
     if not O0O0o0oOOO . string == None :
      if 'sop://' in O0O0o0oOOO :
       Oo00OOo00O = 'plugin://plugin.video.p2p-streams/?url=' + O0O0o0oOOO . string + '&amp;mode=2&amp;' + 'name=' + IIIII
       O0O . append ( Oo00OOo00O )
      else :
       o0Ii1Iii111IiI1 = 'plugin://plugin.video.p2p-streams/?url=' + O0O0o0oOOO . string + '&amp;mode=1&amp;' + 'name=' + IIIII
       O0O . append ( o0Ii1Iii111IiI1 )
   elif len ( O0OO0oOOo ( 'vaughn' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'vaughn' ) :
     if not O0O0o0oOOO . string == None :
      O00oOooo0 = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + O0O0o0oOOO . string
      O0O . append ( O00oOooo0 )
   elif len ( O0OO0oOOo ( 'ilive' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'ilive' ) :
     if not O0O0o0oOOO . string == None :
      if not 'http' in O0O0o0oOOO . string :
       OoOO = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + O0O0o0oOOO . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       OoOO = 'plugin://plugin.video.tbh.ilive/?url=' + O0O0o0oOOO . string + '&amp;link=99&amp;mode=iLivePlay'
   elif len ( O0OO0oOOo ( 'yt-dl' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'yt-dl' ) :
     if not O0O0o0oOOO . string == None :
      iIII1I1i1i = O0O0o0oOOO . string + '&mode=18'
      O0O . append ( iIII1I1i1i )
   elif len ( O0OO0oOOo ( 'utube' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'utube' ) :
     if not O0O0o0oOOO . string == None :
      if len ( O0O0o0oOOO . string ) == 11 :
       o0OIIiI1I1 = 'plugin://plugin.video.youtube/play/?video_id=' + O0O0o0oOOO . string
      elif O0O0o0oOOO . string . startswith ( 'PL' ) and not '&order=' in O0O0o0oOOO . string :
       o0OIIiI1I1 = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + O0O0o0oOOO . string
      else :
       o0OIIiI1I1 = 'plugin://plugin.video.youtube/play/?playlist_id=' + O0O0o0oOOO . string
    O0O . append ( o0OIIiI1I1 )
   elif len ( O0OO0oOOo ( 'imdb' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'imdb' ) :
     if not O0O0o0oOOO . string == None :
      if I1IiI . getSetting ( 'genesisorpulsar' ) == '0' :
       I11I1IIiiII1 = 'plugin://plugin.video.genesis/?action=play&imdb=' + O0O0o0oOOO . string
      else :
       I11I1IIiiII1 = 'plugin://plugin.video.pulsar/movie/tt' + O0O0o0oOOO . string + '/play'
      O0O . append ( I11I1IIiiII1 )
   elif len ( O0OO0oOOo ( 'f4m' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'f4m' ) :
     if not O0O0o0oOOO . string == None :
      if '.f4m' in O0O0o0oOOO . string :
       IIIIIii1ii11 = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( O0O0o0oOOO . string )
      elif '.m3u8' in O0O0o0oOOO . string :
       IIIIIii1ii11 = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( O0O0o0oOOO . string ) + '&amp;streamtype=HLS'
       if 86 - 86: I11iii11IIi * iIiiiI1IiI1I1 - OOO0O0O0ooooo . I11iii11IIi % IIii1I / oOOOo0o0O
      else :
       IIIIIii1ii11 = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( O0O0o0oOOO . string ) + '&amp;streamtype=SIMPLE'
    O0O . append ( IIIIIii1ii11 )
   elif len ( O0OO0oOOo ( 'ftv' ) ) > 0 :
    for O0O0o0oOOO in O0OO0oOOo ( 'ftv' ) :
     if not O0O0o0oOOO . string == None :
      IiIIiIIIiIii = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( IIIII ) + '&url=' + O0O0o0oOOO . string + '&mode=125&ch_fanart=na'
     O0O . append ( IiIIiIIIiIii )
   if len ( O0O ) < 1 :
    raise
  except :
   O00o0o0000o0o ( 'Error <link> element, Passing:' + IIIII . encode ( 'utf-8' , 'ignore' ) )
   continue
   if 23 - 23: OOooO + OoOoo0 . I11iii11IIi * IIiIiII11i + OOO0O
  OO0oO0o = False
  if 18 - 18: ooO00oo * o0ooo . ooO00oo / OOO0O0O0ooooo
  try :
   OO0oO0o = O0OO0oOOo ( 'externallink' ) [ 0 ] . string
  except : pass
  if 8 - 8: o0ooo
  if OO0oO0o :
   II1II1 = [ OO0oO0o ]
   OO0oO0o = True
  else :
   OO0oO0o = False
  try :
   III111i11IiI = O0OO0oOOo ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if III111i11IiI :
   II1II1 = [ III111i11IiI ]
   III111i11IiI = True
  else :
   III111i11IiI = False
  try :
   I1ii11 = O0OO0oOOo ( 'thumbnail' ) [ 0 ] . string
   if I1ii11 == None :
    raise
  except :
   I1ii11 = ''
  try :
   if not O0OO0oOOo ( 'fanart' ) :
    if I1IiI . getSetting ( 'use_thumb' ) == "true" :
     i1III = I1ii11
    else :
     i1III = fanart
   else :
    i1III = O0OO0oOOo ( 'fanart' ) [ 0 ] . string
   if i1III == None :
    raise
  except :
   i1III = fanart
  try :
   oo0O0 = O0OO0oOOo ( 'info' ) [ 0 ] . string
   if oo0O0 == None :
    raise
  except :
   oo0O0 = ''
   if 48 - 48: O00ooooo00 + OoOoo0 % I11iii11IIi / IiIIi1I1Iiii - o0ooo
  try :
   OoOOoooOO0O = O0OO0oOOo ( 'genre' ) [ 0 ] . string
   if OoOOoooOO0O == None :
    raise
  except :
   OoOOoooOO0O = ''
   if 67 - 67: I1ii % o0ooo . II1 + oOOOo0o0O * OoOoo0 * I11iii11IIi
  try :
   iI1i11 = O0OO0oOOo ( 'date' ) [ 0 ] . string
   if iI1i11 == None :
    raise
  except :
   iI1i11 = ''
   if 36 - 36: OOO0O0O0ooooo + IiIIi1I1Iiii
  IIIIi1 = None
  if O0OO0oOOo ( 'regex' ) :
   try :
    iIIIi1i1I11i = O0OO0oOOo ( 'regex' )
    IIIIi1 = iIi11iiIiI1I ( iIIIi1i1I11i )
   except :
    pass
    if 55 - 55: IiIIi1I1Iiii - oOOOo0o0O
  try :
   if len ( O0O ) > 1 :
    if 84 - 84: o00ooooO0oO + IiIIi1I1Iiii - I11iii11IIi * I11iii11IIi
    i1i = 0
    OoooO0o = [ ]
    for O0O0o0oOOO in O0O :
     if I1IiI . getSetting ( 'ask_playlist_items' ) == 'true' :
      if IIIIi1 :
       OoooO0o . append ( O0O0o0oOOO + '&regexs=' + IIIIi1 )
      elif any ( x in O0O0o0oOOO for x in OO0o ) and O0O0o0oOOO . startswith ( 'http' ) :
       OoooO0o . append ( O0O0o0oOOO + '&mode=19' )
     else :
      OoooO0o . append ( O0O0o0oOOO )
    if I1IiI . getSetting ( 'add_playlist' ) == "false" :
     for O0O0o0oOOO in O0O :
      i1i += 1
      print 'ADDLINK 1'
      IIIii1II1II ( O0O0o0oOOO , '%s) %s' % ( i1i , IIIII . encode ( 'utf-8' , 'ignore' ) ) , I1ii11 , i1III , oo0O0 , OoOOoooOO0O , iI1i11 , True , OoooO0o , IIIIi1 , OOo0 )
    else :
     IIIii1II1II ( '' , IIIII . encode ( 'utf-8' , 'ignore' ) , I1ii11 , i1III , oo0O0 , OoOOoooOO0O , iI1i11 , True , OoooO0o , IIIIi1 , OOo0 )
   else :
    if OO0oO0o :
     ooOoOoo0O ( IIIII . encode ( 'utf-8' ) , II1II1 [ 0 ] . encode ( 'utf-8' ) , 1 , I1ii11 , fanart , oo0O0 , OoOOoooOO0O , iI1i11 , None , 'source' )
    elif III111i11IiI :
     ooOoOoo0O ( IIIII . encode ( 'utf-8' ) , II1II1 [ 0 ] , 53 , I1ii11 , fanart , oo0O0 , OoOOoooOO0O , iI1i11 , None , 'source' )
    elif O0O [ 0 ] . find ( 'sublink' ) > 0 :
     ooOoOoo0O ( IIIII . encode ( 'utf-8' ) , O0O [ 0 ] , 30 , I1ii11 , fanart , '' , '' , '' , '' )
     if 24 - 24: I11iii11IIi % O00ooooo00 + OOooO . i11iIiiIii . OOO0O
    else :
     IIIii1II1II ( O0O [ 0 ] , IIIII . encode ( 'utf-8' , 'ignore' ) , I1ii11 , i1III , oo0O0 , OoOOoooOO0O , iI1i11 , True , None , IIIIi1 , OOo0 )
     if 17 - 17: OOO0O . iIiiiI1IiI1I1 . IiIi11i / OOO0O
     if 57 - 57: OoOoo0
  except :
   O00o0o0000o0o ( 'There was a problem adding item - ' + IIIII . encode ( 'utf-8' , 'ignore' ) )
 print 'FINISH GET ITEMS *****'
 if 67 - 67: Ooo00oOo00o . IiIi11i
def iIi11iiIiI1I ( reg_item ) :
 try :
  IIIIi1 = { }
  for O0O0o0oOOO in reg_item :
   IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] = { }
   if 87 - 87: I1ii % oOOoo
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'expre' ] = O0O0o0oOOO ( 'expres' ) [ 0 ] . string
    if not IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'expre' ] :
     IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'expre' ] = ''
   except :
    O00o0o0000o0o ( "Regex: -- No Referer --" )
   IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'page' ] = O0O0o0oOOO ( 'page' ) [ 0 ] . string
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'refer' ] = O0O0o0oOOO ( 'referer' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No Referer --" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'connection' ] = O0O0o0oOOO ( 'connection' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No connection --" )
    if 83 - 83: iIiiiI1IiI1I1 - OoOoo0
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = O0O0o0oOOO ( 'notplayable' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No notplayable --" )
    if 35 - 35: O00ooooo00 - IIii1I + O00ooooo00
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = O0O0o0oOOO ( 'noredirect' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No noredirect --" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'origin' ] = O0O0o0oOOO ( 'origin' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No origin --" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = O0O0o0oOOO ( 'includeheaders' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No includeheaders --" )
    if 86 - 86: IIii1I + I11iii11IIi . i11iIiiIii - oOOoo
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = O0O0o0oOOO ( 'x-req' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No x-req --" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = O0O0o0oOOO ( 'x-forward' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No x-forward --" )
    if 51 - 51: I11iii11IIi
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'agent' ] = O0O0o0oOOO ( 'agent' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- No User Agent --" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'post' ] = O0O0o0oOOO ( 'post' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a post" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = O0O0o0oOOO ( 'rawpost' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a rawpost" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = O0O0o0oOOO ( 'htmlunescape' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a htmlunescape" )
    if 14 - 14: ooO00oo % I1ii % IiIIi1I1Iiii - i11iIiiIii
    if 53 - 53: oOOoo % IiIIi1I1Iiii
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = O0O0o0oOOO ( 'readcookieonly' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a readCookieOnly" )
    if 59 - 59: oOOOo0o0O % IIii1I . O00ooooo00 + iIiiiI1IiI1I1 * ooO00oo
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = O0O0o0oOOO ( 'cookiejar' ) [ 0 ] . string
    if not IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    O00o0o0000o0o ( "Regex: -- Not a cookieJar" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = O0O0o0oOOO ( 'setcookie' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a setcookie" )
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = O0O0o0oOOO ( 'appendcookie' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- Not a appendcookie" )
    if 41 - 41: oOOoo % OOO0O
   try :
    IIIIi1 [ O0O0o0oOOO ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = O0O0o0oOOO ( 'ignorecache' ) [ 0 ] . string
   except :
    O00o0o0000o0o ( "Regex: -- no ignorecache" )
    if 12 - 12: oOOOo0o0O
    if 69 - 69: II1 + oOOOo0o0O
    if 26 - 26: IiIIi1I1Iiii + oOOOo0o0O / Ooo00oOo00o % I11iii11IIi % OOO0O + iIiiiI1IiI1I1
    if 31 - 31: OoOoo0 % oOOOo0o0O * OoOoo0
    if 45 - 45: O00ooooo00 . IIiIiII11i + oOOOo0o0O - II1 % IiIi11i
  IIIIi1 = urllib . quote ( repr ( IIIIi1 ) )
  return IIIIi1
  if 1 - 1: IIii1I
 except :
  IIIIi1 = None
  O00o0o0000o0o ( 'regex Error: ' + IIIII . encode ( 'utf-8' , 'ignore' ) )
  if 93 - 93: O00ooooo00 . i11iIiiIii . IiIIi1I1Iiii
def O0O00OOo ( url ) :
 try :
  for O0O0o0oOOO in range ( 1 , 51 ) :
   oO0O = OoOOo ( url )
   if "EXT-X-STREAM-INF" in oO0O : return url
   if not "EXTM3U" in oO0O : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 17 - 17: O00ooooo00
  if 1 - 1: IiIi11i
def oOO0oo ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
  if 29 - 29: IIiIiII11i * iIiiiI1IiI1I1 * II1 - OOO0O * iIiiiI1IiI1I1
  if 41 - 41: OOO0O0O0ooooo
 I111I11I111 = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 if 46 - 46: i11iIiiIii - OOO0O0O0ooooo . I1ii
 Oo0O = True
 if 1 - 1: OOO0O0O0ooooo / OOooO % o00ooooO0oO . IiIIi1I1Iiii + ooO00oo
 if 27 - 27: o00ooooO0oO % II1 + ooO00oo % O00ooooo00 / I1ii / II1
 if 11 - 11: oOOOo0o0O % oOOoo - i11iIiiIii - I1ii + IiIi11i + ooO00oo
 if 87 - 87: o00ooooO0oO * O00ooooo00 / OOO0O
 for IIII1i1 in I111I11I111 :
  if IIII1i1 in regexs :
   if 70 - 70: i11iIiiIii % OOO0O / IIiIiII11i
   ooOOOOo0 = regexs [ IIII1i1 ]
   if 38 - 38: II1 / OOO0O . OOO0O0O0ooooo / O00ooooo00 / IiIIi1I1Iiii + IIii1I
   ooO00O00oOO = False
   if 40 - 40: OOooO . I1ii + IIiIiII11i + OOO0O + o00ooooO0oO
   if 26 - 26: IIii1I
   if 'cookiejar' in ooOOOOo0 :
    if 87 - 87: OOO0O / II1 - IiIIi1I1Iiii % I11iii11IIi % ooO00oo % IiIIi1I1Iiii
    ooO00O00oOO = ooOOOOo0 [ 'cookiejar' ]
    if '$doregex' in ooO00O00oOO :
     cookieJar = oOO0oo ( regexs , ooOOOOo0 [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     ooO00O00oOO = True
    else :
     ooO00O00oOO = True
     if 29 - 29: II1 . IIiIiII11i % OOO0O - OOooO
   if ooO00O00oOO :
    if cookieJar == None :
     if 8 - 8: O00ooooo00
     cookie_jar_file = None
     if 'open[' in ooOOOOo0 [ 'cookiejar' ] :
      cookie_jar_file = ooOOOOo0 [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 32 - 32: I1ii / iIiiiI1IiI1I1
     cookieJar = II1Iii ( cookie_jar_file )
     if cookie_jar_file :
      O0oooo0OoO0oo ( cookieJar , cookie_jar_file )
      if 16 - 16: IIiIiII11i * iIiiiI1IiI1I1 / IIii1I - OOooO
      if 3 - 3: IIiIiII11i * IiIi11i + iIiiiI1IiI1I1 - Ooo00oOo00o
      if 97 - 97: OOO0O / I1ii - o0ooo - IIiIiII11i - IIiIiII11i
    elif 'save[' in ooOOOOo0 [ 'cookiejar' ] :
     cookie_jar_file = ooOOOOo0 [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     OOooo00 = os . path . join ( iIiiiI , cookie_jar_file )
     print 'complete_path' , OOooo00
     O0oooo0OoO0oo ( cookieJar , cookie_jar_file )
     if 35 - 35: o00ooooO0oO . I11iii11IIi * i11iIiiIii
     if 44 - 44: i11iIiiIii / IiIIi1I1Iiii
   if ooOOOOo0 [ 'page' ] and '$doregex' in ooOOOOo0 [ 'page' ] :
    ooOOOOo0 [ 'page' ] = oOO0oo ( regexs , ooOOOOo0 [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 42 - 42: II1 + IiIIi1I1Iiii % iIiiiI1IiI1I1 + Ooo00oOo00o
   if 'setcookie' in ooOOOOo0 and ooOOOOo0 [ 'setcookie' ] and '$doregex' in ooOOOOo0 [ 'setcookie' ] :
    ooOOOOo0 [ 'setcookie' ] = oOO0oo ( regexs , ooOOOOo0 [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in ooOOOOo0 and ooOOOOo0 [ 'appendcookie' ] and '$doregex' in ooOOOOo0 [ 'appendcookie' ] :
    ooOOOOo0 [ 'appendcookie' ] = oOO0oo ( regexs , ooOOOOo0 [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 24 - 24: OOooO * iIiiiI1IiI1I1 % OOooO % ooO00oo + II1
    if 29 - 29: iIiiiI1IiI1I1 - II1 - i11iIiiIii . o0ooo
   if 'post' in ooOOOOo0 and '$doregex' in ooOOOOo0 [ 'post' ] :
    ooOOOOo0 [ 'post' ] = oOO0oo ( regexs , ooOOOOo0 [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    print 'post is now' , ooOOOOo0 [ 'post' ]
    if 19 - 19: iIiiiI1IiI1I1
   if 'rawpost' in ooOOOOo0 and '$doregex' in ooOOOOo0 [ 'rawpost' ] :
    ooOOOOo0 [ 'rawpost' ] = oOO0oo ( regexs , ooOOOOo0 [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 72 - 72: II1 / IIiIiII11i + oOOoo / I11iii11IIi * oOOoo
    if 34 - 34: OOO0O0O0ooooo * OOO0O0O0ooooo % II1 + OOooO * IIii1I % oOOoo
   if 'rawpost' in ooOOOOo0 and '$epoctime$' in ooOOOOo0 [ 'rawpost' ] :
    ooOOOOo0 [ 'rawpost' ] = ooOOOOo0 [ 'rawpost' ] . replace ( '$epoctime$' , I1iI1I1 ( ) )
    if 48 - 48: IIiIiII11i / i11iIiiIii - o0ooo * I1ii / II1
   if 'rawpost' in ooOOOOo0 and '$epoctime2$' in ooOOOOo0 [ 'rawpost' ] :
    ooOOOOo0 [ 'rawpost' ] = ooOOOOo0 [ 'rawpost' ] . replace ( '$epoctime2$' , OoOo ( ) )
    if 17 - 17: oOOoo . i11iIiiIii
    if 5 - 5: OOO0O + OOO0O0O0ooooo + OOO0O0O0ooooo . o00ooooO0oO - IiIi11i
   I11II1i = ''
   if ooOOOOo0 [ 'page' ] and ooOOOOo0 [ 'page' ] in cachedPages and not 'ignorecache' in ooOOOOo0 and forCookieJarOnly == False :
    I11II1i = cachedPages [ ooOOOOo0 [ 'page' ] ]
   else :
    if ooOOOOo0 [ 'page' ] and not ooOOOOo0 [ 'page' ] == '' and ooOOOOo0 [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in ooOOOOo0 [ 'page' ] :
      ooOOOOo0 [ 'page' ] = ooOOOOo0 [ 'page' ] . replace ( '$epoctime$' , I1iI1I1 ( ) )
     if '$epoctime2$' in ooOOOOo0 [ 'page' ] :
      ooOOOOo0 [ 'page' ] = ooOOOOo0 [ 'page' ] . replace ( '$epoctime2$' , OoOo ( ) )
      if 63 - 63: I1ii
      if 71 - 71: O00ooooo00 . oOOoo * OOooO % II1 + oOOOo0o0O
     iIIi1iiI1i11 = ooOOOOo0 [ 'page' ] . split ( '|' )
     oooiIii11i1I = iIIi1iiI1i11 [ 0 ]
     oOOOoOoO = None
     if len ( iIIi1iiI1i11 ) > 1 :
      oOOOoOoO = iIIi1iiI1i11 [ 1 ]
     O00O0O0O0 = urllib2 . Request ( oooiIii11i1I )
     O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     if 'refer' in ooOOOOo0 :
      O00O0O0O0 . add_header ( 'Referer' , ooOOOOo0 [ 'refer' ] )
     if 'agent' in ooOOOOo0 :
      O00O0O0O0 . add_header ( 'User-agent' , ooOOOOo0 [ 'agent' ] )
     if 'x-req' in ooOOOOo0 :
      O00O0O0O0 . add_header ( 'X-Requested-With' , ooOOOOo0 [ 'x-req' ] )
     if 'x-forward' in ooOOOOo0 :
      O00O0O0O0 . add_header ( 'X-Forwarded-For' , ooOOOOo0 [ 'x-forward' ] )
     if 'setcookie' in ooOOOOo0 :
      print 'adding cookie' , ooOOOOo0 [ 'setcookie' ]
      O00O0O0O0 . add_header ( 'Cookie' , ooOOOOo0 [ 'setcookie' ] )
     if 'appendcookie' in ooOOOOo0 :
      print 'appending cookie to cookiejar' , ooOOOOo0 [ 'appendcookie' ]
      I1i = ooOOOOo0 [ 'appendcookie' ]
      I1i = I1i . split ( ';' )
      for i1II1iII in I1i :
       iI1ii11iIi1i , II1i = i1II1iII . split ( '=' )
       o0OO00oo , iI1ii11iIi1i = iI1ii11iIi1i . split ( ':' )
       i1i1IiIiIi1Ii = cookielib . Cookie ( version = 0 , name = iI1ii11iIi1i , value = II1i , port = None , port_specified = False , domain = o0OO00oo , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( i1i1IiIiIi1Ii )
       if 64 - 64: oOOOo0o0O + II1 * II1
       if 41 - 41: IiIi11i . IiIIi1I1Iiii + IIiIiII11i
       if 100 - 100: oOOoo + Ooo00oOo00o
       if 73 - 73: O00ooooo00 - o00ooooO0oO % IiIi11i / Ooo00oOo00o
     if 'origin' in ooOOOOo0 :
      O00O0O0O0 . add_header ( 'Origin' , ooOOOOo0 [ 'origin' ] )
     if oOOOoOoO :
      oOOOoOoO = oOOOoOoO . split ( '&' )
      for i1II1iII in oOOOoOoO :
       iI1ii11iIi1i , II1i = i1II1iII . split ( '=' )
       O00O0O0O0 . add_header ( iI1ii11iIi1i , II1i )
       if 40 - 40: OOO0O * IiIi11i - IIiIiII11i / ooO00oo / i11iIiiIii
       if 83 - 83: OOO0O / o00ooooO0oO - i11iIiiIii . IIii1I + IiIIi1I1Iiii
     if not cookieJar == None :
      if 59 - 59: OOO0O0O0ooooo % IiIIi1I1Iiii
      O0o00O0Oo0 = urllib2 . HTTPCookieProcessor ( cookieJar )
      o0I11iII = urllib2 . build_opener ( O0o00O0Oo0 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      o0I11iII = urllib2 . install_opener ( o0I11iII )
      if 'noredirect' in ooOOOOo0 :
       IiiIiI = urllib2 . build_opener ( I1IiiI )
       o0I11iII = urllib2 . install_opener ( IiiIiI )
       if 23 - 23: OoOoo0
     if 'connection' in ooOOOOo0 :
      print '..........................connection//////.' , ooOOOOo0 [ 'connection' ]
      from keepalive import HTTPHandler
      iIiiIiiIi = HTTPHandler ( )
      o0I11iII = urllib2 . build_opener ( iIiiIiiIi )
      urllib2 . install_opener ( o0I11iII )
      if 40 - 40: o0ooo
      if 78 - 78: IIii1I
     ooO0oo0o0 = None
     if 9 - 9: IIiIiII11i + OOO0O / IIiIiII11i . I1ii * IiIi11i
     if 'post' in ooOOOOo0 :
      i1i1ii1111i1i = ooOOOOo0 [ 'post' ]
      if '$LiveStreamRecaptcha' in i1i1ii1111i1i :
       ( iIiI , ii1iIIiii1 ) = ooOo0O0o0 ( ooOOOOo0 [ 'page' ] )
       if iIiI :
        i1i1ii1111i1i += 'recaptcha_challenge_field:' + iIiI + ',recaptcha_response_field:' + ii1iIIiii1
      o0oo0O = i1i1ii1111i1i . split ( ',' ) ;
      ooO0oo0o0 = { }
      for I1iiIII in o0oo0O :
       iI1ii11iIi1i = I1iiIII . split ( ':' ) [ 0 ] ;
       II1i = I1iiIII . split ( ':' ) [ 1 ] ;
       ooO0oo0o0 [ iI1ii11iIi1i ] = II1i
      ooO0oo0o0 = urllib . urlencode ( ooO0oo0o0 )
      if 16 - 16: I1ii + IiIi11i / o0ooo
     if 'rawpost' in ooOOOOo0 :
      ooO0oo0o0 = ooOOOOo0 [ 'rawpost' ]
      if '$LiveStreamRecaptcha' in ooO0oo0o0 :
       ( iIiI , ii1iIIiii1 ) = ooOo0O0o0 ( ooOOOOo0 [ 'page' ] )
       if iIiI :
        ooO0oo0o0 += '&recaptcha_challenge_field=' + iIiI + '&recaptcha_response_field=' + ii1iIIiii1
        if 82 - 82: ooO00oo * i11iIiiIii % iIiiiI1IiI1I1 - II1
        if 90 - 90: IiIIi1I1Iiii . I1ii * O00ooooo00 - O00ooooo00
        if 16 - 16: IIiIiII11i * O00ooooo00 - o0ooo . ooO00oo % OoOoo0 / o0ooo
        if 14 - 14: IIii1I * o00ooooO0oO * OOO0O / IIii1I * ooO00oo / OoOoo0
     if ooO0oo0o0 :
      ooO0O = urllib2 . urlopen ( O00O0O0O0 , ooO0oo0o0 )
     else :
      ooO0O = urllib2 . urlopen ( O00O0O0O0 )
      if 77 - 77: Ooo00oOo00o + o00ooooO0oO + o00ooooO0oO * oOOoo / II1 . oOOoo
     I11II1i = ooO0O . read ( )
     I11II1i = ooo0O0OO ( I11II1i )
     if 61 - 61: ooO00oo + IIii1I + i11iIiiIii / i11iIiiIii % iIiiiI1IiI1I1
     if 'includeheaders' in ooOOOOo0 :
      I11II1i += str ( ooO0O . headers . get ( 'Set-Cookie' ) )
      if 42 - 42: oOOoo * o00ooooO0oO . ooO00oo * IIiIiII11i + I11iii11IIi
     ooO0O . close ( )
     cachedPages [ ooOOOOo0 [ 'page' ] ] = I11II1i
     if 25 - 25: OoOoo0 . IIiIiII11i + I1ii
     if 75 - 75: ooO00oo - o0ooo % OOooO + i11iIiiIii
     if 100 - 100: OoOoo0 + o0ooo - i11iIiiIii - iIiiiI1IiI1I1
     if forCookieJarOnly :
      return cookieJar
    elif ooOOOOo0 [ 'page' ] and not ooOOOOo0 [ 'page' ] . startswith ( 'http' ) :
     if ooOOOOo0 [ 'page' ] . startswith ( '$pyFunction:' ) :
      iIIIiIi1I1i = OoOOoO0oOo ( ooOOOOo0 [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar )
      if forCookieJarOnly :
       return cookieJar
      I11II1i = iIIIiIi1I1i
     else :
      I11II1i = ooOOOOo0 [ 'page' ]
   if '$pyFunction:playmedia(' in ooOOOOo0 [ 'expre' ] or 'ActivateWindow' in ooOOOOo0 [ 'expre' ] or any ( x in url for x in Oo0Ooo ) :
    Oo0O = False
   if '$doregex' in ooOOOOo0 [ 'expre' ] :
    ooOOOOo0 [ 'expre' ] = oOO0oo ( regexs , ooOOOOo0 [ 'expre' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 70 - 70: OoOoo0 % IIii1I . IiIIi1I1Iiii + IiIIi1I1Iiii - o0ooo % o00ooooO0oO
    if 38 - 38: o00ooooO0oO % oOOOo0o0O - II1
   if not ooOOOOo0 [ 'expre' ] == '' :
    print 'doing it ' , ooOOOOo0 [ 'expre' ]
    if '$LiveStreamCaptcha' in ooOOOOo0 [ 'expre' ] :
     iIIIiIi1I1i = oOo0OOoooO ( ooOOOOo0 , I11II1i , cookieJar )
     if 26 - 26: o0ooo * ooO00oo . O00ooooo00
     url = url . replace ( "$doregex[" + IIII1i1 + "]" , iIIIiIi1I1i )
    elif ooOOOOo0 [ 'expre' ] . startswith ( '$pyFunction:' ) :
     if 59 - 59: OOO0O0O0ooooo + O00ooooo00 - o0ooo
     iIIIiIi1I1i = OoOOoO0oOo ( ooOOOOo0 [ 'expre' ] . split ( '$pyFunction:' ) [ 1 ] , I11II1i , cookieJar )
     if 'ActivateWindow' in ooOOOOo0 [ 'expre' ] : return
     print 'still hre'
     print 'url k val' , url , IIII1i1 , iIIIiIi1I1i
     if 62 - 62: i11iIiiIii % oOOOo0o0O . ooO00oo . oOOOo0o0O
     url = url . replace ( "$doregex[" + IIII1i1 + "]" , iIIIiIi1I1i )
    else :
     if not I11II1i == '' :
      ooOo0O0O0oOO0 = re . compile ( ooOOOOo0 [ 'expre' ] ) . search ( I11II1i )
      iIIIiIi1I1i = ''
      try :
       iIIIiIi1I1i = ooOo0O0O0oOO0 . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     else :
      iIIIiIi1I1i = ooOOOOo0 [ 'expre' ]
     if rawPost :
      print 'rawpost'
      iIIIiIi1I1i = urllib . quote_plus ( iIIIiIi1I1i )
     if 'htmlunescape' in ooOOOOo0 :
      if 10 - 10: IiIIi1I1Iiii + OOO0O0O0ooooo
      import HTMLParser
      iIIIiIi1I1i = HTMLParser . HTMLParser ( ) . unescape ( iIIIiIi1I1i )
     url = url . replace ( "$doregex[" + IIII1i1 + "]" , iIIIiIi1I1i )
     if 43 - 43: IIii1I / iIiiiI1IiI1I1 % o0ooo - oOOOo0o0O
   else :
    url = url . replace ( "$doregex[" + IIII1i1 + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , I1iI1I1 ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , OoOo ( ) )
  if 62 - 62: OoOoo0
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , O000oOo ( cookieJar ) )
  if 53 - 53: IIii1I + o0ooo - I11iii11IIi - I1ii / IiIi11i % i11iIiiIii
 if recursiveCall : return url
 print 'final url' , url
 if url == "" :
  return
 else :
  return url , Oo0O
  if 3 - 3: OOooO . IiIi11i % IIiIiII11i + OOO0O
  if 64 - 64: O00ooooo00
  if 29 - 29: o0ooo / i11iIiiIii / IIiIiII11i % I1ii % i11iIiiIii
def i111II ( t ) :
 import hashlib
 i1II1iII = hashlib . md5 ( )
 i1II1iII . update ( t )
 return i1II1iII . hexdigest ( )
 if 63 - 63: IIiIiII11i - Ooo00oOo00o % OOooO % OoOoo0 / o0ooo / O00ooooo00
def OO0oo0O0OOO0 ( encrypted ) :
 OoOOoIii1 = ""
 for iIIIiIi1I1i in encrypted . split ( ':' ) :
  OoOOoIii1 += chr ( int ( iIIIiIi1I1i . replace ( "0m0" , "" ) ) / 84 / 5 )
 return OoOOoIii1
 if 78 - 78: i11iIiiIii + o0ooo + o00ooooO0oO / o0ooo % IIii1I % ooO00oo
def Oo0O0Oo00O ( media_url ) :
 try :
  import CustomPlayer
  iIoo0ooooO = CustomPlayer . MyXBMCPlayer ( )
  iiIIi = xbmcgui . ListItem ( label = str ( IIIII ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  iIoo0ooooO . play ( media_url , iiIIi )
  xbmc . sleep ( 1000 )
  while iIoo0ooooO . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 36 - 36: OoOoo0 . iIiiiI1IiI1I1
 if 25 - 25: I1ii
def iI1 ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  iiII11I = page_value
  page_value = OoOOo ( page_value , headers = referer )
  if 32 - 32: oOOOo0o0O % IiIi11i - I11iii11IIi % OOooO . o00ooooO0oO
 i1Iii1I1I1 = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 67 - 67: I11iii11IIi * I11iii11IIi . I11iii11IIi + oOOoo / I1ii
 i1iI1IIIII1 = re . compile ( i1Iii1I1I1 ) . findall ( page_value )
 OO0o0oO = ""
 if i1iI1IIIII1 and len ( i1iI1IIIII1 ) > 0 :
  for II1i in i1iI1IIIII1 :
   iI1I1IiIi1I = II1i1ii ( II1i )
   OOOo00 = IIIIIo0ooOoO000oO ( iI1I1IiIi1I , '\'(.*?)\'' )
   if 'unescape' in iI1I1IiIi1I :
    iI1I1IiIi1I = urllib . unquote ( OOOo00 )
   OO0o0oO += iI1I1IiIi1I + '\n'
  print 'final value is ' , OO0o0oO
  if 91 - 91: IIii1I . o0ooo . OOO0O + II1
  iiII11I = IIIIIo0ooOoO000oO ( OO0o0oO , 'src="(.*?)"' )
  if 69 - 69: o00ooooO0oO - IIiIiII11i
  page_value = OoOOo ( iiII11I , headers = referer )
  if 95 - 95: IIiIiII11i * i11iIiiIii . IiIi11i
  if 41 - 41: iIiiiI1IiI1I1
  if 37 - 37: OoOoo0 . IiIIi1I1Iiii % ooO00oo * O00ooooo00
 oOOOOi11i11 = IIIIIo0ooOoO000oO ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 i1iiIII1IIiIIII = IIIIIo0ooOoO000oO ( page_value , 'file\',\s\'(.*?)\'' )
 if 19 - 19: OOooO - o0ooo / o0ooo + IiIIi1I1Iiii
 if 98 - 98: IIii1I % oOOOo0o0O + OoOoo0 . IiIi11i
 return oOOOOi11i11 + ' playpath=' + i1iiIII1IIiIIII + ' pageUrl=' + iiII11I
 if 99 - 99: OOO0O0O0ooooo + OOO0O0O0ooooo * OoOoo0 + OOO0O0O0ooooo * I1ii
def oOoO0O00oo ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = OoOOo ( page_value , headers = referer )
 i1Iii1I1I1 = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 i1iI1IIIII1 = re . compile ( i1Iii1I1I1 ) . findall ( page_value ) [ 0 ]
 if 93 - 93: OOO0O % I11iii11IIi . OOO0O0O0ooooo / OOooO * I1ii
 O0oo00o0O , i1I1I , iiiI1I1iIIIi1 , i1iii1ii , II1I11Iii1 , II1i = ( i1iI1IIIII1 )
 II1I11Iii1 = int ( II1I11Iii1 )
 O0oo00o0O = int ( O0oo00o0O ) / II1I11Iii1
 i1I1I = int ( i1I1I ) / II1I11Iii1
 iiiI1I1iIIIi1 = int ( iiiI1I1iIIIi1 ) / II1I11Iii1
 i1iii1ii = int ( i1iii1ii ) / II1I11Iii1
 if 16 - 16: oOOoo * Ooo00oOo00o / I1ii
 II1iiI = 'rtmp://' + str ( O0oo00o0O ) + '.' + str ( i1I1I ) + '.' + str ( iiiI1I1iIIIi1 ) + '.' + str ( i1iii1ii ) + II1i ;
 return II1iiI
 if 31 - 31: o0ooo % OoOoo0 + IIii1I + i11iIiiIii * o00ooooO0oO
def I1i1I1I11IiiI ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 iiIIIII1i1iI = os . path . join ( iIiiiI , 'testfile.m3u' )
 str += '\n'
 I1IiI1iI11 ( iiIIIII1i1iI , str )
 if 2 - 2: IIii1I
 return iiIIIII1i1iI
 if 45 - 45: II1 / i11iIiiIii
def I1IiI1iI11 ( file_name , page_data , append = False ) :
 if append :
  II1I11Iii1 = open ( file_name , 'a' )
  II1I11Iii1 . write ( page_data )
  II1I11Iii1 . close ( )
 else :
  II1I11Iii1 = open ( file_name , 'wb' )
  II1I11Iii1 . write ( page_data )
  II1I11Iii1 . close ( )
  return ''
  if 10 - 10: OOooO - I1ii * IIii1I % IIii1I * ooO00oo - OOO0O
def OoO0O0oO00 ( file_name ) :
 II1I11Iii1 = open ( file_name , 'rb' )
 i1iii1ii = II1I11Iii1 . read ( )
 II1I11Iii1 . close ( )
 return i1iii1ii
 if 33 - 33: OOO0O0O0ooooo
def oo0oO ( page_data ) :
 import re , base64 , urllib ;
 IiIi1iI11 = page_data
 while 'geh(' in IiIi1iI11 :
  if IiIi1iI11 . startswith ( 'lol(' ) : IiIi1iI11 = IiIi1iI11 [ 5 : - 1 ]
  if 11 - 11: OOO0O
  IiIi1iI11 = re . compile ( '"(.*?)"' ) . findall ( IiIi1iI11 ) [ 0 ] ;
  IiIi1iI11 = base64 . b64decode ( IiIi1iI11 ) ;
  IiIi1iI11 = urllib . unquote ( IiIi1iI11 ) ;
 print IiIi1iI11
 return IiIi1iI11
 if 26 - 26: IIii1I * o00ooooO0oO - oOOOo0o0O
def III1II111Ii1 ( page_data ) :
 print 'get_dag_url2' , page_data
 o0O0OO0o = OoOOo ( page_data ) ;
 OOOoOo = '(http.*)'
 import uuid
 OOoO0oo0O = str ( uuid . uuid1 ( ) ) . upper ( )
 oO0OOoO0 = re . compile ( OOOoOo ) . findall ( o0O0OO0o )
 O0o0Oo = [ ( 'X-Playback-Session-Id' , OOoO0oo0O ) ]
 for iiI1I1ii in oO0OOoO0 :
  try :
   o00IiI1iiII1i1i = OoOOo ( iiI1I1ii , headers = O0o0Oo ) ;
   if 18 - 18: IIiIiII11i
  except : pass
  if 80 - 80: OOO0O / IIii1I % I11iii11IIi
 return page_data + '|&X-Playback-Session-Id=' + OOoO0oo0O
 if 80 - 80: Ooo00oOo00o % OOooO
 if 99 - 99: IiIi11i / IIii1I - oOOoo * OOO0O % IIiIiII11i
def i1II1i ( page_data ) :
 print 'get_dag_url' , page_data
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  O0o0Oo = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = OoOOo ( page_data , headers = O0o0Oo ) ;
  if 10 - 10: oOOoo - I11iii11IIi . II1 . oOOOo0o0O . Ooo00oOo00o * OOooO
 if '127.0.0.1' in page_data :
  return OOOO ( page_data )
 elif IIIIIo0ooOoO000oO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  Oo = IIIIIo0ooOoO000oO ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + IIIIIo0ooOoO000oO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + IIIIIo0ooOoO000oO ( page_data , '\\?y=([^&]+)&' )
 else :
  Oo = IIIIIo0ooOoO000oO ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( Oo ) == 0 :
   Oo = page_data
 Oo = Oo . replace ( ' ' , '%20' )
 return Oo
 if 50 - 50: oOOoo - i11iIiiIii + IIii1I / OOO0O0O0ooooo - oOOoo + o0ooo
def IIIIIo0ooOoO000oO ( data , re_patten ) :
 o0 = ''
 ooOOOOo0 = re . search ( re_patten , data )
 if ooOOOOo0 != None :
  o0 = ooOOOOo0 . group ( 1 )
 else :
  o0 = ''
 return o0
 if 22 - 22: iIiiiI1IiI1I1 - oOOoo / IiIi11i % II1 + oOOOo0o0O
def OOOO ( page_data ) :
 Oo = ''
 if '127.0.0.1' in page_data :
  Oo = IIIIIo0ooOoO000oO ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + IIIIIo0ooOoO000oO ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 5 - 5: Ooo00oOo00o / OOooO + i11iIiiIii % OoOoo0
 if IIIIIo0ooOoO000oO ( page_data , 'token=([^&]+)&' ) != '' :
  Oo = Oo + '?token=' + IIIIIo0ooOoO000oO ( page_data , 'token=([^&]+)&' )
 elif IIIIIo0ooOoO000oO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  Oo = IIIIIo0ooOoO000oO ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + IIIIIo0ooOoO000oO ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + IIIIIo0ooOoO000oO ( page_data , '\\?y=([^&]+)&' )
 else :
  Oo = IIIIIo0ooOoO000oO ( page_data , 'HREF="([^"]+)"' )
  if 93 - 93: I11iii11IIi % IIii1I
 if 'dag1.asx' in Oo :
  return i1II1i ( Oo )
  if 90 - 90: IIiIiII11i - oOOOo0o0O / oOOoo / OOO0O0O0ooooo / OoOoo0
 if 'devinlivefs.fplive.net' not in Oo :
  Oo = Oo . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in Oo :
  Oo = Oo . replace ( 'permlive' , 'flive' )
 return Oo
 if 87 - 87: I11iii11IIi / ooO00oo + IIii1I
 if 93 - 93: IIii1I + I1ii % IiIi11i
def iii1IiI1I1 ( str_eval ) :
 O00o = ""
 try :
  oO0o00ooO0OoO = "w,i,s,e=(" + str_eval + ')'
  exec ( oO0o00ooO0OoO )
  O00o = IIoO00OoOo ( w , i , s , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 74 - 74: iIiiiI1IiI1I1 . OOO0O0O0ooooo - IIiIiII11i + ooO00oo % i11iIiiIii % I11iii11IIi
 return O00o
 if 78 - 78: oOOoo + I11iii11IIi + ooO00oo - ooO00oo . i11iIiiIii / Ooo00oOo00o
def IIoO00OoOo ( w , i , s , e ) :
 I11i11i1 = 0 ;
 OOO = 0 ;
 ii1i1iiI = 0 ;
 Oo0oOo0ooOOOo = [ ] ;
 OoO0000o = [ ] ;
 while True :
  if ( I11i11i1 < 5 ) :
   OoO0000o . append ( w [ I11i11i1 ] )
  elif ( I11i11i1 < len ( w ) ) :
   Oo0oOo0ooOOOo . append ( w [ I11i11i1 ] ) ;
  I11i11i1 += 1 ;
  if ( OOO < 5 ) :
   OoO0000o . append ( i [ OOO ] )
  elif ( OOO < len ( i ) ) :
   Oo0oOo0ooOOOo . append ( i [ OOO ] )
  OOO += 1 ;
  if ( ii1i1iiI < 5 ) :
   OoO0000o . append ( s [ ii1i1iiI ] )
  elif ( ii1i1iiI < len ( s ) ) :
   Oo0oOo0ooOOOo . append ( s [ ii1i1iiI ] ) ;
  ii1i1iiI += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( Oo0oOo0ooOOOo ) + len ( OoO0000o ) + len ( e ) ) :
   break ;
   if 90 - 90: ooO00oo . IiIi11i / IIii1I
 I1IIi1I = '' . join ( Oo0oOo0ooOOOo )
 iIii1i1 = '' . join ( OoO0000o )
 OOO = 0 ;
 oOoO00 = [ ] ;
 for I11i11i1 in range ( 0 , len ( Oo0oOo0ooOOOo ) , 2 ) :
  if 45 - 45: oOOoo . II1
  i1iIIi11i111I = - 1 ;
  if ( ord ( iIii1i1 [ OOO ] ) % 2 ) :
   i1iIIi11i111I = 1 ;
   if 16 - 16: IIiIiII11i . IIii1I
  oOoO00 . append ( chr ( int ( I1IIi1I [ I11i11i1 : I11i11i1 + 2 ] , 36 ) - i1iIIi11i111I ) ) ;
  OOO += 1 ;
  if ( OOO >= len ( OoO0000o ) ) :
   OOO = 0 ;
 II1iiI = '' . join ( oOoO00 )
 if 'eval(function(w,i,s,e)' in II1iiI :
  print 'STILL GOing'
  II1iiI = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( II1iiI ) [ 0 ]
  return iii1IiI1I1 ( II1iiI )
 else :
  print 'FINISHED'
  return II1iiI
  if 27 - 27: i11iIiiIii - IIiIiII11i
def II1i1ii ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  iii1IIiI = None
  if page_value . startswith ( "http" ) :
   page_value = OoOOo ( page_value )
  print 'page_value' , page_value
  if regex_for_text and len ( regex_for_text ) > 0 :
   page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   if 33 - 33: OoOoo0
  page_value = oOo00OoO0O ( page_value , iterations , total_iteration )
 except : traceback . print_exc ( file = sys . stdout )
 print 'unpacked' , page_value
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  print 'sav1 unpacked' , page_value
 return page_value
 if 69 - 69: IIii1I * IIiIiII11i - OOooO + OOO0O0O0ooooo + OOO0O0O0ooooo
def oOo00OoO0O ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 print 'iteration' , iteration
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  O0oo = sJavascript . split ( 'var _0xcb8a=' )
  oO0o00ooO0OoO = "myarray=" + O0oo [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( oO0o00ooO0OoO )
  ooOooO00Oo = 62
  ooO00o = int ( O0oo [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  o0o00O0oOooO0 = myarray [ 0 ]
  o0oO0OO00ooOO = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as IiIIiii11II1 :
   IiIIiii11II1 . write ( str ( o0oO0OO00ooOO ) )
   if 42 - 42: O00ooooo00 % iIiiiI1IiI1I1 . IiIi11i
 else :
  if 7 - 7: OOO0O - I1ii * oOOOo0o0O + o0ooo . OOO0O
  O0oo = sJavascript . split ( "rn p}('" )
  print O0oo
  if 85 - 85: OOO0O0O0ooooo
  o0o00O0oOooO0 , ooOooO00Oo , ooO00o , o0oO0OO00ooOO = ( '' , '0' , '0' , '' )
  if 32 - 32: II1 . Ooo00oOo00o / IiIIi1I1Iiii * o0ooo / o0ooo * oOOoo
  oO0o00ooO0OoO = "p1,a1,c1,k1=('" + O0oo [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( oO0o00ooO0OoO )
 o0oO0OO00ooOO = o0oO0OO00ooOO . split ( '|' )
 O0oo = O0oo [ 1 ] . split ( "))'" )
 if 19 - 19: oOOoo
 if 55 - 55: oOOOo0o0O % oOOOo0o0O / OOO0O0O0ooooo % OOooO - o0ooo . IiIIi1I1Iiii
 if 49 - 49: IIii1I * O00ooooo00 . II1
 if 90 - 90: o0ooo % OOO0O - IIii1I % I11iii11IIi
 if 8 - 8: I11iii11IIi * IiIIi1I1Iiii / ooO00oo % oOOoo - IIiIiII11i
 if 71 - 71: OOooO
 if 23 - 23: O00ooooo00 . IIii1I . oOOOo0o0O . OOO0O0O0ooooo % oOOoo % i11iIiiIii
 if 11 - 11: OOO0O0O0ooooo - iIiiiI1IiI1I1 . oOOOo0o0O . oOOoo % o00ooooO0oO
 if 21 - 21: IiIIi1I1Iiii / OOooO . o00ooooO0oO * II1 + OoOoo0 - O00ooooo00
 if 58 - 58: OOO0O
 if 2 - 2: iIiiiI1IiI1I1 / o00ooooO0oO
 if 54 - 54: O00ooooo00 . OoOoo0 - OOO0O + IiIi11i + IiIIi1I1Iiii / IiIIi1I1Iiii
 if 22 - 22: IiIi11i . IIii1I
 if 12 - 12: oOOoo
 if 71 - 71: IIiIiII11i . iIiiiI1IiI1I1 . IIiIiII11i - IiIi11i
 if 45 - 45: ooO00oo / OOO0O0O0ooooo / I11iii11IIi * oOOOo0o0O
 if 18 - 18: IIii1I + oOOOo0o0O + IIii1I . OOO0O + o00ooooO0oO . IiIi11i
 if 7 - 7: OOO0O + IIii1I * OoOoo0 * OoOoo0 / iIiiiI1IiI1I1 - oOOoo
 if 65 - 65: I1ii + I11iii11IIi + iIiiiI1IiI1I1
 if 77 - 77: iIiiiI1IiI1I1
 if 50 - 50: OOO0O0O0ooooo . OOO0O0O0ooooo . IiIi11i % IiIIi1I1Iiii
 if 68 - 68: I1ii
 iii11iII = ''
 i1iii1ii = ''
 if 10 - 10: oOOoo
 if 77 - 77: oOOOo0o0O / iIiiiI1IiI1I1 + ooO00oo + IiIi11i - i11iIiiIii
 IiIIiI = str ( oOo0Oo0O0O ( o0o00O0oOooO0 , ooOooO00Oo , ooO00o , o0oO0OO00ooOO , iii11iII , i1iii1ii , iteration ) )
 if 48 - 48: IiIIi1I1Iiii - IiIi11i + IiIIi1I1Iiii - IIiIiII11i * i11iIiiIii . OOooO
 if 35 - 35: ooO00oo . OOO0O0O0ooooo + IiIIi1I1Iiii + oOOOo0o0O + O00ooooo00
 if 65 - 65: OOO0O0O0ooooo * IIiIiII11i / IIiIiII11i . I11iii11IIi
 if 87 - 87: iIiiiI1IiI1I1 * OOO0O % IiIIi1I1Iiii * IiIIi1I1Iiii
 if 58 - 58: oOOOo0o0O . o0ooo + IIiIiII11i % IiIIi1I1Iiii - Ooo00oOo00o
 if iteration >= totaliterations :
  if 50 - 50: OOooO % iIiiiI1IiI1I1 - IiIi11i . O00ooooo00 + OOO0O0O0ooooo % OOooO
  return IiIIiI
 else :
  if 10 - 10: OOooO . O00ooooo00 + oOOoo
  return oOo00OoO0O ( IiIIiI , iteration + 1 )
  if 66 - 66: Ooo00oOo00o % o0ooo
def oOo0Oo0O0O ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 21 - 21: I11iii11IIi - II1 % i11iIiiIii
 if 71 - 71: O00ooooo00 - OoOoo0 * o00ooooO0oO + I1ii - Ooo00oOo00o % OOO0O
 if 63 - 63: IIii1I + oOOOo0o0O . Ooo00oOo00o / IIiIiII11i
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   oO0OIiii1I = str ( ooooo0Oo0 ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + oO0OIiii1I + '\\b' , k [ c ] , p )
   else :
    p = o0I1IIIi11ii11 ( p , oO0OIiii1I , k [ c ] )
    if 53 - 53: o00ooooO0oO * ooO00oo / IIii1I / IIiIiII11i % OOO0O
    if 39 - 39: Ooo00oOo00o / II1 . Ooo00oOo00o * OOO0O / I11iii11IIi
    if 38 - 38: Ooo00oOo00o / IiIi11i % o00ooooO0oO * OoOoo0 + i11iIiiIii % IiIi11i
    if 61 - 61: o00ooooO0oO - oOOoo % OOO0O / IiIi11i / OOooO + IIii1I
    if 87 - 87: o00ooooO0oO + IiIi11i + OOO0O0O0ooooo / O00ooooo00 % ooO00oo / o00ooooO0oO
    if 64 - 64: Ooo00oOo00o % ooO00oo . o00ooooO0oO % Ooo00oOo00o + OoOoo0 * ooO00oo
 return p
 if 83 - 83: o0ooo % I1ii + OoOoo0 % i11iIiiIii + OOO0O0O0ooooo
 if 65 - 65: IIii1I % I1ii + OOO0O0O0ooooo / II1
 if 52 - 52: oOOoo % oOOOo0o0O * IIiIiII11i % OoOoo0 + oOOOo0o0O / OOooO
def o0I1IIIi11ii11 ( source_str , word_to_find , replace_with ) :
 oo000o = None
 oo000o = source_str . split ( word_to_find )
 if len ( oo000o ) > 1 :
  OO00o0oOO = [ ]
  i1i1I1 = 0
  for I1iOOo0O in oo000o :
   if 100 - 100: Ooo00oOo00o % Ooo00oOo00o
   OO00o0oOO . append ( I1iOOo0O )
   iIIIiIi1I1i = word_to_find
   if 15 - 15: I1ii / o00ooooO0oO
   if 37 - 37: i11iIiiIii + IIiIiII11i . oOOOo0o0O % OoOoo0 % OoOoo0
   if i1i1I1 == len ( oo000o ) - 1 :
    iIIIiIi1I1i = ''
   else :
    if len ( I1iOOo0O ) == 0 :
     if ( len ( oo000o [ i1i1I1 + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( oo000o [ i1i1I1 + 1 ] ) > 0 and oo000o [ i1i1I1 + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      iIIIiIi1I1i = replace_with
      if 26 - 26: OOO0O0O0ooooo
    else :
     if ( oo000o [ i1i1I1 ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( oo000o [ i1i1I1 + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( oo000o [ i1i1I1 + 1 ] ) > 0 and oo000o [ i1i1I1 + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      iIIIiIi1I1i = replace_with
      if 34 - 34: IiIi11i * o00ooooO0oO
   OO00o0oOO . append ( iIIIiIi1I1i )
   i1i1I1 += 1
   if 97 - 97: i11iIiiIii % I1ii / IiIIi1I1Iiii / IiIIi1I1Iiii
  source_str = '' . join ( OO00o0oOO )
 return source_str
 if 97 - 97: iIiiiI1IiI1I1 - o00ooooO0oO - IIii1I * IIiIiII11i
def oooO0o0O0oo0o ( num , radix ) :
 if 100 - 100: ooO00oo . oOOoo - IIii1I . i11iIiiIii / iIiiiI1IiI1I1
 oO0O = ""
 if num == 0 : return '0'
 while num > 0 :
  oO0O = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + oO0O
  num /= radix
 return oO0O
 if 71 - 71: o00ooooO0oO * IiIIi1I1Iiii . OoOoo0
def ooooo0Oo0 ( cc , a ) :
 oO0OIiii1I = "" if cc < a else ooooo0Oo0 ( int ( cc / a ) , a )
 cc = ( cc % a )
 i1ii1iiIi1II = chr ( cc + 29 ) if cc > 35 else str ( oooO0o0O0oo0o ( cc , 36 ) )
 return oO0OIiii1I + i1ii1iiIi1II
 if 98 - 98: Ooo00oOo00o - oOOoo . ooO00oo % i11iIiiIii
 if 69 - 69: OOO0O + OOooO * OOO0O0O0ooooo . oOOOo0o0O % I11iii11IIi
def O000oOo ( cookieJar ) :
 try :
  O0O000O = ""
  for i11IIIiI11 , iiii1IIi1 in enumerate ( cookieJar ) :
   O0O000O += iiii1IIi1 . name + "=" + iiii1IIi1 . value + ";"
 except : pass
 if 87 - 87: ooO00oo
 return O0O000O
 if 17 - 17: oOOoo / IIii1I - Ooo00oOo00o + IIiIiII11i % oOOOo0o0O
 if 14 - 14: o0ooo % ooO00oo + OOO0O + Ooo00oOo00o
def O0oooo0OoO0oo ( cookieJar , COOKIEFILE ) :
 try :
  OOooo00 = os . path . join ( iIiiiI , COOKIEFILE )
  cookieJar . save ( OOooo00 , ignore_discard = True )
 except : pass
 if 76 - 76: Ooo00oOo00o - i11iIiiIii + I11iii11IIi + oOOOo0o0O / II1
def II1Iii ( COOKIEFILE ) :
 if 50 - 50: iIiiiI1IiI1I1 - o00ooooO0oO + IIii1I + IIii1I
 OoooooOo = None
 if COOKIEFILE :
  try :
   OOooo00 = os . path . join ( iIiiiI , COOKIEFILE )
   OoooooOo = cookielib . LWPCookieJar ( )
   OoooooOo . load ( OOooo00 , ignore_discard = True )
  except :
   OoooooOo = None
   if 67 - 67: iIiiiI1IiI1I1 / o0ooo . oOOOo0o0O . II1
 if not OoooooOo :
  OoooooOo = cookielib . LWPCookieJar ( )
  if 19 - 19: ooO00oo . OOO0O / I11iii11IIi
 return OoooooOo
 if 68 - 68: IiIi11i / II1 * OoOoo0 / I1ii
def OoOOoO0oOo ( fun_call , page_data , Cookie_Jar ) :
 ooooO000 = ''
 if o0oO0 not in sys . path :
  sys . path . append ( o0oO0 )
  if 61 - 61: IiIi11i - oOOOo0o0O + oOOOo0o0O
 print fun_call
 try :
  iiiIiIIII1iiIIi = 'import ' + fun_call . split ( '.' ) [ 0 ]
  print iiiIiIIII1iiIIi , sys . path
  exec ( iiiIiIIII1iiIIi )
  print 'done'
 except :
  print 'error in import'
  traceback . print_exc ( file = sys . stdout )
 print 'ret_val=' + fun_call
 exec ( 'ret_val=' + fun_call )
 print ooooO000
 if 17 - 17: OoOoo0
 return str ( ooooO000 )
 if 97 - 97: OOO0O * OOO0O / OOooO
def ooOo0O0o0 ( url ) :
 i1111IIiI = OoOOo ( url )
 I11I1IIii = ""
 oO0O0oo = ""
 ii1I = "<script.*?src=\"(.*?recap.*?)\""
 o0 = re . findall ( ii1I , i1111IIiI )
 Ooo000000 = False
 Oo00ooOoO = None
 oO0O0oo = None
 if 100 - 100: i11iIiiIii / i11iIiiIii
 if o0 and len ( o0 ) > 0 :
  o00iIiiiII = o0 [ 0 ]
  Ooo000000 = True
  if 5 - 5: II1 / o0ooo % OoOoo0 % Ooo00oOo00o * OOooO + IIii1I
  I11iiI11iiI = 'challenge.*?\'(.*?)\''
  OOOII1i1II = '\'(.*?)\''
  iIIi1Ii1III = OoOOo ( o00iIiiiII )
  I11I1IIii = re . findall ( I11iiI11iiI , iIIi1Ii1III ) [ 0 ]
  Oooo00 = 'http://www.google.com/recaptcha/api/reload?c=' ;
  iii1II1iI1IIi = o00iIiiiII . split ( 'k=' ) [ 1 ]
  Oooo00 += I11I1IIii + '&k=' + iii1II1iI1IIi + '&captcha_k=1&type=image&lang=en-GB'
  Ii11iiI1 = OoOOo ( Oooo00 )
  Oo00ooOoO = re . findall ( OOOII1i1II , Ii11iiI1 ) [ 0 ]
  oO0OOOoooO00o0o = 'http://www.google.com/recaptcha/api/image?c=' + Oo00ooOoO
  if not oO0OOOoooO00o0o . startswith ( "http" ) :
   oO0OOOoooO00o0o = 'http://www.google.com/recaptcha/api/' + oO0OOOoooO00o0o
  import random
  iI1ii11iIi1i = random . randrange ( 100 , 1000 , 5 )
  I1ii1Ii1 = os . path . join ( iIiiiI , str ( iI1ii11iIi1i ) + "captcha.img" )
  OoOoO = open ( I1ii1Ii1 , "wb" )
  OoOoO . write ( OoOOo ( oO0OOOoooO00o0o ) )
  OoOoO . close ( )
  iI111I1III = i111IiiI1Ii ( captcha = I1ii1Ii1 )
  oO0O0oo = iI111I1III . get ( )
  os . remove ( I1ii1Ii1 )
 return Oo00ooOoO , oO0O0oo
 if 72 - 72: OOO0O0O0ooooo . I11iii11IIi * IiIIi1I1Iiii + OOO0O - o0ooo
def OoOOo ( url , cookieJar = None , post = None , timeout = 20 , headers = None ) :
 if 40 - 40: Ooo00oOo00o + Ooo00oOo00o
 if 94 - 94: OOooO * IIii1I . OoOoo0
 O0o00O0Oo0 = urllib2 . HTTPCookieProcessor ( cookieJar )
 o0I11iII = urllib2 . build_opener ( O0o00O0Oo0 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 if 13 - 13: IIii1I * I11iii11IIi / o00ooooO0oO % IiIi11i + I1ii
 O00O0O0O0 = urllib2 . Request ( url )
 O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for i1II1iII , iiiI1iI1 in headers :
   O00O0O0O0 . add_header ( i1II1iII , iiiI1iI1 )
   if 15 - 15: ooO00oo . O00ooooo00 * I11iii11IIi % IIii1I
 ooO0O = o0I11iII . open ( O00O0O0O0 , post , timeout = timeout )
 I11II1i = ooO0O . read ( )
 ooO0O . close ( )
 return I11II1i ;
 if 35 - 35: OOO0O + o00ooooO0oO - I11iii11IIi % I1ii % o0ooo % I11iii11IIi
def ii1IIiII111I ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 O00OoOoO = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 ooO0o0oo = '' ;
 for O0O0o0oOOO in range ( len ( O00OoOoO ) ) :
  ooO0o0oo += chr ( ord ( O00OoOoO [ O0O0o0oOOO ] ) - O00OoOoO [ len ( O00OoOoO ) - 1 ] ) ;
 ooO0o0oo = urllib . unquote ( ooO0o0oo )
 print ooO0o0oo
 return ooO0o0oo
 if 79 - 79: ooO00oo % Ooo00oOo00o
def ooo0O0OO ( str ) :
 Oo0oOO = re . findall ( 'unescape\(\'(.*?)\'' , str )
 print 'js' , Oo0oOO
 if ( not Oo0oOO == None ) and len ( Oo0oOO ) > 0 :
  for ooooo in Oo0oOO :
   if 26 - 26: IIiIiII11i
   str = str . replace ( ooooo , urllib . unquote ( ooooo ) )
 return str
 if 41 - 41: IIiIiII11i - i11iIiiIii
iIiI1 = 0
def oOo0OOoooO ( m , html_page , cookieJar ) :
 global iIiI1
 iIiI1 += 1
 iII1IiiIIII = m [ 'expre' ]
 iiII11I = m [ 'page' ]
 I11iI = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( iII1IiiIIII ) [ 0 ]
 if 79 - 79: OOO0O0O0ooooo + I1ii
 o00iIiiiII = re . compile ( I11iI ) . findall ( html_page ) [ 0 ]
 print iII1IiiIIII , I11iI , o00iIiiiII
 if not o00iIiiiII . startswith ( "http" ) :
  I11II1 = 'http://' + "" . join ( iiII11I . split ( '/' ) [ 2 : 3 ] )
  if o00iIiiiII . startswith ( "/" ) :
   o00iIiiiII = I11II1 + o00iIiiiII
  else :
   o00iIiiiII = I11II1 + '/' + o00iIiiiII
   if 46 - 46: I11iii11IIi
 I1ii1Ii1 = os . path . join ( iIiiiI , str ( iIiI1 ) + "captcha.jpg" )
 OoOoO = open ( I1ii1Ii1 , "wb" )
 print ' c capurl' , o00iIiiiII
 O00O0O0O0 = urllib2 . Request ( o00iIiiiII )
 O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'refer' in m :
  O00O0O0O0 . add_header ( 'Referer' , m [ 'refer' ] )
 if 'agent' in m :
  O00O0O0O0 . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  print 'adding cookie' , m [ 'setcookie' ]
  O00O0O0O0 . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 83 - 83: i11iIiiIii * o00ooooO0oO
  if 49 - 49: IiIIi1I1Iiii * I1ii + o0ooo - i11iIiiIii
  if 74 - 74: IiIIi1I1Iiii / IIii1I . iIiiiI1IiI1I1 - Ooo00oOo00o
  if 62 - 62: oOOOo0o0O / iIiiiI1IiI1I1 + I11iii11IIi % IiIi11i / I11iii11IIi + OOO0O
 urllib2 . urlopen ( O00O0O0O0 )
 ooO0O = urllib2 . urlopen ( O00O0O0O0 )
 if 2 - 2: i11iIiiIii - o00ooooO0oO + Ooo00oOo00o % OoOoo0 * oOOoo
 OoOoO . write ( ooO0O . read ( ) )
 ooO0O . close ( )
 OoOoO . close ( )
 iI111I1III = i111IiiI1Ii ( captcha = I1ii1Ii1 )
 oO0O0oo = iI111I1III . get ( )
 return oO0O0oo
 if 54 - 54: OOO0O0O0ooooo - OOooO . oOOOo0o0O % OOooO + OOooO
class i111IiiI1Ii ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 36 - 36: oOOOo0o0O % i11iIiiIii
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   Iiii1Ii = self . kbd . getText ( )
   self . close ( )
   return Iiii1Ii
  self . close ( )
  return False
  if 62 - 62: O00ooooo00 % I11iii11IIi
def I1iI1I1 ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 37 - 37: OoOoo0 * O00ooooo00
def OoOo ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 20 - 20: ooO00oo + I11iii11IIi - oOOOo0o0O - oOOOo0o0O - OOO0O
def ii ( ) :
 o0o000Oo = [ ]
 oO0o0O0o0OO00 = sys . argv [ 2 ]
 if len ( oO0o0O0o0OO00 ) >= 2 :
  iIiiiIi = sys . argv [ 2 ]
  OooooOo = iIiiiIi . replace ( '?' , '' )
  if ( iIiiiIi [ len ( iIiiiIi ) - 1 ] == '/' ) :
   iIiiiIi = iIiiiIi [ 0 : len ( iIiiiIi ) - 2 ]
  IIIiiiIiI = OooooOo . split ( '&' )
  o0o000Oo = { }
  for O0O0o0oOOO in range ( len ( IIIiiiIiI ) ) :
   OO0OOoooo0o = { }
   OO0OOoooo0o = IIIiiiIiI [ O0O0o0oOOO ] . split ( '=' )
   if ( len ( OO0OOoooo0o ) ) == 2 :
    o0o000Oo [ OO0OOoooo0o [ 0 ] ] = OO0OOoooo0o [ 1 ]
 return o0o000Oo
 if 13 - 13: IIiIiII11i + OOO0O0O0ooooo - OOO0O % IiIIi1I1Iiii / oOOoo . O00ooooo00
 if 60 - 60: IiIIi1I1Iiii . ooO00oo % IIiIiII11i - o00ooooO0oO
def oooOo ( ) :
 OOo00OoO = json . loads ( open ( iI111iI ) . read ( ) )
 OOo0 = len ( OOo00OoO )
 for O0O0o0oOOO in OOo00OoO :
  IIIII = O0O0o0oOOO [ 0 ]
  O0O = O0O0o0oOOO [ 1 ]
  oOoO0Oo0 = O0O0o0oOOO [ 2 ]
  try :
   i1III = O0O0o0oOOO [ 3 ]
   if i1III == None :
    raise
  except :
   if I1IiI . getSetting ( 'use_thumb' ) == "true" :
    i1III = oOoO0Oo0
   else :
    i1III = oOooOOOoOo
  try : OoooO0o = O0O0o0oOOO [ 5 ]
  except : OoooO0o = None
  try : IIIIi1 = O0O0o0oOOO [ 6 ]
  except : IIIIi1 = None
  if 7 - 7: IiIi11i + oOOoo
  if O0O0o0oOOO [ 4 ] == 0 :
   IIIii1II1II ( O0O , IIIII , oOoO0Oo0 , i1III , '' , '' , '' , 'fav' , OoooO0o , IIIIi1 , OOo0 )
  else :
   ooOoOoo0O ( IIIII , O0O , O0O0o0oOOO [ 4 ] , oOoO0Oo0 , oOooOOOoOo , '' , '' , '' , '' , 'fav' )
   if 32 - 32: IIii1I % IIiIiII11i / i11iIiiIii + oOOOo0o0O - o0ooo . OOooO
   if 86 - 86: O00ooooo00 / oOOoo * IIiIiII11i
def OOoO0OOoO0ooo ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 ii11i1ii1 = [ ]
 if not os . path . exists ( iI111iI + 'txt' ) :
  os . makedirs ( iI111iI + 'txt' )
 if not os . path . exists ( IiII ) :
  os . makedirs ( IiII )
 try :
  if 37 - 37: i11iIiiIii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( iI111iI ) == False :
  O00o0o0000o0o ( 'Making Favorites File' )
  ii11i1ii1 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  O0oo00o0O = open ( iI111iI , "w" )
  O0oo00o0O . write ( json . dumps ( ii11i1ii1 ) )
  O0oo00o0O . close ( )
 else :
  O00o0o0000o0o ( 'Appending Favorites' )
  O0oo00o0O = open ( iI111iI ) . read ( )
  oo = json . loads ( O0oo00o0O )
  oo . append ( ( name , url , iconimage , fanart , mode ) )
  i1I1I = open ( iI111iI , "w" )
  i1I1I . write ( json . dumps ( oo ) )
  i1I1I . close ( )
  if 12 - 12: OOO0O / oOOoo
  if 5 - 5: II1
def IIIii11i1I ( name ) :
 oo = json . loads ( open ( iI111iI ) . read ( ) )
 for i11IIIiI11 in range ( len ( oo ) ) :
  if oo [ i11IIIiI11 ] [ 0 ] == name :
   del oo [ i11IIIiI11 ]
   i1I1I = open ( iI111iI , "w" )
   i1I1I . write ( json . dumps ( oo ) )
   i1I1I . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 79 - 79: o00ooooO0oO
def ooO000 ( url ) :
 if I1IiI . getSetting ( 'Updatecommonresolvers' ) == 'true' :
  iiI1I1ii = os . path . join ( Iii1ii1II11i , 'genesisresolvers.py' )
  if xbmcvfs . exists ( iiI1I1ii ) :
   os . remove ( iiI1I1ii )
   if 31 - 31: oOOOo0o0O % o00ooooO0oO
  O0oo00oOOO0o = 'https://raw.githubusercontent.com/lambda81/lambda-addons/master/plugin.video.genesis/commonresolvers.py'
  II1iI111iiIIiI1I = urllib . urlretrieve ( O0oo00oOOO0o , iiI1I1ii )
  I1IiI . setSetting ( 'Updatecommonresolvers' , 'false' )
 try :
  import genesisresolvers
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Supremacy,Please enable Update Commonresolvers to Play in Settings. - ,10000)" )
  if 51 - 51: IIiIiII11i + oOOOo0o0O + OoOoo0
 i1Iiii = genesisresolvers . get ( url ) . result
 if url == i1Iiii or i1Iiii is None :
  if 87 - 87: ooO00oo / o00ooooO0oO - IiIIi1I1Iiii
  xbmc . executebuiltin ( "XBMC.Notification(Supremacy,Is Finding Your Link - ,5000)" )
  import resolveurl
  oOOoOOO0oOoo = resolveurl . HostedMediaFile ( url )
  if oOOoOOO0oOoo :
   o0O0ooooooo00 = resolveurl . resolve ( url )
   i1Iiii = o0O0ooooooo00
 if i1Iiii :
  if isinstance ( i1Iiii , list ) :
   for IIII1i1 in i1Iiii :
    I1111ii11IIII = I1IiI . getSetting ( 'quality' )
    if IIII1i1 [ 'quality' ] == 'HD' :
     o0O0ooooooo00 = IIII1i1 [ 'url' ]
     break
    elif IIII1i1 [ 'quality' ] == 'SD' :
     o0O0ooooooo00 = IIII1i1 [ 'url' ]
    elif IIII1i1 [ 'quality' ] == '1080p' and I1IiI . getSetting ( '1080pquality' ) == 'true' :
     o0O0ooooooo00 = IIII1i1 [ 'url' ]
     break
  else :
   o0O0ooooooo00 = i1Iiii
 return o0O0ooooooo00
def IiIi1II111I ( name , mu_playlist ) :
 import urlparse
 if I1IiI . getSetting ( 'ask_playlist_items' ) == 'true' :
  i111IiI1I = [ ]
  for O0O0o0oOOO in mu_playlist :
   o00o = urlparse . urlparse ( O0O0o0oOOO ) . netloc
   if o00o == '' :
    i111IiI1I . append ( name )
   else :
    i111IiI1I . append ( o00o )
  oOOOO = xbmcgui . Dialog ( )
  i11IIIiI11 = oOOOO . select ( 'Choose a video source' , i111IiI1I )
  if i11IIIiI11 >= 0 :
   if "&mode=19" in mu_playlist [ i11IIIiI11 ] :
    xbmc . Player ( ) . play ( ooO000 ( mu_playlist [ i11IIIiI11 ] . replace ( '&mode=19' , '' ) ) )
   elif "$doregex" in mu_playlist [ i11IIIiI11 ] :
    if 45 - 45: OOO0O + o00ooooO0oO . OOooO . OOooO
    iI1Iii11i1 = mu_playlist [ i11IIIiI11 ] . split ( '&regexs=' )
    if 34 - 34: I1ii - IiIi11i * IiIIi1I1Iiii / o0ooo
    O0O , Oo0O = oOO0oo ( iI1Iii11i1 [ 1 ] , iI1Iii11i1 [ 0 ] )
    xbmc . Player ( ) . play ( O0O )
   else :
    O0O = mu_playlist [ i11IIIiI11 ]
    xbmc . Player ( ) . play ( O0O )
 else :
  OoooO0o = xbmc . PlayList ( 1 )
  OoooO0o . clear ( )
  O0OO0oOOo = 0
  for O0O0o0oOOO in mu_playlist :
   O0OO0oOOo += 1
   iI1iiIi1 = xbmcgui . ListItem ( '%s) %s' % ( str ( O0OO0oOOo ) , name ) )
   OoooO0o . add ( O0O0o0oOOO , iI1iiIi1 )
   xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
   if 49 - 49: IiIi11i . iIiiiI1IiI1I1
   if 24 - 24: OOO0O0O0ooooo . II1 - Ooo00oOo00o * II1
def Ii11iiI ( name , url ) :
 if I1IiI . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('Supremacy','Choose a location to save files.',15000," + O0oo0OO0 + ")" )
  I1IiI . openSettings ( )
 iIiiiIi = { 'url' : url , 'download_path' : I1IiI . getSetting ( 'save_location' ) }
 downloader . download ( name , iIiiiIi )
 oOOOO = xbmcgui . Dialog ( )
 II1iiI = oOOOO . yesno ( 'Supremacy' , 'Do you want to add this file as a source?' )
 if II1iiI :
  O0I11Iiii1I ( os . path . join ( I1IiI . getSetting ( 'save_location' ) , name ) )
  if 71 - 71: o00ooooO0oO - o0ooo - oOOOo0o0O
  if 28 - 28: IIii1I
def ooOoOoo0O ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False ) :
 if 7 - 7: o0ooo % ooO00oo * I11iii11IIi
 O0O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOiI11I = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 o0O0O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  Iii11I1iII1 = [ ]
  if showcontext == 'source' :
   if name in str ( i1 ) :
    Iii11I1iII1 . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'download' :
   Iii11I1iII1 . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'fav' :
   Iii11I1iII1 . append ( ( 'Remove from Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 24 - 24: I1ii / o00ooooO0oO / OoOoo0 % I11iii11IIi / OOO0O * IiIi11i
  if not name in o0oOoO00o :
   Iii11I1iII1 . append ( ( 'Add to Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  o0O0O0o . addContextMenuItems ( Iii11I1iII1 )
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0O00 , listitem = o0O0O0o , isFolder = True )
 if 8 - 8: oOOoo
 return OOiI11I
def iIIi1 ( url , title , media_type = 'video' ) :
 if 75 - 75: ooO00oo % i11iIiiIii + IIii1I
 if 92 - 92: I11iii11IIi % OOO0O0O0ooooo
 import youtubedl
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 55 - 55: IIii1I * OOooO
   YDStreamExtractor . manageDownloads ( )
  else :
   ooIi11iI = xbmc . Player ( ) . getPlayingFile ( )
   if 22 - 22: oOOOo0o0O
   ooIi11iI = ooIi11iI . split ( '|User-Agent=' ) [ 0 ]
   iI1iiIi1 = { 'url' : ooIi11iI , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = iI1iiIi1 )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 22 - 22: OOooO * OoOoo0 - IiIIi1I1Iiii * OOO0O0O0ooooo / i11iIiiIii
def OOooO0Oo0o000 ( site_name , search_term = None ) :
 I1ii11 = ''
 if os . path . exists ( IiII ) == False or I1IiI . getSetting ( 'clearseachhistory' ) == 'true' :
  I1IiI1iI11 ( IiII , '' )
  I1IiI . setSetting ( "clearseachhistory" , "false" )
 if site_name == 'history' :
  I11i1iIiIIIIIii = OoO0O0oO00 ( IiII )
  o0 = re . compile ( '(.+?):(.*?)(?:\r|\n)' ) . findall ( I11i1iIiIIIIIii )
  if 17 - 17: IIii1I + IIiIiII11i
  for IIIII , search_term in o0 :
   if 'plugin://' in search_term :
    IIIii1II1II ( search_term , IIIII , I1ii11 , '' , '' , '' , '' , '' , None , '' , total = int ( len ( o0 ) ) )
   else :
    ooOoOoo0O ( IIIII + ':' + search_term , IIIII , 26 , O0oo0OO0 , I1i1iiI1 , '' , '' , '' , '' )
 if not search_term :
  ii111I = xbmc . Keyboard ( '' , 'Enter Search Term' )
  ii111I . doModal ( )
  if ( ii111I . isConfirmed ( ) == False ) :
   return
  search_term = ii111I . getText ( )
  if len ( search_term ) == 0 :
   return
 search_term = search_term . replace ( ' ' , '+' )
 search_term = search_term . encode ( 'utf-8' )
 if 'youtube' in site_name :
  if 57 - 57: o0ooo / o00ooooO0oO
  import _ytplist
  if 13 - 13: II1 + Ooo00oOo00o
  ii1IIii = { }
  ii1IIii = _ytplist . YoUTube ( 'searchYT' , youtube = search_term , max_page = 4 , nosave = 'nosave' )
  OOo0 = len ( ii1IIii )
  for O0OO0oOOo in ii1IIii :
   try :
    IIIII = ii1IIii [ O0OO0oOOo ] [ 'title' ]
    iI1i11 = ii1IIii [ O0OO0oOOo ] [ 'date' ]
    try :
     IiI11i1I11111 = ii1IIii [ O0OO0oOOo ] [ 'desc' ]
    except Exception :
     IiI11i1I11111 = 'UNAVAIABLE'
     if 34 - 34: IIiIiII11i * I11iii11IIi * I1ii + OOO0O
    O0O = 'plugin://plugin.video.youtube/play/?video_id=' + ii1IIii [ O0OO0oOOo ] [ 'url' ]
    I1ii11 = 'http://img.youtube.com/vi/' + ii1IIii [ O0OO0oOOo ] [ 'url' ] + '/0.jpg'
    IIIii1II1II ( O0O , IIIII , I1ii11 , '' , '' , '' , '' , '' , None , '' , OOo0 )
   except Exception :
    O00o0o0000o0o ( 'This item is ignored::' )
  II1iO00Oo = site_name + ':' + search_term + '\n'
  I1IiI1iI11 ( os . path . join ( iIiiiI , 'history' ) , II1iO00Oo , append = True )
 elif 'dmotion' in site_name :
  iiiO0ooO0O0Ooo0o = "https://api.dailymotion.com"
  if 25 - 25: oOOOo0o0O * oOOOo0o0O / I1ii % IiIIi1I1Iiii
  import _DMsearch
  i1iiiiI11ii = str ( I1IiI . getSetting ( 'familyFilter' ) )
  _DMsearch . listVideos ( iiiO0ooO0O0Ooo0o + "/videos?fields=description,duration,id,owner.username,taken_time,thumbnail_large_url,title,views_total&search=" + search_term + "&sort=relevance&limit=100&family_filter=" + i1iiiiI11ii + "&localization=en_EN&page=1" )
  if 73 - 73: O00ooooo00 % II1
  II1iO00Oo = site_name + ':' + search_term + '\n'
  I1IiI1iI11 ( os . path . join ( iIiiiI , 'history' ) , II1iO00Oo , append = True )
 elif 'IMDBidplay' in site_name :
  iiiO0ooO0O0Ooo0o = "http://www.omdbapi.com/?t="
  O0O = iiiO0ooO0O0Ooo0o + search_term
  if 25 - 25: I1ii + iIiiiI1IiI1I1
  O0o0Oo = dict ( { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; rv:33.0) Gecko/20100101 Firefox/33.0' , 'Referer' : 'http://joker.org/' , 'Accept-Encoding' : 'gzip, deflate' , 'Content-Type' : 'application/json;charset=utf-8' , 'Accept' : 'application/json, text/plain, */*' } )
  if 79 - 79: IiIi11i
  OO0o0oO = requests . get ( O0O , headers = O0o0Oo )
  oo = OO0o0oO . json ( )
  iI1111i = oo [ 'Response' ]
  if iI1111i == 'True' :
   I1Ii1iIIIIi = oo [ 'imdbID' ]
   IIIII = oo [ 'Title' ] + oo [ 'Released' ]
   oOOOO = xbmcgui . Dialog ( )
   II1iiI = oOOOO . yesno ( 'Check Movie Title' , 'PLAY :: %s ?' % IIIII )
   if II1iiI :
    O0O = 'plugin://plugin.video.pulsar/movie/' + I1Ii1iIIIIi + '/play'
    II1iO00Oo = IIIII + ':' + O0O + '\n'
    I1IiI1iI11 ( IiII , II1iO00Oo , append = True )
    return O0O
  else :
   xbmc . executebuiltin ( "XBMC.Notification(SimpleKore,No IMDB match found ,7000," + O0oo0OO0 + ")" )
   if 14 - 14: II1 . o0ooo . OoOoo0
def I1IIIIIi1IIiI ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def III11I11ii ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def O0OoO0oO00 ( s ) : return "" . join ( filter ( lambda I1i1Iiiii : ord ( I1i1Iiiii ) < 128 , s ) )
if 2 - 2: o00ooooO0oO - OOO0O + o0ooo * Ooo00oOo00o / OOooO
def iIIiI11iI1Ii1 ( command ) :
 oo = ''
 try :
  oo = xbmc . executeJSONRPC ( III11I11ii ( command ) )
 except UnicodeEncodeError :
  oo = xbmc . executeJSONRPC ( I1IIIIIi1IIiI ( command ) )
  if 94 - 94: IiIi11i / i11iIiiIii % OOO0O0O0ooooo
 return III11I11ii ( oo )
 if 70 - 70: OoOoo0 - IiIIi1I1Iiii / II1 % II1
 if 95 - 95: II1 % II1 . oOOoo
def I111i1II ( ) :
 III1ii = xbmc . getSkinDir ( )
 if III1ii == 'skin.confluence' :
  xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 elif III1ii == 'skin.aeon.nox' :
  xbmc . executebuiltin ( 'Container.SetViewMode(511)' )
 else :
  xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  if 38 - 38: OOO0O + I11iii11IIi
  if 68 - 68: OOO0O0O0ooooo
def o0oOoO00 ( url ) :
 oOO000 = III11I11ii ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":["thumbnail","title","year","dateadded","fanart","rating","season","episode","studio"]},"id":1}' ) % url
 if 95 - 95: OOO0O0O0ooooo + IIiIiII11i + I11iii11IIi . oOOOo0o0O
 OO0 = json . loads ( iIIiI11iI1Ii1 ( oOO000 ) )
 for O0O0o0oOOO in OO0 [ 'result' ] [ 'files' ] :
  url = O0O0o0oOOO [ 'file' ]
  IIIII = O0OoO0oO00 ( O0O0o0oOOO [ 'label' ] )
  I1ii11 = O0OoO0oO00 ( O0O0o0oOOO [ 'thumbnail' ] )
  try :
   oOooOOOoOo = O0OoO0oO00 ( O0O0o0oOOO [ 'fanart' ] )
  except Exception :
   oOooOOOoOo = ''
  try :
   iI1i11 = O0O0o0oOOO [ 'year' ]
  except Exception :
   iI1i11 = ''
  try :
   oOOOoo00 = O0O0o0oOOO [ 'episode' ]
   Ooo0oOooo0 = O0O0o0oOOO [ 'season' ]
   if oOOOoo00 == - 1 or Ooo0oOooo0 == - 1 :
    IiI11i1I11111 = ''
   else :
    IiI11i1I11111 = '[COLOR yellow] S' + str ( Ooo0oOooo0 ) + '[/COLOR][COLOR hotpink] E' + str ( oOOOoo00 ) + '[/COLOR]'
  except Exception :
   IiI11i1I11111 = ''
  try :
   IIIIIIi111i = O0O0o0oOOO [ 'studio' ]
   if IIIIIIi111i :
    IiI11i1I11111 += '\n Studio:[COLOR steelblue] ' + IIIIIIi111i [ 0 ] + '[/COLOR]'
  except Exception :
   IIIIIIi111i = ''
   if 37 - 37: OOooO
  if O0O0o0oOOO [ 'filetype' ] == 'file' :
   IIIii1II1II ( url , IIIII , I1ii11 , oOooOOOoOo , IiI11i1I11111 , '' , iI1i11 , '' , None , '' , total = len ( OO0 [ 'result' ] [ 'files' ] ) )
   if 33 - 33: Ooo00oOo00o - OOO0O0O0ooooo - Ooo00oOo00o
   if 94 - 94: ooO00oo * OoOoo0 * II1 / o0ooo . ooO00oo - o0ooo
  else :
   ooOoOoo0O ( IIIII , url , 53 , I1ii11 , oOooOOOoOo , IiI11i1I11111 , '' , iI1i11 , '' )
   if 13 - 13: oOOOo0o0O / ooO00oo - Ooo00oOo00o / oOOOo0o0O . O00ooooo00
   if 22 - 22: OOO0O0O0ooooo - OoOoo0 + o00ooooO0oO . oOOoo * O00ooooo00
def IIIii1II1II ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" ) :
 if 26 - 26: IIii1I * o0ooo . OoOoo0
 Iii11I1iII1 = [ ]
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 OOiI11I = True
 if 10 - 10: o00ooooO0oO * I1ii % IiIIi1I1Iiii - OoOoo0 % IiIIi1I1Iiii
 if regexs :
  o0O0OOO0Ooo = '17'
  if 65 - 65: OOooO * IIii1I / OOO0O0O0ooooo . OoOoo0
  Iii11I1iII1 . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif any ( x in url for x in OO0o ) and url . startswith ( 'http' ) :
  o0O0OOO0Ooo = '19'
  if 94 - 94: IiIIi1I1Iiii . IiIi11i * i11iIiiIii - o0ooo . OOooO
  Iii11I1iII1 . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  o0O0OOO0Ooo = '18'
  if 98 - 98: oOOOo0o0O + oOOoo
  Iii11I1iII1 . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if I1IiI . getSetting ( 'dlaudioonly' ) == 'true' :
   Iii11I1iII1 . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'magnet:?xt=' ) or '.torrent' in url :
  if 52 - 52: IiIIi1I1Iiii / I11iii11IIi - o00ooooO0oO . OOooO
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
  url = 'plugin://plugin.video.pulsar/play?uri=' + url
  o0O0OOO0Ooo = '12'
  if 50 - 50: IIii1I - OOooO - OoOoo0
 else :
  o0O0OOO0Ooo = '12'
  if 60 - 60: IIii1I * IiIi11i
  Iii11I1iII1 . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 O0O00 = sys . argv [ 0 ] + "?"
 oO0O0o0o000 = False
 if 6 - 6: I11iii11IIi / IiIi11i + OOooO - o0ooo * oOOOo0o0O + IiIi11i
 if playlist :
  if I1IiI . getSetting ( 'add_playlist' ) == "false" :
   O0O00 += "url=" + urllib . quote_plus ( url ) + "&mode=" + o0O0OOO0Ooo
  else :
   O0O00 += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR magenta] (' + str ( len ( playlist ) ) + ' items )[/COLOR]'
   oO0O0o0o000 = True
 else :
  O0O00 += "url=" + urllib . quote_plus ( url ) + "&mode=" + o0O0OOO0Ooo
 if regexs :
  O0O00 += "&regexs=" + regexs
 if not setCookie == '' :
  O0O00 += "&setCookie=" + urllib . quote_plus ( setCookie )
  if 76 - 76: iIiiiI1IiI1I1 - II1 % ooO00oo
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
 o0O0O0o . setProperty ( "Fanart_Image" , fanart )
 if 40 - 40: oOOoo
 if ( not oO0O0o0o000 ) and not any ( x in url for x in Oo0Ooo ) :
  if regexs :
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) :
    if 59 - 59: OoOoo0 * II1 + oOOOo0o0O . IIii1I / O00ooooo00
    o0O0O0o . setProperty ( 'IsPlayable' , 'true' )
  else :
   o0O0O0o . setProperty ( 'IsPlayable' , 'true' )
 else :
  O00o0o0000o0o ( 'NOT setting isplayable' + url )
  if 75 - 75: OoOoo0 . oOOOo0o0O - IIii1I * Ooo00oOo00o * OOooO
 if showcontext :
  Iii11I1iII1 = [ ]
  if showcontext == 'fav' :
   Iii11I1iII1 . append (
 ( 'Remove from Add-on Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) )
 )
  elif not name in o0oOoO00o :
   ooo0OO0OOooO0 = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) )
 )
   if playlist :
    ooo0OO0OOooO0 += 'playlist=' + urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) )
   if regexs :
    ooo0OO0OOooO0 += "&regexs=" + regexs
   Iii11I1iII1 . append ( ( 'Add to Add-on Favorites' , 'XBMC.RunPlugin(%s)' % ooo0OO0OOooO0 ) )
  o0O0O0o . addContextMenuItems ( Iii11I1iII1 )
  if 96 - 96: oOOOo0o0O + oOOOo0o0O % ooO00oo % oOOOo0o0O
 if not playlist is None :
  if I1IiI . getSetting ( 'add_playlist' ) == "false" :
   IiiI1I = name . split ( ') ' ) [ 1 ]
   Ii11iIII = [
 ( 'Play ' + IiiI1I + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( IiiI1I ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
   o0O0O0o . addContextMenuItems ( Ii11iIII )
   if 58 - 58: OOO0O0O0ooooo
   if 91 - 91: OOooO / OOO0O . OOooO - o0ooo + OOO0O
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0O00 , listitem = o0O0O0o , totalItems = total )
 if 72 - 72: oOOoo . ooO00oo * OOO0O / OOO0O / OOooO
 return OOiI11I
 if 13 - 13: O00ooooo00
def Ii1IIII1ii1I ( url , name , iconimage , setresolved = True ) :
 if setresolved :
  o0O0O0o = xbmcgui . ListItem ( name , iconImage = iconimage )
  o0O0O0o . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  o0O0O0o . setProperty ( "IsPlayable" , "true" )
  o0O0O0o . setPath ( str ( url ) )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , o0O0O0o )
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 79 - 79: OOO0O + o0ooo % IiIIi1I1Iiii * o0ooo
  if 21 - 21: OOooO
  if 24 - 24: OOooO / IiIi11i
  if 61 - 61: IIii1I + I1ii
def OOooOO00O0OO00oo ( link ) :
 O0O = urllib . urlopen ( link )
 i1IiiI = O0O . read ( )
 O0O . close ( )
 O0OOO0 = i1IiiI . split ( "Jetzt" )
 o0OIi = O0OOO0 [ 1 ] . split ( 'programm/detail.php?const_id=' )
 IIi1iiI = o0OIi [ 1 ] . split ( '<br /><a href="/' )
 o0o = IIi1iiI [ 0 ] [ 40 : len ( IIi1iiI [ 0 ] ) ]
 oOO00OO0o0O = o0OIi [ 2 ] . split ( "</a></p></div>" )
 III1IiiIiiI1i = oOO00OO0o0O [ 0 ] [ 17 : len ( oOO00OO0o0O [ 0 ] ) ]
 III1IiiIiiI1i = III1IiiIiiI1i . encode ( 'utf-8' )
 return "  - " + III1IiiIiiI1i + " - " + o0o
 if 73 - 73: O00ooooo00 % OoOoo0 - IiIi11i / o0ooo % Ooo00oOo00o / o00ooooO0oO
def O00Oo ( ) :
 II ( '[COLOR aqua] Featured 24/7[/COLOR]' , '' , 907 , 'http://stephen-builds.uk/art/24%207%20shows.png' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 II ( '[COLOR aqua] 24/7 Tv Shows[/COLOR]' , '' , 908 , 'http://stephen-builds.uk/art/rolling-stone-100-best-tv-shows-of-all-time-c76cdd0b-2e04-4769-84c1-0faab178ddbf.jpg' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 II ( '[COLOR aqua] 24/7 Movies[/COLOR]' , '' , 909 , 'http://stephen-builds.uk/art/24%20MOVIES.png' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 II ( '[COLOR aqua] 24/7 Cable[/COLOR]' , '' , 910 , 'http://stephen-builds.uk/art/cableheader-graypurple-590x236.jpg' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 II ( '[COLOR aqua] 24/7 Random Stream[/COLOR]' , '' , 911 , 'http://stephen-builds.uk/art/maxresdefault.jpg' , 'http://stephen-builds.uk/art/20839702_10207884860798337_363786087_o.jpg' , '' , '' )
 if 10 - 10: OoOoo0
def o0o0OO0OO000OO ( ) :
 O0O = 'http://arconaitv.me/'
 i11IIIiI11 = 'index.php#shows'
 I11i1 = BeautifulSoup ( requests . get ( O0O + i11IIIiI11 ) . content )
 O00oO = I11i1 . findAll ( 'div' , attrs = { 'class' : 'stream-nav shows' } )
 for I11i1I1I in O00oO :
  oO0OOoO0 = I11i1I1I . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I11II1i in oO0OOoO0 :
   O00o0000OO = I11II1i . text
  O0Ooo0O0OO = I11i1I1I . findAll ( 'a' )
  for I11II1i in O0Ooo0O0OO :
   if I11II1i . has_key ( 'href' ) :
    o00oO0oo0OO = O0O + I11II1i [ 'href' ]
   if I11II1i . has_key ( 'title' ) :
    IIIII = I11II1i [ 'title' ]
   iiI1iiii1Iii = { 'User-Agent' : random_agent ( ) }
   OoOOOOOoOo0 = requests . get ( o00oO0oo0OO , headers = iiI1iiii1Iii ) . content
   iIioOo = packets ( OoOOOOOoOo0 )
   if 66 - 66: iIiiiI1IiI1I1 + Ooo00oOo00o
   o0 = re . compile ( "'https:(.+?)'" ) . findall ( iIioOo )
   for II1iI1iiiI in o0 :
    II1iI1iiiI = II1iI1iiiI . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    OoOoO00o00 = 'https:' + II1iI1iiiI + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    ooooooO0oo ( IIIII , OoOoO00o00 , 906 , '' , '' , '' , '' )
    if 51 - 51: IiIIi1I1Iiii * IIii1I . II1 . oOOoo - oOOOo0o0O / IIiIiII11i
    if 98 - 98: iIiiiI1IiI1I1 + oOOoo + II1 / O00ooooo00 - oOOoo
def O0o0Oo0OOooo ( ) :
 O0O = 'http://arconaitv.me/'
 i11IIIiI11 = 'index.php#movies'
 I11i1 = BeautifulSoup ( requests . get ( O0O + i11IIIiI11 ) . content )
 O00oO = I11i1 . findAll ( 'div' , attrs = { 'class' : 'stream-nav movies' } )
 for I11i1I1I in O00oO :
  oO0OOoO0 = I11i1I1I . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I11II1i in oO0OOoO0 :
   O00o0000OO = I11II1i . text
  O0Ooo0O0OO = I11i1I1I . findAll ( 'a' )
  for I11II1i in O0Ooo0O0OO :
   if I11II1i . has_key ( 'href' ) :
    o00oO0oo0OO = O0O + I11II1i [ 'href' ]
   if I11II1i . has_key ( 'title' ) :
    IIIII = I11II1i [ 'title' ]
   iiI1iiii1Iii = { 'User-Agent' : random_agent ( ) }
   OoOOOOOoOo0 = requests . get ( o00oO0oo0OO , headers = iiI1iiii1Iii ) . content
   iIioOo = packets ( OoOOOOOoOo0 )
   if 100 - 100: I1ii + OOO0O0O0ooooo . IIiIiII11i + O00ooooo00 - I11iii11IIi + o0ooo
   o0 = re . compile ( "'https:(.+?)'" ) . findall ( iIioOo )
   for II1iI1iiiI in o0 :
    II1iI1iiiI = II1iI1iiiI . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    OoOoO00o00 = 'https:' + II1iI1iiiI + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    ooooooO0oo ( IIIII , OoOoO00o00 , 906 , '' , '' , '' , '' )
    if 65 - 65: iIiiiI1IiI1I1 / IiIIi1I1Iiii
    if 42 - 42: i11iIiiIii . OOO0O0O0ooooo
def o0oo0Oo ( ) :
 O0O = 'http://arconaitv.me/'
 i11IIIiI11 = 'index.php#cable'
 I11i1 = BeautifulSoup ( requests . get ( O0O + i11IIIiI11 ) . content )
 O00oO = I11i1 . findAll ( 'div' , attrs = { 'class' : 'stream-nav cable' } )
 for I11i1I1I in O00oO :
  oO0OOoO0 = I11i1I1I . findAll ( 'div' , attrs = { 'class' : 'stream-initial' } )
  for I11II1i in oO0OOoO0 :
   O00o0000OO = I11II1i . text
  O0Ooo0O0OO = I11i1I1I . findAll ( 'a' )
  for I11II1i in O0Ooo0O0OO :
   if I11II1i . has_key ( 'href' ) :
    o00oO0oo0OO = O0O + I11II1i [ 'href' ]
   if I11II1i . has_key ( 'title' ) :
    IIIII = I11II1i [ 'title' ]
   iiI1iiii1Iii = { 'User-Agent' : random_agent ( ) }
   OoOOOOOoOo0 = requests . get ( o00oO0oo0OO , headers = iiI1iiii1Iii ) . content
   iIioOo = packets ( OoOOOOOoOo0 )
   if 10 - 10: OOO0O
   o0 = re . compile ( "'https:(.+?)'" ) . findall ( iIioOo )
   for II1iI1iiiI in o0 :
    II1iI1iiiI = II1iI1iiiI . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
    OoOoO00o00 = 'https:' + II1iI1iiiI + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
    ooooooO0oo ( IIIII , OoOoO00o00 , 906 , '' , '' , '' , '' )
    if 87 - 87: IiIIi1I1Iiii % oOOoo
def ooO0o0oO0 ( ) :
 OOoo0O = 'http://arconaitv.me/stream.php?id=random'
 iiI1iiii1Iii = { 'User-Agent' : random_agent ( ) }
 OoOOOOOoOo0 = requests . get ( OOoo0O , headers = iiI1iiii1Iii ) . content
 iIioOo = packets ( OoOOOOOoOo0 )
 if 66 - 66: o00ooooO0oO % OOO0O0O0ooooo
 o0 = re . compile ( "'https:(.+?)'" ) . findall ( iIioOo )
 for II1iI1iiiI in o0 :
  II1iI1iiiI = II1iI1iiiI . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
  OoOoO00o00 = 'https:' + II1iI1iiiI + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
  ooooooO0oo ( 'Random Pick' , OoOoO00o00 , 906 , '' , '' , '' , '' )
  if 55 - 55: IiIi11i % OoOoo0 / i11iIiiIii
def I1111 ( ) :
 O0O = 'http://arconaitv.me/'
 i11IIIiI11 = 'index.php#shows'
 if 90 - 90: o00ooooO0oO % Ooo00oOo00o . o00ooooO0oO
 I11i1 = BeautifulSoup ( requests . get ( O0O + i11IIIiI11 ) . content )
 O00oO = I11i1 . findAll ( 'div' , attrs = { 'class' : 'box-content' } )
 for I11i1I1I in O00oO :
  oO0OOoO0 = I11i1I1I . findAll ( 'a' )
  for I11II1i in oO0OOoO0 :
   if I11II1i . has_key ( 'href' ) :
    o00oO0oo0OO = O0O + I11II1i [ 'href' ]
   if I11II1i . has_key ( 'title' ) :
    IIIII = I11II1i [ 'title' ]
   O0O0OOOOoo = I11II1i . findAll ( 'img' )
   for oOo0O0Oo00oO in O0O0OOOOoo :
    o00oOO0o = O0O + oOo0O0Oo00oO [ 'src' ]
    iiI1iiii1Iii = { 'User-Agent' : random_agent ( ) }
    OoOOOOOoOo0 = requests . get ( o00oO0oo0OO , headers = iiI1iiii1Iii ) . content
    iIioOo = packets ( OoOOOOOoOo0 )
    if 51 - 51: OOO0O
    o0 = re . compile ( "'https:(.+?)'" ) . findall ( iIioOo )
    for II1iI1iiiI in o0 :
     II1iI1iiiI = II1iI1iiiI . replace ( '\\' , '' ) . replace ( 'm3u8/' , 'm3u8' )
     OoOoO00o00 = 'https:' + II1iI1iiiI + '|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
     ooooooO0oo ( IIIII , OoOoO00o00 , 906 , o00oOO0o , o00oOO0o , '' , '' )
     if 70 - 70: i11iIiiIii
def ooooooO0oo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description )
 OOiI11I = True
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = " " , thumbnailImage = iconimage )
 o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0O0o . setProperty ( "Fanart_Image" , fanart )
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0O00 , listitem = o0O0O0o , isFolder = False )
 return OOiI11I
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 57 - 57: OoOoo0 % oOOOo0o0O + IiIi11i * oOOoo . IiIIi1I1Iiii
 if 78 - 78: II1 / O00ooooo00 . oOOOo0o0O
def II ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus (
 name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus (
 fanart ) + "&description=" + urllib . quote_plus ( description ) + "&extra=" + urllib . quote_plus ( extra )
 OOiI11I = True
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 o0O0O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0O0o . setProperty ( "Fanart_Image" , fanart )
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0O00 , listitem = o0O0O0o , isFolder = True )
 return OOiI11I
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 88 - 88: OoOoo0 + IIiIiII11i - OoOoo0 / II1 - i11iIiiIii
def OO ( name , url ) :
 import resolveurl
 try :
  i1II1 = resolveurl . resolve ( url )
  xbmc . Player ( ) . play ( i1II1 , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 24 - 24: IIii1I
 if 89 - 89: oOOoo / O00ooooo00 - o0ooo % IIiIiII11i . IiIIi1I1Iiii - OOO0O0O0ooooo
def Oo00oO0O ( url , regex ) :
 oo = o0O0 ( url )
 try :
  O0OO0oOOo = re . findall ( regex , oo ) [ 0 ]
  return O0OO0oOOo
 except :
  O00o0o0000o0o ( 'regex failed' )
  O00o0o0000o0o ( regex )
  return
  if 71 - 71: Ooo00oOo00o % IIiIiII11i - OOooO . OOooO
def I1I1 ( name , url , iconimage ) :
 if 78 - 78: OoOoo0 . oOOOo0o0O + I1ii * OOooO - O00ooooo00
 if 27 - 27: oOOoo % O00ooooo00 . IiIIi1I1Iiii % o00ooooO0oO
 import resolveurl
 if 'acestream' in url :
  O00o0OO = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  o0O0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  o0O0O0o . setPath ( url )
  xbmc . Player ( ) . play ( O00o0OO , o0O0O0o , False )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  Ii111iIi1iIi = resolveurl . HostedMediaFile ( url ) . resolve ( )
  o0O0O0o = xbmcgui . ListItem ( name , iconImage = O0oo0OO0 , thumbnailImage = O0oo0OO0 )
  o0O0O0o . setPath ( Ii111iIi1iIi )
  xbmc . Player ( ) . play ( Ii111iIi1iIi , o0O0O0o , False )
  time . sleep ( 2 )
  quit ( )
 else :
  Ii111iIi1iIi = url
  o0O0O0o = xbmcgui . ListItem ( name , iconImage = O0oo0OO0 , thumbnailImage = O0oo0OO0 )
  o0O0O0o . setPath ( Ii111iIi1iIi )
  xbmc . Player ( ) . play ( Ii111iIi1iIi , o0O0O0o , False )
  time . sleep ( 2 )
  quit ( )
  if 10 - 10: ooO00oo / II1
  if 50 - 50: i11iIiiIii - II1 . I1ii + OOO0O0O0ooooo . O00ooooo00
  if 91 - 91: o0ooo . OOooO % IiIIi1I1Iiii - OOooO . I1ii % i11iIiiIii
def iIiO0O ( name , url , mode , iconimage , fanart , description = '' ) :
 if not iconimage :
  iconimage = O0oo0OO0
 if not fanart :
  fanart = I1i1iiI1
 O0O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOiI11I = True
 o0O0O0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 o0O0O0o . setProperty ( "fanart_Image" , fanart )
 o0O0O0o . setProperty ( "icon_Image" , iconimage )
 o0O0O0o . setInfo ( 'video' , { 'Plot' : description } )
 oOOoooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 O0oIi1iIiIi1I11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0O0O0o . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + oOOoooo + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + O0oIi1iIiIi1I11 + ')' ) ] )
 if 12 - 12: IIii1I . IiIi11i
 OOiI11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0O00 , listitem = o0O0O0o , isFolder = False )
 return OOiI11I
 if 36 - 36: o00ooooO0oO . ooO00oo * II1 - o0ooo
def O0oo0O ( url ) :
 O00O0O0O0 = urllib2 . Request ( url )
 O00O0O0O0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 O00O0O0O0 . add_header ( 'Referer' , 'https://livesportshd.net/lfctv' )
 ooO0O = urllib2 . urlopen ( O00O0O0O0 , timeout = 10 )
 I11II1i = ooO0O . read ( )
 I11II1i = I11II1i . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 ooO0O . close ( )
 I11II1i = I11II1i . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 return I11II1i
 if 94 - 94: OOO0O0O0ooooo % o00ooooO0oO . oOOOo0o0O . IiIIi1I1Iiii / OoOoo0
def oOo0o ( ) :
 if 39 - 39: oOOOo0o0O + Ooo00oOo00o
 O0O = 'http://jkarakizi.com/updated-acestream-channels-for-2018/'
 I11II1i = O0oo0O ( O0O )
 o0 = re . compile ( '<tr>(.*?)</tr>' ) . findall ( I11II1i )
 for OOo00OoO in o0 :
  try :
   O0 = re . compile ( '<td class=".+?">(.*?)</td>' ) . findall ( OOo00OoO ) [ 0 ]
   I11II1i = re . compile ( '<td class="tg-yw4l">(.*?)</td>' ) . findall ( OOo00OoO ) [ 1 ]
   I11II1i = 'acestream://' + I11II1i + '&name=My+acestream+channel'
   iIiO0O ( "[COLOR aqua]" + O0 + "[/COLOR]" , I11II1i , 505 , oOoO0Oo0 , oOooOOOoOo , O0 + ' Acestream Channels Can Sometimes Go Down' )
  except : pass
  if 80 - 80: oOOOo0o0O % Ooo00oOo00o / I11iii11IIi
  if 54 - 54: IiIIi1I1Iiii % Ooo00oOo00o - oOOOo0o0O - OoOoo0
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 71 - 71: IiIi11i . i11iIiiIii
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 56 - 56: OOO0O0O0ooooo * OOooO + OOooO * IIii1I / IiIi11i * o00ooooO0oO
iIiiiIi = ii ( )
if 25 - 25: IIii1I . OoOoo0 * i11iIiiIii + IiIIi1I1Iiii * OoOoo0
O0O = None
IIIII = None
o0O0OOO0Ooo = None
OoooO0o = None
oOoO0Oo0 = None
oOooOOOoOo = I1i1iiI1
OoooO0o = None
o0oOooO0oo00 = None
IIIIi1 = None
if 70 - 70: IIiIiII11i + oOOoo
try :
 O0O = urllib . unquote_plus ( iIiiiIi [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 IIIII = urllib . unquote_plus ( iIiiiIi [ "name" ] )
except :
 pass
try :
 oOoO0Oo0 = urllib . unquote_plus ( iIiiiIi [ "iconimage" ] )
except :
 pass
try :
 oOooOOOoOo = urllib . unquote_plus ( iIiiiIi [ "fanart" ] )
except :
 pass
try :
 o0O0OOO0Ooo = int ( iIiiiIi [ "mode" ] )
except :
 pass
try :
 OoooO0o = eval ( urllib . unquote_plus ( iIiiiIi [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 o0oOooO0oo00 = int ( iIiiiIi [ "fav_mode" ] )
except :
 pass
try :
 IIIIi1 = iIiiiIi [ "regexs" ]
except :
 pass
try :
 o0oO0O00O0Oo0 = iIiiiIi [ "extra" ]
except :
 pass
O00o0o0000o0o ( "Mode: " + str ( o0O0OOO0Ooo ) )
if not O0O is None :
 O00o0o0000o0o ( "URL: " + str ( O0O . encode ( 'utf-8' ) ) )
O00o0o0000o0o ( "Name: " + str ( IIIII ) )
if 53 - 53: O00ooooo00 . O00ooooo00 - OoOoo0 / OOooO - I11iii11IIi % IIiIiII11i
if o0O0OOO0Ooo == None :
 O00o0o0000o0o ( "Index" )
 iiI1IiI ( )
 if 65 - 65: OOooO . II1 - OOO0O0O0ooooo . OOooO - i11iIiiIii
elif o0O0OOO0Ooo == 1 :
 O00o0o0000o0o ( "getData" )
 Oooo ( O0O , oOooOOOoOo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 29 - 29: OOO0O . IIiIiII11i % I1ii - i11iIiiIii
elif o0O0OOO0Ooo == 2 :
 O00o0o0000o0o ( "getChannelItems" )
 i1i1I111iIi1 ( IIIII , O0O , oOooOOOoOo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 27 - 27: OOO0O - i11iIiiIii % o00ooooO0oO / IiIIi1I1Iiii . IiIIi1I1Iiii / II1
elif o0O0OOO0Ooo == 3 :
 O00o0o0000o0o ( "getSubChannelItems" )
 O00oO0 ( IIIII , O0O , oOooOOOoOo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 76 - 76: OoOoo0 * Ooo00oOo00o . IIii1I % II1 % OOO0O
elif o0O0OOO0Ooo == 4 :
 O00o0o0000o0o ( "getFavorites" )
 oooOo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 39 - 39: iIiiiI1IiI1I1 * I11iii11IIi . OOO0O0O0ooooo * OoOoo0
elif o0O0OOO0Ooo == 5 :
 O00o0o0000o0o ( "addFavorite" )
 try :
  IIIII = IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IIIII = IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOoO0OOoO0ooo ( IIIII , O0O , oOoO0Oo0 , oOooOOOoOo , o0oOooO0oo00 )
 if 89 - 89: oOOoo - IiIi11i . OoOoo0 - o00ooooO0oO - IIiIiII11i
elif o0O0OOO0Ooo == 6 :
 O00o0o0000o0o ( "rmFavorite" )
 try :
  IIIII = IIIII . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  IIIII = IIIII . split ( '  - ' ) [ 0 ]
 except :
  pass
 IIIii11i1I ( IIIII )
 if 79 - 79: ooO00oo + ooO00oo + oOOoo
elif o0O0OOO0Ooo == 7 :
 O00o0o0000o0o ( "addSource" )
 O0I11Iiii1I ( O0O )
 if 39 - 39: OOO0O0O0ooooo - II1
elif o0O0OOO0Ooo == 8 :
 O00o0o0000o0o ( "rmSource" )
 iII1I1I1 ( IIIII )
 if 63 - 63: IIii1I % o0ooo * IiIi11i
elif o0O0OOO0Ooo == 9 :
 O00o0o0000o0o ( "download_file" )
 Ii11iiI ( IIIII , O0O )
 if 79 - 79: OOO0O0O0ooooo
elif o0O0OOO0Ooo == 10 :
 O00o0o0000o0o ( "getCommunitySources" )
 iiIII1i ( )
 if 32 - 32: iIiiiI1IiI1I1 . OOO0O0O0ooooo + oOOoo / I11iii11IIi / ooO00oo / oOOOo0o0O
elif o0O0OOO0Ooo == 11 :
 O00o0o0000o0o ( "addSource" )
 O0I11Iiii1I ( O0O )
 if 15 - 15: OOO0O
elif o0O0OOO0Ooo == 12 :
 O00o0o0000o0o ( "setResolvedUrl" )
 if not O0O . startswith ( "plugin://plugin" ) or not any ( x in O0O for x in Oo0Ooo ) :
  O0OO0oOOo = xbmcgui . ListItem ( path = O0O )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0OO0oOOo )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + O0O + ')' )
  if 4 - 4: ooO00oo + IIii1I * OOooO + IiIIi1I1Iiii * o0ooo % iIiiiI1IiI1I1
  if 88 - 88: I1ii - O00ooooo00 % i11iIiiIii % iIiiiI1IiI1I1 * II1
elif o0O0OOO0Ooo == 13 :
 O00o0o0000o0o ( "play_playlist" )
 IiIi1II111I ( IIIII , OoooO0o )
 if 40 - 40: IiIIi1I1Iiii
elif o0O0OOO0Ooo == 14 :
 O00o0o0000o0o ( "get_xml_database" )
 OOOO0OOO ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 47 - 47: I11iii11IIi
elif o0O0OOO0Ooo == 15 :
 O00o0o0000o0o ( "browse_xml_database" )
 OOOO0OOO ( O0O , True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 65 - 65: OOO0O0O0ooooo + o00ooooO0oO % oOOoo * IIiIiII11i / IiIi11i / I11iii11IIi
elif o0O0OOO0Ooo == 16 :
 O00o0o0000o0o ( "browse_community" )
 iiIII1i ( True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 71 - 71: i11iIiiIii / I11iii11IIi . I1ii
elif o0O0OOO0Ooo == 17 :
 O00o0o0000o0o ( "getRegexParsed" )
 O0O , Oo0O = oOO0oo ( IIIIi1 , O0O )
 if O0O :
  Ii1IIII1ii1I ( O0O , IIIII , oOoO0Oo0 , Oo0O )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(Supremacy ,Failed to extract regex. - " + "this" + ",4000," + O0oo0OO0 + ")" )
elif o0O0OOO0Ooo == 18 :
 O00o0o0000o0o ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(Supremacy,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 Ii111iIi1iIi = youtubedl . single_YD ( O0O )
 Ii1IIII1ii1I ( Ii111iIi1iIi , IIIII , oOoO0Oo0 )
elif o0O0OOO0Ooo == 19 :
 O00o0o0000o0o ( "Genesiscommonresolvers" )
 Ii1IIII1ii1I ( ooO000 ( O0O ) , IIIII , oOoO0Oo0 , True )
 if 33 - 33: I1ii
elif o0O0OOO0Ooo == 21 :
 O00o0o0000o0o ( "download current file using youtube-dl service" )
 iIIi1 ( '' , IIIII , 'video' )
elif o0O0OOO0Ooo == 23 :
 O00o0o0000o0o ( "get info then download" )
 iIIi1 ( O0O , IIIII , 'video' )
elif o0O0OOO0Ooo == 24 :
 O00o0o0000o0o ( "Audio only youtube download" )
 iIIi1 ( O0O , IIIII , 'audio' )
elif o0O0OOO0Ooo == 25 :
 O00o0o0000o0o ( "YouTube/DMotion" )
 OOooO0Oo0o000 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 26 :
 O00o0o0000o0o ( "YouTube/DMotion From Search History" )
 IIIII = IIIII . split ( ':' )
 OOooO0Oo0o000 ( O0O , search_term = IIIII [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 27 :
 O00o0o0000o0o ( "Using IMDB id to play in Pulsar" )
 IIIi11 = OOooO0Oo0o000 ( O0O )
 xbmc . Player ( ) . play ( IIIi11 )
elif o0O0OOO0Ooo == 30 :
 I1Iiiiiii ( IIIII , O0O , oOoO0Oo0 , oOooOOOoOo )
 if 69 - 69: OOO0O0O0ooooo - OOO0O0O0ooooo
elif o0O0OOO0Ooo == 40 :
 oO ( )
 I111i1II ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 41 :
 IiI1iiiIii ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 41 - 41: ooO00oo % o0ooo
elif o0O0OOO0Ooo == 53 :
 O00o0o0000o0o ( "Requesting JSON-RPC Items" )
 o0oOoO00 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 67 - 67: OOO0O0O0ooooo % o00ooooO0oO
elif o0O0OOO0Ooo == 69 :
 OOOooOO0 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 907 :
 I1111 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 906 :
 OO ( IIIII , O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 905 :
 O00Oo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 908 :
 o0o0OO0OO000OO ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 909 :
 O0o0Oo0OOooo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 910 :
 o0oo0Oo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 911 :
 ooO0o0oO0 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 999999 :
 o00oooO0Oo ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 999998 :
 IiiiiI1i1Iii ( IIIII , O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 999997 :
 III1Iiii1I11 ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 999996 :
 oO0O00OoOO0 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 999995 :
 I1Ii ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 999994 :
 oO0OOOO0 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 301 :
 oO0 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 302 :
 oOoO00O0 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 400 :
 oooooo0O000o ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 401 :
 mpop ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 402 :
 IiiiIIiIi1 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 403 :
 oo00oO0O0 ( O0O , IIIII , oOoO0Oo0 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 404 :
 o0000oO ( IIIII , o0oO0O00O0Oo0 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 405 :
 Oo0OO ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 406 :
 getseaseps ( IIIII , O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 407 :
 eps ( IIIII , O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 410 :
 oO00OOoO00 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 500 :
 i1I1iI ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 501 :
 iIIIi1 ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 502 :
 OoOO0oo0o ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 503 :
 iII ( O0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 504 :
 oOo0o ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 505 :
 I1I1 ( IIIII , O0O , oOoO0Oo0 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o0O0OOO0Ooo == 510 :
 Ooo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 35 - 35: IIiIiII11i . I11iii11IIi + II1 % IiIIi1I1Iiii % oOOOo0o0O
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
