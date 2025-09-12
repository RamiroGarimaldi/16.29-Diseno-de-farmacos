from admet_module import analisis_completo

mis_moleculas = {
    'Caffeine': 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C',
    'Aspirin': 'CC(=O)OC1=CC=CC=C1C(=O)O',
    'Paracetamol': 'CC(=O)NC1=CC=C(C=C1)O',
    'Salicilato de Amilo (Átomo Desinflamante)': 'CCCCCOC(=O)C1=CC=CC=C1O',
    'Dimenhidrinato (Dramamine)': 'CN1C2=C(C(=O)N(C1=O)C)NC(=N2)Cl.CN(C)CCOC(C1=CC=CC=C1)C2=CC=CC=C2',
    'Isotretinoína (Roaccutan)': 'CC1=C(C(CCC1)(C)C)/C=C/C(=C/C=C/C(=C\C(=O)O)/C)/C',
    'Ácido Glicirrícico': 'C[C@]12CC[C@](C[C@H]1C3=CC(=O)[C@@H]4[C@]5(CC[C@@H](C([C@@H]5CC[C@]4([C@@]3(CC2)C)C)(C)C)O[C@@H]6[C@@H]([C@H]([C@@H]([C@H](O6)C(=O)O)O)O)O[C@H]7[C@@H]([C@H]([C@@H]([C@H](O7)C(=O)O)O)O)O)C)(C)C(=O)O',
    'N,N-Dipropiltriptamina': 'CCCN(CCC)CCC1=CNC2=CC=CC=C21'
}

resultados_todos = {}

for nombre, smiles in mis_moleculas.items():
    resultados_todos[nombre] = analisis_completo({nombre: smiles})

for nombre, res in resultados_todos.items():
    for ficha in res['fichas']:
        print(ficha)
        
        #Cálculo criterio Veber
        props = res['propiedades'].iloc[0]
        tpsa = props['TPSA'].item() if hasattr(props['TPSA'], 'item') else props['TPSA']
        enlaces_rot = props['RotatableBonds'].item() if hasattr(props['RotatableBonds'], 'item') else props['RotatableBonds']
        if tpsa <= 140 and enlaces_rot <= 10:
            veber = "Cumple"
        else:
            veber = "No cumple"
        print(f"\nCRITERIO DE VEBER: {veber}\n")