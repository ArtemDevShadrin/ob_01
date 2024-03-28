class Store:
    stores = []
    items = {}

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def create_new_store(self):
        new_store = {'name': self.name, 'address': self.address, 'items': {}}  # Создание словаря с информацией о магазине
        self.stores.append(new_store)
        print(f"Магазин '{self.name}' по адресу '{self.address}' успешно добавлен.")

    def create_new_product(self, name, price):
        self.items[name] = price
        print(f"Товар '{name}' добавлен в магазин '{self.name}'.")

    def delete_product(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Товар '{name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товар '{name}' не найден в магазине '{self.name}'.")

    def get_price(self, name):
        return self.items.get(name)

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            print(f"Цена товара '{name}' обновлена.")
        else:
            print(f"Товар '{name}' не найден в магазине '{self.name}'.")

    def show_items(self):
        print(f"Товары в магазине '{self.name}':")
        for name, price in self.items.items():
            print(f"Название: {name}, Цена: {price}")