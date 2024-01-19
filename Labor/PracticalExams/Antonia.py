import random

import numpy as np
import matplotlib.pyplot as plt

'''
Die Zufallsgröße Y ist gegeben durch

P (X = 1) = 0.4, P (Y = 2) = 0.6.

(a) Experiment: Man generiert 3 zufällige Werte für Y. Sei Z die Zufallsgröße die anzeigt wie oft die 2 unter diesen 3 Werten auftaucht (z.B. [2,1, 1] → Z = 1; [1, 1, 1] → Z = 0 usw.)

Man generiere 2000 zufällige Werte für die Zufallsgröße Z. Man gebe jeden möglichen Wert von Z und die entsprechende relative hfg an mit print -> hat die relative Hfg.= ...")).

(B) man gebe die theoretische wharscheinlichkeitsverteilung von Z an  dh alle theoretische werte die Z annehmen kann und die entsprechenden Wahrscheinlichkeiten zb mit print()
annehmen kann und die entsprechenden Wahrscheinlichkeiten, zB. mit print (f" P (Z=. ..)=...").

(c) Man zeichne das Histogramm der relativen Häufigkeiten von den 2000 simulierten Werten für Z.

(d) Man schätze die Wahrscheinlichkeit P({Z = 0} oder {Z = 3}) und gebe den theoretischen Wert an für P({Z = 0} oder {Z = 3}).
'''

y_values = [1, 2]
p_y = [0.4, 0.6]
Z = [0, 1, 2, 3]
N = 2000
count_2 = 0
count_0 = 0
count_1 = 0
count_3 = 0
simulated_values = []
for _ in range(N):
    count = 0
    D = np.random.choice(y_values, p=p_y, size=3, replace=True)
    for value in D:
        if value == 2:
            count += 1
        if count == 0:
            count_0 += 1
        if count == 1:
            count_1 += 1
        if count == 2:
            count_2 += 1
        if count == 3:
            count_3 += 1
    simulated_values.append(count)

counts = [count_0, count_1, count_2, count_3]
print(f"Z = 0 Relative Haufigkeiten: {count_0 / N}")
print(f"Z = 1 Relative Haufigkeeiten: {count_1 / N}")
print(f"Z = 2 Relative Haufigkeiten: {count_2 / N}")
print(f"Z = 3 Relative Haufigkeeiten: {count_3 / N}")

relative_frequencies = [count_0 / N, count_1 / N, count_2 / N, count_3 / N]

# Plot a bar chart with relative frequencies
plt.bar(Z, relative_frequencies, width=0.8, color="cyan", edgecolor="black")
# Set plot attributes
plt.grid()
plt.xlabel("")
plt.ylabel("relative Haufigkeiten")
plt.title("")
# Set x-axis ticks
plt.xticks(range(0, 4))
# Display the plot
plt.show()

probability_0 = np.mean(simulated_values == 0)
probability_3 = np.mean(simulated_values == 3)
simulated_probability = probability_0 + probability_3
print(f"Simulated probability P(Z=0 oder Z = 3) : {simulated_probability}")

print(f"Theoretische Whk: P(Z = 0) {0.4 ** 3}")
print(f"Theoretische Whk: P(Z = 3) {0.6 ** 3}")
th_probability = 0.4 * 3 + 0.6 * 3

print(f"Theoretische Whk: P(Z=0 oder Z = 3): {th_probability}")

th_probability_0 = 0.4 ** 3
th_probability_3 = 0.6 ** 3
# 2,1,2, 2,2,1 1,2,2
th_probability_2 = 0.6 * 0.4 * 0.6 + 0.6 * 0.6 * 0.4 + 0.4 * 0.6 * 0.6
th_probability_1 = 1 - (th_probability_2 + th_probability_3 + th_probability_0)
whk_verteilung = [th_probability_0,th_probability_1,th_probability_2,th_probability_3]
for i in range(len(Z)):
    print(f"P(Z = {Z[i]}) = {whk_verteilung[i]}")