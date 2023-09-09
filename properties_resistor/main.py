from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

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

print("____________ klasa VoltageResistance _______________")
r2 = VoltageResistance(1E2)
print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 321
print(f'opór: {r2.ohms}')
print(f'natężenie prądu: {r2.current} A')
print(f'napięcie prądu: {r2.voltage} V')

print("____________ klasa VoltageResistance _______________")
try:
      r3 = BoundedResistance(1E2)
      print(r3.ohms)
      r3.ohms = -34
      print(f'oporność: {r3.ohms} OMÓW')
except ValueError as d:
      print(d)
except Exception as ex:
      print(ex)
