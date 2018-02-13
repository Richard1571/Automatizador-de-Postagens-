import facebook

class Post(object):

    def __init__(self, token):
        self.token = token
        self.graph = facebook.GraphAPI(self.token)


    def public_post(self, message):
        self.mensagem = message
        self.graph.put_wall_post(message)

    def public_photo(self, image, message_post):
        self.message = message_post
        self.image = image
        self.graph.put_photo(self.image,message=self.message)
