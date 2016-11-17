# Hello World program in Python
    
MageSecrets=['Counterspell', 'Duplicate', 'Effigy', 'IceBarrier', 'IceBlock', 'MirrorEntity', 'Spellbender', 'Vaporize']
PaladinSecrets=[]
HunterSecrets=[]

Class=raw_input('Against which class are you playing? ')

if Class == 'Mage':
    while len(MageSecrets)>1:
        print MageSecrets
        action=raw_input('What did you do? ')
        if action == 'CastSpellHero':
            MageSecrets.remove('Counterspell')
        elif action == 'KillMinion':
            MageSecrets.remove('Duplicate')
            MageSecrets.remove('Effigy')
        elif action == 'AttHero':
            MageSecrets.remove('IceBarrier')
            MageSecrets.remove('Vaporize')
        elif action == 'KillHero':
            MageSecrets.remove('IceBlock')
        elif action == 'PlayMinion':
            MageSecrets.remove('MirrorEntity')
        elif action == 'CastSpellMinion':
            MageSecrets.remove('Counterspell')
            MageSecrets.remove('Spellbender')
        else:
            print 'What is that?'
            
elif Class == 'Paladin':
    while len(PaladinSecrets)>1:
        print 'hello'

print