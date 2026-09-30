class Plant:
    def __init__ (self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        print(f"\n{self.name} attacks {zombie.name} for {self.damage} damage.")
        zombie.take_damage(self.damage)


    def take_damage(self, amount):
        self.amount -= amount
        self.health -= amount
        if self.health > 0:
            self.health = 0
        print(f"\nPlant has been hit by {zombie.take_damage}")


class zombie:
    def __init__ (self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage =  damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance -= 1
        print(f"\n{self.name} walked 1 step close. Current distance: {self.distance}")

    def attack(self, plant):
        print(f"\n{self.name} attacks {plant.name} for {self.damage} damage.")
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"\n{self.name} took {amount} damage. (Remaining health: {self.health})")

    def run_game():
        plant1 = Plant("Yohann", 65, 15)
        plant2 = Plant("Kurt", 67, 10)
        zombie = zombie("Jamich", 300, 40, 8)
        plants = {plant1, plant2}

        turn = 1

        while True:
            print(f"\nTurn {turn}")

        for plant in plants:
            if plant.health > 0:
                plant.attack(zombie)
            if zombie.health <= 0:
                print(f"\n{zombie.name} has been defeated. Plants win.") 
                return
            if zombie.distance > 0:
                zombie.move()
            else:
                target = target = next((p for p in plants if p.health > 0), None)
            if target:
                zombie.attack(target)

            if all(p.health <= 0 for p in plants):
                print (f"Both plants have been defeated, {zombie.name} win!")
                return
                print(f"{p.name} HP: {p.health}")
                print(f"\n {zombie.name} HP: {zombie.health}.")
                turn += 1
                
            if___name__ == "__main__"
            run.game()





            


