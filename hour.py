from datetime import datetime

class Hour(object):


    def __init__(self, post):
        self.post = post

    def post_hour(self):
        self.hour = [
                [int(input('\nHorario do post {} : '.format(hour_count))),
                        int(input('Minuto : '))]
                for hour_count in range(1, self.post + 1)]
        self.hour_check()

        return self.hour


    def hour_check(self):
        for check in self.hour:
            if (check[0] > 23 or check[0] < 0
                    and check[1] > 59 or check[1] < 0):
                print('Horario Invalido.')
                print('\n')
                self.post_hour()
