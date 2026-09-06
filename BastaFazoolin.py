class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.brunch = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
    self.early_bird = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
    self.dinner = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
    self.kids ={'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
    
    if name == "brunch" and start_time >= 1100 and end_time <= 1600:
      print("Brunch menu available from 1100 to 1600\n")
      print(self.brunch)
    elif name == "early bird" and start_time >= 1500 and end_time <= 1800:
      print("Early bird menu available from 1500 to 1800\n")
      print(self.early_bird)
    elif name == "dinner" and start_time >= 1700 and end_time <= 2300:
      print("Dinner menu available from 1700 to 2300\n")
      print(self.dinner)
    elif name == "kids" and start_time >= 1100 and end_time <= 2100:
      print("Kids menu available from 1100 to 2100\n")
      print(self.kids)
    else :
      print("Restart program. ")
      return 0

    food = []
    total = 0

    for item in range(0,items):
      self.temp = input("Choose item no." + str(item+1) + " from the menu :")
      self.temp = self.temp.lower()
      if name == "brunch" :
        for item_brunch in self.brunch :
          if self.temp == item_brunch :
            food.append(self.temp)
            total += self.brunch[self.temp]
          else:
            print("Item not found in brunch menu")
      elif name == "early bird" :
        for item_early_bird in self.early_bird :
          if self.temp == item_early_bird :
            food.append(self.temp)
            total += self.early_bird[self.temp]
          else:
            print("Item not found in brunch menu")
      elif name == "dinner" :
        for item_dinner in self.dinner :
          if self.temp == item_dinner :
            food.append(self.temp)
            total += self.dinner[self.temp]
          else:
            print("Item not found in brunch menu")
      elif name == "kids" :
        for item_kids in self.kids :
          if self.temp == item_kids :
            food.append(self.temp)
            total += self.kids[self.temp]
          else:
            print("Item not found in brunch menu")

    print("List of ordered food: ", food)
    print(f"Total price of food ordered : {total:.2f}")

    

print("Welcome to Basta Fazoolin!")
type_of_meal = input("""Memu Timings:
Brunch : 1100 - 1600 hours
Early Bird : 1500 - 1800 hours
Dinner : 1700 - 2300 hours
Kids : 1100 - 2100 hours
Which menu would you like to choose (Brunch, Early Bird, Dinner, Kids) : """)
type_of_meal = type_of_meal.lower()
time_entry = int(input("Time of entry (24 hrs): "))
time_exit = int(input("Time of exit (24 hrs): "))
item_num = int(input("Number of items : "))
Menu(type_of_meal,item_num,time_entry,time_exit)
