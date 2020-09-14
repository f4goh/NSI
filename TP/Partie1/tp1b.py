"""
Boucles TP1b
https://www.w3schools.com/python/ref_func_zip.asp
https://www.w3schools.com/python/ref_func_enumerate.asp
"""
import doctest

def fct_1(val_x):
    """
    fonction que vous pouvez modifier selon les questions.
    La valeur de retour de la fonction est égal à
    x^2+2x+1
    Argument:
    x -- nombre
    >>> fct_1(3)
    16
    >>> fct_1(-4)
    9
    """
    return val_x ** 2 + 2 * val_x + 1

def fct_2(val_x):
    """
    fonction que vous pouvez modifier selon les questions.
    La valeur de retour de la fonction est égal à
    x^2-2x-1
    Argument:
    x -- nombre
    >>> fct_2(3)
    2
    >>> fct_2(-4)
    23
    """
    return val_x ** 2 - 2 * val_x - 1

doctest.testmod()
print("fc1 avec liste")
x = []
y = []
for v in range(0, 10):
    x.append(v)
    y.append(fct_1(v))
print('Les valeurs de x :', x)
print('les valeurs de fct1(x) : ', y)


print("fc1 avec zip")
for a,b in zip(x, y):
    print(a, '/*/', b)


print("fc1 avec enumerate")
for idx,v in enumerate(x):
    print(v, '/*/', y[idx])

print("fc2 avec liste")
x = []
y = []
for v in range(0, 10):
    x.append(v)
    y.append(fct_2(v))
print('Les valeurs de x :', x)
print('les valeurs de fct2(x) : ', y)


print("fc2 avec zip")
for a,b in zip(x, y):
    print(a, '/*/', b)


print("fc2 avec enumerate")
for idx,v in enumerate(x):
    print(v, '/*/', y[idx])
