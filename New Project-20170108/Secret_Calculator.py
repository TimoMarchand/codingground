# Hello World program in Python

MageSecrets=['Counterspell', 'Duplicate', 'Effigy', 'IceBarrier', 'IceBlock', 'MirrorEntity', 'PotionOfPolymorph', 'Spellbender', 'Vaporize']
PaladinSecrets=['Avenge', 'CompetitiveSpirit', 'EyeForAnEye', 'GetawayKodo', 'NobleSacrifice', 'Redemption', 'Repentance', 'SacredTrial']
HunterSecrets=['BearTrap', 'CatTrick', 'DartTrap', 'ExplosiveTrap', 'FreezingTrap', 'HiddenCache', 'Misdirection', 'SnakeTrap', 'Snipe']

Class = raw_input('Against which class are you playing? ')

if Class == 'Mage':
    while len(MageSecrets)>1:
        print MageSecrets
        action = raw_input('What did you do? ')
        if action == 'CastSpellHero':
            if MageSecrets.count('Counterspell') == 1:
                MageSecrets.remove('Counterspell')
        elif action == 'KillMinion':
            if MageSecrets.count('Duplicate') == 1:
                MageSecrets.remove('Duplicate')
            if MageSecrets.count('Effigy') == 1:
                MageSecrets.remove('Effigy')
        elif action == 'AttHeroWithHero':
            if MageSecrets.count('IceBarrier') == 1:
                MageSecrets.remove('IceBarrier')
        elif action == 'AttHeroWithMinion':
            if MageSecrets.count('IceBarrier') == 1:
                MageSecrets.remove('IceBarrier')
            if MageSecrets.count('Vaporize') == 1:
                MageSecrets.remove('Vaporize')
        elif action == 'KillHero':
            if MageSecrets.count('IceBlock') == 1:
                MageSecrets.remove('IceBlock')
        elif action == 'PlayMinion':
            if MageSecrets.count('MirrorEntity') == 1:
                MageSecrets.remove('MirrorEntity')
            if MageSecrets.count('PotionOfPolymorph') == 1:
                MageSecrets.remove('PotionOfPolymorph')
        elif action == 'CastSpellMinion':
            if MageSecrets.count('Spellbender') == 1:
                MageSecrets.remove('Spellbender')
            if MageSecrets.count('Counterspell') == 1:
                MageSecrets.remove('Counterspell')
        else:
            print 'What is that?'
            print 'Choose from: CastSpellHero, KillMinion, AttHeroWithHero, AttHeroWithMinion, KillHero, PlayMinion, CastSpellMinion'
            
elif Class == 'Paladin':
    while len(PaladinSecrets)>1:
        print PaladinSecrets
        action = raw_input('What did you do? ')
        if action == 'KillOneOfOpponentMinions':
            if PaladinSecrets.count('Avenge') == 1:
                PaladinSecrets.remove('Avenge')
            if PaladinSecrets.count('GetawayKodo') == 1:
                PaladinSecrets.remove('GetawayKodo')
            if PaladinSecrets.count('Redemption') == 1:
                PaladinSecrets.remove('Redemption')
        elif action == 'OppTurnStart':
            if PaladinSecrets.count('CompetitiveSpirit') == 1:
                PaladinSecrets.remove('CompetitiveSpirit')
        elif action == 'DealDamageHero':
            if PaladinSecrets.count('EyeForAnEye') == 1:
                PaladinSecrets.remove('EyeForAnEye')
        elif action == 'KillOnlyMinion':
            if PaladinSecrets.count('GetawayKodo') == 1:
                PaladinSecrets.remove('GetawayKodo')
            if PaladinSecrets.count('Redemption') == 1:
                PaladinSecrets.remove('Redemption')
        elif action == 'Attack':
            if PaladinSecrets.count('NobleSacrifice') == 1:
                PaladinSecrets.remove('NobleSacrifice')
        elif action == 'PlayMinion':
            if PaladinSecrets.count('Repentance') == 1:
                PaladinSecrets.remove('Repentance')
        elif action == 'PlayMinionWithAtLeast3Minions':
            if PaladinSecrets.count('Repentance') == 1:
                PaladinSecrets.remove('Repentance')
            if PaladinSecrets.count('SacredTrial') == 1:
                PaladinSecrets.remove('SacredTrial')
        else:
            print 'What is that?'
            print wif2
            
elif Class == 'Hunter':
    while len(HunterSecrets)>1:
        print HunterSecrets
        action = raw_input('What did you do? ')
        if action == 'AttHeroWithHero':
            if HunterSecrets.count('BearTrap') == 1:
                HunterSecrets.remove('BearTrap')
            if HunterSecrets.count('ExplosiveTrap') == 1:
                HunterSecrets.remove('ExplosiveTrap')
            if HunterSecrets.count('Misdirection') == 1:
                HunterSecrets.remove('Misdirection')
        elif action == 'AttHeroWithMinion':
            if HunterSecrets.count('BearTrap') == 1:
                HunterSecrets.remove('BearTrap')
            if HunterSecrets.count('ExplosiveTrap') == 1:
                HunterSecrets.remove('ExplosiveTrap')
            if HunterSecrets.count('FreezingTrap') == 1:
                HunterSecrets.remove('FreezingTrap')
            if HunterSecrets.count('Misdirection') == 1:
                HunterSecrets.remove('Misdirection')
        elif action == 'AttMinionWithHero':
            if HunterSecrets.count('SnakeTrap') == 1:
                HunterSecrets.remove('SnakeTrap')
        elif action == 'AttMinionWithMinion':
            if HunterSecrets.count('FreezingTrap') == 1:
                HunterSecrets.remove('FreezingTrap')
            if HunterSecrets.count('SnakeTrap') == 1:
                HunterSecrets.remove('SnakeTrap')
        elif action == 'CastSpell':
            if HunterSecrets.count('CatTrick') == 1:
                HunterSecrets.remove('CatTrick')
        elif action == 'UseHeroPower':
            if HunterSecrets.count('DartTrap') == 1:
                HunterSecrets.remove('DartTrap')
        elif action == 'PlayMinion':
            if HunterSecrets.count('HiddenCache') == 1:
                HunterSecrets.remove('HiddenCache')
            if HunterSecrets.count('Snipe') == 1:
                HunterSecrets.remove('Snipe')
        else:
            print 'What is that?'
            print wif2
            
print MageSecrets
