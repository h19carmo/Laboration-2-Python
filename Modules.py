def meny():
    val = 0
    print("""

        1. Läs in originalfil

        2. Visa json-data

        3. Lägg till en person

        4. Ta bort en person

        5. Spara fil

        6. Avsluta programmet 

        """)
    while val != 6:
        
        val = input("Välj ett av följande alternativ: ")
        if val =="1":
            filen()
        elif val =="2":
            print('Du har valt att läsa in Originalfilen')
        elif val =="3":
            print('Du har valt att läsa in Originalfilen')
        elif val =="4":
            print('Du har valt att läsa in Originalfilen')
        elif val =="5":
            print('Du har valt att läsa in Originalfilen')
        elif val =="6":
            break

def filen():
    from csv import reader

    with open('personer.csv', 'r') as csvfile:
        csv_reader = reader(csvfile)
        for row in reader:
            print(row)


