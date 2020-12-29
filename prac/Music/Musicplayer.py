
import random

# 1.음악추가
def add():
    f=open("C:/Users/준/desktop/dongjoon/파이썬/Music/music.txt","r")
    title =input('제목 : ')
    singer=input('가수 : ')
    song=title+'-'+singer+'\n'
    while True:
        txt=f.readline()
        if txt==song:
            print('<이미 추가되어있는 곡입니다>')
            return
        if not txt:
            break
    f=open("C:/Users/준/desktop/dongjoon/파이썬/Music/music.txt","a")
    f.write("%s"%song)
    f.close()
    print('<곡이 추가되었습니다>')

# 2.음악삭제
def rem():
    f=open("C:/Users/준/desktop/dongjoon/파이썬/Music/music.txt","r")
    mls=f.readlines()
    i=int(input('삭제할 곡을 선택하세요\n>>>'))
    del(mls[i-1])
    f=open("C:/Users/준/desktop/dongjoon/파이썬/Music/music.txt","w")
    for j in range(0,len(mls)):
        f.write('%s'%mls[j])
    f.close()

# 3.재생목록
def player():
    f=open("C:/Users/준/desktop/dongjoon/파이썬/Music/music.txt","r")
    mls=f.readlines()
    playmusic='';i=0
    if len(mls)==0:
        print('<플레이리스트에 저장된 곡이 없습니다>')
        return
    while True:
        print('-----------------------------------------------------------------------------------------')
        for i in range(0,len(mls)):
            print("%d.%s"%(i+1,mls[i]),end='')
        print('-----------------------------------------------------------------------------------------')
        print('1.▶ 2.■ 3.▶▶ 4.◀◀ 0.음악메뉴로')
        cho=int(input('>>> '))
        if cho==1:
            #print('재생할 음악을 선택하세요')
            #int(input('>>> '))-1
            i=random.randint(0,len(mls))
            playmusic=mls[i+1]
            print('<%s'%playmusic,end=' 을(를) 재생합니다>')
            print()
        elif cho==2:
            if(playmusic==''):
                print('<현재 재생중인 음악이 없습니다>')
            else:
                print('<%s'%playmusic,end=' 을(를) 정지합니다>')
                playmusic=''
                print()
        elif cho==3:
            if(playmusic==''):
                print('<현재 재생중인 음악이 없습니다>')
            else:
                i+=1
                if i>=len(mls) :   i=0
                playmusic=mls[i]
                print('<%s'%playmusic,end=' 을(를) 재생합니다>')
                print()
        elif cho==4:
            if(playmusic==''):
                print('<현재 재생중인 음악이 없습니다>')
            else:
                i-=1
                if i<=len(mls) :   i=0
                playmusic=mls[i]
                print('<%s'%playmusic,end=' 을(를) 재생합니다>')
                print()
        elif cho==0:
            print('<음악메뉴로 이동합니다>')
            return
        else:
            print('<잘못된 입력입니다>')
