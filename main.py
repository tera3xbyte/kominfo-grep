import os, sys, json, requests
from bs4 import BeautifulSoup as BS

PSE_FOREIGN_URL = "https://pse.kominfo.go.id/home/pse-asing"
PSE_DOMESTIC_URL = "https://pse.kominfo.go.id/home/pse-domestik"

#soup = BS(pass, "html.parser")
#result =

def main():
    pass

def refresh_cache():
    pass

def helpmessege():
    msg = """
USAGE: kmfgrep [OPTIONS] PATTERS
kominfo-grep  - a utility for searching blocked / provided services by Kominfo 
                https://pse.kominfo.go.id 
OPTIONS:
    --version   displays the version
    --help      displays this messege
    -a          search foreign services
    -d          search domestic services
    -i          ignore case

Report bugs to <tera3xbyte@yahoo.com> / github issues
    """
    print(msg)
if __name__ == '__main__':
    main()
