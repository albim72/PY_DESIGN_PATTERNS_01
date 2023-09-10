from abstract import AbstractFactory
from concretefactory import ConcreteFactory1, ConcreteFactory2

def client_mode(factory:AbstractFactory)->None:
    product_a = factory.create_product_a()
    prduct_b = factory.create_product_b()

    print(f'{prduct_b.useful_function_b()}')
    print(f"{prduct_b.another_useful_function_b(product_a)}")

print("Klient: testowanie klienta w pierwszym typie fabryki...")
client_mode(ConcreteFactory1())
print("\n")

print("Klient: testowanie klienta w drugim typie fabryki...")
client_mode(ConcreteFactory2())
print("\n")
