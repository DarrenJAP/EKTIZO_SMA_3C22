products = [
    ["Sop Iga", 50000],
    ["Siomay Ikan", 21000],
    ["Beef Cheese Ball", 18000]
]

def makeTransaction():

  print("\n\nWelcome to Code Cafe")

  print("Input product code (0-2):", end=" ")

  productCode = int(input(""))

  if (0 <= productCode <= 2):
    print(f"{products[productCode][0]} Rp {products[productCode][1]}")

  print("Input quantity:", end=" ")

  productQuantity = int(input(""))
  totalPrice = productQuantity * products[productCode][1]

  print(f"Total Price: Rp {totalPrice}")

  print("Input payment:", end=" ")

  userPayment = int(input(""))
  change = userPayment - totalPrice

  # RECEIPT

  if userPayment >= totalPrice:
    print("\nRECEIPT:")
    print(f"Product: {products[productCode][0]}")
    print(f"Total  : Rp {products[productCode][1]} x {productQuantity} = {totalPrice}")
    print(f"Payment: Rp {userPayment}")
    print(f"Change : Rp {change}")
    print("Thank You\n")
  else:
    print("Sorry, not enough payment\n")

  # New or exit

  print("1) New Transaction")
  print("0) Exit")
  print("Input: ", end="")
  userInput = int(input(""))
  if userInput == 1:
    makeTransaction()

makeTransaction()

# Welcome to Code Cafe
# Input product code (0-2): 2
# Beef Cheese Ball Rp 18000
# Input quantity: 5
# Total Price: Rp 90000
# Input payment: 100000

# RECEIPT:
# Product: Beef Cheese Ball
# Total  : Rp 18000 x 5 = 90000
# Payment: Rp 100000
# Change : Rp 10000
# Thank You

# 1) New Transaction
# 0) Exit
# Input: 0