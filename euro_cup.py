import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Dados dos jogos da Eurocopa
data1 = {
    'Team': ['Germany', 'Scotland', 'Hungary', 'Switzerland', 'Spain', 'Croatia',
             'Italy', 'Albania', 'Poland', 'Netherlands', 'Slovenia', 'Denmark',
             'Serbia', 'England', 'Romania', 'Ukraine', 'Belgium', 'Slovakia',
             'Austria', 'France', 'Türkiye', 'Georgia', 'Portugal', 'Czechia']
}

data2 = {
    'Wins':   [3, 1, 1, 1, 3, 1, 2, 0, 1, 2, 0, 1, 0, 1, 3, 0, 0, 2, 1, 3, 3, 1, 2, 0],
    'Draws':  [2, 1, 2, 3, 2, 2, 1, 1, 0, 1, 3, 2, 2, 2, 1, 2, 2, 1, 1, 1, 0, 1, 1, 1],
    'Losses': [0, 3, 1, 1, 0, 1, 1, 3, 2, 1, 2, 1, 2, 1, 0, 1, 2, 2, 1, 0, 1, 1, 1, 2]
}

# Criando o DataFrame a partir dos dados
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Combinando os dois DataFrames
df = pd.concat([df1, df2], axis=1)

# Adicionando a coluna de peso
df['Weight'] = 2 * df['Wins'] + df['Draws'] - df['Losses']

# Codificando as categorias das equipes como números
label_encoder = LabelEncoder()
df['Team_encoded'] = label_encoder.fit_transform(df['Team'])

# Definindo variáveis independentes (X) como as estatísticas de vitórias, empates, derrotas e peso
X = df[['Wins', 'Draws', 'Losses', 'Weight']]

# Criando e treinando o modelo de Regressão Logística multinomial
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X, df['Team_encoded'])

# Calculando estatísticas dinamicamente com base nos dados
stats_finalists = [
    [3, 2, 0, 8],  # (Spain)
    [3, 1, 0, 7],  # (France)
    [2, 1, 1, 4]   # (Netherlands)
]

# Realizando a predição com base nas estatísticas fornecidas
predicted_teams_encoded = model.predict(stats_finalists)

# Decodificando os números de volta para os nomes das equipes
predicted_teams = label_encoder.inverse_transform(predicted_teams_encoded)

print("Os 3 times que chegaram na final são:")
for team in predicted_teams:
    print(team)
