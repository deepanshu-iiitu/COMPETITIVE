def simple():
    print("I am a function")
def rupee_convertor(inr):
    usd = inr / 68
    print(usd)
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age
def gender(inp='Unknown'):
    if inp is "m":
        inp = "Male"
    if inp is "f":
        inp = "Female"
    print(inp)
simple()
rupee_convertor(1000)
age = allowed_dating_age(19)
print(age)
gender('m')
gender('f')
gender()