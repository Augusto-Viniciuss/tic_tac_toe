import pygame, os

def CarregaImagem(name, colorkey = None, scale = 0.3):
    caminhoCompleto = os.path.join("./imgs", name)
    imagem = pygame.image.load(caminhoCompleto)
    
    tamanho = imagem.get_size()
    tamanho = (tamanho[0] * scale, tamanho[1] * scale)
    imagem = pygame.transform.scale(imagem, tamanho)
    
    imagem = imagem.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = imagem.get_at((0, 0))
        imagem.set_colorkey(colorkey, pygame.RLEACCEL)
    return imagem, imagem.get_rect()
