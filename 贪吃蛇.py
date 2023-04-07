import pygame as pg,sys,os,random as rd


pg.init()


pg.display.set_caption('贪吃蛇')
screen=pg.display.set_mode((1350,710))
s_col=(0,100,0)
pla=[(30,200),(60,200),(90,200),(120,200)]
long,flag,stop=4,2,None
food,obs=[],[]
pg.time.set_timer(pg.USEREVENT,300)
pg.time.set_timer(pg.USEREVENT+1,3000)
pg.time.set_timer(pg.USEREVENT+2,10000)


def p_text(text,color,font,x,y,size):
    f=pg.font.SysFont(font,size)
    t=f.render(text,True,color)
    screen.blit(t,(x,y))


def fod():
    a=rd.randint(0,45)*30
    b=rd.randint(3,24)*30-10
    while (a,b) in (pla or food or obs):
        a=rd.randint(0,45)*30
        b=rd.randint(3,24)*30-10
    food.append((a,b))


fod()
while True:
    over,p=True,[i for i in pla[:-1]]
    if 0<=pla[-1][0]<=1320 and 80<=pla[-1][1]<=690 and pla[-1] not in p: over=None
    for eve in pg.event.get():
        if eve.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if eve.type==pg.KEYDOWN:
            if eve.key==pg.K_w and flag!=3: flag=1
            if eve.key==pg.K_s and flag!=1: flag=3
            if eve.key==pg.K_a and flag!=2: flag=4
            if eve.key==pg.K_d and flag!=4: flag=2
            stop=None
        if eve.type==pg.USEREVENT and not over and not stop:
                if flag==1: pla.append((pla[-1][0],pla[-1][1]-30))
                elif flag==2: pla.append((pla[-1][0]+30,pla[-1][1]))
                elif flag==3: pla.append((pla[-1][0],pla[-1][1]+30))
                elif flag==4: pla.append((pla[-1][0]-30,pla[-1][1]))
                q=pla[0]
                del pla[0]
        if eve.type==pg.USEREVENT+1 and not over: fod()
        if eve.type==pg.USEREVENT+2 and not over:
            k=rd.randint(0,45)*30
            l=rd.randint(3,24)*30-10
            while (k,l) in (pla or food or obs):
                k=rd.randint(0,45)*30
                l=rd.randint(3,24)*30-10
            obs.append((k,l))
    if not over:
        ti=pg.time.get_ticks()//1000
        screen.fill((40,40,60))
        p_text('贪吃蛇','green','SimSun',600,10,50)
        p_text('长度：{}格'.format(long),'white','SimSun',1130,30,30)
        p_text('时间：{}秒'.format(ti),'white','SimSun',30,30,30)
        for n in food: pg.draw.rect(screen,(100,100,100),(n[0],n[1],30,30))
        for m in pla: pg.draw.rect(screen,s_col,(m[0],m[1],30,30))
        for v in obs: pg.draw.rect(screen,(0,0,0),(v[0],v[1],30,30))
        pg.draw.line(screen,'black',(0,78),(1350,78),3)
        for i in range(30, 1350, 30): pg.draw.line(screen, 'black', (i, 80), (i, 710))
        for j in range(110, 710, 30): pg.draw.line(screen, 'black', (0, j), (1350, j))
        if pla[-1] in food:
            long+=1
            pla.insert(0,q)
            food.remove(pla[-1])
        if food==[]: fod()
        if flag==1: area=(pla[-1][0],pla[-1][1]-30)
        elif flag==2: area=(pla[-1][0]+30,pla[-1][1])
        elif flag==3: area=(pla[-1][0],pla[-1][1]+30)
        elif flag==4: area=(pla[-1][0]-30,pla[-1][1])
        if area in obs: stop=True
    else:
        screen.fill((40,40,60))
        p_text('GAME OVER!','red','Microsaft YaHei',225,200,200)
        pg.draw.rect(screen,'red',(750,500,200,50))
        p_text('退出','white','SimSun',820,510,30)
        pg.draw.rect(screen,'green',(400,500,200,50))
        p_text('重新开始','white','SimSun',440,510,30)
        p_text('时间：{}秒'.format(ti),'white','SimSun',250,350,40)
        p_text('长度：{}格'.format(long),'white','SimSun',900,350,40)
        if eve.type==pg.MOUSEBUTTONDOWN:
            p_x,p_y=eve.pos
            if 400<=p_x<=600 and 500<=p_y<=550:
                python=sys.executable
                os.execl(python,python,*sys.argv)
            elif 750<=p_x<=950 and 500<=p_y<=550:
                pg.quit()
                sys.exit()
    pg.display.flip()