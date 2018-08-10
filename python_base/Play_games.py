from random import random
def main():
	printIntro()
	proA,proB,n=getInputs()
	winsA,winsB=simNGames(n,proA,proB)
	printSummary(winsA,winsB)
def printIntro():
	print("这个程序模拟两个选手A和B的某种竞技比赛")
	print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
def getInputs():
	a=eval(input("Please input A(0~1): "))
	b=eval(input("Please input B(0~1): "))
	n=eval(input("Please input n: "))
	return a,b,n
def printSummary(winsA,winsB):
	n=winsA+winsB
	print("Play {} games".format(n))
	print("A win {} games,{:.1%}".format(winsA,winsA/n))
	print("B win {} games,{:.1%}".format(winsB,winsB/n))
def simNGames(n,proA,proB):
	winsA,winsB=0,0
	for i in range(n):
		scoreA,scoreB=simOneGame(proA,proB)
		if scoreA>scoreB:
			winsA+=1
		else:
			winsB+=1
	return winsA,winsB
def simOneGame(proA,proB):
	scoreA,scoreB=0,0
	serving='A'
	while not gameOver(scoreA,scoreB):
		if serving=='A':
			if random()<proA:
				scoreA+=1
			else:
				serving='B'
		else:
			if random()<proB:
				scoreB+=1
			else:
				serving='A'
	return scoreA,scoreB
def gameOver(scoreA,scoreB):
	return scoreA==15 or scoreB==15
main()