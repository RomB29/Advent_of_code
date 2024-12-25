from collections import defaultdict

with open("11.in") as file:
    data = list(map(str, file.read().strip().split(" ")))

def rules(stone):
    if int(stone) == 0:
        stone = "1"
        return stone
    if len(stone) % 2 == 0:
        stone_left = str(int(stone[0 : len(stone) // 2]))
        stone_right = str(int(stone[len(stone) // 2 : ]))

        return stone_left, stone_right
    else:
        stone = int(stone) * 2024
    return str(stone)

def blink(data):
    new_order = []
    for stone in data:
        test = rules(stone)
        if isinstance(test, tuple):
            new_order.append(test[0])
            new_order.append(test[1])
        else:
            new_order.append(test)
    return new_order

nb_blinks = 25
stones_order = data
for n in range(nb_blinks):
    stones_order = blink(stones_order)
    print(len(stones_order))

print(len(stones_order))



# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

# # Les termes de la séquence
# terms = np.array([11, 14, 22, 36, 55, 67, 101, 163, 258, 380, 547, 863, 1294, 1979, 3108, 4480, 6812, 10614, 16107, 24581, 36354, 55899, 86088, 128479, 197157, 298207, 451511, 691050, 1042454, 1593214, 2412128, 3647808, 5588381, 8443081, 12833134])

# # Les indices des termes
# n = np.arange(len(terms))

# # Fonction exponentielle
# def exponential_func(x, a, b):
#     return a * np.power(b, x)

# # Ajustement de la courbe
# params, covariance = curve_fit(exponential_func, n, terms)

# # Extraction des paramètres
# a, b = params

# print(a * b ** 35)
# # Affichage des résultats
# print(f"Équation exponentielle approximative : y = {a:.2f} * {b:.2f}^n")

# # Tracer les données et la courbe ajustée
# plt.scatter(n, terms, label='Données')
# plt.plot(n, exponential_func(n, a, b), label=f'y = {a:.2f} * {b:.2f}^n', color='red')
# plt.xlabel('n')
# plt.ylabel('Termes')
# plt.legend()
# plt.show()