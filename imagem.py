import os 

def add_imagem():
    try:
        os.chdir('Imagens')
        imagem = [open(input('Imagem name : '),'rb').read(),input('Mensagem : ')]
    except:
        add_imagem()
    return imagem
