import random
tiempo = 0
jargentina= [('Agustina Gorzelany',11),
             ('Maria Jose Granatto',9),
             ('Sofia Toccalino',20),
             ('Agostina Alonso',10),
             ('Valentina Raposo',8),
             ('Clara Barberi',5),
             ('Delfina Thome',4),
             ('Sofia Cairó',7),
             ('Pilar Campoy',16),
             ]
jaustralia= [('Madonna Blyth',9),
             ('Toni Cronk',8),
             ('',20),
             ('Katrina Powell',10),
             ('',8),
             ('',5),
             ('',4),
             ('',7),
             ('',16),
            ]
def pase():
        if randint(0,1)==1:
            print('el pase fue exitoso')
        else
            print('el pase no fue exitoso')
def paseargentina():
    print('La jugadora 'jargentina[randint(0,8)],' hizo un pase en el minuto 'tiempo,end=' ')
def paseaustralia():
    print('La jugadora 'jaustralia[randint(0,8)],' hizo un pase en el minuto 'tiempo,end=' ')
while tiempo<=60:
    tiempo = randint(tiempo,60)
    if randint(0,1)==0:
        paseaustralia(tiempo)
        pase()
    else:
        paseargentina(tiempo)
        pase()