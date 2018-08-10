#HollandRadarDraw
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.rcParams['font.family']='STSong'
radar_labels=np.array(['YanJiu(I)','YiShu(A)','SheHui(S)',\
						'QiYe(E)','ChangGui(C)','XianShi(R)'])
data=np.array([[0.40,0.32,0.35,0.30,0.30,0.88],
				[0.85,0.35,0.30,0.40,0.40,0.30],
				[0.43,0.89,0.30,0.28,0.22,0.30],
				[0.30,0.25,0.48,0.85,0.45,0.40],
				[0.20,0.38,0.87,0.45,0.32,0.28],
				[0.34,0.31,0.38,0.40,0.92,0.28]])
data_lables=('Artist','Experimenter','Engineer','Salesman','CaseWorker','Clerk')
angles=np.linspace(0,2*np.pi,6,endpoint=False)
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure(facecolor="white")
plt.subplot(111,polar=True)
plt.plot(angles,data,'o-',linewidth=1,alpha=0.2)
plt.fill(angles,data,alpha=0.25)
plt.thetagrids(angles*180/np.pi,radar_labels,frac=1.2)
plt.figtext(0.25,0.95,'Analysis of Hollander\'s persionality',ha='center',size=20)
legend=plt.legend(data_lables,loc=(0.94,0.80),labelspacing=0.1)
plt.setp(legend.get_texts(),fontsize='large')
plt.grid(True)
plt.savefig('holland_radar.jpg')
plt.show()