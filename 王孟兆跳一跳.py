import pygame as pg,sys,os,random as rd


pg.init()


pg.display.set_caption('王孟兆跳一跳')
screen=pg.display.set_mode((1000,600))
type,ti,b,t12,long,_time=1,60,0,285,0,None
i1=pg.image.load('OVER.png').convert()
i_p=pg.image.load('文字.jpg').convert()
pg.time.set_timer(pg.USEREVENT,2000)
pg.time.set_timer(pg.USEREVENT+1,5000)


def p_text(text,color,font,x,y,size):
    f=pg.font.SysFont(font,size)
    t=f.render(text,True,color)
    screen.blit(t,(x,y))


class hin(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.transform.rotozoom(pg.image.load('障碍.png').convert(),0,0.2)
        self.rect=self.image.get_rect(left=1000,top=322.9)
        self.mask=pg.mask.from_surface(self.image)
        self.long=0
    def update(self): self.rect.x-=5
    def draw(self): screen.blit(self.image,self.rect)


class player(pg.sprite.Sprite):
    def __init__(self,a):
        pg.sprite.Sprite.__init__(self)
        self.a=a
        self.t12=t12
        if self.a==0: self.image=pg.transform.rotozoom(pg.image.load('王孟兆.png').convert(),0,0.2)
        elif self.a==1: self.image=pg.transform.rotozoom(pg.image.load('王孟兆 - 副本.png').convert(),0,0.2)
        self.rect=self.image.get_rect(left=200,top=self.t12)
        self.mask=pg.mask.from_surface(self.image)
        self.j_v=19
        self.jump=None
    def update(self):
        if self.jump:
            self.rect.y-=self.j_v
            self.j_v-=1
            if self.rect.y==self.t12:
                self.j_v=19
                self.jump=None
    def draw(self): screen.blit(self.image,self.rect)


clock=pg.time.Clock()
hins=pg.sprite.Group()
player1=player(0)
player2=player(1)
while True:
    clock.tick(ti)
    screen.fill('white')
    for eve in pg.event.get():
        if eve.type==pg.QUIT:
            pg.quit()
            sys.exit()
        elif eve.type==pg.MOUSEBUTTONDOWN and type==1:
            p_x,p_y=eve.pos
            if 380<=p_x<=600 and 240<=p_y<=310:
                type=2
                _time=True
                hins.add(hin())
        elif type==2:
            if eve.type==pg.KEYDOWN:
                if eve.key==pg.K_SPACE: player1.jump=True
            elif eve.type==pg.USEREVENT:
                d1=rd.randint(-1,3)
                if d1!=0 and _time==None: hins.add(hin())
                else: _time=None
            elif eve.type==pg.USEREVENT+1 and ti<=100: ti+=2
        elif type==3 and eve.type==pg.MOUSEBUTTONDOWN:
            p_x,p_y=eve.pos
            if 280<=p_x<=370 and 350<=p_y<=400:
                pg.quit()
                sys.exit()
            if 600<=p_x<=740 and 350<=p_y<=400:
                python=sys.executable
                os.execl(python,python,*sys.argv)
    if type!=3:
        pg.draw.line(screen,'black',(0,400),(1000,400),2)
        if type==1:
            player1.draw()
            screen.blit(i_p,(100,50))
            pg.draw.rect(screen,'blue',(380,240,220,70))
            p_text('开始游戏','white','SimSun',390,250,50)
        elif type==2:
            long+=5
            for i in hins:
                if i.rect.x<=-50: hins.remove(i)
            hins.update()
            hins.draw(screen)
            player1.update()
            if b==0 or player1.jump or type==1:
                if pg.sprite.spritecollide(player1,hins,False,pg.sprite.collide_mask): type=3
                player1.draw()
                b=1
            else:
                if pg.sprite.spritecollide(player1,hins,False,pg.sprite.collide_mask): type=3
                player2.draw()
                b=0
            p_text('距离:{}m'.format(long//100),'black','SimSun',20,10,30)
    else:
        screen.blit(i1,(0,0))
        pg.draw.rect(screen,'red',(280,350,90,50))
        p_text('退 出','white','SimSun',290,360,30)
        pg.draw.rect(screen,'blue',(600,350,140,50))
        p_text('再试一次','white','SimSun',610,360,30)
    pg.display.flip()
