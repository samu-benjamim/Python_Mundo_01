preco = float(input("Qual é o preço do produto? R$"))
preco_novo = preco - (preco * (5/100))
print("O produto que custava R${:.2f} com desconto custa R${:.2f}".format(preco, preco_novo))