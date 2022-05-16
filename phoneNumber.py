def create_phone_number(n):
    n = "".join([str(x) for x in n] )
    return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))


def create_phone_number2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number([3,5,0,6,5,0,9,0,4,4]))
print(create_phone_number2([3,5,0,6,5,0,9,0,4,4]))