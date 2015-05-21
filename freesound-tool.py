import urllib.request
import bs4

#   Steps

#   Getting links to files
#get links to all files on free sound - eg open them all in new tabs then
#use copy to clipboard extension on chrome
#save to a file called links.txt

#   Getting cookies to pretend you're not a bot
#go to free sound and login
#go onto developer mode on chrome and go on network
#download a file, you can cancel the download after clicking download
#copy the request headers
#save to a file called headers.txt
#if there are any, remove uneeded headers from file but i didn't need to

def loadHeadersFromFile():
    headers = {}
    for line in open("headers.txt","r").read().split("\n"):
        parts = line.split(":",1)
        headers[parts[0]] = parts[1][1:]

    return headers

def download(url,name,headers):
    req = urllib.request.Request(url=url, headers = headers)
    file = urllib.request.urlopen(req)
    with open(name, 'b+w') as f:
        f.write(file.read())

headers = loadHeadersFromFile()

for link in open("links.txt","r").read().split("\n"):
    if "/sounds/" in link:
        html = urllib.request.urlopen(link).read().decode('utf-8')
        soup = bs4.BeautifulSoup(html)
        tags = soup.find_all(id="download_login_button")
        for tag in tags:
            url = "http://www.freesound.org"+tag["href"]
            filename = "./"+url.split("/")[-1]
            download(url,filename,headers)
            print("downloaded:","./"+url.split("/")[-1])

