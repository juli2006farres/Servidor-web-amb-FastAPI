import os
import json

# Definim el nom del fitxer que contindrà les dades i les variables inicials.
arxiu_dades = "estudiants.json"
llista_estudiants = []  # Llistat on es guardaran els estudiants.
id_actual = 0  # ID inicial per a assignar als estudiants.

# Carregar les dades inicials si el fitxer ja existeix
if os.path.exists(arxiu_dades):  # Si el fitxer existeix, el llegim i carreguem les dades.
    with open(arxiu_dades, 'r') as arxiu:
        llista_estudiants = json.load(arxiu)  # Carreguem les dades des del fitxer.
        # Obtenim el valor més alt de l'ID per continuar assignant IDs únics.
        id_actual = max((e['id'] for e in llista_estudiants), default=0)

# Funció per mostrar el menú d'opcions
def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Netegem la pantalla depenent del sistema operatiu.
    print("""\nGestió d'estudiants\n-------------------------------
1. Visualitzar estudiants
2. Afegir estudiant
3. Consultar detall estudiant
4. Eliminar estudiant
5. Desar a fitxer
6. Llegir fitxer
0. Sortir\n""")
    return input("> ")  # Retornem l'entrada de l'usuari.

# Bucle principal per gestionar les opcions del menú.
while True:
    opcio = mostrar_menu()  # Mostrem el menú i agafem l'opció de l'usuari.
    
    if opcio == "1":  # Visualitzar estudiants
        os.system('cls')  # Netegem la pantalla.
        print("\nLlista d'estudiants:")
        if not llista_estudiants:  # Si no hi ha estudiants, mostrem un missatge.
            print("Encara no hi ha estudiants registrats.")
        else:
            for estudiant in llista_estudiants:
                print(f"ID: {estudiant['id']} - {estudiant['nom']} {estudiant['cognom']}")  # Mostrem les dades bàsiques.
        input("\nPrem Enter per continuar...")

    elif opcio == "2":  # Afegir estudiant
        os.system('cls')  # Netegem la pantalla.
        id_actual += 1  # Incrementem l'ID per garantir que sigui únic.
        # Sol·licitem les dades per crear un nou estudiant.
        nou_estudiant = {
            'id': id_actual,
            'nom': input("Nom: "),
            'cognom': input("Cognom: "),
            'data_naixement': {
                'dia': int(input("Dia de Naixement: ")),
                'mes': int(input("Mes de Naixement: ")),
                'any': int(input("Any de Naixement: "))
            },
            'email': input("Email: "),
            'treballa': input("Està treballant? (si/no): ").lower() == 'si',  # Convertim la resposta a booleà.
            'curs': input("Curs actual: ")
        }
        llista_estudiants.append(nou_estudiant)  # Afegim l'estudiant a la llista.
        input("\nEstudiant afegit correctament. Prem Enter per continuar...")

    elif opcio == "3":  # Consultar detall d'un estudiant
        os.system('cls')  # Netegem la pantalla.
        id_buscar = input("Introdueix l'ID de l'estudiant: ")  # Demanem l'ID de l'estudiant.
        if id_buscar.isdigit():  # Si l'ID és un número...
            id_buscar = int(id_buscar)
            estudiant_trobat = None
            for est in llista_estudiants:
                if est['id'] == id_buscar:  # Busquem l'estudiant amb l'ID corresponent.
                    estudiant_trobat = est
                    break
            if estudiant_trobat:  # Si trobem l'estudiant, mostrem les dades.
                print("\nDetalls de l'estudiant:")
                for clau, valor in estudiant_trobat.items():
                    if clau == 'data_naixement':  # Si la clau és 'data_naixement', imprimim la data.
                        print(f"{clau.capitalize()}: {valor['dia']}/{valor['mes']}/{valor['any']}")
                    else:
                        print(f"{clau.capitalize()}: {valor}")
            else:
                print("\nEstudiant no trobat.")  # Si no trobem l'estudiant, mostrem un missatge.
        else:
            print("\nL'ID ha de ser un número.")  # Si l'ID no és un número, mostrem un missatge d'error.
        input("\nPrem Enter per continuar...")

    elif opcio == "4":  # Eliminar estudiant
        os.system('cls')  # Netegem la pantalla.
        id_eliminar = input("Introdueix l'ID de l'estudiant a eliminar: ")  # Demanem l'ID de l'estudiant a eliminar.
        if id_eliminar.isdigit():  # Si l'ID és un número...
            id_eliminar = int(id_eliminar)
            estudiant_eliminat = False
            for i in range(len(llista_estudiants)):
                if llista_estudiants[i]['id'] == id_eliminar:  # Busquem l'estudiant per ID.
                    llista_estudiants.pop(i)  # Elimina l'estudiant de la llista.
                    estudiant_eliminat = True
                    print("\nEstudiant eliminat correctament.")
                    break
            if not estudiant_eliminat:  # Si no s'ha trobat l'estudiant, mostrem un missatge d'error.
                print("\nEstudiant no trobat.")
        else:
            print("\nL'ID ha de ser un número.")  # Si l'ID no és un número, mostrem un missatge d'error.
        input("\nPrem Enter per continuar...")

    elif opcio == "5":  # Desar les dades al fitxer
        with open(arxiu_dades, 'w') as arxiu:  # Obrim el fitxer per escriure-hi.
            json.dump(llista_estudiants, arxiu, indent=4)  # Desa les dades de la llista d'estudiants al fitxer.
        input("\nDades desades correctament. Prem Enter per continuar...")

    elif opcio == "6":  # Llegir les dades des del fitxer
        if os.path.exists(arxiu_dades):  # Si el fitxer existeix...
            with open(arxiu_dades, 'r') as arxiu:  # Obrim el fitxer per llegir-hi.
                llista_estudiants = json.load(arxiu)  # Carreguem les dades des del fitxer.
                id_actual = max((e['id'] for e in llista_estudiants), default=0)  # Calcula el màxim ID.
            input("\nDades carregades amb èxit. Prem Enter per continuar...")
        else:
            input("\nNo existeix el fitxer de dades. Prem Enter per continuar...")  # Si no existeix el fitxer, mostrem un missatge.

    elif opcio == "0":  # Sortir del programa
        os.system('cls')  # Netegem la pantalla abans de sortir.
        print("Fins aviat!")  # Imprimim un missatge d'acomiadament.
        break  # Trenquem el bucle i sortim del programa.

    else:  # Si l'usuari introdueix una opció incorrecta.
        input("\nOpció incorrecta. Prem Enter per continuar...")
