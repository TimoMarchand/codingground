# Hello World program in Python

Bluegill=input('Anzahl Bluegill Warriors: ')
Warleader=input('Anzahl Murloc Warleaders: ')
Murkeye=input('Anzahl Old Murk-Eyes: ')
Grimscale=input('Anzahl Grimscale Oracles: ')
Bluegill2=Bluegill
Warleader2=Warleader
Murkeye2=Murkeye
Grimscale2=Grimscale


if Bluegill+Warleader+Murkeye+Grimscale>7:
    while Bluegill+Warleader+Murkeye+Grimscale>7:
        if Grimscale>0:
            Grimscale=Grimscale-1
        elif Warleader>0:
            Warleader=Warleader-1
        elif Bluegill>0:
            Bluegill=Bluegill-1
        elif Murkeye>0:
            Murkeye=Murkeye-1
            
    MaxSchaden=Bluegill*2+(Warleader*(Bluegill+Murkeye))*2+(Murkeye*(1+Bluegill+Warleader+Murkeye+Grimscale))+Grimscale*(Murkeye+Bluegill)
    print MaxSchaden
    
    while Bluegill2+Warleader2+Murkeye2+Grimscale2>7:
        if Murkeye2>0:
            Murkeye2=Murkeye2-1
        elif Bluegill2>0:
            Bluegill2=Bluegill2-1
        elif Warleader2>0:
            Warleader2=Warleader2-1
        elif Grimscale2>0:
            Grimscale2=Grimscale2-1
            
    MinSchaden=Bluegill2*2+(Warleader2*(Bluegill2+Murkeye2))*2+(Murkeye2*(1+Bluegill2+Warleader2+Murkeye2+Grimscale2))+Grimscale2*(Murkeye2+Bluegill2)
    print MinSchaden
    
else:
    GesamtSchaden=Bluegill*2+(Warleader*(Bluegill+Murkeye))*2+(Murkeye*(1+Bluegill+Warleader+Murkeye+Grimscale))+Grimscale*(Murkeye+Bluegill)
    print GesamtSchaden