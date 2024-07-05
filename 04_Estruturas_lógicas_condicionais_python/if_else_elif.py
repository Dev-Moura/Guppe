"""
Estruturar condicionais
if (Se), else, elif
"""

idade = 16

"""
# Estrutura condicional if, em C

if(idade < 18){
    print("Menor de idade");
}else{
    print("Maior de idade");
}
"""

"""
# Estrutura condicional if, em Java

if(idade < 18){
    System.out.println("Menor de idade");
}else{
    printf("Maior de idade");
}
"""

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")
