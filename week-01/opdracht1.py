# Oefening 1
# Print de volgende zin "Hello World"

print(Hello World)


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Burak"
leeftijd = 16
woonstad = "Utrecht"


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")


print("hallo mijn naam is", naam, "Mijn leeftijd is", leeftijd, "Ik woon in", woonstad)

# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"

game = "Warzone"
duur = 150
print("Mijn favoriete game is:" + game)

# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit

number1 = 8
number2 = 6


som = number1 + number2
verschil = number1 - number2
product = number1 * number2
print(som,verschil,product)

# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

name = "Max"
health = 150
level = 12 
damage = 50

print(name,health,level,damage)

health -= 20
print(health)

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 

name = "Max"
health = 150
level = 12 
damage = 50
weapon ="machine gun"
print(name,health,level,damage)

health -= 20
damage += 25
level += 1
print(health,damage,level)



# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

name ="Burak"
age = 16
favouriteGame = "Warzone"
hoursPlayed = 100
level = 96
score = 360
power = 450
speed = 10
gun = "uzi"

print(Name, age, favouriteGame, hoursPlayed, level, score, power, speed, gun)
score +=250
print(score)

