def atm_simulator():
    saldo = 1000.0
    print("\nTervetuloa Pankkiautomaattiin!")

    while True:

        print("\nValitse toiminto:")
        print("1. Saldo")
        print("2. Talletus")
        print("3. Otto")
        print("4. Lopetus")
        
        valinta = input("Valitse (1-4): ")
        
        if valinta == '1':
            # tarkistetaan saldo
            print(f"Saldosi on: {saldo:.2f} €")
        
        elif valinta == '2':
            # talletus
            try:
                summa = float(input("Syötä tallettamasi summa: "))
                if summa > 0:
                    if summa >10000:
                        print("Voit tallettaa enintään 10 000 euroa yhdellä kerralla.")
                    else:
                        saldo += summa
                        print(f"{summa:.2f} € Talletus onnistui!")
                else:
                    print("Syötä positiivinen numero")
            except ValueError:
                    print("Virhe. Syötä numeerinen arvo.")

        elif valinta == '3':
            # varojen nosto
            try:
                summa = float(input("Kuinka paljon haluat nostaa? "))
                if summa > 0:
                    if summa % 5 != 0: #modulo -katsoo, että summa on jaollinen viidellä
                        print("Yritä uudelleen. Voit nostaa vain seteleitä!")
                    elif saldo >= summa:
                        saldo -= summa
                        print(f"{summa:.2f} euron nosto onnistui.")
                    else:
                        print(f"Nosto epäonnistui. Varoja liian vähän. (Nostoyritys {summa:.2f}. Nykyinen saldo: {saldo:.2f})")
                else:
                    print("Syötä positiivinen numero.")
            except ValueError:
                print("Virhe. Syötä numeerinen arvo.")

        elif valinta == '4':
            # Exit
            print("Kiitos, että käytit pankkiautomaattia. Näkemiin!")
            break
        
        else:
            print("Virheellinen valinta. Yritä uudelleen!")

if __name__ == "__main__":
    atm_simulator()