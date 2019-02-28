import re
import random


rubrica = []
nuovo_contatto = []
saluti = ['ciao','A presto!!','Bella!']
insulti = ['Ignorante!','Imapara a scrivere!','Mi prendi in giro?']

i = 0
def program():
    try:
        print('''
            
          §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
          §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
          §§                                                                             §§
          §§                Benvenuto al programma Rubrica!                              §§
          §§                Per vedere i contatti premi L;                               §§
          §§                Per cercare un contatto premi R;                             §§
          §§                Per creare un contatto premi C;                              §§
          §§                Per cancellare un contatto premi E;                          §§
          §§                Per modificare un contatto premi M;                          §§
          §§                Per uscire dal programma premi Q;                            §§
          §§                © By jaskomalpreet                                           §§
          §§                                                                             §§
          §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
          §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

        ''')

        while True:
            choose = input('\n===> ').upper()
            
            if not re.match("^[A-Z]*$", choose):
                print(random.choice(insulti))
                print('\nACCETTO SOLO LETTERE!')
            
            if len(choose) > 15:
                print('NON ACCETTO TROPPI CARATTERI.')


            if choose == 'Q':
                print(random.choice(saluti))

                break


            if choose == 'L':
                if rubrica == []:
                    print("La tua rubrica e' vuota")
                    print('Dunque ora uscirai dalla funzione LISTA.')
                else:
                    print('La tua rubrica è composta da: \n')
                    for contatto in rubrica:
                        i +=1
                        print('{}. {}'.format(i, contatto))
                       
           
            if choose == 'R':
                if rubrica == []:
                    print('Non puoi cercare contatti perchè la tua rubrica è vuota...')
                    print('Dunque ora uscirai dalla funzione CERCA')
                else :
                    print('Scrivi il nome o il cognome del contatto che vuoi cercare;')
                    cerca1 = input()
                        
                    for contact in rubrica:
                        if cerca1 in contact :
                            print('-.-\n')
                            print(contact)
                        


            if choose == 'C':
                print('Inserisci il nome del nuovo contatto')
                nome = input('===> ')
                print('Inserisci il cognome del nuovo contatto')
                cognome = input('===> ')
                print('Inserisci il numero del nuovo contatto')
                numero = input('===> ')
                while not re.match("^[0-9]*$", numero):
                    print(random.choice(insulti))
                    print('\n COME PUOI METTERE LETTERE NEL NUMERO TELEFONICO?!?!')
                    print('Inserisci il numero del nuovo contatto')
                    numero = input('===> ')
                
                newContact = str(' ' + nome +' ' + cognome + ' ' + numero)
                print('CONFERMI LA CREAZIONE DI UN NUOVO CONTATTO: ')
                print(newContact)
                print('Y/N')
                n = input().upper()
                if n == 'Y':
                    rubrica.append(newContact)
                    print('Contatto creato.')
                else :
                    print('Crezione del contatto annullata.')
                    continue
            
            if choose == 'E':
                if rubrica == []:
                    print('La tua rubrica è vuota, perciò non puoi eliminare contatti')
                    print('Dunque ora uscirai dalla funzione ELIMINA')

                else:
                    print('Scrivi il nome del contatto che vuoi eliminare: ')
                    name = input()
                    for contact in rubrica:
                        if  name in contact:
                            rubrica.remove(contact)
                            if contact not in rubrica:
                                print('{}: {}'.format('Ho rimosso',contact))
            



            if choose == 'M':
                if rubrica == []:
                    print('La tua rubrica è vuota, perciò non puoi modificare niente.')
                    print('Dunque ora uscirai dalla funzione MODIFCA')    

                else:
                    print('Dimmi il nome o il cognome del contatto che vuoi modificare.')
                    name = input('===> ')
                    for contact in rubrica:
                        
                        if name in contact:
                            print(contact)
                            print('è questo il contatto che vuoi modificare?\n Y/N')
                            qw = input('===> ').upper()
                            if qw == 'Y':
                                rubrica.remove(contact)
                                print('Inserisci il nome del nuovo contatto')
                                nome = input('===> ')
                                print('Inserisci il cognome del nuovo contatto')
                                cognome = input('===> ')
                                print('Inserisci il numero del nuovo contatto')
                                numero = input('===> ')
                                while not re.match("^[0-9]*$", numero):
                                    print(random.choice(insulti))
                                    print('\n COME PUOI METTERE LETTERE NEL NUMERO TELEFONICO?!?!')
                                    print('Inserisci il numero del nuovo contatto')
                                    numero = input('===> ')
                                
                                newContact = str(' ' + nome +' ' + cognome + ' ' + numero)
                                print('CONFERMI LA CREAZIONE DI UN NUOVO CONTATTO: ')
                                print(newContact)
                                print('Y/N')
                                n = input().upper()
                                if n == 'Y':
                                    rubrica.append(newContact)
                                    print('Contatto creato.')
    
    except KeyboardInterrupt:
        print('Potevi anche uscire normamente dal programma anzichè interrompermi....')




program()


    







