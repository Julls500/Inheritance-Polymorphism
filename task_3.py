class PointsForPlace:
    def __init__(self):
        pass

    @staticmethod
    def get_points_for_place(place):
        points = 0
        if type(place) != int:
            print('Неверный формат параметра "место". Введите целое число!')
        elif place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - place
        return points

class PointsForMeters:
    def __init__(self):
        pass

    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if type(meters) != int:
            print('Неверный формат параметра "метры". Введите целое число!')
        elif meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = int(meters * 0.5)
        return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        PointsForPlace.__init__(self)
        PointsForMeters.__init__(self)

    @staticmethod
    def get_total_points(meters, place):
        total = PointsForPlace.get_points_for_place(place) + PointsForMeters.get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))




