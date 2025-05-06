def f(x, y):
    resultat = 3 * x**2 - 2 * y + 5
    return resultat


def aire_trapeze(B, b, h):
    A = ((B + b) / 2) * h  # (B + b) * h / 2
    return A


def prix(n, p, p_enfant=8.5, p_adulte=12.0):
    total_enfant = n * p_enfant
    total_adulte = p * p_adulte
    total = total_enfant + total_adulte
    return total


print("Fonction deux variables")
print(f(2, 3))
print(f(10, 1))


print("Aires trapezes")
print(aire_trapeze(5, 3, 4))  # 16.0
print(aire_trapeze(10, 5, 2))  # 15.0

print("Prix entrées")
print(prix(2, 3))
print(prix(10, 1))
