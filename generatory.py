#przykład 1
def liczby():
    for i in range(11):
        yield i*2

print(type(liczby()))
for p in liczby():
    print(p)
    
