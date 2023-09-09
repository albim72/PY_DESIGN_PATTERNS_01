#przykład 1
def liczby():
    for i in range(11):
        yield i*2

print(type(liczby()))
for p in liczby():
    print(p)

#przykład 2
def wznowienia(n,k):
    print("wstrzymanie działania....")
    yield 1000
    print("wznowienie działania!")

    print("wstrzymanie działania....")
    yield n+k
    print("wznowienie działania!")

    print("wstrzymanie działania....")
    yield n-k
    print("wznowienie działania!")

    print("wstrzymanie działania....")
    yield n*k
    print("wznowienie działania!")

    print("wstrzymanie działania....")
    yield n**k
    print("wznowienie działania!")

    print("wstrzymanie działania....")
    yield "to jest ostatni  yield"
    print("wznowienie działania!")

for i in wznowienia(8,12):
    print("_______________________________")
    print(type(i))
    print(f'zwrócono wartość: {i}')
