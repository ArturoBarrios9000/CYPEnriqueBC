#import modulos
#modulos.mi_print("Hola")

from modulos import mi_print , otro_print , sumar , restar

mi_print("Hola de nuevo")
otro_print("Otro print usado")
print(sumar(4,5))
print(restar(10,7))

from modulos import *

mi_print("Hola de nuevo")
otro_print("Otro print usado")
print(sumar(4,5))
print(restar(10,7))
from asciistuff import Banner
import time
import sys
for i in range (10,0,-1):
    print(i,"..." )
    time.sleep(1)
print(Banner("Boommmm!!!!"))
print(sys.platform)
print(Banner("ICO"))
    
