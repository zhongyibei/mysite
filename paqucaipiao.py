import requests
import re
def getinfo(url):
    r = requests.get(url)
    r.encoding = 'gbk'
    res = r.text
    no = "".join(re.findall(r'<font class="cfont2"><strong>(.+?)</strong>',res))
    red = ",".join(re.findall(r'<li class="ball_red">(.+?)</li>',res))
    blue = "".join(re.findall(r'<li class="ball_blue">(.+?)</li>',res))

    res = "第" + no + "期：" +red + "  " + blue

    print(res)
for i in range(19001,19040):
    url = "http://kaijiang.500.com/shtml/ssq/"+str(i)+".shtml"
    getinfo(url)