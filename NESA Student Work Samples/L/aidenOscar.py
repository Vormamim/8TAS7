import sys
from yachalk import chalk
output_text = chalk.green
errorText = chalk.red
choiceText = chalk.yellow_bright
def animate_text(self, text, delay=0.09):
      for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
class Game:
  def __init__(self):
      self.player_health = 100
      self.has_allied_with_khaleed = False
      self.has_potion = False
  def start(self):
      print("Welcome to the Quest to Save the Princess!")
      self.scene1_gates_of_runella()

  def scene1_gates_of_runella(self):
      print("\nScene 1: Gates of Runella")
      print("A towering gate looms above you. A guard stands in your way.")
      choice = input("Do you want to (1) fight the guard or (2) sneak past? Enter 1 or 2: ")
      if choice == "1":
          print("You fight and defeat the guard, but you lose 20 health.")
          self.player_health -= 20
      elif choice == "2":
          print("You successfully sneak past the guard.")
      else:
          print("Invalid choice. Try again.")
          self.scene1_gates_of_runella()
      self.scene2_city_of_runella()

  def scene2_city_of_runella(self):
      print("\nScene 2: City of Runella")
      print("You discover that the princess has been captured and venture into the Mystic Forest.")
      self.scene3_mystic_forest()

  def scene3_mystic_forest(self):
      print("\nScene 3: The Mystic Forest")
      print("You encounter magical trees and spirits.")
      event = input("Do you want to (1) rest or (2) continue? Enter 1 or 2: ")
      if event == "1":
          print("You rest. There is a random event.")
          random_event = ["poisonous water", "quick healing", "strength boost"]
          from random import choice
          event_outcome = choice(random_event)
          if event_outcome == "poisonous water":
              print("You drank poisonous water. You lose 30 health.")
              self.player_health -= 30
          elif event_outcome == "quick healing":
              print("You feel rejuvenated and gain 20 health.")
              self.player_health += 20
          else:
              print("You feel a surge of strength.")
      print("You move on toward the northern border - the desert.")
      self.scene4_desert()

  def scene4_desert(self):
      print("\nScene 4: The Desert")
      print("You must cross the harsh, grueling desert. Your health depletes with each step.")
      self.player_health -= 10
      choice = input("Do you want to (1) find the ruler Khaleed or (2) cross the desert alone? Enter 1 or 2: ")
      if choice == "1":
          print("You ally with Khaleed, who helps you cross the desert safely.")
          self.has_allied_with_khaleed = True
      else:
          print("You cross alone and lose more health.")
          self.player_health -= 20
      self.scene5_fake_castle()

  def scene5_fake_castle(self):
      print("\nScene 5: The Fake Castle")
      print("You find a potion of healing.")
      self.has_potion = True
      print("You encounter a clone of the evil lord.")
      choice = input("Do you want to (1) use the secret weapon or (2) fight normally? Enter 1 or 2: ")
      if choice == "1":
          print("You use the secret weapon and defeat the clone. He reveals he is not the real lord.")
      else:
          print("You fight and defeat the clone, but he reveals he is not the real lord.")
      self.scene6_castle_of_runella()

  def scene6_castle_of_runella(self):
      print("\nScene 6: The Castle of Runella")
      print("Weary and weak, you press on to rescue the princess.")
      if self.has_potion:
          print("You drink the potion and regain some strength.")
          self.player_health += 20
      print("You confront the real evil lord.")
      if self.player_health > 0:
          print("The evil lord is weak. You defeat him and save the princess.")
          print("Congratulations, you have completed your quest!")
      else:
          print("You are too weak to defeat the evil lord. Game Over.")

game = Game()
game.start()
