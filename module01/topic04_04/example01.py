# Условный оператор с несколькими ветвями

price = int(input("Цена товара: "))
total = price
if price >= 100 and price <= 500:
    total = price * 0.7
if price > 500 and price <= 1000:
    total = price * 0.8
if price > 1000:
    total = price * 0.9
print("К оплате: %.2f" %total)