import random
jargentina = [(1,'Agustina Gorzelany'),
             (2,'Maria Jose Granatto'),
             (3,'Sofia Toccalino'),
             (4,'Agostina Alonso'),
             (5,'Valentina Raposo'),
             (6,'Clara Barberi'),
             (7,'Delfina Thome'),
             (8,'Sofia Cairó'),
             (9,'Pilar Campoy'),
             (10,'Agustina Albetario'),
             (11,'Maria Pilar Campoy'),]
jaustralia = [(1,'Madonna Blyth'),
             (2,'Toni Cronk'),
             (3,'Alice Arnot'),
             (4,'Katrina Powell'),
             (5,'Kobie Mcgurk'),
             (6,'Jocelyn Bartman'),
             (7,'Maddison Brooks'),
             (8,'Jane Claxton'),
             (9,'Claire Colwill'),
             (10,'Penny Squibb'),
             (11,'Grace Stewart'),]
f = open('pases.txt', 'w') #Abre o crea el archivo .txt
 
def escribir_resultado(pais, jugador, tiempo, estado_pase): # Escribe en txt (Sobreescribe si es necesario)
    f.write(f"{pais};{jugador[0]};{jugador[1]};{estado_pase};{tiempo}\n") # Escribe en el archivo .txt con el orden de los datos precisado con un salto de renglón guardado todo en una variable
    
def main():
    tiempo = 0
    while tiempo<=60: # Se utiliza para que sea dentro del partido de 60 minutos
        pases = 0
        while pases<819: # Se necesita esta cantidad para generar los 50000 registros propuestos en promedio
            if random.randint(0,1)==0: # Determina de manera aleatoria si la jugadora es Australiana, que jugador es el que realiza el pase, si el pase es efectivo y envia los valores hacia la funcion escribir_resultado
                escribir_resultado("Australia", random.choice(jaustralia) ,tiempo,random.randint(0,1))
            else: # Determina de manera aleatoria si la jugadora es Argentina, que jugador es el que realiza el pase, si el pase es efectivo y envia los valores hacia la funcion escribir_resultado
                escribir_resultado("Argentina", random.choice(jargentina) ,tiempo,random.randint(0,1))
            pases +=1 
        tiempo +=1
    f.close() # Cierra el archivo para poder visualizarlo
main() # Ejecuta el programa principal
