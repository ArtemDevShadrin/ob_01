from dz_store.class_Store import Store

store1 = Store("Магазин 1", "Адрес 1")
store2 = Store("Магазин 2", "Адрес 2")
store3 = Store("Магазин 3", "Адрес 3")


store1.create_new_store()
store1.create_new_product("Товар 1", 100)
store1.create_new_product("Товар 2", 200)

store2.create_new_store()
store2.create_new_product("Товар 3", 150)
store2.create_new_product("Товар 4", 250)

store3.create_new_store()
store3.create_new_product("Товар 5", 120)
store3.create_new_product("Товар 6", 220)


print(store1.get_price("Товар 1"))
store1.update_price("Товар 1", 150)
print(store1.get_price("Товар 1"))

store1.show_items()

store1.delete_product("Товар 1")
store1.show_items()