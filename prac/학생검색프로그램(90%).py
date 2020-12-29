'''	학생의 인적사항 등록 후 검색 하는 프로그램을 만드시오
	 (학번, 이름, 생년월일, 등급(A,B,C,D,E,F))
	 (ex. dic1 = {key:{학생정보}})
	1.인적사항 등록
	2.학생 검색
	3.학생 수정
	4.학생 삭제
	5.전체학생 보기
	6.종료
	* 깊은복사를 사용하시는게 편하실거에요
'''
import copy
'''
def add():
def sec():
def mod():
def era():
def all():
'''

stu=[];
while True:
    print('1.인적사항 등록 2.학생검색 3.학생수정 4.학생삭제 5.전체학생보기 0.종료')
    cho=int(input('>>> ')) 
    if(cho==1):
        num=input('학번입력 : ')
        name=input('이름입력 : ')
        birth=input('생일입력 : ')
        grade=input('등급입력 : ')
        prof=(num,name,birth,grade)
        stu.append(prof)
    elif(cho==2):
        num=input('검색할 학생의 학번 : ')
        print()
        for i in range(0,len(stu)):
            if(num in stu[i][0]):
                print('학번\t\t이름\t\t생일\t\t등급')
                for j in range(0,4):
                    print(stu[i][j],end='\t\t')
                print();print()
                break
            else:
                print('해당 학번의 학생은 존재하지 않습니다')
                print()
    elif(cho==3):
        num=input('수정할 학생의 학번 : ')
        for i in range(0,len(stu)):
            if(num in stu[i][0]):
                stu[i]=list(stu[i])
                stu[i][1]=input('변경할 이름 : ')
                stu[i][2]=input('변경할 생일 : ')
                stu[i][3]=input('변경할 등급 : ')
                stu[i]=tuple(stu[i])
                print('인적사항이 변경되었습니다')
                break
            else:
                print('해당 학번의 학생은 존재하지 않습니다')
                print()
    elif(cho==4):
        num=input('삭제할 학생의 학번 : ')
        for i in range(0,len(stu)):
            if(num in stu[i][0]):
                del(stu[i])
                print('%s 학번의 학생이 삭제되었습니다'%num)
                break
        else:
            print('해당 학번의 학생은 존재하지 않습니다')
            print()
    elif(cho==5):
        print('학번\t\t이름\t생일\t\t등급')
        for i in range (0,len(stu)):
            for j in range(0,4):
                print(stu[i][j],end='\t')
            print()
    elif(cho==0):
        print('프로그램이 종료됩니다')
        break
    else:
        print('잘못된 입력입니다')
        print('메뉴로 돌아갑니다')
    
    



