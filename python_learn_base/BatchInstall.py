#BatchInstall.py
'''
pip install numpy			NumPy 			N维数据表示和运算
pip install matplotlib		Matplotlib 		二维数据可视化
pip inatall pillow			PIL 			图像处理
pip install	sklean			Scikit-Learn    机器学习和数据挖掘
pip install requests		Requests 		HTTP协议访问及网络爬虫
...
'''
import os
libs={"numpy","matplotlib","pillow","sklean","requests"}
try:
	for lib in libs:
		os.system("pip install "+lib)
	print("Sucessful")
except:
	print("Failed Somehow")