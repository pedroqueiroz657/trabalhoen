import mysql.connector

v = input('identifique o vendendor')

pu = list()

cp = list()

qv = int(input('insira a quantidade vendida'))

for c in range(0 ,qv):

    cp.append(int(input('insira o codigo da peça: ')))
soma1 = 0
for c in range(0, qv):

    pu.append(float(input('insira o preço do produto: ')))
    soma1 = soma1 + pu[c]
    pu[c] = pu[c]  * 0.05

soma = 0
for c in range(0, qv):

    soma = soma + pu[c]

print(f'a comição de {v} é {soma} reais')

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='pedro657ryan',
    database='dados',
)
cursor = conexao.cursor()

# CRUD
nome_vendedor = v
valor_vendas = soma1
valor_comissão = soma
comando = f'INSERT INTO vendas (nome_vendedor, valor_vendas,valor_comissão) VALUES ("{nome_vendedor}", {valor_vendas},{valor_comissão})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

cursor.close()
conexao.close()
