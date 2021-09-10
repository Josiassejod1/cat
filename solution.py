
class Cat:
 def __init__(self, name="cat", energy=2, stomach=2):
 self.name = name;
 self.energy = energy;
 self.stomach = stomach;

 def play(self):
 if self.energy > 0:
 print(f"{self.name} says meow");
 self.energy = self.energy - 1;
 elif self.energy < 1:
 print(f"{self.name} is tired.");
 

 def eat(self):
 if self.stomach > 0:
 print(f"{self.name} says nom");
 self.stomach = self.stomach - 1
 elif self.stomach < 1:
 print(f"{self.name} is full");


def main():
 name = input("Please enter the name of your cat: ")
 cat = Cat(name);
 def game():
 decision = input(f"How would you like to interact with {name}? Enter 'play' or 'feed': ");
 if decision == "feed":
 cat.eat();
 if decision == "q":
 exit()
 elif decision == "play": 
 cat.play();
 return cat
 
 chose = "";

 while(chose != "n"):
 cat = game();
 chose = input("Would you like to continue? y/n: ");
 
 print("Goodbye!")

main()
