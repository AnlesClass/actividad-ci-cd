import pytest

from actividad import calcular_area, clasificar_tamanio_area

## Cálculo de área correcto
def test_calcular_area():
    assert calcular_area(10, 5.3) == 53

## Clasificar área: Pequeña
def test_area_incorrecta_base_cero():
    assert clasificar_tamanio_area(50) == "AREA_PEQUENIA"

## Clasificar área: Mediana
def test_area_incorrecta_base_negativa():
    assert clasificar_tamanio_area(150) == "AREA_MEDIANA"

## Clasificar área: Grande
def test_area_incorrecta_altura_cero():
    assert clasificar_tamanio_area(250) == "AREA_GRANDE"