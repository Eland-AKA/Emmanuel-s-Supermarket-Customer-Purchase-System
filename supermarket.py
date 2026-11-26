customer_name = input("Enter customer's full name: ")
product_name = input("Enter product name: ")
unit_price = float(input("Enter product unit price: "))
quantity = int(input("Enter quantity purchased: "))
subtotal = unit_price * quantity 
if quantity >= 5:
    discount = subtotal * 0.10
else:
    discount = 0
final_amount = subtotal - discount
quantity_remainder = quantity % 2
double_quantity_price = unit_price ** 2
items_per_group = quantity // 2
subtotal = unit_price * quantity 
if quantity >= 5:
    discount = subtotal * 0.10
else:
    discount = 0
final_amount = subtotal - discount
quantity_remainder = quantity % 2
double_quantity_price = unit_price ** 2
items_per_group = quantity // 2
if final_amount >= 100000:
    purchase_category = "Premium Purchase"
else:
    purchase_category = "Regular Purchase"
membership_status = input("Does the customer have a special membership card? (yes/no): ")
if (final_amount >= 50000 and quantity >= 3) or membership_status.lower() == "yes":
    free_delivery = True
else:
    free_delivery = False
print("\n SUPERMARKET RECEIPT ")
print(f"Store: ELAND'S Supermarket")
print(f"Customer Name: {customer_name}")
print(f"Product: {product_name}")
print(f"Unit Price: ₦{unit_price:,.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ₦{subtotal:,.2f}")
print(f"Discount: ₦{discount:,.2f}")
print(f"Final Amount: ₦{final_amount:,.2f}")
print(f"Quantity Classification: {'Even' if quantity % 2 == 0 else 'Odd'}")
print(f"Purchase Category: {purchase_category}")
print(f"Membership Status: {membership_status}")
print(f"Free Delivery: {'Eligible' if free_delivery else 'Not Eligible'}")
print("=========================================")
