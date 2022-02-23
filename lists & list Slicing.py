li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2.5,'a', True]

# Data Structure

# amazon_cart = ['notebooks', 'sunglasses']
# print(amazon_cart[2])


# List Slicing
# string = 'helllooo'
# amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
# print(amazon_cart[0::2])

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop'
print(amazon_cart[0:3])
print(amazon_cart)  

# another example
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop'
print(amazon_cart[1:3])
print(amazon_cart)  

# another example

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop'
print(amazon_cart)  

# another example

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)  

# another example

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop'
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# another example

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

