from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress','queue preparation baking ready')
PizzaDough = Enum('PizzaDough','thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato cream_fraiche')
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella bacon ham mushrooms redonion oregano')
STEP_DELAY = 3
