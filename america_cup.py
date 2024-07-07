import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Dados dos jogos da Copa América
data1 = {
    'Team': ['Argentina', 'Canada', 'Peru', 'Chile', 'Ecuador', 'Venezuela',
             'Mexico', 'Jamaica', 'USA', 'Bolivia', 'Uruguay', 'Panama',
             'Colombia', 'Paraguay', 'Brazil', 'Costa Rica']
}

data2 = {
    'Wins':   [2, 1, 0, 0, 1, 2, 1, 0, 1, 0, 4, 2, 3, 1, 1, 1],
    'Draws':  [1, 1, 2, 2, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 1],
    'Losses': [0, 1, 1, 1, 1, 1, 1, 3, 2, 3, 0, 1, 0, 2, 0, 1]
}

# Criando o DataFrame a partir dos dados
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Combinando os dois DataFrames
df = pd.concat([df1, df2], axis=1)

# Codificando as categorias das equipes como números
label_encoder = LabelEncoder()
df['Team_encoded'] = label_encoder.fit_transform(df['Team'])

# Definindo variáveis independentes (X) como as estatísticas de vitórias, empates e derrotas
X = df[['Wins', 'Draws', 'Losses']]

# Criando e treinando o modelo de Regressão Logística multinomial
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X, df['Team_encoded'])

# Calculando estatísticas dinamicamente com base nos dados
stats_finalists = [
    [3, 0, 0],  # Exemplo: 3 vitórias, 0 empates, 0 derrotas (Uruguai)
    [2, 1, 0],  # Exemplo: 2 vitórias, 1 empate, 0 derrotas (Argentina)
    [3, 1, 0]   # Exemplo: 2 vitórias, 1 empate, 0 derrotas (Colômbia)
]

# Realizando a predição com base nas estatísticas fornecidas
predicted_teams_encoded = model.predict(stats_finalists)

# Decodificando os números de volta para os nomes das equipes
predicted_teams = label_encoder.inverse_transform(predicted_teams_encoded)

print("Os 3 times que chegaram na final são:")
for team in predicted_teams:
    print(team)
