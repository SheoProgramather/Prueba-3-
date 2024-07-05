import os
import json 
import math 
import random
import globales



def valores_aleatorios():
    ventas = globales.leer_archivo_json('ventas.json')

    productos = [
        "Café Americano",
        "Té Chai",
        "Croissant",
        "Jugo Naranja",
        "Panini de Pavo y Queso",
        "Pastel de Zanahoria",
        "Espresso Doble",
        "Ba;do de Frutas",
        "Muffin",
        "Ensalada",
        "Chocolate Caliente",
        "Tarta de Frambuesa",
        "Sándwich de Huevo",
        "Galletas de Avena",
        "Frappé de Caramelo"
        ]
    
    ventas = []


    for p in range(15):
        nombre = random.choice(productos)
        valor = random.randint(20, 100)*100
        iva = int(valor * 0.19)

        ventas.append({
            "nombre": nombre,
            "valor": valor,
            "iva": iva
        })

    globales.guardar_archivo_json('ventas.json', ventas)

def ver_estadisticas():
    ventas = globales.leer_archivo_json('ventas.json')

    if not ventas:
        print("No se encuentran ventas disponibles")
        return

    v = [valor['valor'] for valor in ventas]
    iva = [iva['iva'] for iva in ventas]
    p = [nombre['nombre'] for nombre in ventas]
    
    
    

    producto_caro = max(v)
    producto_iva = max(iva)
    promedio_producto = sum(v) / len(v)
    media_geometrica = math.exp(sum(math.log(valor) for valor in v) / len(v))


    print(f"El producto con el valor más alto es de: ${producto_caro}")
    print(f"El iva más alto es de: ${producto_iva}")
    print(f"El promedio del valor de los productos es de: ${int(promedio_producto)}")
    print(f"La media geométrica del valor de los prodcutos es de: ${int(media_geometrica)}")


