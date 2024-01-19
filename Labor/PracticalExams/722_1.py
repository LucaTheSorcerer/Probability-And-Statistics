import numpy as np
import matplotlib.pyplot as plt

"""
Die unabhängigen Zufallsgrößen X und Y haben foldende Wahrscheinlichkeitsverteilung
       -1   0    1   2
X,Y ~ (025 0.25 025 025)
 - a) Man generiere 2000 zufällige Daten für die Zufallsgröße X + Y. Man gebe die erhaltenen Werte und die entsprechenden
relativen Häufigkeiten an, zB. mit print (f" X+y=... hat relative Hfg.=...").
 - (b) Man zeichne das Histogramm der relativen Häufigkeiten von den 2000 simulierten Werten für X + Y
 - (c) Man schätze P(X + Y < 1).
 - (b) Man gebe die theoretische Wahrscheinlichkeitsverteilung von X + Y an, d.h. alle möglichen Werte die X + Y annehmen
kann und die entsprechenden Wahrscheinlichkeiten, zB. mit print (f" P (X+Y=. . .) =.. ").
 - (c) Man gebe die theoretischen Wert an für P(X + Y < 1).
"""

# #a)

# N = 2000
# x = [-1, 0, 1, 2]
# P = [0.25, 0.25, 0.25, 0.25]
# rng = np.random.default_rng()
# x_rng = rng.choice(x, size=N, replace=True, p=P)
# y_rng = rng.choice(x, size=N, replace=True, p=P)

# print(f"X+Y = {x_rng + y_rng} hat relative Hfg. = {np.unique(x_rng + y_rng, return_counts=True)[1] / N}")

# #b)
# plt.hist(x_rng + y_rng, bins=4, color="red", edgecolor="black", label="relative Haufigkeiten")
# plt.legend(loc="upper left")
# plt.grid()
# plt.show()

# #c)
# print(f"P(X+Y<1) = {np.sum(np.where(x_rng + y_rng < 1, 1, 0)) / N}")

# #d)
# print(f"P(X+Y=-1) = {P[0]}")
# print(f"P(X+Y=0) = {P[1]}")
# print(f"P(X+Y=1) = {P[2]}")
# print(f"P(X+Y=2) = {P[3]}")

import numpy as np
import matplotlib.pyplot as plt

# Given probabilities
P = [0.25, 0.25, 0.25, 0.25]
x = [-1, 0, 1, 2]
N = 2000

# Generate random data for X and Y
rng = np.random.default_rng()
x_rng = rng.choice(x, size=N, replace=True, p=P)
y_rng = rng.choice(x, size=N, replace=True, p=P)

# a) Calculate and print the relative frequencies for X + Y
xy_sum = x_rng + y_rng
unique_values, counts = np.unique(xy_sum, return_counts=True)
relative_frequencies = counts / N

for i in range(len(unique_values)):
    print(f"X + Y = {unique_values[i]} has relative frequency = {relative_frequencies[i]}")

# b) Plot the histogram of the relative frequencies
plt.hist(xy_sum, bins=4, color="red", edgecolor="black", label="Relative Frequencies")
plt.legend(loc="upper left")
plt.grid()
plt.show()

# c) Estimate P(X + Y < 1)
p_x_y_lt_1 = np.sum(np.where(xy_sum < 1, 1, 0)) / N
# p_x_y_lt_2 = np.mean(xy_sum < 1)
print(f"P(X + Y < 1) = {p_x_y_lt_1}")
# print(f"P(X + Y < 1) = {p_x_y_lt_2}")

# d) Theoretical probability distribution of X + Y
theoretical_probabilities = [P[0], P[1], P[2], P[3]]
x_values = [-1, 0, 1, 2]

for x_val in x_values:
    print(f"P(X + Y = {x_val}) = {theoretical_probabilities[x_val + 1]}")


# e) Theoretical value for P(X + Y < 1)
theoretical_p_x_y_lt_1 = np.sum([theoretical_probabilities[i] for i in range(len(unique_values)) if unique_values[i] < 1])
print(f"Theoretical P(X + Y < 1) = {theoretical_p_x_y_lt_1}")


