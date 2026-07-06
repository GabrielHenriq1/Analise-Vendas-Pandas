
# PROJETO: ANÁLISE DE VENDAS

# 1. Importar biblioteca
import pandas as pd

# 2. Carregar dados
df_vendas = pd.read_csv("../data/vendas.csv")

# 3. Explorar dados
print("=== PRIMEIRAS LINHAS ===")
print(df_vendas.head())

print("\n=== INFORMAÇÕES DO DATASET ===")
print(df_vendas.info())

# 4. Análises
print("\n=== CATEGORIAS EXISTENTES ===")
print(df_vendas['categoria'].unique())

print("\n=== PREÇOS ===")
print("Mínimo:", df_vendas['preco_unitario'].min())
print("Máximo:", df_vendas['preco_unitario'].max())
print("Média:", df_vendas['preco_unitario'].mean())

# 5. Filtros
df_online = df_vendas[df_vendas['loja'] == 'ONLINE']
print(f"\nVendas ONLINE: {len(df_online)}")

df_eletronicos = df_vendas[df_vendas['categoria'] == 'Eletrônicos']
print(f"Vendas Eletrônicos: {len(df_eletronicos)}")

df_mais_5 = df_vendas[df_vendas['quantidade'] > 5]
print(f"Vendas com quantidade > 5: {len(df_mais_5)}")

df_sp_roupas = df_vendas[(df_vendas['loja'] == 'SP') & (df_vendas['categoria'] == 'Roupas')]
print(f"Vendas SP + Roupas: {len(df_sp_roupas)}")

# 6. Criar colunas
df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']
df_vendas['data'] = pd.to_datetime(df_vendas['data'])
df_vendas['dia_da_semana'] = df_vendas['data'].dt.day_name()
df_vendas['mes'] = df_vendas['data'].dt.month_name()

# 7. Classificação
def classificar(valor):
    if valor > 1000:
        return "Alta"
    elif valor >= 200:
        return "Média"
    else:
        return "Baixa"

df_vendas['categoria_faturamento'] = df_vendas['valor_total'].apply(classificar)

df_vendas['preco_com_desconto'] = df_vendas['preco_unitario'] * 0.90

# 8. Agrupamentos
print("\n=== FATURAMENTO POR LOJA ===")
print(df_vendas.groupby('loja')['valor_total'].sum().sort_values(ascending=False))

print("\n=== QUANTIDADE POR CATEGORIA ===")
print(df_vendas.groupby('categoria')['quantidade'].sum().sort_values(ascending=False))

print("\n=== PRODUTO MAIS VENDIDO ===")
print(df_vendas.groupby('produto')['quantidade'].sum().sort_values(ascending=False).head(1))

print("\n=== FATURAMENTO POR MÊS ===")
print(df_vendas.groupby('mes')['valor_total'].sum().sort_values(ascending=False))

print("\n=== CLIENTE QUE MAIS COMPROU ===")
print(df_vendas.groupby('cliente')['quantidade'].count().sort_values(ascending=False).head(1))

# 9. Média móvel
faturamento_diario = df_vendas.groupby('data')['valor_total'].sum().sort_index()
media_movel = faturamento_diario.rolling(7).mean()
print("\n=== MÉDIA MÓVEL (primeiros 10 dias) ===")
print(media_movel.head(10))