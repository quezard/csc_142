from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def calculate_cost(self):
        pass
class ByWeightItem(Item):
    def __init__(self, name, weight, cost_per_pound):
        super().__init__(name)
        self._weight = weight
        self._cost_per_pound = cost_per_pound

    def calculate_cost(self):
        return self._weight * self._cost_per_pound


class ByQuantityItem(Item):
    def __init__(self, name, quantity, cost_each):
        super().__init__(name)
        self._quantity = quantity
        self._cost_each = cost_each

    def calculate_cost(self):
        return self._quantity * self._cost_each
class Grapes(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Grapes", weight, 2.50)  # price per pound


class Bananas(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Bananas", weight, 1.20)


class Oranges(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Oranges", quantity, 0.75)  # price each


class Cantaloupes(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Cantaloupes", quantity, 3.00)
class Order:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def calculate_total(self):
        return sum(item.calculate_cost() for item in self._items)

    def get_items(self):
        return self._items

    def __len__(self):
        return len(self._items)
def main():
    order = Order()

    # Add items
    order.add_item(Grapes(2.0))       # 2 lbs
    order.add_item(Bananas(3.5))      # 3.5 lbs
    order.add_item(Oranges(4))        # 4 oranges
    order.add_item(Cantaloupes(2))    # 2 cantaloupes

    print("===== RECEIPT =====")

    for item in order.get_items():
        print(f"{item.name}: ${item.calculate_cost():.2f}")

    print("-------------------")
    print(f"Total items: {len(order)}")
    print(f"Total cost: ${order.calculate_total():.2f}")


if __name__ == "__main__":
    main()