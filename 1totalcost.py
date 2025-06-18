# Function to calculate total bill
... def calculate_total_bill(items):
...     total_cost = 0.0  # Using float for monetary values
...     for item in items:
...         price, quantity = item['price'], item['quantity']
...         total_cost += price * quantity
...     return total_cost
... 
... # Sample list of items with price and quantity
... items = [
...     {"name": "Apples", "price": 30.5, "quantity": 2},
...     {"name": "Bananas", "price": 15.0, "quantity": 5},
...     {"name": "Milk", "price": 50.0, "quantity": 1}
... ]
... 
... # Calculate and display total bill
... total_bill = calculate_total_bill(items)
