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
            print(filen())
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
    import csv 
    
    lines = []
    try:
        with open('personer.csv') as csv_file:
            for line in csv_file:
                lines.append(line)
            return lines
    except FileNotFoundError as ferr:
        print(ferr) 

"""
    f = open('personer.csv', 'r')
    
    reader = csv.reader(f)

    personer = []

    for row in reader:
        try:
            people.append([row[0], row[1], row[2], row[3]])
        except:
            pass

    print('Här är originalfilen personer.csv')
    for item in personer:
        print(item)
"""
