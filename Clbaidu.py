#ending='utf-8'

from urllib.request import urlopen
from urllib.parse import urlencode
import re

wd = input('请输入要搜索的关键词：')
wd = urlencode({'wd':wd})
url = 'http://www.baidu.com/s?{}'.format(wd)
page = urlopen(url).read()
content = (page.decode('utf-8')).replace("\n","").replace("\n","")
title = re.findall(r'<h3 class="t".*?h3>',content)
title = [item[item.find('herf =')+6:item.find('target=')] for item in title]
title = [item.replace(' ','').replace('"','') for item in title]
for item in title:
    print (item)