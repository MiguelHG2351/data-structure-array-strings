# Solución de la clase de platzi


# Mi solución

def verifyingAlienDictionary(words: list, order: str):
    _order = [letra for letra in order]
    for i in range(len(words) - 1):
        if len(words[i]) > len(words[i + 1]):
            return False
        j = 0
        while j < len(words[i]) and j < len(words[i + 1]):
            if _order.index(words[i][j]) > _order.index(words[i + 1][j]):
                return False
            j += 1
    return True



if __name__ == "__main__":
    print(verifyingAlienDictionary(["cono", "conocer"],
                                   "hlabcdefgijkmnopqrstuvwxyz"))
