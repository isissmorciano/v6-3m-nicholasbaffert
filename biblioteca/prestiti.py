from .libri import info_libro, libro_disponibile

def crea_utente(nome: str, cognome: str) -> dict:
    return {"nome": nome, "cognome":cognome}

def crea_biblioteca() -> dict:
    return {"libri": []}

def aggiungi_libro(biblioteca: dict, libro: dict) -> None:
    biblioteca['libri'].append(libro)

def presta_libro(biblioteca: dict, libro:dict) -> bool:
    if libro_disponibile(libro) == True:
        biblioteca['libri'] -= 1
        return True
    return False

def restituisci_libro(biblioteca: dict, libro: dict, prestiti: list) -> bool:
    if presta_libro
        biblioteca['libri'] += 1
        return True

def libri_prestati(biblioteca: dict) -> list[dict]:
    prestati = [dict]
    for 
