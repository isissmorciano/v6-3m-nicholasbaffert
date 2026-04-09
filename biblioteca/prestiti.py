from .libri import info_libro, libro_disponibile

def crea_utente(nome: str, cognome: str) -> dict:
    return {"nome": nome, "cognome":cognome}

def crea_biblioteca() -> dict:
    return {}

def aggiungi_libro(biblioteca: dict, libro: dict) -> None:
    

