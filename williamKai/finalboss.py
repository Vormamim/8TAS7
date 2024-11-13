import random
import sys
import time


def animateText(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

#stats for the player and boss
boss_hp = 80
player_hp = 20
player_healPotions = 4
with open('williamKai/enteringBossfight.txt', 'r') as enterBossFight:
    bossfightTXT = enterBossFight.read()

def attackBoss():
    global player_hp
    global boss_hp
    player_dmg = random.randint(3,10)
    bossDodge = random.randint(1,8)

    #add different lines of dialouge as a random chance (randint x,y - if z = x print 'example')

    print('You attacked the boss...\n')

    if bossDodge <= 7:
        print(f'You struck the boss for {player_dmg} damage!\n')
        boss_hp -= player_dmg
        print(f'The boss is now on {boss_hp} health!\n')
    elif bossDodge > 7:
        animateText(f'The boss jumps out of the way and evades your swing.\nThe boss is still on {boss_hp} health!\n')
    print(f'You are on {player_hp} health!')

def useHealBoss():
    global boss_hp
    global player_hp
    global player_healPotions

    if player_healPotions > 0:

        healAmt = random.randint(7,15)

        animateText(f'You use a healing potion!\nYou healed... {healAmt} health!')
        player_hp += healAmt
        if player_hp > 20:
            player_hp = 20

        player_healPotions -= 1
        print(f'You are now at {player_hp} health with {player_healPotions} heal potions left!\nThe boss is at {boss_hp} health!')
    else:
        animateText('You look for a healing potion, but it seems you don\'t have any healing potions left!!\nWhile you\'re distracted, the boss attacks!f')

def bossAttack():
    global boss_hp
    global player_hp
    boss_dmg = random.randint(1,3)
    player_dodgeChance = random.randint(1,6)
    if player_dodgeChance <= 5:
        print(f'The boss attacks and hits you for {boss_dmg} damage!')
        player_hp -= boss_dmg
        print(f'You are now on {player_hp} health')
    elif player_dodgeChance > 5:
        animateText('The boss attacks you, but you see it coming and evade the attack.')
        print(f'You are still on {player_hp} health.')

def playerTurnBoss():
    global boss_hp
    global player_hp
    print('You find an opening to do something! What would you like to do?\nType: a (attack), h (heal), hint')
    playerBattleMove = input().strip().lower()
    if playerBattleMove[0] == str('a'):
        attackBoss()
    elif playerBattleMove[0] == str('h'):
        useHealBoss()
    else:
        animateText(f'When using a healing potion, it can heal anywhere from 2 to 7 health.\nThe boss is on {boss_hp}/80 health! Keep attacking to destroy it!')

def bossBattleSequence():
    if player_hp <= 0:
        animateText("Game Over! The mechanical monster proved too powerful.")
        sys.exit()
    bossAttack()
    playerTurnBoss()
    print('\n')



#Start scene
    #Entering bossfight room
def sceneFive():
    animateText(bossfightTXT)
    enterBossFight.close()
    doYouSummon = input('You understand the words and go over to it, you see a hole the right shape for your fragment. Do you place? Yes/No').strip().lower()
    if doYouSummon == str('yes'):
        animateText('You place the fragment into the pedestal and you immeditely see the pillar give way to what looks to be a cluster of pieces from your teleportation machine, moving around. It looks at you, menacingly, and you know you have to fight.')
        while boss_hp > 0:
            bossBattleSequence()

    else:
        animateText('You don\'t listen to the desicion you made, and go and place the fragment anyways.')
        animateText('You place the fragment into the pedestal and you immeditely see the pillar give way to what looks to be a cluster of pieces from your teleportation machine, moving around. It looks at you, menacingly, and you know you have to fight.')
        while boss_hp > 0:
            bossBattleSequence()

    animateText('After you dealt that blow, you felt the ground below you shake, as the mechanical robot begins to spazm and eventually, you see a glow coming from inside the robot as it explodes and all that is left is a big mass of light. As you are blinded, you feel your body being pulled in, and eventually consumed. The next thing you know, your eyes adjust to see that you are standing outside the lab waving goodbye to your colleagues as they pack up the experiments for the day. "What happened?", you think, as you slowly walk home. "Oh well, musn\'t dwell on it too long, I\'ve got work tomorrow. I hear that someone\'s going to be lounching the first test of our new machine! Exciting."')


if __name__ == "__main__":
    sceneFive()
