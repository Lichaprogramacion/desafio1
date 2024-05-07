import random
tiempo = 0
jargentina= [(1,'Agustina Gorzelany'),
             (2,'Maria Jose Granatto'),
             (3,'Sofia Toccalino'),
             (4,'Agostina Alonso'),
             (5,'Valentina Raposo'),
             (6,'Clara Barberi'),
             (7,'Delfina Thome'),
             (8,'Sofia Cairó'),
             (9,'Pilar Campoy'),
             (10,'Agustina Albetario'),
             (11,'Maria Pilar Campoy'),
             ]
jaustralia= [(1,'Madonna Blyth'),
             (2,'Toni Cronk'),
             (3,'Alice Arnot'),
             (4,'Katrina Powell'),
             (5,'Kobie Mcgurk'),
             (6,'Jocelyn Bartman'),
             (7,'Maddison Brooks'),
             (8,'Jane Claxton'),
             (9,'Claire colwill'),
             (10,'Penny Squibb'),
             (11,'Grace Stewart'),
            ]
f = open('resultado.txt', 'w')
def pase():
        if random.randint(0,1)==1:
            return 1
        else:
            return 0
def paseargentina(tiempo):
    escribir=str(('Argentina',jargentina[random.randint(0,8)],pase(),tiempo))
    f.write(escribir + '\n')
def paseaustralia(tiempo):
    escribir=str(('Australia',jaustralia[random.randint(0,8)],pase(),tiempo,))
    f.write(escribir + '\n')
while tiempo<60:
    tiempo = random.randint(tiempo,tiempo+1)
    if random.randint(0,1)==0:
        jugadora=paseaustralia(tiempo)
        pase()
    else:
        jugadora=paseargentina(tiempo)
        pase()
f.close()

