#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CLASSES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MINÉRIOS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Pedra (pygame.sprite.Sprite):
    def __init__(self,x_pedra,y_pedra,durabilidade=1):
        pygame.sprite.Sprite.__init__(self)
        #propriedades básicas
        self.durabilidade=durabilidade
        self.x=x_pedra
        self.y=y_pedra
        self.pedra=False
        self.image=0
        self.cor=(0,0,0)
        self.rect="" #objeto retângulo
    
    #desenhar a pedra na tela
    '''    def definir(self):
        self.pedra=True
        self.image=pygame.image.load("overlay.png")
        self.rect=self.image.get_rect()
        self.rect.topleft = self.x, self.y
        todas_as_sprites.add(self)'''
    
    '''
    def mostrar (self):
        self.cor=(140-self.durabilidade*4,140-self.durabilidade*4,140-self.durabilidade*4)
        self.rect=pygame.draw.rect(tela,self.cor,(self.x,self.y,size_pedra,size_pedra))'''
    
    #função chamada para reduzir a durabilidade
    def quebrar (self, nome):
        self.durabilidade-=nome.dano_picareta
        if self.durabilidade<=0:
            nome.items["Pedra"]+=2
            rect_pedras.remove(self)
            self.kill()
    def restaurar (self, nome):
        while (self.durabilidade<=31) and (nome.items["Pedra"]>0):
            self.durabilidade+=1
            nome.items["Pedra"]-=1

class Magnetita(Pedra):
    '''def definir (self):
        self.image=pygame.image.load("minerio_magnetita.png")
        self.rect=self.image.get_rect()
        self.rect.topleft = self.x, self.y
        todas_as_sprites.add(self)'''
    
    def restaurar (self, nome):
        pass
    
    #função chamada para reduzir a durabilidade
    def quebrar (self,nome):
        nome.items["Magnetita"]+=1
        nome.dano_picareta=1+(nome.items["Magnetita"]//2)
        rect_pedras.remove(self)
        self.kill()
        print(nome.items)

class Cobre(Pedra):
    '''def definir (self):
        self.image=pygame.image.load("minerio_cobre.png")
        self.rect=self.image.get_rect()
        self.rect.topleft = self.x, self.y
        todas_as_sprites.add(self)'''
    
    def restaurar (self, nome):
        pass
    
    #função chamada para reduzir a durabilidade
    def quebrar (self,nome):
        nome.items["Cobre"]+=1
        rect_pedras.remove(self)
        self.kill()
        print(nome.items)

class Ouro(Pedra):
    '''def definir (self):
        self.image=pygame.image.load("minerio_ouro.png")
        self.rect=self.image.get_rect()
        self.rect.topleft = self.x, self.y
        todas_as_sprites.add(self)'''
    
    def restaurar (self, nome):
        pass
    
    #função chamada para reduzir a durabilidade
    def quebrar (self,nome):
        nome.items["Ouro"]+=1
        rect_pedras.remove(self)
        self.kill()
        print(nome.items)

class Muro (Pedra):
    '''def definir (self):
        self.image=pygame.image.load("muro.png")
        self.rect=self.image.get_rect()
        self.rect.topleft = self.x, self.y
        todas_as_sprites.add(self)'''
    
    def restaurar (self, nome):
        pass
    
    def quebrar (self, nome):
        pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PERSONAGEM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Personagem (pygame.sprite.Sprite):
    def __init__(self,x_personagem,y_personagem):
        pygame.sprite.Sprite.__init__(self)
        self.x=x_personagem
        self.y=y_personagem
        self.picareta=""
        self.x_picareta=0
        self.y_picareta=0
        self.pic_size=0
        self.facing="up"
        self.dano_picareta=1
        self.picareta_ativa=False
        self.restaurar_ativa=False
        self.items={"Magnetita":0,"Cobre":0,"Ouro":0, "Pedra":0}
        self.images=0
        self.rect=""
        self.imagem_atual="robo_cima_1.png"
        self.Magnetita=""
        self.Cobre=""
        self.Ouro=""
        self.Pedra=""
    
    def mover (self):
        self.rect.topleft = self.x, self.y
    
    '''def definir (self,imagem):
        self.kill()
        self.image=pygame.image.load(imagem)
        self.image=pygame.transform.scale(self.image,(x_jog,y_jog))
        self.rect=self.image.get_rect()
        self.rect.topleft = self.x, self.y
        todas_as_sprites.add(self)'''
    
    def minerar(self,modo):
        
        self.pic_size=16
        
        if self.facing=="up":
            self.x_picareta=self.x+x_jog/2
            self.y_picareta=self.y-self.pic_size
            self.pic_size=1
        
        if self.facing=="down":
            self.x_picareta=self.x+x_jog/2
            self.y_picareta=self.y+y_jog
            self.pic_size=1
        
        if self.facing=="left":
            self.x_picareta=self.x-self.pic_size
            self.y_picareta=self.y+y_jog/2
        
        if self.facing=="right":
            self.x_picareta=self.x+x_jog
            self.y_picareta=self.y+y_jog/2
        
        #desenhar a picareta/
        self.picareta=pygame.draw.rect(tela,(255,255,255),(self.x_picareta,self.y_picareta,self.pic_size,17-self.pic_size))
        if modo=="destruir":
            self.picareta_ativa=True
        elif modo=="restaurar":
            self.restaurar_ativa=True
    
    def mostrar_pontuação (self):
        a=0
        base=0
        if self == oponente:
            base=360
        for minerio in self.items:
            a+=1
            self.minerio=f":{self.items[minerio]}"
            self.minerio = fonte.render(self.minerio, False, (255,255,255))
            if a>1:
                base+=30
            tela.blit(self.minerio,(40*a+base,655))