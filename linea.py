import math

class Point:

    """
    Esta clase representa un punto en un espacio bidimensional.
    """

    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."

    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y

    # Este método cambia los valores de x y y del punto
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    # Este método resetea los valores de x y y del punto a cero
    def reset(self):
        self.x = 0
        self.y = 0
        
    # Este método calcula la distancia entre dos puntos    
    def compute_distance(self, point: "Point")-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance
    
class Rectangle:
    """
    Representa un rectángulo en un espacio bidimensional. 
    El rectángulo puede ser definido de tres maneras:
    1. Dando la esquina inferior izquierda y el ancho y alto.
    2. Dando el centro y el ancho y alto.
    3. Dando dos esquinas opuestas.
    """

    # Atributos de clase
    def __init__(self, *args):
        self.lines = Line()
        if len(args) == 3:  # Método 1: Esquina inferior izquierda + ancho y alto
            bottom_left, width, height = args
            self.bottom_left = bottom_left
            self.width = width
            self.height = height
            self.center = Point(
                bottom_left.x + width / 2,
                bottom_left.y + height / 2,
            )
        elif len(args) == 3:  # Método 2: Centro + ancho y alto
            center, width, height = args
            self.center = center
            self.width = width
            self.height = height
            self.bottom_left = Point(
                center.x - width / 2,
                center.y - height / 2,
            )
        elif len(args) == 2:  # Método 3: Dos esquinas opuestas
            bottom_left, top_right = args
            self.bottom_left = bottom_left
            self.width = top_right.x - bottom_left.x
            self.height = top_right.y - bottom_left.y
            self.center = Point(
                bottom_left.x + self.width / 2,
                bottom_left.y + self.height / 2,
            )
        else:
            raise ValueError("Número de argumentos inválido para inicializar un rectángulo.")

    def compute_area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def compute_perimeter(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.width + self.height)

    def compute_interference_point(self, point: Point):
        """Verifica si un punto está dentro del rectángulo."""
        return (self.bottom_left.x <= point.x <= self.bottom_left.x + self.width) and \
            (self.bottom_left.y <= point.y <= self.bottom_left.y + self.height)
    

    def four_lines(self):
            """Genera las líneas que forman el rectángulo."""
            self.lines = [Line(self.bottom_left, Point(self.bottom_left.x + self.width, self.bottom_left.y)),
                        Line(Point(self.bottom_left.x + self.width, self.bottom_left.y), Point(self.bottom_left.x + self.width, self.bottom_left.y + self.height)),
                        Line(Point(self.bottom_left.x + self.width, self.bottom_left.y + self.height), Point(self.bottom_left.x, self.bottom_left.y + self.height)),
                        Line(Point(self.bottom_left.x, self.bottom_left.y + self.height), self.bottom_left)]

class Line(Point):  
    """
    Representa una línea en un espacio bidimensional. La línea es definida 
    por dos puntos: x, y; que hereda de la clase Point.
    """

    def __init__(self, start, end, n: int = 2):
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise ValueError("Los puntos deben ser instancias de la clase Point") 
            
        self.start = start
        self.end = end
        super().__init__(start.x, start.y)
        self.length = self.compute_length()
        self.slope = self.compute_slope()
        self.discretize_points = self.discretize_line(n)

    # Método que hereda de la clase Point y calcula la distancia 
    # entre los dos puntos
    def compute_length(self) -> float:
        return self.start.compute_distance(self.end)

    # Método que calcula la pendiente de la línea
    def compute_slope(self) -> float:
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y

        if dx == 0:
            return math.inf

        angle_rad = math.atan2(dy, dx)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg, 2)
    

    # Método que verifica si la línea pasa por el eje x.
    def compute_horizontal_cross(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        m = dy / dx
        if  self.start.x == self.end.x: return f"La recta es vertical y no tiene intersección en el eje x"
        b = self.start.y - m * self.start.x
        x = - b / m
        x_rounded = round(x, 2)
        min_x = min(self.start.x, self.end.x)
        max_x = max(self.start.x, self.end.x)
        if min_x <= x <= max_x:
            return f"La recta cruza en el eje x e intersecciona en el punto {x_rounded}"
        else:
            return f"La recta no intersecciona en ningún punto del eje x"

    # Método que verifica si la línea pasa por el eje y.
    def compute_vertical_cross(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        m = dy / dx
        if  self.start.y == self.end.y: return f"La recta es horizontal y no tiene intersección en el eje y"
        b = self.start.x - m * self.start.y
        y = - b / m
        y_rounded = round(y, 2)
        min_y = min(self.start.y, self.end.y)
        max_y = max(self.start.y, self.end.y)
        if min_y <= y <= max_y:
            return f"La recta cruza en el eje y e intersecciona en el punto ({self.start.x}, {y_rounded})"
        else:
            return f"La recta no intersecciona en ningún punto del eje y"
        
    
    # Método que discretiza la línea en n puntos.
    def discretize_line(self, n: int):
        if n < 2:
            raise ValueError("El número de divisiones debe ser al menos 2")
        
        x_values = [self.start.x + i * (self.end.x - self.start.x) / (n - 1) for i in range(n)]
        y_values = [self.start.y + i * (self.end.y - self.start.y) / (n - 1) for i in range(n)]
        
        return [Point(x, y) for x, y in zip(x_values, y_values)]
        


punto_1 = Point(1, 2)
punto_2 = Point(4, -2)

linea = Line(punto_1, punto_2)
linea_2 = Line(punto_1, punto_2, 5)

print("Coordenadas de los puntos:")

print(f"P1: ({punto_1.x}, {punto_1.y})")
print(f"P2: ({punto_2.x}, {punto_2.y})")

length = linea.compute_length()
print(f"La longitud de la línea es: {length}")

slope = linea.compute_slope()
print(f"La pendiente de la línea es: {slope}°")

print("---------------------------------")

interseccion_x = linea.compute_horizontal_cross()
interseccion_y = linea.compute_vertical_cross()
print(interseccion_x)
print(interseccion_y)

print("---------------------------------")

# Acceso a los puntos discretizados:
print("Puntos discretizados automáticamente:")
for point in linea_2.discretize_points:
    print(f"({point.x}, {point.y})")

# Generar una nueva discretización con 10 divisiones
print("\nNueva discretización con 10 puntos:")
new_points = linea_2.discretize_line(10)
for point in new_points:
    print(f"({point.x}, {point.y})")


