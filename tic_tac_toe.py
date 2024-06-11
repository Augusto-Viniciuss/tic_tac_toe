import pygame, sys, time
import load_assets as cr

dimensaoX = 600
dimensaoY = 800

checaErros = pygame.init()

if checaErros[1] > 0:
    print(f"Erro: {checaErros[1]}")
else:
    print("Jogo Inicializado com Sucesso")
    
pygame.display.set_caption("Jogo da Velha")
janelaDoJogo = pygame.display.set_mode((dimensaoX, dimensaoY)) 
 
branco = pygame.Color(255, 255, 255)
cinza = pygame.Color(54, 54, 54)
violeta = pygame.Color(72, 61, 139)

X, XRect = cr.CarregaImagem("X.png")
O, ORect = cr.CarregaImagem("O.png")
 
controleDeFPS = pygame.time.Clock()
    
class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [0, 1, 2, 
                          3, 4, 5,
                          6, 7, 8]
        
        self.numeroDeJogadas = 0
        
    def insereJogada(self, indice, simbolo):
        self.tabuleiro[indice] = simbolo
        self.numeroDeJogadas += 1
    
    def verificaTabuleiro(self):
        if self.tabuleiro[0] == self.tabuleiro[1] and self.tabuleiro[1] == self.tabuleiro[2]:
            return True, self.tabuleiro[0]
        elif self.tabuleiro[3] == self.tabuleiro[4] and self.tabuleiro[4] == self.tabuleiro[5]:
            return True, self.tabuleiro[3]
        elif self.tabuleiro[6] == self.tabuleiro[7] and self.tabuleiro[7] == self.tabuleiro[8]:
            return True, self.tabuleiro[6] 
        elif self.tabuleiro[0] == self.tabuleiro[4] and self.tabuleiro[4] == self.tabuleiro[8]:
            return True, self.tabuleiro[4]
        elif self.tabuleiro[2] == self.tabuleiro[4] and self.tabuleiro[4] == self.tabuleiro[6]:
            return True, self.tabuleiro[2]
        elif self.tabuleiro[0] == self.tabuleiro[3] and self.tabuleiro[3] == self.tabuleiro[6]:
            return True, self.tabuleiro[0]
        elif self.tabuleiro[1] == self.tabuleiro[4] and self.tabuleiro[4] == self.tabuleiro[7]:
            return True, self.tabuleiro[1]
        elif self.tabuleiro[2] == self.tabuleiro[5] and self.tabuleiro[5] == self.tabuleiro[8]:
            return True, self.tabuleiro[2]
        elif self.numeroDeJogadas == 9:
            return True, "VELHA" 
        else:
            return False, ""
                
def MontaTabuleiro():
    pygame.draw.rect(janelaDoJogo, cinza, pygame.Rect(50, 50, 500, 500), border_radius= 20)
       
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(65, 65, 150, 150), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(225, 65, 150, 150), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(385, 65, 150, 150), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(65, 225, 150, 150), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(225, 225, 150, 150), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(385, 225, 150, 150), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(65, 385, 150, 150), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(225, 385, 150, 150), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, branco, pygame.Rect(385, 385, 150, 150), border_radius= 20)
  
def InformaAVezDoJogador(rodada, fonte, cor, tamanho):
    if rodada % 2 == 0:
        simbolo = "O"
    else:
        simbolo = "X"
    
    fonteDoTexto = pygame.font.SysFont(fonte, tamanho)

    textoQueInforma = fonteDoTexto.render(f"Vez de: {simbolo}", True, cor)
    textoQueInformaRect = textoQueInforma.get_rect()
    textoQueInformaRect.midtop = (300, 580)
    
    pygame.draw.rect(janelaDoJogo, cinza, pygame.Rect(220, 580, 160, 40), border_radius= 20)   
    
    janelaDoJogo.blit(textoQueInforma, textoQueInformaRect)

