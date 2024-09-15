#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.En una dimensión, puedes tener diferentes ciudades,
# en otra dimensión,días de la semana y en la tercera dimensión, semanas.
#Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.
print("UEA\nPatrick Luna\nDeber semana 12 temperaturas" )
temperaturas = [
    [   #   Ciudad 1 Quito
        [   # Semana 1
            {"dia": "Lunes", "temp": 19},
            {"dia": "Martes", "temp": 19},
            {"dia": "Miércoles", "temp": 20},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 23},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 19}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 20},
            {"dia": "Martes", "temp": 22},
            {"dia": "Miércoles", "temp": 19},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 19}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 23},
            {"dia": "Martes", "temp": 24},
            {"dia": "Miércoles", "temp": 23},
            {"dia": "Jueves", "temp": 23},
            {"dia": "Viernes", "temp": 22},
            {"dia": "Sábado", "temp": 20},
            {"dia": "Domingo", "temp": 14}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 13},
            {"dia": "Martes", "temp": 18},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 22},
            {"dia": "Viernes", "temp": 23},
            {"dia": "Sábado", "temp": 23},
            {"dia": "Domingo", "temp": 21}
        ]
    ],
    [   #   Ciudad 2 Sevilla
        [   # Semana 1
            {"dia": "Lunes", "temp": 35},
            {"dia": "Martes", "temp": 35},
            {"dia": "Miércoles", "temp": 35},
            {"dia": "Jueves", "temp": 36},
            {"dia": "Viernes", "temp": 35},
            {"dia": "Sábado", "temp": 34},
            {"dia": "Domingo", "temp": 36}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 34},
            {"dia": "Martes", "temp": 34},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 32},
            {"dia": "Viernes", "temp": 32},
            {"dia": "Sábado", "temp": 31},
            {"dia": "Domingo", "temp": 35}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 36},
            {"dia": "Martes", "temp": 32},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 28},
            {"dia": "Sábado", "temp": 27},
            {"dia": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 29},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 28},
            {"dia": "Viernes", "temp": 33},
            {"dia": "Sábado", "temp": 35},
            {"dia": "Domingo", "temp": 36}
        ]
    ],
    [   #   Ciudad 3 New York
        [   # Semana 1
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 26},
            {"dia": "Miércoles", "temp": 27},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 26}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 27},
            {"dia": "Martes", "temp": 26},
            {"dia": "Miércoles", "temp": 27},
            {"dia": "Jueves", "temp": 26},
            {"dia": "Viernes", "temp": 26},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 26}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 23},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 22},
            {"dia": "Viernes", "temp": 19},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 22}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 24},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 22},
            {"dia": "Viernes", "temp": 21},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 32}
        ]
    ]
]
# Damos nombres de las 3 ciudades
ciudades = ["Quito", "Sevilla", "New York"]

# Iteramos sobre cada ciudad usando el índice y los datos de temperaturas
for ciudad_es, ciudad in enumerate(temperaturas):
    # Mostramos el nombre de la ciudad,
    #Se añadió un bloque de impresión con + "-" * 30 para separar las ciudades visualmente.
    print(f"\nTemperaturas para {ciudades[ciudad_es]}:\n" + "-" * 40)

    # Dentro de cada ciudad, iteramos sobre las semanas
    for semana_s, semana in enumerate(temperaturas[ciudad_es]):
        # Calculamos la suma de temperaturas en la semana actual
        suma_temp = sum([dia["temp"] for dia in semana])
        # Calculamos el promedio de temperaturas dividiendo la suma entre el número de días
        promedio = suma_temp / len(semana)
        # Mostramos el promedio con dos decimales
        print(f"Semana {semana_s + 1}: Promedio = {promedio:.2f}ª grados")
    # Imprimir línea separadora entre ciudades
    print("-" * 40)


