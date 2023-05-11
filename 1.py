from scipy.integrate import quad


def f(x):
    return x * (x + 1/2)


print(quad(f, 0, 1))
