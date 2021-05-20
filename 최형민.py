import random
x=int(input("x=  "))
y=int(input("y=  "))
N_students=int(input("전체 학생 수를 입력해 주세요"))
if N_students>x*y:
	print('학생이 너무 많습니다.')
	quit()
R_p_F=first_like=list(map(int,input('앞쪽에 앉고 싶은 학생의 번호를 써주세요. ※단 띄어쓰기로 다른 번호와 구별해 주세요.').split()))
for i in first_like:
	if i>N_students:
		print('없는 학생입니다')
		quit()
for i in range(0,len(first_like)):
	for n in range(0,len(first_like)):
		if i !=n:
			if first_like[i]==first_like[n]:
				print('중복된 학생이 있습니다')
				quit()
if len(first_like)>2*x:
	print("앞쪽 자리 부족! 다시 시도해주세요.")
	quit()
Doppelganger=list(map(int,input('같이 앉으면 안되는 두 사람의 번호를 적어주세요.※단 띄어쓰기로 다른 번호와 구분해 주세요.').split()))
for i in Doppelganger:
		if i>N_students:
			print('없는 학생입니다')
			quit()
for i in range(0,len(Doppelganger)):
		for n in range(0,len(Doppelganger)):
			if i !=n:
				if Doppelganger[i]==Doppelganger[n]:
				    print('중복된 학생이 있습니다')
				    quit()

remain=N_students%x
class_mate_number=[int(a) for a in range(1, N_students+1)]
line_y=int(0)

D_G_x=list()

D_G_y=list()
Fin=0
if remain != 0:
	y=y-1
if x%2==0:
    x_x=x/2
else:
	x_x=(x+1)/2
x_max=x_x
if y%2==0:
	y_y=y/2
else:
	y_y=(x+1)/2
y_max=y_y
if remain==0:
	error_1=x_max*y_max
else:
	if remain%2==0:
		error_1=x_max*y_max+remain/2
	else:
		error_1=x_max*y_max+(remain+1)/2
if (len(Doppelganger)>error_1):
	print('자리가 부족해요 붙으면 안되는 인원을 줄여주세요')
	quit()
D_point=0
for i in Doppelganger:
	for n in first_like:
		if i==n:
			D_point+=1
if D_point>x_max:
	print('앞자리가 부족해요 붙으면 안되는 학생을 바꾸어 주세요 ')
	quit()
for i in range(0,len(first_like)):
	    c=first_like[i]
	    class_mate_number.remove(c)
R_p_C=class_mate_number
seat=[]
while Fin==0:
	first_like=R_p_F
	class_mate_number=R_p_C
	chm=random.sample(class_mate_number,2*x-len(first_like))
	first_like.extend(chm)
	first_location=random.sample(first_like,x)
	seat+=[first_location]
	for i in range(0,len(chm)):
	        c=chm[i]
	        class_mate_number.remove(c)
	del(chm)
	for i in range(0,len(first_location)):
		c=first_location[i]
		first_like.remove(c)
		seat+=[first_like]
		for i in range(3,y+1):
			p=random.sample(class_mate_number,x)
			seat+=[p]
			for i in range(0,len(p)):
				c=p[i]
				class_mate_number.remove(c)
		del(p)
		if len(class_mate_number) != 0:
			seat+=[class_mate_number]
	del(first_location)
	for i in Doppelganger:
	    peace=1
	    while peace==1:
	        try:
	        	line_x=seat[line_y].index(i)
	        	D_G_x.append(line_x)
	        	D_G_y.append(line_y)
	        	peace=0
	        except:
	        	line_y=int(line_y+1)
	    for i in  D_G_x:
	        for n in D_G_x:
	        	if i !=n:
	        		if abs(i-n)>1:
	        			fin=1
	        		else:
	        			fin=0
	    for i in  D_G_y:
	        for n in D_G_y:
	        	if i !=n:
	        		if abs(i-n)>1:
	        			fin=fin+1
	if len(Doppelganger)==0:
	    Fin=1
	else:
	    if fin==2:
	        Fin=1

for i in seat:
	print(i)
