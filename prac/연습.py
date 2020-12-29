# 도서관 시스템 코딩
# 1.회원 2.관리자
# 회원 >> 1.로그인 2.책대여  3.책반납  4.책찾기 0.로그아웃
# 관리자 >> 1.로그인 2.책등록 3.책목록보기 4.책페기 0.로그아웃

from loginsystem import loginservice
from loginsystem import login
from libsystem import rootmenu
# main 함수
def root():
    log=login()
    if log==1:
        log=2
    return log
def menu(sel):
    if sel==2:
        while True:
            print('1.책등록 2.책목록보기 3.책폐기 0.로그아웃')
            cho=int(input('>>>'))
            rootmenu(cho)
    elif sel==1:
        pass
    elif sel==0:
        return

log=0
while True : 
    print("{:^50}".format('도서관 시스템'))
    print('1.회원 2.관리자 0.종료')
    cho=int(input('>>>'))
    if cho==1:
        log=loginservice()
        menu(log)
    elif cho==2:
        log=root()
        menu(log)
    elif cho==0:
        log=0
        print('<사용을 종료합니다>')
        break
    else:
        print('<잘못된 선택입니다>')
    