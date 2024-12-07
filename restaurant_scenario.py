class MenuItem:
    """
    Clase base que representa un artículo del menú en el restaurante.
    Tiene atributos para el nombre, precio y descuento.
    """
    def __init__(self, name: str, price: float, discount: float = 0.0):

        # Validación de tipos de datos de cada uno de los argumentos.
        if not isinstance(name, str): 
            raise TypeError("The name must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("The price must be a positive number.")    
        if not (0 <= discount <= 1):
            raise ValueError("Discount must be between 0 and 1.")
        
        # Asignación de valores a los atributos.
        self.name = name
        self.price = price
        self.discount = discount

    # Método que calcula el precio del producto con descuento
    def calculate(self) -> float:
        return self.price * (1 - self.discount)

    # Método que devuelve una representación en cadena del objeto.
    def __str__(self):
        discount_price = self.calculate() 

        # Si el descuento es mayor a cero, devuelve la representación 
        # en cadena con el descuento.
        if self.discount > 0:
            return (f"{self.name}: ${self.price:.2f} "
            f"(Discounted: ${discount_price:.2f})")
        return f"{self.name}: ${self.price:.2f}"



"""
Este módulo contiene clases que heredan de MenuItem y representan 
diferentes categorías de productos en el sistema.
"""
class Beverage(MenuItem):
    pass

class Appetizers(MenuItem):
    pass

class SideDishes(MenuItem):
    pass

class MainCourses(MenuItem):
    pass

class Desserts(MenuItem):
    pass


# Clase que representa una orden en el restaurante.
class Order:
    def __init__(self):
        self.items = []

    # Método que agrega un artículo al pedido.
    def add_item(self, item: MenuItem):
        self.items.append(item)

    # Método que calcula el monto total después de los 
    # descuentos individuales.
    def bill_amount(self) -> float:
        """Calculates the total amount after individual discounts."""
        return sum(item.calculate() for item in self.items)

    # Método que aplica un descuento global al monto total.
    def discount(self, global_discount: float) -> float:

        # Aplica un descuento global al monto total.
        if not (0 <= global_discount <= 1):
            raise ValueError("Discount must be between 0 and 1.")
        total = self.bill_amount()
        return total * (1 - global_discount)


# Lista de productos 
menu = [
    Beverage("Coca Cola", 2.5),
    Beverage("Sprite", 1.5),
    Beverage("Water", 1.0),
    Appetizers("Fries", 3.0),
    Appetizers("Egg Rolls", 3.0),
    Appetizers("Crab Chips", 3.0),
    SideDishes("Tacos", 4.0),
    SideDishes("Soup", 3.0),
    SideDishes("Salad", 2.0),
    SideDishes("Charred Sweetcorn Salsa", 6.0),
    MainCourses("Burger", 5.0),
    MainCourses("Chicken Fried Steak", 6.0),
    MainCourses("Pizza", 8.0),
    Desserts("Cake", 3.5),
    Desserts("Ice Cream", 4.0)
]

# Creación de una orden
beverage = Beverage("Coca Cola", 2.5, 0.2)   
appetizer = Appetizers("Fries", 3.0, 0.05)
side_dish = SideDishes("Tacos", 4.0, 0.05)
main_course = MainCourses("Burger", 5.0, 0.1)
dessert = Desserts("Cake", 3.5)

# Mensaje de bienvenida
print("Welcome to our restaurant!")
"""print("Here is our menu:")
items = [beverage, appetizer, side_dish, main_course, dessert]

for item in items:
    print(item)"""

order = Order()
order.add_item(beverage)
order.add_item(appetizer)
order.add_item(side_dish)
order.add_item(main_course)
order.add_item(dessert)

print("This is your order:")
for item in order.items:
    print(item)

print("Bill Amount:", order.bill_amount())
print("Your discount is:", order.discount(0.1))

