#회원가입
def join():
    print("{:^50}".format('회원가입'))
    f=open("C:/Users/준/desktop/user.txt","r")
    name=input('[이름]\t: ')
    id=input('[ID]\t: ')
    while True:
        txt=f.readline()
        if id in txt:
            print("이미 존재하는 아이디입니다")
            return
        if not txt: break
    pw=input('[PW]\t: ')
    rpw=input('[PW 확인]\t: ')
    while rpw!=pw:
        print('<비밀번호가 일치하지 않습니다>')
        rpw=input('[PW 확인]\t: ')
    gender=input('[성별]\t: ')
    print('\n<회원가입이 완료되었습니다>')
    f=open("C:/Users/준/desktop/user.txt","a")
    f.write("%s\t%s\t%s\t%s\n"%(name,id,pw,gender))
    f.close()
#로그인
def login():
    print("{:^50}".format('로그인'))
    id=input('[아이디입력]\t: ')
    pw=input('[비밀번호입력]\t: ')
    f=open("C:/Users/준/desktop/user.txt","r")
    while True:
        txt=f.readline()
        if id in txt:
            info=txt.split('\t')
            if pw==info[2]:
                print('<로그인 되었습니다>')
                return 1
            else:
                print('<비밀번호가 일치하지 않습니다>')
                return 0
        if not txt:
            print('<일치하는 아이디가 없습니다>')
            return 0
#로그인 서비스
def loginservice():
    log=0      
    while True:
        print('1.로그인 2.회원가입 0.메인(메뉴)으로')
        cho=int(input('>>>'))
        if cho==1:
            if log==1:
                print('<이미 로그인 되어있습니다>')
            else:
                log=login()
        elif cho==2:
                log=join()
        elif cho==0:
            print('<메인화면으로 돌아갑니다>')
            return log
        else:
            print('<잘못된 선택입니다>')


'''
        !! 일단 주석처리
        elif cho==3:
            if log==1:
                print('<로그아웃 되었습니다>')
                log=0

            else:
                print('<로그인 되어있지 않습니다>')
'''













    



    