def binary_addition(A, B):
    max_length = max(len(A), len(B))
    A = A.zfill(max_length)
    B = B.zfill(max_length)

    result = ''
    carry = 0

    for i in range(max_length - 1, -1, -1):
        bit_a = int(A[i])
        bit_b = int(B[i])

        # Calcul de la somme et de la retenue
        sum_bit = bit_a ^ bit_b ^ carry
        carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))

        # Ajout du bit de somme au résultat
        result = str(sum_bit) + result

    # Ajout de la retenue finale si elle existe
    if carry:
        result = '1' + result

    return result

# Exemples d'utilisation
A = "1101"
B = "111"
print(binary_addition(A, B))
