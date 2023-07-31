# Solución de la clase de platzi


# Mi solución

def verifyingAlienDictionary(words: list, order: str):
    _order = order.split()
    # Primero validar la longitud de las palabras
    for i in range(len(words) - 1):
        if len(words[i]) > len(words[i + 1]):
            return False
        # if 


    print(_order)
    print(words)


if __name__ == "__main__":
    print(verifyingAlienDictionary(["conocer", "cono"],
                                   "hlabcdefgijkmnopqrstuvwxyz"))
