from bs4 import BeautifulSoup as bs
import requests
import re
import sys
import getopt
import pyfiglet
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def banner():
    banner = pyfiglet.figlet_format("CVE-TOOL")
    print(color.BOLD + color.RED + banner + color.END)
def usage():
    print (color.DARKCYAN + "usage: python cve.py [-c --cve <CVE-YYYY-XXXX>] | [-h --help]" + color.END)
def mymethod(argv):
    if(len(sys.argv)<2):
        usage()
        sys.exit(2)
    try:
        opts, args = getopt.getopt(argv, "c:h",["cve=","help="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-c", "--cve"):
            print (color.UNDERLINE + color.BOLD + 'CVE ID'+ color.END + " : "+ arg)
def data(cve):
    url = "https://www.cvedetails.com/cve/"+cve
    response = requests.get(url)
    soup=bs(response.text, 'html.parser')
    divss=soup.find_all('div',"cvedetailssummary")
    yt=soup.find_all('td',colspan="4")
    csv_data_h=[]
    csv_data_d=[]
    csv_data=[]
    csv_data_s=[]
    links=[]
    for div in divss:
        csv_data_d.append(div.text)
    divs=soup.find_all('table',id="cvssscorestable")
    for div in divs:
        tr_tags=div.find_all('tr')
        for tr_tag in tr_tags:
            th_tags = tr_tag.find_all('th')
            for th in th_tags:
                csv_data_h.append(th.text)
            td_tags = tr_tag.find_all('td')
            for td in td_tags:
                csv_data.append(td.text)
            span_tags = tr_tag.find_all('span')
            for span in span_tags:
                csv_data_s.append(span.text)
    for yy in yt:        
        a_tags=yy.find_all('a')
        for a in a_tags:
            links.append(a.get('href'))
    #csv_data.append(a.get('hef'))
    #sv_str ="".join(csv_data)
    for i in range(len(csv_data)):
        print("\n"+ color.UNDERLINE + color.BOLD + csv_data_h[i]+ color.END + " : " + csv_data[i]+"\n")
    print (color.UNDERLINE + color.BOLD + "Twitter Link" + color.END + " : " + links[0])
    print (color.UNDERLINE + color.BOLD + "Youtube Link" + color.END + " : " + links[1])
    print (color.UNDERLINE + color.BOLD + "Google Link" + color.END + "  : " + links[2])
if __name__=='__main__':
    banner()
    mymethod(sys.argv[1:])
    data(sys.argv[2])
