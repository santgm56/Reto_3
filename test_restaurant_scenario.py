import unittest

# Importar las clases MenuItem y Order del archivo restaurant_scenario.py
from restaurant_scenario import MenuItem, Order

# Clase para pruebas de la clase MenuItem
class TestMenuItem(unittest.TestCase):

    def test_calculate(self):
        # Crear un objeto de prueba con descuento
        item = MenuItem("Pizza", 10.0, 0.2)
        # Comprobar el precio calculado con descuento
        self.assertAlmostEqual(item.calculate(), 8.0)

    def test_string_representation(self):
        # Comprobar la representación en cadena
        item = MenuItem("Pizza", 10.0, 0.2)
        self.assertEqual(str(item), "Pizza: $10.00 (Discounted: $8.00)")

# Clase para pruebas de la clase Order
class TestOrder(unittest.TestCase):

    def test_bill_amount(self):
        # Crear una orden con varios elementos
        order = Order()
        order.add_item(MenuItem("Pizza", 10.0, 0.1))
        order.add_item(MenuItem("Burger", 5.0, 0.2))
        # Comprobar el monto total después de aplicar sus respectivos descuentos
        self.assertAlmostEqual(order.bill_amount(), 10.0 * 0.9 + 5.0 * 0.8)

    def test_discount(self):
        # Crear una orden con varios elementos
        order = Order()
        order.add_item(MenuItem("Pizza", 10.0, 0.1))
        order.add_item(MenuItem("Burger", 5.0, 0.2))
        # Aplicar un descuento global
        self.assertAlmostEqual(order.discount(0.1), (10.0 * 0.9 + 5.0 * 0.8) * 0.9)


if __name__ == '__main__':
    unittest.main()
