#!/usr/bin/python3
#TempConvert.py
TempStr = input("please input TempStr ")
if TempStr[-1] in ['F','f']:
	C=(eval(TempStr[0:-1])-32)/1.8 
	print("temp is {:.2f}C".format(C))
elif TempStr[-1]in ['C','c']:
	F=1.8*eval(TempStr[0:-1])+32
	print("temp is {:.2f}F".format(F))
else:
	print("error")
'''
"abcdefg"[:3]=abc
"abcdefg"[0:-1:2]=aceg
"abcdefg"[::-1]=gfedcba
"abc"+"def"="abcdef"
"abc"*3=3*"abc"="abcabcabc"
"abc"in "abcdef"=Ture 
len("abc")=3
str(1.23)="1.23" eval("1.23")=1.23
hex(425)="0x1a9" oct(425)="0o651"
chr(u) Unicode->char ord(x) char->Unicode
for i in range(12)
	print(chr(9800+i),end="") end="" means don't change line 
str.lower() str.upper() "AbCdEfGh".lower()="abcdefgh"
str.split(sep=None) "A,B,C".split(",")=['A','B','C']
str.count(sub) "aaa".count("a")=3
str.replace(old.new) "abc".replace("c","cdef")="abcdef"
str.center(width[,fillchar]) "python".center(20,"=")  "=======python======="
str.strip(chars) "= python= ".strip(" =npt")  "ytho" remove left and right
str.join(iter) ",".join("12345") "1,2,3,4,5"
"{1}{0}{2}".format('a','b','c')   bac
"{0:=^20}".format("PYTHON")
	=======PYTHON=======	
	fill=	
	left<	right>	mid^
	length 20
"{0:,.2f}".format(12345.6789)
	12,345.68
	1000,	
	0.01 .	
	bcdoxX 425=110101001  Σ 425 651 1a9 1A9
	eEf% 3.14=3.140000e+00 3.140000E+00 3.140000 314.000000% 
'''