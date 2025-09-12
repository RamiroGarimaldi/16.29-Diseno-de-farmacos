# TP2: Evaluación in silico de propiedades ADMET y filtros de selección de candidatos a fármaco

## 1. Selección de compuestos:

### a. Ingresar a PubChem (https://pubchem.ncbi.nlm.nih.gov). Utilizar la barra de búsqueda, para encontrar información de los siguientes compuesto: aspirin, paracetamol y caffeine. Obtener el “Canonical SMILES” del compuesto para los pasos anteriores

**Aspirin (ácido acetilsalicílico)**: CC(=O)OC1=CC=CC=C1C(=O)O 

**Paracetamol**: CC(=O)NC1=CC=C(C=C1)O  

**Caffeine**: CN1C=NC2=C1C(=O)N(C(=O)N2C)C 

### b. Seleccionar 3 fármacos conocidos y 2 experimentales utilizando las palabras clave: anticancer candidate, natural product, experimental drug.

**Fármaco Conocido 1**: Salicilato de Amilo (Átomo Desinflamante), CCCCCOC(=O)C1=CC=CC=C1O  

**Fármaco Conocido 2**: Dimenhidrinato (Dramamine), CN1C2=C(C(=O)N(C1=O)C)NC(=N2)Cl.CN(C)CCOC(C1=CC=CC=C1)C2=CC=CC=C2 

**Fármaco Conocido 3**: Isotretinoína (Roaccutan), CC1=C(C(CCC1)(C)C)/C=C/C(=C/C=C/C(=C\C(=O)O)/C)/C 

**Producto Natural**: Ácido Glicirrícico,```
C[C@]12CC[C@](C[C@H]1C3=CC(=O)[C@@H]4[C@]5(CC[C@@H](C([C@@H]5CC[C@]4([C@@]3(CC2)C)C)(C)C)O[C@@H]6[C@@H]([C@H]([C@@H]([C@H](O6)C(=O)O)O)O)O[C@H]7[C@@H]([C@H]([C@@H]([C@H](O7)C(=O)O)O)O)O)C)(C)C(=O)O```

**Droga experimental**: N,N-Dipropiltriptamina, CCCN(CCC)CCC1=CNC2=CC=CC=C21 

## 2. Realizar la predicción de propiedades fisicoquímicas de las moléulas obtenidas en el punto 1.a, mediante el uso de la herramienta SwissADME (http://www.swissadme.ch). Utilizando los SMILES obtenidos en el punto anterior, obtener de ambos fármacos:

|    Compuesto     | Peso molecular (g/mol) | LogP | H-bond acceptors | H-bond donors | TPSA (Å²) | Rotatable bonds |
|----------------|------------------------|------|------------------|---------------|-----------|-----------------|
| **Caffeine**   |        194.19          | 0.08 |        3         |      0        |   61.82   |        0        |
| **Aspirin**   |        180.16          | 1.28 |        4         |      1        |   63.60   |        3        |
| **Paracetamol**|        155.19          | 0.93 |        2         |      2        |   49.33   |        2        |

En LogP consideramos el valor de _consensus LogP_.


 ## 3. Identificar subestructuras indeseables de los compuestos del punto 1.a y 1.b usando la siguiente módulo de python creado para tal fin siguiendo el tutorial:

Tomamos el parámetro _Lipinski_Violations_ como identificador de subestructuras indeseadbles. A continuación se presenta la cantidad por compuesto:

**Caffeine** = 0

**Aspirin** = 0

**Paracetamol** = 0

**Dimenhidrinato (Dramamine)** = 0

**Salicilato de Amilo (Átomo Desinflamante)** = 0

**Isotretinoína (Roaccutan)** = 1

**Ácido Glicirrícico** = 3

**N,N-Dipropiltriptamina** = 0


## 4. Realizar la predicción de toxicidad in silico utilizando ProTox-II (https://tox-new.charite.de/protox_II/). Utilizando los SMILES de moléculas del punto 1.a y 1.b, obtener a y b. ¿Cuál de las moléculas seleccionadas muestra menor toxicidad según ProTox-II?:

### a. Predicted LD50 (mg/kg) y clase de toxicidad (I–VI).

### b. Riesgo de hepatotoxicidad, mutagenicidad, carcinogenicidad.
| Compuesto      | LD50 Predicho (mg/kg) | Clase de toxicidad (I-VI) | Riesgo de hepatotoxicidad | Riesgo de mutagenicidad | Riesgo de carcinogenicidad |
|--------------|------------------------|---------------------------|---------------------------|--------------------------|-----------------------------|
|Caffeine|127|III|Inactivo (0.97)|Inactivo (0.94)|Inactivo (0.93)|
|Aspirin|250|III|Inactivo (0.51)|Inactivo (0.97)|Inactivo (0.86)|
|Paracetamol|338|IV|Activo (0.74)|Inactivo (0.90)|Inactivo (0.51)|
|Salicilato de Amilo|4100|V|Inactivo (0.66)|Inactivo (0.91)|Inactivo (0.83)|
|Dimenhidrinato|300|III|Inactivo (0.80)|Inactivo (0.59)|Inactivo (0.69)|
|Isotretinoína|1100|IV|Activo (0.76)|Inactivo (0.82)|Inactivo (0.82)|
|Ácido Glicirrícico|1750|IV|Inactivo (0.88)|Inactivo (0.96)|Inactivo (0.96)|
|N,N-Dipropiltriptamina|96|III|Inactivo (0.94)|Inactivo (0.53)|Inactivo (0.69)|

De las moléculas seleccionadas, la que presenta menor toxicidad según ProTox-II es el **Salicilato de Amilo** (átomo desinflamante), ya que presenta un LD50 alto (4100 mg/kg) y por lo tanto una clase de toxicidad de valor alto (V), indicando una que se deben ingerir grandes cantidades del mismo para que sea nocivo a la salud. Además, para los riesgos de hepatoxicidad, mutagenicidad y carcinogenicidad es inactivo.

## 5. Construir una ficha técnica de cada compuesto que considere las respuestas a las siguientes preguntas: ¿Qué compuestos cumplen mejor con los filtros de Lipinski y Veber? ¿Aparecieron moléculas con alertas PAINS? ¿Cuál es su toxicidad?

|Compuesto| Violaciones Lipinski | Cumplimiento Lipinski | Cumplimiento Veber | Alertas PAINS | Toxicidad|
|--------------|------------------------|---------------------------|---------------------------|--------------------------|-----------------------------|
|Caffeine|0|Cumple|Cumple|0|Baja|
|Aspirin|0|Cumple|Cumple|0|Baja|
|Paracetamol|0|Cumple|Cumple|0|Baja|
|Salicilato de Amilo|0|Cumple|Cumple|0|Baja|
|Dimenhidrinato|0|Cumple|Cumple|0|Baja|
|Isotretinoína|1|Cumple|Cumple|0|Baja|
|Ácido Glicirrícico|3|No Cumple|No Cumple|0|Baja|
|N,N-Dipropiltriptamina|0|Cumple|Cumple|0|Baja|

En esta tabla se resume la ficha técnica de cada compuesto, que puede observarse al ejecutar el archivo TP2.py. 

A excepción de Isotretinoína y Ácido Glicirrícico, todos cumplen con los filtros de Lipinski y Veber. En cuanto a la toxicidad, la función predice un LD50 > 5000mg/kg para todos los compuestos, por eso la toxicidad es baja en todos los casos.
