agenda = {"48064936L":["Alfonso","622279990"],"54321890S":["Alonso","78945214"],"48976547F":["Montse","609490193"]}

nombreBuscar = str(input("Escriba el nombre que deseé: ")).title()

for dni, persona in agenda.items():
    if persona[0] == nombreBuscar:
        print(f"Hemos encontrado a la persona {nombreBuscar}, desea eliminarla? ")

        eliminar = str(input("Escriba si desea eliminar el nombre SI/NO")).lower()

        if eliminar == "si":
            print("Procedemos a eliminar el contacto de la AGENDA DE CONTACTOS\n")
            #del agenda[dni] = [None,persona[1]] -> Esta opción comentada nos permite eliminar a la persona pero dejar su teléfonfo de contacto
            del agenda[dni]
            print("Nombre de persona Eliminada")
            break
        elif eliminar == "no":
            print("No deseas eliminar a la persona... Por lo tanto te devolvemos al menú principal")
            menuSeguir = True

        else:
            print("No has introducido un nombre de forma adecuada")