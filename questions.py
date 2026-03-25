import random
categoria = {
    'programacion' : ["python","programa","variable","funcion","bucle","cadena","entero","lista",],
    'deportes' : ["rugby",'futbol','hockey','voley','basquet','golf','tenis'],
    'comida' : ['milanesa','hamburguesa','panchos','pescado','verdura','zanahoria']
}
print('Categorias Disponibles: ')
for cat in categoria.keys():
    print(cat)
categoria_elegida = input('Elegi una categoria: ').lower()
if categoria_elegida in categoria:
    palabra_ronda = random.sample(categoria[categoria_elegida],len(categoria[categoria_elegida]))
else:
    print("Categoría inválida, se elige 'programacion' por defecto.")
    palabra_ronda = random.sample(categoria['programacion'],len(categoria['programacion']))
puntaje = 0
for word in palabra_ronda:
    guessed = []
    attempts = 6
    print("Nueva Ronda del Ahorcado!")
    print()

    while attempts > 0: # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress) # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            puntaje += 10
            print(f"¡Ganaste! Tu puntaje final es: {puntaje}")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue
        if letter in guessed:
                print("Ya usaste esa letra.")
        elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
        else:
                guessed.append(letter)
                attempts -= 1
                puntaje -= 2
                print("Esa letra no está en la palabra.")
                print()
    else:
        print(f"¡Perdiste esta ronda! La palabra era: {word}")

print(f'Juego Terminado. Tu Puntaje Final: {puntaje}')
    
    
