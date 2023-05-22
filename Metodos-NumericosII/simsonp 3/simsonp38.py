# Se importan las funciones sympify y Symbol de la biblioteca sympy para poder convertir cadenas de texto en expresiones simbólicas.
from sympy import sympify, Symbol
# Se importa el símbolo x predefinido de sympy para poder utilizarlo en las expresiones simbólicas.
from sympy.abc import x

# Esta función implementa el método de Simpson 3/8 para aproximar la integral de una función f en el intervalo [a, b] con n subintervalos.
def simpson38(f, a, b, n):

# Primero se calcula el tamaño de cada subintervalo (h) dividiendo el tamaño total del intervalo (b - a) entre el número de subintervalos (n).
    h = (b - a) / n

# Luego se inicializa la variable s con el valor de la función en los extremos del intervalo (f(a) + f(b)).
    s = f.subs(x, a) + f.subs(x, b)

 # Se muestra el cálculo de h y el valor inicial de s al usuario.
    print(f"\nPaso 1: Calcular h = (b - a) / n")
    print(f"h = ({b} - {a}) / {n} = {h}")
    print(f"\nPaso 2: Inicializar s = f(a) + f(b)")
    print(f"s = f({a}) + f({b}) = {s}")

    # Se itera sobre cada uno de los n subintervalos.
    for i in range(1, n):
        # Se calcula el valor de x en el i-ésimo subintervalo.
        x_val = a + i * h
       
        # Si i es múltiplo de 3, se suma 2 * f(x_val) a s.
        if i % 3 == 0:
            s += 2 * f.subs(x, x_val)
            # Se muestra el cálculo intermedio al usuario.
            print(f"\nPaso 3.{i}: Sumar 2 * f({x_val}) a s")
            print(f"s += 2 * f({x_val}) = {s}")
       
        # Si i no es múltiplo de 3, se suma 3 * f(x_val) a s.
    else:
        s += 3 * f.subs(x, x_val)
        # Se muestra el cálculo intermedio al usuario.
        print(f"\nPaso 3.{i}: Sumar 3 * f({x_val}) a s")
        print(f"s += 3 * f({x_val}) = {s}")

    # Finalmente, se calcula el resultado final como 3 * h / 8 * s y se devuelve ese valor.
    result = 3 * h / 8 * s
    # Se muestra el cálculo final al usuario.
    print(f"\nPaso 4: Calcular el resultado final como 3 * h / 8 * s")
    print(f"\nResultado = 3 * {h} / 8 * {s} = {result}")
    return result

# Se pide al usuario que ingrese la función a integrar como una cadena de texto.
expr = input("Ingresa la función a integrar: ")
# Se utiliza la función sympify para convertir esa cadena en una expresión simbólica que puede ser evaluada para diferentes valores de x.
f = sympify(expr)

# Se pide al usuario que ingrese los valores de a, b y n.
a = float(input("Ingresa el valor de a (Intervalo inferior): "))
b = float(input("Ingresa el valor de b (Intervalo superior): "))
n = int(input("Ingresa el valor de n (Numero de subintervalos): "))

# Se llama a la función simpson38 para calcular la integral de la función f en el intervalo [a, b] con n subintervalos utilizando el método de Simpson 3/8.
result = simpson38(f, a, b, n)
# Se muestra el resultado final al usuario.
print(f"El resultado de la integral es: {result}")