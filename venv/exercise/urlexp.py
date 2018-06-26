import webbrowser
import time
#print("hello python")
#a="nielit"
#print (a)
list=["http://youtube.com","http://google.com","http://youtube.com"]
i=0
while(i<3):
    time.sleep(5)
    webbrowser.open_new(list[i])
    i=i+1
