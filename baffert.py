from biblioteca import libri,prestiti


# libri di esempio
l1 = libri.crea_libro("1984", "George Orwell", "Fantascienza", 1)
l2 = libri.crea_libro("Dune", "Frank Herbert", "Fantascienza", 2)
l3 = libri.crea_libro("Il piccolo principe", "Antoine de Saint-Exupéry", "Romanzo", 1)
l4 = libri.crea_libro("Harry Potter", "J.K. Rowling", "Fantasy", 3)

# utenti di esempio
u1 = prestiti.crea_utente("Mario", "Rossi")
u2 = prestiti.crea_utente("Laura", "Bianchi")
u3 = prestiti.crea_utente("Carlo", "Verdi")

# Nel `main()` del tuo file principale (`cognome.py`):
# - Crea almeno 4 libri diversi.
# - Stampa le informazioni di ogni libro.
# Nel `main()`:
# - Filtra i libri di un genere specifico e stampa i titoli.
# - Stampa i titoli dei libri disponibili.
# - Cerca i libri di un autore e stampa i titoli trovati.

for libro in libri.libri_disponibili([l1, l2, l3, l4]):
    print(libri.info_libro(libro))

fantascienza = libri.filtra_per_genere([l1, l2, l3, l4], "Fantascienza")