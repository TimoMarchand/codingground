# Hello World program in Python
    
HunterSecrets=['BearTrap', 'CatTrick', 'DartTrap', 'ExplosiveTrap', 'FreezingTrap', 'Misdirection', 'SnakeTrap', 'Snipe']    
MageSecrets=['Counterspell', 'Duplicate', 'Effigy', 'IceBarrier', 'IceBlock', 'MirrorEntity', 'PotionOfPolymorph', 'Spellbender', 'Vaporize']
PaladinSecrets=['Avenge', 'CompetitiveSpirit', 'EyeForAnEye', 'GetawayKodo', 'Noble Sacrifice', 'Redemption', 'Repentance', 'SacredTrial']

Class=raw_input('Against which class are you playing? ')

if Class == 'Hunter':
    while len(HunterSecrets)>1:
        print HunterSecrets
        action = raw_input('What did you do? ')
        if action == 'AttHeroWithHero':
            HunterSecrets.remove('BearTrap')
            HunterSecrets.remove('ExplosiveTrap')
            HunterSecrets.remove('Misdirection')
        elif action == 'AttHeroWithMinion':
            HunterSecrets.remove('BearTrap')
            HunterSecrets.remove('ExplosiveTrap')
            HunterSecrets.remove('FreezingTrap')
            HunterSecrets.remove('Misdirection')
        elif action == 'AttMinionWithHero':
            HunterSecrets.remove('SnakeTrap')
        elif action == 'AttMinionWithMinion':
            HunterSecrets.remove('FreezingTrap')
            HunterSecrets.remove('SnakeTrap')
        elif action == 'CastSpell':
            HunterSecrets.remove('CatTrick')
        elif action == 'UseHeroPower':
            HunterSecrets.remove('DartTrap')
        elif action == 'PlayMinion':
            HunterSecrets.remove('Snipe')
        else:
            print 'What is that?'
            

elif Class == 'Mage':
    while len(MageSecrets)>1:
        print MageSecrets
        action = raw_input('What did you do? ')
        if action == 'CastSpellHero':
            MageSecrets.remove('Counterspell')
        elif action == 'KillMinion':
            MageSecrets.remove('Duplicate')
            MageSecrets.remove('Effigy')
        elif action == 'AttHeroWithMinion':
            MageSecrets.remove('IceBarrier')
            MageSecrets.remove('Vaporize')
        elif action == 'AttHeroWithHero':
            MageSecrets.remove('IceBarrier')
        elif action == 'KillHero':
            MageSecrets.remove('IceBlock')
        elif action == 'PlayMinion':
            MageSecrets.remove('MirrorEntity')
            MageSecrets.remove('PotionOfPolymorph')
        elif action == 'CastSpellMinion':
            MageSecrets.remove('Counterspell')
            MageSecrets.remove('Spellbender')
        else:
            print 'What is that?'
            
elif Class == 'Paladin':
    while len(PaladinSecrets)>1:
        print PaladinSecrets
        action == raw_input('What did you do? ')
        if action == 'KillOnlyMinion':
            PaladinSecrets.remove('GetawayKodo')
            PaladinSecrets.remove('Redemption')
        elif action == 'KillMinionWithOpp2OrMoreMinions':
            PaladinSecrets.remove('Avenge')
            PaladinSecrets.remove('GetawayKodo')
            PaladinSecrets.remove('Redemption')
        elif action == 'EndTurnWithOppMinion':
            PaladinSecrets.remove('CompetitiveSpirit')
        elif action == 'DealDamageToEnemyHero':
            PaladinSecrets.remove('EyeForAnEye')
        elif action == 'AttWithMinion':
            PaladinSecrets.remove('NobleSacrifice')
        elif action == 'PlayMinionWith2OrLessMinions':
            PaladinSecrets.remove('Repentance')
        elif action == 'PlayMinionwith3OrMoreMinions':
            PaladinSecrets.remove('Repentance')
            PaladinSecrets.remove('SacredTrial')

print