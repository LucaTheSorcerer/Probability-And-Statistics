import random
import matplotlib.pyplot as plt

# Funktion zur Generierung von 3 zufälligen Werten für Y und Berechnung von Z
def generate_Z():
    Y = [random.randint(1, 6) for _ in range(3)]
    return Y.count(2)

# Simuliere 2000 Zufallsereignisse für Z
simulated_values = [generate_Z() for _ in range(2000)]

# Berechne relative Häufigkeiten
relative_frequencies = {i: simulated_values.count(i) / 2000 for i in set(simulated_values)}

# Gebe jeden möglichen Wert von Z und die entsprechende relative Häufigkeit aus
print("Z   Relative Häufigkeit")
for value, frequency in sorted(relative_frequencies.items()):
    print(f"{value}   {frequency:.4f}")

# Theoretische Wahrscheinlichkeitsverteilung von Z
theoretical_distribution = {0: (5/6) * 3, 1: 3 * (1/6) * (5/6) * 2, 2: 3 * (1/6) * 2 * (5/6), 3: (1/6) * 3}

# Gebe die theoretischen Werte und ihre Wahrscheinlichkeiten aus
print("\nTheoretische Wahrscheinlichkeitsverteilung:")
for value, probability in sorted(theoretical_distribution.items()):
    print(f"{value}   {probability:.4f}")

# Histogramm der relativen Häufigkeiten
plt.bar(relative_frequencies.keys(), relative_frequencies.values(), width=0.5, align='center', alpha=0.7)
plt.title('Histogramm der relativen Häufigkeiten von Z')
plt.xlabel('Z')
plt.ylabel('Relative Häufigkeit')
plt.show()