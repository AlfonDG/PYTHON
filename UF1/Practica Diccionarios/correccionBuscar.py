agenda = {"48064936L":["Alfonso","622279990"],"54321890S":["Alonso","78945214"],"48976547F":["Montse","609490193"]}

buscar = str(input("Nombre a buscar: ")).title()

for nombre,telefono in agenda.values():
    if nombre.startswith(buscar):
        print(f"Los nombres que empiezan por los carácteres {buscar:} son -> {nombre:^5} y el número de teléfono es {telefono:^5}")