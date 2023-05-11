import numpy as np


def funct(u):
    return (-1 + np.sqrt(1 + 8 * u)) / 2


N_10_3 = 10**3
N_10_5 = 10**5
N_10_7 = 10**7
U_3 = np.random.uniform(0, 1, N_10_3)
U_5 = np.random.uniform(0, 1, N_10_5)
U_7 = np.random.uniform(0, 1, N_10_7)


X_3 = funct(U_3)
X_5 = funct(U_5)
X_7 = funct(U_7)

print(X_3)
print(X_5)
print(X_7)


print(np.mean(X_3))
print(np.mean(X_5))
print(np.mean(X_7))

print(np.abs(7/12 - np.mean(X_3)))
print(np.abs(7/12 - np.mean(X_5)))
print(np.abs(7/12 - np.mean(X_7)))
