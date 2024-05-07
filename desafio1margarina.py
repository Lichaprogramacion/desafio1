import random
tiempo = 0
jargentina= [(11,'Agustina Gorzelany'),
             (9,'Maria Jose Granatto'),
             (20,'Sofia Toccalino'),
             (10,'Agostina Alonso'),
             (8,'Valentina Raposo'),
             (5,'Clara Barberi'),
             (4,'Delfina Thome'),
             (7,'Sofia Cairó'),
             (16,'Pilar Campoy'),
             ]
jaustralia= [(9,'Madonna Blyth'),
             (8,'Toni Cronk'),
             (20,'Alice Arnot'),
             (10,'Katrina Powell'),
             (1,'Kobie Mcgurk'),
             (5,'Jocelyn Bartman'),
             (4,'Maddison Brooks'),
             (7,'Jane Claxton'),
             (16,'Claire colwill'),
            ]
def pase():
        if random.randint(0,1)==1:
            print('el pase fue exitoso')
        else:
            print('el pase no fue exitoso')
def paseargentina(tiempo):
    print('La jugadora',jargentina[random.randint(0,8)],'hizo un pase en el minuto',tiempo,end=' ')
def paseaustralia(tiempo):
    print('La jugadora',jaustralia[random.randint(0,8)],'hizo un pase en el minuto',tiempo,end=' ')
while tiempo<60:
    tiempo = random.randint(tiempo,tiempo+1)
    if random.randint(0,1)==0:
        jugadora=paseaustralia(tiempo)
        pase()
    else:
        jugadora=paseargentina(tiempo)
        pase()
