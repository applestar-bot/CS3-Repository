cart_total= float(input(int))
print("input shipping speed")

def calculate_checkout(cart_total, shipping_speed):
 if shipping_speed == "express":
  shipping = 20
 elif shipping_speed =="overnight":
  shipping = 35
 elif shipping_speed == "standard" and cart_total>=100:
  shipping = 0
 elif shipping_speed == "standard" and cart_total < 100:
  shipping = 10
 else:
  print("err0r")
  shipping = 0

  cart_total == shipping + calculate_checkout
  

 return 


 
