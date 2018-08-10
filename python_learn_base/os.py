import os
path="/home/neco/python/os.py"
os.path.abspath("os.py")					#/home/neco/python/os.py	返回绝对路径
os.path.normpath(path)						#统一格式		D://PYE//file.txt -> 'D:\\PYE\\file.txt'
os.path.relpath("os.py")					#返回当前程序与文件的相对路径
os.path.dirname(path)						#返回目录名字
os.path.basename(path)						#返回文件名称
os.path.join("/home/","neco/python/os.py")	#组合(path,*paths)
os.path.exists(path)						#判断是否存在
os.path.isfile(path)
os.path.isdir(path)
os.path.getatime(path)						#上次访问时间			access
os.path.getmtime(path)						#最近一次修改时间		modify
os.path.getctime(path)						#创建时间				create
# time.ctime(os.path.getatime(path))
# time.ctime(os.path.getmtime(path))
# time.ctime(os.path.getctime(path))
os.path.getsize(path)

os.system(path)								#调用其他程序,可以给程序加参数

os.chdir(path)								#修改当前程序操作的路径
os.getcwd()									#返回程序的当前路径
os.getlogin()								#获取当前系统登录用户名称
os.cpu_count()
n=10
os.urandom(n)								#10个字节的随机字符