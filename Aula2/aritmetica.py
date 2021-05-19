try:
    x = int(input())
    s1 = input()
    y = int(input())
    s2 = input()
    z = int(input())
    resultado = 0

    if (s1 == "+" and s2 == "-"):
        resultado = x + y - z

    elif (s1 == "+" and s2 == "*"):
        resultado = x + y * z

    elif (s1 == "+" and s2 == "/"):
        resultado = x + y // z

    elif (s1 == "+" and s2 == "+"):
        resultado = x + y + z

    elif (s1 == "-" and s2 == "+"):
        resultado = x - y + z

    elif (s1 == "-" and s2 == "*"):
        resultado = x - y * z

    elif (s1 == "-" and s2 == "/"):
        resultado = x - y // z

    elif (s1 == "-" and s2 == "-"):
        resultado = x - y - z

    elif (s1 == "*" and s2 == "+"):
        resultado = x * y + z

    elif (s1 == "*" and s2 == "-"):
        resultado = x * y - z

    elif (s1 == "*" and s2 == "/"):
        resultado = x * y // z

    elif (s1 == "*" and s2 == "*"):
        resultado = x * y * z

    elif (s1 == "/" and s2 == "+"):
        resultado = x // y + z

    elif (s1 == "/" and s2 == "-"):
        resultado = x // y - z

    elif (s1 == "/" and s2 == "/"):
        resultado = x // y / z

    elif (s1 == "/" and s2 == "*"):
        resultado = x // y * z

    print(resultado, end="")

except ZeroDivisionError:
    print("erro", end="")
