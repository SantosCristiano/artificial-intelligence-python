import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import imdb
from tensorflow.keras.callbacks import EarlyStopping

# Carregar dados IMDB e limitar o vocabulário
vocab_size = 20000
maxlen = 200
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)

# Pad sequences para terem o mesmo tamanho
X_train = pad_sequences(X_train, maxlen=maxlen)
X_test = pad_sequences(X_test, maxlen=maxlen)

# Construir o modelo de rede neural
model = Sequential([
    Embedding(vocab_size, 128, input_length=maxlen),
    Bidirectional(LSTM(64)),
    Dense(1, activation='sigmoid')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Definir callbacks para parada antecipada
early_stopping = EarlyStopping(monitor='val_loss', patience=2)

# Treinar o modelo
history = model.fit(X_train, y_train,
                    epochs=10,
                    batch_size=128,
                    validation_data=(X_test, y_test),
                    callbacks=[early_stopping])

# Avaliar o modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {accuracy * 100:.2f}%')


# Fazer predições
def predict_sentiment(review, model, vocab_size, maxlen):
    # Processar texto de entrada
    review = tf.keras.preprocessing.text.text_to_word_sequence(review)
    review = [word_index[word] if word_index.get(word) and word_index[word] < vocab_size else 2 for word in review]
    review = pad_sequences([review], maxlen=maxlen)

    # Fazer predição
    prediction = model.predict(review)[0]
    sentiment = 'Positive' if prediction >= 0.5 else 'Negative'
    confidence = prediction if sentiment == 'Positive' else (1 - prediction)

    return sentiment, confidence


# Exemplo de uso
review = "This movie was really great! I enjoyed it a lot."
sentiment, confidence = predict_sentiment(review, model, vocab_size, maxlen)
print(f'Review: {review}')
print(f'Sentiment: {sentiment} (Confidence: {confidence * 100:.2f}%)')
