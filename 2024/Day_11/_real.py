from collections import defaultdict

with open("11.in") as file:
    data = list(map(int, file.read().strip().split(" ")))


nums = defaultdict(int)
for val in data:
    nums[val] += 1

def blink(nums):
    updated_data = defaultdict(int)

    for stone in nums:
        stone_length = len(str(stone))
        if int(stone) == 0:
            updated_data[1] += nums[0]
        elif stone_length % 2 == 0:
            updated_data[int(str(stone)[:(stone_length // 2)])] += nums[stone]
            updated_data[int(str(stone)[stone_length // 2:])] += nums[stone]
        else:
            updated_data[int(stone) * 2024] += nums[stone]
    return updated_data

nb_blinks = 75
stones_order = nums
for n in range(nb_blinks):
    stones_order = blink(stones_order)

ans = 0
for x in stones_order:
    ans += stones_order[x]

print(ans)



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