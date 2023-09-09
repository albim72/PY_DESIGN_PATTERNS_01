#przykład 1

def witaj(imie):
    return f'dziękujemy za złożenie konta: {imie}'

def egzamin(imie,punkty,zaliczono):
    return f'osoba egzaminowana: {imie}, liczba punktów: {punkty}, egzamin zdany: {zaliczono}'

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(egzamin,"Olga",57,"tak"))

liczba = [3,6,78,9,12,11,34,33,101,2,0,-5,-33,-2,19]

parz = list(filter(lambda x:x%2==0,liczba))
print(parz)
cube = list(map(lambda x:x**3,liczba))
print(cube)
