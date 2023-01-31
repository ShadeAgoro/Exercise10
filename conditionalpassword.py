# assigned password digits/integers to the hardcoded value of pin with an assignment operator
pin_value = "1234"
input_pin = ""
pin_attempt = 1
is_pin_lock = False
# use of is_pin_lock variable to check if first pin attempt is correct or not
# if incorrect, it will return the boolean value false
# until third incorrect pin attempt is made and true boolean value is returned

while input_pin != pin_value and not(is_pin_lock):
    if pin_attempt <= 3:
        input_pin = input("Enter Pin: ")

    else :
         is_pin_lock = True
    pin_attempt = pin_attempt + 1

if is_pin_lock:
    print("Account is locked due to exceed in limits")
else :
    print("Pin accepted")
