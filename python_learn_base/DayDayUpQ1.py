#DayDayUpQ1.py
def dayUP(df):
	dayup=1.0
	for i in range(365):
		if i%7 in [6,0]:
			dayup = dayup*(1 - 0.01)
		else:
			dayup = dayup*(1 + df)
	return dayup
dayfactory=0.01
while dayUP(dayfactory)<37.78:
	dayfactory+=0.001
print("dayfactory:{:.3f}".format(dayfactory))
'''
round(x[,d]) round(1/3,2)=0.33
pow(a,b[,c])=a^b%c abs(a)=|a| divmod(x,y)=(x//y,x%y)
max(1,2,3) min(1,2,3)
int(1.23) float(1) complex(4)=4+0j
z=1.23e-4+5.6e+89j z.real z.imag
10/3=3.33333 10//3=3 x**y=pow(x,y)
'''