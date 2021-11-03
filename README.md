# NEUNetworkConnect_Python
东北大学（NEU）校园网，python连接脚本

不带有GUI界面的Linux使用方法：

1、找到并修改此处的代码

例如：学号：2188888，密码：goodjob8888

payload={

    "rsa":"2188888goodjob8888"+lt_execution_id[0][0],
    
    "ul":"7", #学号长度
    
    "pl":"11", #密码长度
    
    "lt":lt_execution_id[0][0],
    
    "execution":lt_execution_id[0][1],
    
    "_eventId":"submit"
    
}

2、在控制台输入指令

python /你的脚本文件存放目录/NEUNetworkConnect.py

***
**最新版本补充说明：匹配最新的2021年11月2日之后，东北大学升级后的网关登陆脚本。**

升级后的网关登陆方式由原来的账号登陆（pc）改为了CAS登陆（sso），因此增加了一步跳转，增加了sever ticket认证。
这里相应匹配了自动获取ticket，并保存登陆cookie。

另外附送了一个利用chromedrive and selenium 进行模拟浏览器登陆的脚本。脚本利用chrome的headless模式可以实现linux自动登陆。

相关参考教程：
1. sso登陆：https://www.jianshu.com/p/8cd6e9bc2680
2. linux环境下chromedrive headless 设置：https://blog.csdn.net/qq_41963758/article/details/80320309
3. linux下使用selenium（环境部署）：https://www.jianshu.com/p/cbc01d32c7b0/
4. ubuntu（64位）三行命令安装chrome浏览器：https://www.cnblogs.com/Rainingday/p/12426010.html

新闻链接：
1. http://xwb.neu.edu.cn/2021/1029/c5728a205587/page.htm

chrome登陆分析：
[![IAVQns.png](https://z3.ax1x.com/2021/11/03/IAVQns.png)](https://imgtu.com/i/IAVQns)
[![IAVN3F.png](https://z3.ax1x.com/2021/11/03/IAVN3F.png)](https://imgtu.com/i/IAVN3F)

***
*另附：ubuntu自启动教程，例如：*

python路径：`/home/root/miniconda3/bin/python`

自动登陆脚本路径：`/home/root/NEUNetworkConnect.py`

在/etc/rc.local脚本中添加

```
#!/bin/sh -e

/home/root/miniconda3/bin/python /home/root/NEUNetworkConnect.py

#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

exit 0
```
