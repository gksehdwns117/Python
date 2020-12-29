import loginsystem
import Musicplayer

# 로그인 후 user 선택메뉴
def user():
    while True:
        print('1.음악추가 2.음악삭제 3.재생목록으로 0.로그아웃')
        cho=int(input('>>> '))
        if cho==1:
            Musicplayer.add()
        elif cho==2:
            Musicplayer.rem()
        elif cho==3:
            Musicplayer.player()
        elif cho==0:
            print('<로그아웃됩니다>')
            break
        else:
            print('<잘못된 입력입니다>')
            continue
# main
while True:
    log=0
    print("{:^50}".format('--- 메인 ---'))
    print('1.로그인 2.회원가입 0.종료')
    cho=int(input('>>> '))
    if cho==1:
        log=loginsystem.login("C:/Users/준/desktop/dongjoon/파이썬/Music/user.txt")
        if log==1:
            user()
        elif log==0:
            continue
    elif cho==2:
        loginsystem.join("C:/Users/준/desktop/dongjoon/파이썬/Music/user.txt")
    elif cho==0:
        print('<프로그램이 종료됩니다>')
        break
    else:
        print('<잘못된 입력입니다>')
        continue








