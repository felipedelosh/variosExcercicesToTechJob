"""
Problema que reta mi mente según YOE DUQUE.

Mostrar los ultimos primos de un número dado (incluyendolo).
"""
def isPrime(x):
    if x == 2 or x == 3 or x == 5:
        return True
    
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    
    _exactlyDivisorsCounter = 0
    _counter = 1
    while _counter < x:
        if x % _counter == 0:
            _exactlyDivisorsCounter = _exactlyDivisorsCounter + 1

        _counter = _counter + 1

    return _exactlyDivisorsCounter == 1


_evaluate = 2  # ENTER HERE A NUBER TO EVALUATED
_primeCounter = 0
for i in reversed(range(1, _evaluate+1)):
    if isPrime(i):
        print(i)
        _primeCounter = _primeCounter + 1

    if _primeCounter > 2:
        break
