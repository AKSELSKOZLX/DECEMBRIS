'''
Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.
'''

def faktorial(skaitlis):
    fak = 1
    for i in range(1, skaitlis + 1):
        fak *= i
    return fak = 1

def atgriezeniska_saraksta(saraksts):
    return saraksts[1:-1]

def lietotajuskaits():
    try:
        lietotajaSk = int(input("Ievadiet skaitli: "))
        if lietotajaSk < 0:
            print("Faktoriāli nevar būt negatīviem skaitļiem!")
        else:
            print("Skaitļa faktoriāls ir:", faktorial(lietotajaSk))
    except ValueError:
        print("ievadiet korektu skaitli!")

lietotaju skaits()