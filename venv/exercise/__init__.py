import webbrowser
import time
#print("hello python")
#a="nielit"
#print (a)
url1="http://youtube.com"
url2="http://google.com"
url3="http://youtube.com"
i=0
while(i<3):
    time.sleep(5)
    webbrowser.open_new(url1)
    i=i+1
    url1=url1+1