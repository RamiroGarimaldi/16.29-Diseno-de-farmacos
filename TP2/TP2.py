from admet_module import analisis_completo

mis_moleculas = {
    'Caffeine': 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C',
    'Aspirin': 'CC(=O)OC1=CC=CC=C1C(=O)O',
    'Paracetamol': 'CC(=O)NC1=CC=C(C=C1)O'
}

resultados_todos = {}

for nombre, smiles in mis_moleculas.items():
    resultados_todos[nombre] = analisis_completo({'molecula': smiles})

for nombre, res in resultados_todos.items():
    print(f"\n=== {nombre} ===")
    print(res.keys())
    print(res['propiedades'])
