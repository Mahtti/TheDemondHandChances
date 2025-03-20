# Datos de los ataques existentes con su base damage
ataques = {
    "Solo": {"base_damage": 10},
    "Dyad": {"base_damage": 20},
    "Dyad Set": {"base_damage": 40},
    "Triad": {"base_damage": 80},
    "March": {"base_damage": 100},
    "Horde": {"base_damage": 125},
    "Grand Warhost": {"base_damage": 175},
    "Tetrad": {"base_damage": 400},
    "Marching Horde": {"base_damage": 600},
    "The Demon's Hand": {"base_damage": 2000},
}

# Pedir al usuario los valores de "Times Played"
for nombre in ataques:
    while True:
        try:
            times_played = int(input(f"Ingrese el valor de 'Times Played' para {nombre}: "))
            if times_played < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            ataques[nombre]["times_played"] = times_played
            break
        except ValueError:
            print("Error: Ingrese un número válido.")

# Función para analizar los ataques
def analizar_ataques(ataques):
    print("\nAnálisis de eficiencia:")

    mejor_ataque = None
    max_eficiencia = 0

    for nombre, datos in ataques.items():
        total_damage = datos["base_damage"] * datos["times_played"]
        eficiencia = datos["base_damage"] / max(1, datos["times_played"])  # Evita división por cero
        
        print(f"{nombre}: Total Damage = {total_damage}, Promedio Daño por Uso = {eficiencia:.2f}")
        
        if eficiencia > max_eficiencia and datos["times_played"] > 0:
            max_eficiencia = eficiencia
            mejor_ataque = nombre

    print(f"\nEl ataque más eficiente es: {mejor_ataque} con {max_eficiencia:.2f} daño por uso.")

# Ejecutar análisis
analizar_ataques(ataques)
input("\nPresiona ENTER para salir...")
