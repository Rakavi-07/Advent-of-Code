import shapely
from shapely import LineString, Point, Polygon

class day_09:

    def __init__(self):
        self.coords = []
        self.max_area = 0

    def open_and_store(self):

        self.path = 'C:\\2025_12_09.txt.txt'

        with open(self.path, 'r') as file:
            for row in file:
                row = list(str(row.replace('\n', '')).split(','))
                row = [ int(i) for i in row ]
                self.coords.append(row)

    def calc_area(self,a,b):
        c = abs(b[0]-a[0])+1
        d = abs(b[1]-a[1])+1
        return c*d

    def find_biggest_area(self):

        coords = []

        for k in self.coords:
            coords.append((float(k[0]), float(k[1])))

        area_full = Polygon(coords)

        for i in range(len(self.coords)):
            coords_i = self.coords[i]
            for j in range(1,len(self.coords)):

                coords_j = self.coords[j]
                area_partly = Polygon([(coords_i[0],coords_j[1]), (coords_j[0], coords_j[1]), (coords_j[0],coords_i[1]), (coords_i[0],coords_i[1]) ])

                if shapely.within(area_partly,area_full):
                    temp = self.calc_area(coords_i, coords_j)
                    if self.max_area < temp:
                        self.max_area = temp

def main() -> None:

    day = day_09()
    day.open_and_store()
    day.find_biggest_area()

    print(day.max_area)

if __name__ == '__main__':
    main()