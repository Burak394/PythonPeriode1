# Cijfers voor drie vakken
math_grade = 7
english_grade = 6
dutch_grade = 5

# Gemiddelde berekenen
average = (math_grade + english_grade + dutch_grade) / 3

# Gemiddelde laten zien
print("Gemiddelde:", average)

# Controleren of de student geslaagd is
if average >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")