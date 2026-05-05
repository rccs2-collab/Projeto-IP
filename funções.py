# Talvez não seja necessário então não precisa ler se não quiser

# a partir da linha 23

#para ser usado em um lado
count=[80, 7, 3, 10, 27] #soma igual a 127 pois exclui o lugar do jogador
valores=["P","M","O","C","N"]
ordem=[]

size_pedra=40

#parametros
M="M"
O="O"
C="C"
X="X"
N="N"


# a partir da linha 204

def mapear():
    objeto=""
    for y in range(16):
        for x in range(17):
            objeto = mapa[y][x]
            print(objeto)
            if type(objeto)==int:
                rect_pedras.append(Pedra(x*40,y*40,objeto))
                rect_pedras[-1].definir()
            elif objeto=="M":
                rect_pedras.append(Magnetita(x*40,y*40))
                rect_pedras[-1].definir()
            elif objeto=="O":
                rect_pedras.append(Ouro(x*40,y*40))
                rect_pedras[-1].definir()
            elif objeto=="C":
                rect_pedras.append(Cobre(x*40,y*40))
                rect_pedras[-1].definir()
            elif objeto=="X":
                rect_pedras.append(Muro(x*40,y*40))
                rect_pedras[-1].definir()
            elif objeto=="N":
                pass
            else:
                print(objeto)
                print("erro")
            

def espelhar():
    for y in range(16):
        for x in range(8):
            mapa[y][-x-1]=mapa[y][x]

def construir():
    a=0
    b=0
    c=False
    for i in range(127):
        c=False
        a=random.randrange(sum(count))
        for f in range(len(count)):
            if c==False:
                if count[f]>a:
                    a=f
                    c=True
                else:
                    a-=count[f]
        
        if valores[a]=="P":
            b=random.randrange(11)
            if b<6:
                ordem.append(15)
            elif b<10:
                ordem.append(22)
            else:
                ordem.append(30)
        else:
            ordem.append(valores[a])
        count[a]-=1
        if count[a]==0:
            valores.pop(a)
            count.pop(a)
    
    
    a=0
    for y in range(16):
        for x in range(8):
            #vai bloco por bloco, mas não coloca no lugar do jogador
            if not(y==15 and x==0):
                #print(f"a={a}, x={x}, y={y}")
                mapa[y][x]=ordem[a]
                a+=1