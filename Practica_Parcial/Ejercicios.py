#Ejercicio 1

import pandas as pd
from admet_module import get_scaffolds 

moleculas = {
    "CMP-1": "CC(CCCCC)C(O)CCCC(=O)O",
    "CMP-2": "CC(CC(CC)C)C(O)CCCC(=O)N",
    "CMP-3": "CC(C)CC(CCC)C(O)CCCC(F)(F)F",
    "CMP-4": "CC(CCCCC)C(O)CCCC(=O)O[C@@H]1O[C@H](N)C(=O)C1",
    "CMP-5": "CC(CCN)C(O)CCCC(=O)C#N",
    "CMP-6": "CC(CCCl)C(O)CCCC(=O)Cl"
}

df_scaffolds = get_scaffolds(moleculas)
print(df_scaffolds)

# El único compuesto que presenta un scaffold es el CMP-4, sin embargo, todos comparten C(O)CCCC, por lo que podríamos decir que ese es el andamiaje común.
# Partiendo que el carbón central es CH-OH, cada compuesto tiene dos ramas a partir de él. Los grupos químicos presentes en cada rama son:
# CMP-1: R1: cadena de carbonos lineal      R2: ácido carboxílico C(=O)O
# CMP-2: R1: cadena de carbonos ramificada  R2: grupo amida C(=O)N
# CMP-3: R1: cadena de carbonos ramificada  R2: triflurometilo C(F)(F)F
# CMP-4: R1: cadena de carbonos lineal      R2: éster glicósido
# CMP-5: R1: grupo amino (CCN)              R2: nitrilo C#N
# CMP-6: R1: cloro presente (CCCl)          R2: cloruro de acilo C(=O)Cl


#Ejercicio 2 - Comparación entre compuestos

# a) CMP-1 vs CMP-2: Cambia el grupo carboxilo por un grupo amida, y además la cadena de carbonos está más ramificada. 
#    Este reemplazo de grupo y la ramificación, parecen cruciales para aumentar la actividad.

# b) CMP-2 vs CMP-3: Agrega trifluro terminal a la molécula, y la actividad aumenta aún más. 

# c) CMP-4: Tiene una cadena de carbonos lineal como CMP-1, y además la otra cadena tiene un sacárido que aporta -OH libres que son polares y volumen
#    exta. Esta alta polaridad a diferencia de N o F podría causar esta baja actividad. 

# d) CMP-5 y CMP-6 comparado a CMP-3: Los tres tienen ramas con terminadores no ionizables (F, N, Cl) y una alta actividad, lo que sugiere que 
#    estos terminadores favorecen la unión al sitio diana.  


#Ejercicio 3 - Diseño CMP-7

# - Scaffold comun: R1 - C(O)CCCC - R2
# - Grupo funcional crucial: (F)(F)F (era el de mayor actividad)
# - Rama 1: CC(C) (ramificada pero corta)
#
# CMP-7: CC(C)C(O)CCCC(F)(F)F


#Ejercicio 4 - Propiedades de CMP-7  