def InicializaVariaveis():
    global tabuleiro, simbolo, rodada, acabouAPartida, velocidade
    global campo0, campo1, campo2, campo3, campo4, campo5, campo6, campo7, campo8
    campo0 = campo1 = campo2 = campo3 = campo4 = campo5 = campo6 = campo7 = campo8 = False
    velocidade = 30
    simbolo = "X"
    rodada = 1
    acabouAPartida = False
    tabuleiro = Tabuleiro()
    janelaDoJogo.fill(violeta)
    InformaAVezDoJogador(rodada, "arial black", branco, 25)
    MontaTabuleiro()
    
pontosDoJogador1 = pontosDoJogador2 = 0
posicaoDoMouse = [0, 0]

InicializaVariaveis()

def AtualizaCampos(simbolo, indice):
    if indice == 0:
        if simbolo == "X":
            XRect.midtop = (145, 68)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (145, 68)
            janelaDoJogo.blit(O, ORect)
    elif indice == 1:
        if simbolo == "X":
            XRect.midtop = (305, 68)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (305, 68)
            janelaDoJogo.blit(O, ORect)
    elif indice == 2:
        if simbolo == "X":
            XRect.midtop = (465, 68)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (465, 68)
            janelaDoJogo.blit(O, ORect)
    elif indice == 3:
        if simbolo == "X":
            XRect.midtop = (145, 228)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (145, 228)
            janelaDoJogo.blit(O, ORect)
    elif indice == 4:
        if simbolo == "X":
            XRect.midtop = (305, 228)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (305, 228)
            janelaDoJogo.blit(O, ORect)
    elif indice == 5:
        if simbolo == "X":
            XRect.midtop = (465, 228)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (465, 228)
            janelaDoJogo.blit(O, ORect)
    elif indice == 6:
        if simbolo == "X":
            XRect.midtop = (145, 388)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (145, 388)
            janelaDoJogo.blit(O, ORect)
    elif indice == 7:
        if simbolo == "X":
            XRect.midtop = (305, 388)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (305, 388)
            janelaDoJogo.blit(O, ORect)
    elif indice == 8:
        if simbolo == "X":
            XRect.midtop = (465, 388)
            janelaDoJogo.blit(X, XRect)
        elif simbolo == "O":
            ORect.midtop = (465, 388)
            janelaDoJogo.blit(O, ORect)
        
