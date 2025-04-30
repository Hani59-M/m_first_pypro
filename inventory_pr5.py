def fulfill_order(inventory, order, budget):
    total_cost = 0
    product = {}

    for name in order:
        for item in inventory:
            if item['name'] == name:
                price = item['price']
                stock = item['quantity']
                need = order[name]

                buy = min(stock, need)
                cost = buy * price

                if total_cost + cost <= budget:
                    product[name] = buy
                    total_cost += cost
                elif total_cost < budget:
                    affordable = (budget - total_cost) // price
                    buy = min(buy, affordable)
                    if buy > 0:
                        product[name] = buy
                        total_cost += buy * price
                break

    all_product = all(product.get(name, 0) >= order[name] for name in order)

    if all_product:
        print("Order is fulfillable within budget.")
    elif product:
        print("Order is partially budget.")
    else:
        print("Order is impossible budget.")

    print("Items fulfilled:", product)
    print("Total cost:", total_cost)

inventory = [
    {'name': 'pen', 'quantity': 10, 'price': 2},
    {'name': 'banana', 'quantity': 5, 'price': 1},
    {'name': 'samosa', 'quantity': 8, 'price': 3}
]

order = {
    'pen': 2,
    'banana': 2,
    'samosa': 1
}

budget = 10

fulfill_order(inventory, order, budget)
