f=open("C:/Users/준/desktop/dongjoon/파이썬/Music/music.txt","r")
    title =input('제목 : ')
    singer=input('가수 : ')
    sing=title+'-'+singer
    while True:
        txt=f.readline
        if txt==sing:
            print('<이미 추가되어있는 곡입니다>')
            return
        if not txt:
            break
    f=open("C:/Users/준/desktop/dongjoon/파이썬/Music/music.txt","a")
    f.write("%s\n",sing)
    f.close()
    print('<곡이 추가되었습니다>')