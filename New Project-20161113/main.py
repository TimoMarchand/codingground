# Hello World program in Python
    
Secrets=['IceBlock', 'IceBarrier', 'Duplicate']
print Secrets
while len(Secrets)>1:
    action=raw_input('What did you do? ')
    if action == 'KillMinion':
        del Secrets[2]
    elif action == 'AttHero':
        del Secrets[1]
    elif action == 'KillHero':
        del Secrets[0]
    print Secrets
    print len(Secrets)
print Secrets