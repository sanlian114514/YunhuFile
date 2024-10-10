import requests,hashlib
from collections import OrderedDict

def uploadFile(file:bytes,token:str,type=""):
    """上传文件函数

    Args:
        file (bytes):byte类型的文件
        token (str):用户token
        type (str):文件后缀

    Returns:
        str:返回信息
    """
    utoken=requests.get("https://chat-go.jwzhd.com/v1/misc/qiniu-token2",headers={"token":token}).json()["data"]["token"]
    uhost=requests.get(f"https://api.qiniu.com/v4/query?ak={utoken.split(':')[0]}&bucket=chat68-file").json()["hosts"][0]["up"]["domains"][0]
    md5=hashlib.md5(file)
    key=md5.hexdigest()
    params = OrderedDict([("token", (None, utoken)),
                  ("key", (None, key+type)),
                  ("file", (None, file))])
    ret=requests.post("https://"+uhost,files=params).json()
    return ret

def downloadFile(key:str):
    """下载文件函数

    Args:
        key (str):上传时返回的key

    Returns:
        bytes:文件内容
    """
    ret=requests.get("https://chat-file.jwznb.com/"+key,headers={"referer":"http://myapp.jwznb.com"}).content
    return ret