def MostraPontuacao(pontosDoJogador1, pontosDoJogador2, fonte, cor, tamanho):
    fonteDoTexto = pygame.font.SysFont(fonte, tamanho)
    
    textoPontuacao = fonteDoTexto.render("Pontuação", True, cor)
    textoDosPontosDoJogador1 = fonteDoTexto.render(f"X: {pontosDoJogador1}", True, cor)
    textoDosPontosDoJogador2 = fonteDoTexto.render(f"O: {pontosDoJogador2}", True, cor)
    
    RectPontuacao = textoPontuacao.get_rect()
    RectPontosDoJogador1 = textoDosPontosDoJogador1.get_rect()
    RectPontosDoJogador2 = textoDosPontosDoJogador2.get_rect()
    RectPontuacao.midtop = (300, 650)
    RectPontosDoJogador1.midtop = (150, 720)
    RectPontosDoJogador2.midtop = (450, 720)
    
    pygame.draw.rect(janelaDoJogo, cinza, pygame.Rect(210, 650, 180, 40), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, cinza, pygame.Rect(100, 720, 100, 40), border_radius= 20)
    pygame.draw.rect(janelaDoJogo, cinza, pygame.Rect(400, 720, 100, 40), border_radius= 20)
    
    janelaDoJogo.blit(textoPontuacao, RectPontuacao)
    janelaDoJogo.blit(textoDosPontosDoJogador1, RectPontosDoJogador1)
    janelaDoJogo.blit(textoDosPontosDoJogador2, RectPontosDoJogador2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            posicaoDoMouse = pygame.mouse.get_pos()
            if rodada % 2 == 0:
                simbolo = "O"
            else:
                simbolo = "X"
     
    if ((posicaoDoMouse[0] >= 65 and posicaoDoMouse[0] <= 214) and (posicaoDoMouse[1] >= 64 and posicaoDoMouse[1] <= 214)) and not campo0:
        tabuleiro.insereJogada(0, simbolo)
        rodada += 1
        campo0 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 0)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    elif ((posicaoDoMouse[0] >= 224 and posicaoDoMouse[0] <= 375) and (posicaoDoMouse[1] >= 64 and posicaoDoMouse[1] <= 214)) and not campo1:
        tabuleiro.insereJogada(1, simbolo)
        rodada += 1
        campo1 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 1)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    elif ((posicaoDoMouse[0] >= 384 and posicaoDoMouse[0] <= 534) and (posicaoDoMouse[1] >= 64 and posicaoDoMouse[1] <= 214)) and not campo2:
        tabuleiro.insereJogada(2, simbolo)
        rodada += 1
        campo2 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 2)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    elif ((posicaoDoMouse[0] >= 65 and posicaoDoMouse[0] <= 214) and (posicaoDoMouse[1] >= 224 and posicaoDoMouse[1] <= 374)) and not campo3:
        tabuleiro.insereJogada(3, simbolo)
        rodada += 1
        campo3 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 3)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    elif ((posicaoDoMouse[0] >= 224 and posicaoDoMouse[0] <= 375) and (posicaoDoMouse[1] >= 224 and posicaoDoMouse[1] <= 374)) and not campo4:
        tabuleiro.insereJogada(4, simbolo)
        rodada += 1
        campo4 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 4)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    elif ((posicaoDoMouse[0] >= 384 and posicaoDoMouse[0] <= 534) and (posicaoDoMouse[1] >= 224 and posicaoDoMouse[1] <= 374)) and not campo5:
        tabuleiro.insereJogada(5, simbolo)
        rodada += 1
        campo5 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 5)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    elif ((posicaoDoMouse[0] >= 65 and posicaoDoMouse[0] <= 214) and (posicaoDoMouse[1] >= 384 and posicaoDoMouse[1] <= 533)) and not campo6:
        tabuleiro.insereJogada(6, simbolo)
        rodada += 1
        campo6 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 6)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    elif ((posicaoDoMouse[0] >= 224 and posicaoDoMouse[0] <= 375) and (posicaoDoMouse[1] >= 384 and posicaoDoMouse[1] <= 533)) and not campo7:
        tabuleiro.insereJogada(7, simbolo)
        rodada += 1
        campo7 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 7)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    elif ((posicaoDoMouse[0] >= 384 and posicaoDoMouse[0] <= 534) and (posicaoDoMouse[1] >= 384 and posicaoDoMouse[1] <= 533)) and not campo8:
        tabuleiro.insereJogada(8, simbolo)
        rodada += 1
        campo8 = True
        posicaoDoMouse = [0, 0]
        AtualizaCampos(simbolo, 8)
        InformaAVezDoJogador(rodada, "arial black", branco, 25)
    
    acabouAPartida, simboloGanhador = tabuleiro.verificaTabuleiro()
    
    pygame.display.update()
        
    if acabouAPartida:
        controleDeFPS.tick(0.6)
        if simboloGanhador == "X":
            pontosDoJogador1 += 1
            InicializaVariaveis()
            
            acabouAPartida = False
            simboloGanhador = ""
        elif simboloGanhador == "O":
            pontosDoJogador2 += 1
            InicializaVariaveis()
            
            acabouAPartida = False
            simboloGanhador = ""
        else:
            InicializaVariaveis()
            
            acabouAPartida = False
            simboloGanhador = ""
                
    MostraPontuacao(pontosDoJogador1, pontosDoJogador2, "arial black", branco, 25)
    
    controleDeFPS.tick(velocidade)
