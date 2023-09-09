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

#przykład 2

def rejestracja(oplata):
    def lista_zawodnikow():
        return "jeteś na liście zawodników..."

    def brak():
        return "brak wpłaty, za 3 dni zostaniesz usunięty z listy"

    def error():
        return "błąd kodu wpłaty.."

    if oplata == 1:
        return lista_zawodnikow()
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1))
print(rejestracja(33)())
print(rejestracja(0)())
