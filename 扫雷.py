import pygame as pg,sys,random as rd
from key import *


pg.init()


lei,open,qi=[],[],[]
scr_x,scr_y=290,330
l=0
shu=10
c_x1,c_x2,c_x3=70,130,190
over,tool,win=False,False,False
time,time2=0,0


pg.display.set_caption('扫雷')
screen=pg.display.set_mode((scr_x,scr_y))
i1=pg.image.load('Images\雷.png').convert()
i2=pg.image.load('Images\红雷.png').convert()
i3=pg.image.load('Images\旗.jpg').convert()
i4=pg.image.load('Images\雷2.png').convert()
i5=pg.image.load('Images\开发者选项.jpg').convert()


def p_text(text,color,font,x,y,size):
    text=str(text)
    f=pg.font.SysFont(font,size)
    t=f.render(text,True,color)
    screen.blit(t,(x,y))
    return x,y


def reo(x,y,shu2):
    global over,time,time2,lei,open,qi,l,shu,scr_x,scr_y,screen,tool,win
    over,tool,win=False,False,False
    time,time2=0,0
    lei,open,qi=[],[],[]
    l=0
    shu=shu2
    scr_x,scr_y=x,y
    screen=pg.display.set_mode((x,y))


def lis(q):
    q1,q2=q[0],q[1]
    li=[(q1-30,q2-30),(q1,q2-30),(q1+30,q2-30),(q1-30,q2),(q1+30,q2),(q1-30,q2+30),(q1,q2+30),(q1+30,q2+30)]
    return li


def find(a):
    global open,finp
    ing=lis(a)
    n=0
    for i in ing:
        if i in lei: n+=1
    return n


clock=pg.time.Clock()
while True:
    clock.tick(60)
    screen.fill(front)
    num_x,num_y=(scr_x-20)/30,(scr_y-60)/30
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.MOUSEBUTTONDOWN:
            but=event.button
            pos_x,pos_y=event.pos
            if 10<=pos_x<=scr_x-10 and 50<=pos_y<=scr_y-10 and not over and not tool and not win:
                p_x2=pos_x-(pos_x-10)%30
                p_y2=pos_y-(pos_y-50)%30
                xy=(p_x2,p_y2)
                if xy in qi and but==3: qi.remove(xy)
                elif xy not in open:
                    if but==1:
                        if xy in lei: over=True
                        else: open.append(xy)
                    elif but==3 and len(qi)<shu: qi.append(xy)
            elif c_x1<=pos_x<=c_x1+40 and 10<=pos_y<=30:
                reo(290,330,10)
                c_x1,c_x2,c_x3=70,130,190
            elif c_x2<=pos_x<=c_x2+40 and 10<=pos_y<=30:
                reo(500,540,40)
                c_x1,c_x2,c_x3=80,230,400
            elif c_x3<=pos_x<=c_x3+40 and 10<=pos_y<=30:
                reo(920,540,99)
                c_x1,c_x2,c_x3=100,410,790
            elif c_x2-5<=pos_x<=c_x2+45 and 35<=pos_y<=45: tool=True
            elif tool: tool=False
    if len(open)==num_x*num_y-shu and len(qi)==shu: win=True
    for i in open:
        n=find(i)
        pg.draw.rect(screen,ground,(i[0],i[1],30,30))
        if n!=0: p_text(n,'black',font,i[0]+10,i[1]+5,20)
    for i in qi: screen.blit(i3,(i[0],i[1]))
    if time<10: p_text('00{}'.format(time),'black',font,10,10,30)
    elif time<100: p_text('0{}'.format(time),'black',font,10,10,30)
    else: p_text(time,'black',font,10,10,30)
    p_text(shu-len(qi),'black',font,scr_x-40,10,30)
    p_text('初级','black',font,c_x1,10,20)
    p_text('中级','black',font,c_x2,10,20)
    p_text('高级','black',font,c_x3,10,20)
    p_text('开发者选项','red',font,c_x2-5,35,10)
    for i in range(10,scr_x,30): pg.draw.line(screen,'black',(i,50),(i,scr_y-10))
    for j in range(50,scr_y,30): pg.draw.line(screen,'black',(10,j),(scr_x-10,j))
    while l<shu:
        _i=rd.randrange(10,scr_x-39,30)
        _j=rd.randrange(50,scr_y-39,30)
        if (_i,_j) not in lei:
            lei.append((_i,_j))
            l+=1
    if over:
        for i in lei:
            if i!=xy: screen.blit(i1,(i[0]+1,i[1]+1))
        screen.blit(i2,(xy[0]+1,xy[1]+1))
    if tool: screen.blit(i5,(c_x2-110,50))
    elif win:
        for i in lei: screen.blit(i4,(i[0]+1,i[1]+1))
    elif not over:
        time2+=1
        if time2==60:
            time+=1
            time2=0
    pg.display.flip()