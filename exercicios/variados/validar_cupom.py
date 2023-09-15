print("Com que roupa eu vou?")

valor_compra = input("Informe o valor da compra: ")
cupom = input("Digite o cupom de desconto: ")

if cupom.upper() == "NIVER10":
   valor_final = float(valor_compra) * 0.9
else:
   valor_final = float(valor_compra);
   print("CUPOM INVÁLIDO");
print(f"O valor da final da compra é {valor_final}")