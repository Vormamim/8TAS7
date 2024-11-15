import random

# stats
monster_hp = 20
player_hp = 20

def attackMonster():
    global player_hp
    global monster_hp
    player_dmg = random.randint(3,6)
    monsterDodge = random.randint(1,10)

    print('You attacked the monster...\n')

    if monsterDodge <= 9:
        print(f'You hit the monster for {player_dmg} damage!\n')
        monster_hp -= player_dmg
        print(f'The monster is now on {monster_hp} health!\n')
    elif monsterDodge > 9:
        print(f'WOAH! The monster dodged out of the way.\nThe monster is still on {monster_hp} health!\n')
    print(f'You are on {player_hp} health!')
        
def useHeal():
    global monster_hp
    global player_hp
    healAmt = random.randint(1,7)

    print(f'You use a healing potion!\nYou healed... {healAmt} health!')
    player_hp += healAmt
    if player_hp > 20:
        player_hp = 20
    print(f'You are now at {player_hp} health!\nThe monster is at {monster_hp} health!')

def monsterTurn():
    global monster_hp
    global player_hp
    monster_dmg = random.randint(1,2)
    player_dodgeChance = random.randint(1,5)
    if player_dodgeChance <= 4:
        print(f'The monster attacks and hits you for {monster_dmg} damage!')
        player_hp -= monster_dmg
        print(f'You are now on {player_hp} health')
    elif player_dodgeChance > 4:
        print('The monster attacked, but you dodged!')
        print(f'You are still on {player_hp} health')

def playerTurn():
    global monster_hp
    global player_hp
    print('You can now do something! What would you like to do?\nType: attack, heal, hint')
    playerBattleMove = input().strip().lower()
    if playerBattleMove[0] == str('a'):
        attackMonster()
    elif playerBattleMove == str('heal'):
        useHeal()
    else:
        print(f'When using a healing potion, it can heal anywhere from 1 to 7 health.\nThe monster is on {monster_hp} health! Keep attacking to kill it!')

def battleSequence():
    monsterTurn()
    playerTurn()
    print('\n')

#start scene
def sceneThree():
    print('As soon as you leave the building, the harsh light burns your eyes. Once they adjust, you see that a couple meters in front of you, a monster stands in your way. You pull out your pocket knife and get ready to fight.\n')

    while monster_hp > 0:
        battleSequence()

    print('You beat the monster!!!\nIt dropped a fragment of sorts that you put into your pocket. You advance to the next room.')