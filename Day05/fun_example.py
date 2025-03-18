coffee_prices = [('expresso',2.2),('cappuccino',1.5),('moka',1.9)]

def most_expensive(prices):
    higher = 0
    expensive_coffee = ''
    for coffee, price in prices:
        if price > higher:
            higher = price
            expensive_coffee = coffee
        else:
            pass
    return (higher, expensive_coffee)

price, coffee = most_expensive(coffee_prices)
print(f"The most expensive coffee is '{coffee}' and it cost: ${price}")