# carregar dados
dados = [
    {"nome": "Andres", "cidade": "Campinas"},
    {"nome": "Jonatan", "cidade": "Arauca"}
]

# processar
template = """\
<html>
<body>
    <ul>
        <li>Nome: {dados[nome]}</li>
        <li>Cidade: {dados[cidade]}</li>
    </ul>
</body>
</html>
"""

# randerizar
for item in dados:
    print(template.format(dados=item))