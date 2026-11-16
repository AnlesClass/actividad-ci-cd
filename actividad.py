## Calcular área con valores SOLO positivos.
def calcular_area(base, altura):    
    if base <= 0:
        raise ValueError("El valor de la base no puede ser cero o negativo.")

    if altura <= 0:
        raise ValueError("El valor de la altura no puede ser cero o negativo.")

    return base * altura

## Clasifica un área basado en su tamaño 
def clasificar_tamanio_area(area):
    if area < 100:
        return "AREA_PEQUENIA"
    elif area > 100 and area < 200:
        return "AREA_MEDIANA"
    elif area > 200:
        return "AREA_GRANDE"

## Función principal (separa el return)
def main():
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    
    try:
        area = calcular_area(base, altura)
    except ValueError as e:
        print(e)
        return

    area_clasificacion = clasificar_tamanio_area(area)
    
    print(f"Área Calculada: {area:.2f}")
    print(f"Clasificación de área: {area_clasificacion}")

## Verdadera ejecución principal
if __name__ == "__main__":
    main()