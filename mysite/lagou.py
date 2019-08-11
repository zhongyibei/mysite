import requests
from bs4 import BeautifulSoup
import json
import time
import numpy as np
import pandas as pd

headers = {
    'Cookie':'_ga=GA1.2.2046537735.1519346482; user_trace_token=20180223084123-462157d6-1832-11e8-8df7-525400f775ce; LGUID=20180223084123-46215dc1-1832-11e8-8df7-525400f775ce; LG_LOGIN_USER_ID=a74eb645299f49ec2b1f0f98d8f27071b23ad1b8c3e4a22f; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; index_location_city=%E4%B8%8A%E6%B5%B7; WEBTJ-ID=20180417084813-162d112cf2b4d9-0300e63ea642e6-4545092c-2073600-162d112cf2c306; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523407416,1523407491,1523926094; _gid=GA1.2.1279679635.1523926094; LGSID=20180417084813-0203736a-41d9-11e8-b8a4-5254005c3644; PRE_UTM=m_cf_cpt_sogou_pc; PRE_HOST=www.sogou.com; PRE_SITE=https%3A%2F%2Fwww.sogou.com%2Fsogou%3Fquery%3D%25C0%25AD%25B9%25B4%26_asf%3Dwww.sogou.com%26_ast%3D1523926090%26w%3D01019900%26p%3D40040100%26pid%3Dsogou-site-c02d0450cdd75ce7%26sut%3D1050%26sst0%3D1523926089994%26lkt%3D0%252C0%252C0; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_sogou_pc; _putrc=6EA73BBBB51DEF7E; JSESSIONID=ABAAABAAADEAAFI11A5943D5AD8FA9FDAB240DFAD660213; login=true; unick=%E5%86%AF%E7%AB%B9%E5%90%9B; hasDeliver=134; gate_login_token=cc1c59fd3fc91706eb01534899470d38000e54a63b0db428; TG-TRACK-CODE=index_search; LGRID=20180417084823-0861f794-41d9-11e8-88dc-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1523926106; SEARCH_ID=6be8a0349e5e4993a98387489af5cc6c',
     'Host':'www.lagou.com',
     'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
     'Origin':'https://www.lagou.com',
     'X-Anit-Forge-Code':'0',
     'X-Anit-Forge-Token':'None',
     'X-Requested-With':'XMLHttpRequest',
     'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'

}

positions = []

for x in range(1,31):
    data = {
        'first':'true',
        'pn':x,
        'kd':'数据分析'
    }
    result = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false',headers=headers,data=data)
    json_result = result.json()
    #page_position = json_result['content']['positionResult']['result']
    #positions.extend(page_position)
    print(json_result)
    time.sleep(18)
