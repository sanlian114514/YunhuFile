# YunhuFile
## 云湖文件上传/下载器
### 使用方法:
1.下载项目压缩包
2.解压
3.当作模块导入
### 函数:
#### uploadFile(file,token,type)
##### 上传文件函数
##### 参数:
  - file (bytes):byte类型的文件
  - token (str):云湖用户token
  - type (str):文件后缀
##### 返回:
  - str:返回信息
#### downloadFile(key)
##### 下载文件函数
##### 参数:
  - key (str):上传时返回的key
##### 返回:
  - bytes:文件内容
