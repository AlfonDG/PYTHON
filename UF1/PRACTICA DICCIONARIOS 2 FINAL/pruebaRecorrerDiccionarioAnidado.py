import random

fuerza = 0

censoImperio={
"AR1":{"nombre":"Claudia","region":"Roma","edad":23,"sexo":"I","categoría":"centurión","fuerza":random.uniform(50,200)},
"AD3":{"nombre":"Maximo","region":"Hispania","edad":30,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"AC2":{"nombre":"Marco","region":"Hispania","edad":28,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"AV6":{"nombre":"Julius","region":"Roma","edad":35,"sexo":"H","categoría":"césar","fuerza":random.uniform(50,200)},
"SS5":{"nombre":"Augustus","region":"Hispania","edad":21,"sexo":"H","categoría":"soldado","fuerza":random.uniform(50,200)},
"WQ6":{"nombre":"Eugenia","region":"Hispania","edad":28,"sexo":"D","categoría":"centurión","fuerza":random.uniform(50,200)},
"JU8":{"nombre":"Anastacia","region":"Hispania","edad":17,"sexo":"I","categoría":"soldado","fuerza":random.uniform(50,200)},
"DF5":{"nombre":"Aurelia","region":"Hispania","edad":20,"sexo":"D","categoría":"pueblo","fuerza":random.uniform(50,200)},
"BR1":{"nombre":"Antistia","region":"Roma","edad":16,"sexo":"D","categoría":"centurión","fuerza":random.uniform(50,200)},
"KR9":{"nombre":"Apolonia","region":"Roma","edad":25,"sexo":"I","categoría":"centurión","fuerza":random.uniform(50,200)},
"KH7":{"nombre":"Acucia","region":"Roma","edad":29,"sexo":"D","categoría":"centurión","fuerza":random.uniform(50,200)},
"XH4":{"nombre":"Titus","region":"Roma","edad":39,"sexo":"I","categoría":"pueblo","fuerza":random.uniform(50,200)},
"KA2":{"nombre":"Aurelio","region":"Roma","edad":15,"sexo":"H","categoría":"pueblo","fuerza":random.uniform(50,200)},
"MJ8":{"nombre":"Tiberius","region":"Roma","edad":22,"sexo":"H","categoría":"pueblo","fuerza":random.uniform(50,200)},
}

#prueba01 = censoImperio["AR1"]["nombre"]

#print(prueba01)

for idPersona,datosPersona in censoImperio.items():
    print(censoImperio[idPersona]["nombre"])