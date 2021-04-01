#-*-coding:utf-8-*-
import os
try:
 import os,requests, inquirer
 import sys
 import time
 from bs4 import BeautifulSoup as bs
except:os.system('pip2 install requests inquirer')
import os,requests, inquirer
import sys
import time
from bs4 import BeautifulSoup as bs
from urlparse import parse_qs

qu = '\033[0;36m'
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
def downbtube(url):
 btu = requests.get(url,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'}).text
 btu1 = bs(btu,'html.parser')
 return btu1.find('video',{'id':'mediaplayer'}).source["src"]
def downdrive(url):
 mek = []
 gdr = requests.get(url,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'}).text
 gdr1 = bs(gdr,'html.parser')
 for til in gdr1.findAll('a',href=True):
  if til["href"].startswith('https://server'):
   primitif = til["href"]
   break
  else:
   primitif = ""
   continue
 return primitif
def anoboydown(url,directory,dir2):
 with open(directory+"/"+dir2, 'wb+') as f:
  start = time.clock()
  we = time.time()
  link = url
  while True:
   try:
    r = requests.get(link, headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'},stream=True)
    total_length = r.headers.get('content-length')
    print "%s[%s!%s] %sUkuran file : %s%s MB"%(pu,me,pu,qu,ku,str(int(total_length) / 1024 / 1024))
    print "%s[%s!%s] %sSedang mendownload file sebagai %s%s %sdi folder %s%s"%(pu,me,pu,qu,ku,dir2,qu,ku,directory)
    dl = 0
    if total_length is None:
      f.write(r.content)
    else:
      for chunk in r.iter_content(1024):
        dl += len(chunk)
        f.write(chunk)
        done = int(20 * dl / int(total_length))
        sys.stdout.write("\r%s[%s%s%s%s] %s%s %skbps" % (pu,hi,'▭' * done, ' ' * (20-done),pu,ku, dl//(time.clock() - start) / 1024,qu))
        sys.stdout.flush()
   except Exception as e: print ("%s[%s!%s] %sTerjadi kesalahan, mengulangi..."%(pu,me,pu,me));print e;continue
   else: break
 return (time.time() - we)

def anoboysearch(keyword):
 step1 = requests.get('https://anoboy.cc/search/%s/'%keyword,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'}).text
 if "tidak ditemukan" in step1:exit('%s[%s!%s] %sPencarian tidak ditemukan!'%(pu,me,pu,me))
 step2 = bs(step1,'html.parser')
 yups = 0
 nolist = []
 judul = step2.findAll('td',{'class':'videsc'})
 lah = "»»»".decode('utf-8')
 for waw in judul:
  print "%s%s %s(%s%s%s) %s%s"%(hi,lah,pu,me,yups,pu,ku,waw.a.getText())
  yups += 1
  nolist.append("https://anoboy.cc"+waw.a["href"])
 while True:
  try:
   pilihno = int(raw_input("%s[%s?%s] %sSilahkan pilih berdasarkan nomor : %s"%(pu,me,pu,qu,hi)))
  except:print "%s[%s!%s] %sItu bukan nomor,blokk!"%(pu,me,pu,me)
  else:break
 while True:
  try:
   link = nolist[int(pilihno)]
   step3 = requests.get(link,headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'}).text
   step4 = bs(step3,'html.parser')
   desc = step4.find('div',{'class':'detail'}).p.getText()
   eps = step4.find('div',{'class':'ep'})
   yups2 = 0
   noeps = 1
   nolist2 = []
   print "%s[%s!%s] %sDescription : %s%s"%(pu,me,pu,ku,pu,desc)
   for waw2 in eps.findAll('a',href=True):
    print "%s»»» %s(%s%s%s) %sEpisode %s"%(hi,pu,me,yups2,pu,ku,noeps)
    nolist2.append("https://anoboy.cc"+waw2["href"])
    yups2 += 1
    noeps += 1
  except IndexError:print "%s[%s!%s] %sTerjadi masalah, mengulangi..."%(pu,me,pu,me);continue
  else:break
 while True:
  try:
   pilihno2 = int(raw_input('%s[%s?%s] %sSilahkan pilih, berdasarkan nomor : %s'%(pu,me,pu,qu,hi)))
  except:print "%s[%s!%s] %situ bukan nomor, blokk!"%(pu,me,pu,me)
  else:break
 while True:
  try:
   link2 = nolist2[int(pilihno2)]
   inqu1 = []
   inqu2 = []
   step5 = requests.get(link2).text
   step6 = bs(step5,'html.parser')
   for waw3 in step6.findAll('a',href=True):
    if waw3.getText() == "Download Gdrive":
     gdrive = "https:"+waw3["href"]
     inqu1.append('Gdrive')
     break
    else:
     gdrive = ""
     continue
   for waw4 in step6.findAll('a',href=True):
    try:
     if waw4["data-video"].startswith('/btube.php'):
      btubei = "https://anoboy.cc"+waw4["data-video"]
      inqu1.append('Btube')
      break
     else:
      btubei = ""
      continue
    except KeyError:continue
   if btubei == "":
    pass
   else:
    btube = downbtube(btubei)
    inqu2.append(btube)
   if gdrive == "":
    pass
   else:
    gdrivee = downdrive(gdrive)
   ser = inquirer.prompt([inquirer.List('server',message=qu+'Pilih server download',choices=inqu1,),])["server"]
   if ser == "Gdrive":
    title = raw_input("%s[%s!%s] %sSimpan file sebagai (ex:anime.mp4) : %s"%(pu,me,pu,qu,hi))
    print "%s[%s?%s] %sWaktu terpakai : %s%s"%(pu,me,pu,hi,ku,anoboydown(gdrivee,'/sdcard/Download',title))
   else:
    title = raw_input("%s[%s!%s] %sSimpan file sebagai (ex:anime.mp4) : %s"%(pu,me,pu,qu,hi))
    print "%s[%s?%s] %sWaktu terpakai : %s%s"%(pu,me,pu,hi,ku,anoboydown(gdrivee,'/sdcard/Download',title))
  except IndexError as e:print "%s[%s!%s] %sTerjadi masalah, mengulangi..."%(pu,me,pu,me);print e;continue
  else:break
if __name__ == "__main__":
 os.system('clear')
 #males buat banner:v
 print "             Script by abilseno11        "
 quey = raw_input('%s[%s?%s] %sMasukkan keyword : %s'%(pu,me,pu,qu,hi))
 anoboysearch(quey)



