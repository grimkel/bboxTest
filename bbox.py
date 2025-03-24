"""Тестовое задание - подсчет площади пересечения двух прямоугольников"""
from fastapi import FastAPI

app = FastAPI()


def interception(
        start_first: float, end_first: float,
        start_second: float, end_second: float) -> float:
    """Подсчет длины пересечения по одной оси"""

    return max(min(end_first, end_second) -
               max(start_first, start_second), float(0))


@app.get("/area/")
def area(x: float, y: float, w: float, h: float) -> float:
    """
    Подсчет площади пересечения двух прямоугольников:

        x, y - координаты левого нижнего угла 

        w, h - ширина и высота прямоугольника соответственно

    Параметры фиксированного прямоугольника:

        x, y = 0, 0

        w, h = 1000, 500

    Пример http запроса:
        
        http://localhost:8000/area/?x=1&y=2&w=3&h=4
        
    Где x,y,w,h равны 1,2,3,4 соотвественно
    """

    fixed_x = float(0)
    fixed_y = float(0)

    fixed_h = float(500)
    fixed_w = float(1000)

    interception_x: float = interception(x, x + w, fixed_x, fixed_x + fixed_w)
    interception_y: float = interception(y, y + h, fixed_y, fixed_y + fixed_h)

    return interception_x * interception_y
