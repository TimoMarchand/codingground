# Hello World program in Python
import random

Fehler = 0
Wort = ['hallo', 'Tisch', 'Stuhl']

while len(Wort)>0:
    Frage = (random.choice(Wort))
    if Frage == 'hallo':
        RichtigeAntwort = 'hello'
    elif Frage == 'Tisch':
        RichtigeAntwort = 'Table'
    elif Frage == 'Stuhl':
        RichtigeAntwort = 'Chair'
    Antwort = raw_input(Frage+': ')
    if RichtigeAntwort == Antwort:
        print 'Hurra'
        Wort.remove(Frage)
    else:
        print 'Falsch, die richtige Antwort war: '+RichtigeAntwort
        Fehler = Fehler+1
        
print 'Du hast alles geschafft!'
print 'Du hast nur',Fehler,'Fehler gemacht!'