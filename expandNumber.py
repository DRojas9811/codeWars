def expanded_form(num):
    out=""
    for i, b in zip( [num  for num in str(num)], range(len(str(num)),0,-1)):
        if i!="0" : out+=i.ljust(b,"0")+" + "  
    return out[:-3]

def expanded_form2(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

print(expanded_form(5200))
print(expanded_form2(5200))