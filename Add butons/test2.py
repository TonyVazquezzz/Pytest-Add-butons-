def operaciones(lista):
    if not lista:
        return None
    suma = sum(lista)
    promedio = suma / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return (suma, promedio, maximo, minimo)

def test_operaciones():
    assert operaciones([1, 2, 3, 4, 5]) == (15, 3.0, 5, 1)
    assert operaciones([0, 0, 0, 0, 0]) == (0, 0.0, 0, 0)
    assert operaciones([10, -5, 8, -3, 6]) == (16, 3.2, 10, -5)
    assert operaciones([]) is None
