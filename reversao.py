palavra = input("Qual palavra deseja reverter? ")

def reverter_string (palavra):
    return palavra [::-1] #chama slicing

result = reverter_string (palavra)
print (f"A palavra revertida é: {result}")
