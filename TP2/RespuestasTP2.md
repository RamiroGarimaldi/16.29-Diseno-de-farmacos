# TP2: Evaluación in silico de propiedades ADMET y filtros de selección de candidatos a fármaco

## 1. Selección de compuestos:

### a. Ingresar a PubChem (https://pubchem.ncbi.nlm.nih.gov). Utilizar la barra de búsqueda, para encontrar información de los siguientes compuesto: aspirin, paracetamol y caffeine. Obtener el “Canonical SMILES” del compuesto para los pasos anteriores

**Aspirin (ácido acetilsalicílico)**: CC(=O)OC1=CC=CC=C1C(=O)O \

**Paracetamol**: CC(=O)NC1=CC=C(C=C1)O  \

**Caffeine**: CN1C=NC2=C1C(=O)N(C(=O)N2C)C 

### b. Seleccionar 3 fármacos conocidos y 2 experimentales utilizando las palabras clave: anticancer candidate, natural product, experimental drug.

**Fármaco Conocido 1**: Salicilato de Amilo (Átomo Desinflamante), CCCN(CCC)CCC1=CNC2=CC=CC=C21 \

**Fármaco Conocido 2**: Dimenhidrinato (Dramamine), CN1C2=C(C(=O)N(C1=O)C)NC(=N2)Cl.CN(C)CCOC(C1=CC=CC=C1)C2=CC=CC=C2 \

**Fármaco Conocido 3**: Isotretinoína (Roaccutan), CC1=C(C(CCC1)(C)C)/C=C/C(=C/C=C/C(=C\C(=O)O)/C)/C 

**Producto Natural**: Ácido Glicirrícico, ```text
C[C@]12CC[C@](C[C@H]1C3=CC(=O)[C@@H]4[C@]5(CC[C@@H](C([C@@H]5CC[C@]4([C@@]3(CC2)C)C)(C)C)O[C@@H]6[C@@H]([C@H]([C@@H]([C@H](O6)C(=O)O)O)O)O[C@H]7[C@@H]([C@H]([C@@H]([C@H](O7)C(=O)O)O)O)O)C)(C)C(=O)O```
**Droga experimental**: N,N-Dipropiltriptamina, CCCN(CCC)CCC1=CNC2=CC=CC=C21 \

## 2. Realizar la predicción de propiedades fisicoquímicas de las moléulas obtenidas en el punto 1.a, mediante el uso de la herramienta SwissADME (http://www.swissadme.ch). Utilizando los SMILES obtenidos en el punto anterior, obtener de ambos fármacos:

|    Fármaco     | Peso molecular (g/mol) | LogP | H-bond acceptors | H-bond donors | TPSA (Å²) | Rotatable bonds |
|----------------|------------------------|------|------------------|---------------|-----------|-----------------|
| **Caffeine**   |        194.19          | 0.08 |        3         |      0        |   61.82   |        0        |
| **Aspirina**   |        180.16          | 1.28 |        4         |      1        |   63.60   |        3        |
| **Paracetamol**|        155.19          | 0.93 |        2         |      2        |   49.33   |        2        |



3. Subestructuras indeseables (Lipinski violations)

**Caffeine** = 0
**Aspirin** = 0
**Paracetamol** = 0

4. Predicción de la toxicidad
**Caffeine**
**Aspirin**
**Paracetamol**
