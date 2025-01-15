from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        for line in content.splitlines():
            print(line)

    def add(self, *products):
        duplicate_messages = []
        file = open(self.__file_name, 'a+')
        file.seek(0)
        existing_products = {line.strip() for line in file if line.strip()}
        for product in products:
            if str(product) not in existing_products:
                file.write(str(product) + '\n')
            else:
                duplicate_messages.append(f"Продукт {product.name} уже есть в магазине")
        file.close()
        self.get_products()
        print("\n".join(duplicate_messages))
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print("Первый запуск:")
s1.add(p1, p2, p3)

print("\nВторой запуск:")
s1.add(p1, p2, p3)