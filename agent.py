
import random
agent=[]
for ix in range(200):
    a="Mozilla/5.0 (Linux; Android "
    b=random.choice(["12;","13;"])
    c=" Nokia C"
    d=str(random.randint(10,110))
    e=" Build/"
    f=random.choice(["SP1A.","TP1A."])
    g=str(random.randint(210812,220624))
    h=".0"
    i=str(random.randint(14,16))
    j="; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"
    k=str(random.randint(108,118))
    l=".0."
    m=str(random.randint(1,5359))
    n="."
    o=str(random.randint(1,128))
    p=" Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]"
    useragent=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p
    
    agent.append(useragent)




