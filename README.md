# NEUNetworkConnect_Python
东北大学（NEU）校园网，python连接脚本

不带有GUI界面的Linux使用方法：

1、找到并修改此处的代码

例如：学号：123456，密码：abcdefg

payload={

    "rsa":"123456abcdefg"+lt_execution_id[0][0],
    
    "ul":"6",
    
    "pl":"7",
    
    "lt":lt_execution_id[0][0],
    
    "execution":lt_execution_id[0][1],
    
    "_eventId":"submit"
    
}

2、在控制台输入指令

python /你的脚本文件存放目录/NEUNetworkConnect.py
