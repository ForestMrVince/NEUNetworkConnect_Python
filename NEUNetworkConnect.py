import re
import requests
url="https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_portal_sso%3Fac_id%3D1"
head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Connection":"close",
    "Host": "pass.neu.edu.cn",
	"Referer": "https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_portal_sso%3Fac_id%3D1",
    "Origin": "https://pass.neu.edu.cn",
    "Upgrade-Insecure-Requests": "1"
}
sess=requests.session()
req=sess.get(url,headers=head)

cookie = req.cookies
lt_execution_id=re.findall('name="lt" value="(.*?)".*\sname="execution" value="(.*?)"', req.text, re.S)

payload={
    "rsa":"2188888goodjob8888"+lt_execution_id[0][0],
    "ul":"7",
    "pl":"11",
    "lt":lt_execution_id[0][0],
    "execution":lt_execution_id[0][1],
    "_eventId":"submit"
}
r2=sess.post("https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_portal_sso%3Fac_id%3D1", headers=head, data=payload, 
             cookies=cookie, allow_redirects=False, verify=False)

Location = r2.headers['Location']
r2=sess.get(Location.replace('http://ipgw.neu.edu.cn/','http://ipgw.neu.edu.cn/v1/'),headers=head,cookies=cookie)

#---unnecessary----
# import numpy as np
# import time
# def produce_jQuery():
#     global jQuery
#     strnum = ""
#     for i in range(21):
#         strnum = strnum+str(int(np.random.uniform(0, 9)))
#     jQuery = "jQuery"+strnum+"_"

# produce_jQuery()
# callback = jQuery+str(int(time.time()*1000))

# r2=sess.get('http://ipgw.neu.edu.cn/cgi-bin/rad_user_info?callback='+callback,headers=head, cookies=cookie)