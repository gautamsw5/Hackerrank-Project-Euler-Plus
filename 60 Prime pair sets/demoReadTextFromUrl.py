import requests
url="https://chclr5f9ddtblbawhds6tg-on.drv.tw/www.output3.com/"
r = requests.get(url, stream=True)
c=0
ans3=[]
for line in r.iter_lines():
    if line:
        if c==29272:
            break
        if c==3:
            ans3.append(list(map(int,str(line)[5:-1].split())))
        elif c>3:
            ans3.append(list(map(int,str(line)[9:-1].split())))
        c=c+1
