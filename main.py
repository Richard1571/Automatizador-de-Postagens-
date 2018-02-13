import os
from datetime import datetime
from facebook_post import Post
from hour import Hour
from time import sleep
from imagem import add_imagem

def hour():
    try:
        post = int(input('Quantidade de post : '))
        hours = Hour(post).post_hour()
    except:
        hour()

    return hours


def imagem_or_text(hour):
    post_hour = dict()

    for quest in hour:
        question = input('Imagem or text hour {}:{} :  '.format(quest[0],quest[1])).lower()
        if question == 'imagem':
            local = os.getcwd()
            post_hour[str(quest[0]) + ':' + str(quest[1])] = add_imagem()
            os.chdir(local)
        else:
            post_hour[str(quest[0]) + ':' + str(quest[1])] = input('Message : ')

    return post_hour

def main():
    token = input('Token da pagina : ')
    postagen = Post(token)
    post_published = imagem_or_text(hour())

    while True:

        if (str(datetime.now().hour) + ':' + str(datetime.now().minute)
                in post_published.keys()):
            horario = str(datetime.now().hour) + ':' + str(datetime.now().minute)

            if type(post_published[horario]) == list:
                sleep(55)
                postagen.public_photo(post_published[horario][0],
                                            post_published[horario][1])
            else:
                sleep(57)
                postagen.public_post(post_published[horario])

main()
