

import csv

def sorting(crrnalist,start):
	sortedlist=[]
	for i in range(0,len(crrnalist)):
		E=int(crrnalist[i][11])
		print E
		crrna=crrnalist[i][1][4:]
		X=-float(abs(start-int(crrnalist[i][2][int(crrnalist[i][2].find(':'))+1:] )))
		
##################################################
		a=abs(X+125.0)/125
		GC=int(crrnalist[i][5])
		dist=abs(GC-50)
		if dist<10:
			b=0
		elif dist<20:
			b=0.2
		elif dist<30:
			b=0.4
		elif dist<40:
			b=0.6
		else:
			b=0.8

		
		c=float(int(crrnalist[i][10])+int(crrnalist[i][6])+int(crrnalist[i][7])+int(crrnalist[i][8])+int(crrnalist[i][9]))/20
		if crrnalist[i][1].find('TTTTT')>-1:
			d=1
		elif crrnalist[i][1].find('TTTT')>-1:
			d=0.5
		else:
			d=0
		e=1
		if 	 crrnalist[i][1].find('GGGGGG')>-1:
			e=0
		if 	 crrnalist[i][1].find('AAAAAA')>-1:
			e=0
		if 	 crrnalist[i][1].find('CCCCCC')>-1:
			e=0
		if 	 crrnalist[i][1].find('GGTCTC'):
			e=0
		if 	 crrnalist[i][1].find('GAGACC'):
			e=0
		if X
		S=(1+E-a-b-c-d)
		listline=[S,crrnalist[i]]
		sortedlist.append(listline)
	sortedlist.sort(key=lambda tup: tup[0])
	answer=[]
	for i in sortedlist:
		answer.append(i)
	answer.reverse()

	for q2 in range(0,len(answer)-1):
		if abs(int(answer[q2][1][2][int(answer[q2][1][2].find(':'))+1:])-int(answer[q2-1][1][2][int(answer[q2-1][1][2].find(':'))+1:]))<10:
			answer[q2][0]=0

	answer.sort(key=lambda tup: tup[0])
	answer2=[]
	for i in answer:
		answer2.append(i)
	answer2.reverse()
	return answer2
		

