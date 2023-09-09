from pojazd import Pojazd

p1 = Pojazd()
odl = 567
jd = 51
cj = 6.49

print(f'spalanie [l/100km]: {p1.spalanie(odl,jd):.2f}')
print(f'koszt przejazdu na odcinku {odl} km wynosi {p1.kosztyprzejazdu(odl,jd,cj)} zł')
