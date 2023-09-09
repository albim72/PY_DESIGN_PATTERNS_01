from oldresistor import OldResistor
from resistor import Resistor

print("____________ klasa OldResistor _______________")
r0 = OldResistor(10.2E2)
print(r0)
print(r0._ohms)
r0.set_ohms(2.88E3)
print(r0.get_ohms())

print("____________ klasa Resistor _______________")
r1 = Resistor(50E3)
r1.ohms = 11.1E3
print(f'układ elektryczny:\noporność: {r1.ohms} omów,\nnapięcie prądu: {r1.voltage} V,'
      f'\nnatężenie prądu: {r1.current} A')
