# -*- coding:utf-8 -*-
import re
import requests
url="https://ipgw.neu.edu.cn/srun_cas.php?ac_id=1"
head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Connection":"close"
}
sess=requests.session()
req=sess.get(url,headers=head)

lt_execution_id=re.findall('name="lt" value="(.*?)".*\sname="execution" value="(.*?)"', req.text, re.S)
 
payload={
    "rsa":"1910294JoneVince11"+lt_execution_id[0][0],
    "ul":"7",
    "pl":"11",
    "lt":lt_execution_id[0][0],
    "execution":lt_execution_id[0][1],
    "_eventId":"submit"
}
r2=sess.post("https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D1",headers=head,data=payload)
print(r2.text)
"""
东北大学校园网联网代码
"""
