#Codigo triangulo escaleno#


def caracterizar_triangulo(lado_a, lado_b, lado_c):

    if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):

        if lado_a == lado_b == lado_c:
            tipo = "Equilátero"
        elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
        

        return f"Tipo de triángulo: {tipo}"
    else:
        return "No se puede formar un triángulo con esos lados."


try:
    a = float(input("Ingrese el lado A: "))
    b = float(input("Ingrese el lado B: "))
    c = float(input("Ingrese el lado C: "))

    resultado = caracterizar_triangulo(a, b, c)
    print(resultado)

except ValueError:
    print("Por favor ingrese valores numéricos válidos.")