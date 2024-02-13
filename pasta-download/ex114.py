import urllib.request
from urllib import request
try:
    site = urllib.request.urlopen('https://www.youtube.com/watch?v=2pgjRbfr8-Q')
except:
    print(f'\033[31mNão consegui acessar o site\033[m')
else:
    print(f'\033[32mConsegui acessar o site033[m')

    
    

