
# 관리자메뉴
# >> 1.책등록 2.책목록보기 3.책페기 0.로그아웃

def rootmenu(cho):
    if cho==1:
        f=open("C:/Users/준/desktop/book.txt","r")
        tit=input('[책제목]\t:')
        while True:
            txt=f.readline()
            if tit in txt:
                print('이미 존재하는 책입니다')
                return
            if not txt:
                break
        f.close()
        comp=input('[출판사]\t:')
        aut=input('[지은이]\t:')
        loc=input('[책위치]\t:')
        bor='대여가능'                     #대여여부 : 0(대여가능) 1(대여중)
        f=open("C:/Users/준/desktop/book.txt","a")
        f.write("%s\t%s\t%s\t%s\t%s\n"%(tit,comp,aut,loc,bor))
        f.close()
    elif cho==2:
        f=open("C:/Users/준/desktop/book.txt","r")
        while True:
            txt=f.readline()
            txt.replace('\t','\t\t')
        #    info=txt.split('\t')
            print(txt)
        #    print('책제목 : %s'%(info[0]));
        #    print('출판사 : %s'%(info[1]));print('지은이 : %s'%(info[2]));print('책위치 : %s'%(info[3]))
            if not txt:
                break
    










def usermenu():
    print('1.책대여 2.책반납 3.책검색 0.로그아웃')