import math

a = float(input("Informe o valor de A: "));
b = float(input("Informe o valor de B: "));
c = float(input("Informe o valor de b: "));

delta = b * b - 4 * a * c

print(delta)
if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2 * a);
    x2 = (-b - math.sqrt(delta)) / (2 * a);
    print(f"Para a equação {a}x² + {b}x + {c} = 0, obtivemos os seguintes valores: x1 = {x1} e x2 = {x2}");
else:
    print(f"Para a equação {a}x² + {b}x + {c} = 0, não existem valores reais para x")