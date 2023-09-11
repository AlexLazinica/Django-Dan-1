"""
Funkcija za zbir cifri
"""

def zbir_cifara(broj):
    zbir = 0
    while broj !=0:
        zbir += broj%10
        broj = broj//10
    return  zbir

print(zbir_cifara(112))
print(zbir_cifara(114))