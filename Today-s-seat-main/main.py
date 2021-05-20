
import random

x = int(input("x=  "))
y = int(input("y=  "))

N_students = int(input("전체 학생 수를 입력해 주세요"))

while(True) :
	if N_students <= x*y :
	   break

	else:
		if N_students > x*y:
			print('학생이 너무 많습니다.')
			N_students = int(input("전체 학생 수를 입력해 주세요"))


first_like = list(map(int,input('앞쪽에 앉고 싶은 학생의 번호를 써주세요. ※단 띄어쓰기로 다른 번호와 구별해 주세요.').split()))


if len(first_like)>2*x:
	print("앞쪽 자리 부족! 다시 시도해주세요.")
	quit()

Doppelganger = list(map(int,input('같이 앉으면 안되는 두 사람의 번호를 적어주세요. ※단 띄어쓰기로 다른 번호와 구분해 주세요.').split()))

remain = int(N_students%x)
class_mate_number = [int(a) for a in range(1, N_students+1)]

if remain != 0:
	y = y-1

if x%2 == 0:
    x_x = x/2
else:
	x_x = (x+1)/2
x_max = x_x

if y%2 == 0:
	y_y = y/2
else:
	y_y = (x+1)/2
y_max = y_y

if remain == 0:
	error_1 = x_max*y_max
else:
	if remain%2 == 0:
		error_1 = x_max*y_max+remain/2
	else:
		error_1 = x_max*y_max+(remain+1)/2
	
if (len(Doppelganger)>error_1):
	print('자리가 부족해요 인원을 줄여주세요')
	quit()

for i in range(0,len(first_like)):
	    c = first_like[i]
	    class_mate_number.remove(c)
seat=[]

chm = random.sample(class_mate_number,x*2-len(first_like))
first_like.extend(chm)
first_location=random.sample(first_like,x)
seat+=[first_location]

for i in range(0,len(chm)):
	    c=chm[i]
	    class_mate_number.remove(c)

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
    
for i in seat:
    print(i)
