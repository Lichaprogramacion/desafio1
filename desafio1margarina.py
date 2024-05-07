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
        if random.randint(0,1)==1:
            print('el pase fue exitoso')
        else:
            print('el pase no fue exitoso')
def paseargentina():
    print('La jugadora ',jargentina[random.randint(0,8)],' hizo un pase en el minuto ',tiempo,end=' ')
def paseaustralia():
    print('La jugadora ',jaustralia[random.randint(0,8)],' hizo un pase en el minuto ',tiempo,end=' ')
while tiempo<61:
    tiempo = random.randint(tiempo,60)
    if random.randint(0,1)==0:
        jugadora=paseaustralia(tiempo)
        pase()
    else:
        jugadora=paseargentina(tiempo)
        pase()
