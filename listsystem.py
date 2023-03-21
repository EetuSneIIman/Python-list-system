def valikko():
    print("[1] Lisää tuote listaan. ")
    print("[2] Poista viimeksi lisätty tuote listasta. ")
    print("[3] Tulosta lista. ")
    print("[4] Tyhjennä lista. ")
    print("[0] Lopeta ohjelma. ")


valikko()
lista = []
valinta = int(input("Valitse toiminto: "))



while valinta != 0:
    if valinta == 1:
        yksi = input("Lisää tuote. ")
        print(yksi)
        lista.append(yksi)
        pass

    elif valinta == 2:
        poisto = input("Syötä poistettava tuote. ")
        lista.remove(poisto)
        print("Tuote poistettu listasta. ")
        pass

    elif valinta == 3:
        print (lista)
        print("Lista tulostettu. ")
        pass

    elif valinta == 4:
        lista = []
        print("Lista tyhjennetty. ")
        pass

    else:
        print("Epäsopiva valinta. ")

    print()
    valikko()
    valinta = int(input("Valitse toiminto: "))

print("Kiitos ohjelman käytöstä. ")