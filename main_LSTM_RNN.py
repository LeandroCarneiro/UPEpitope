import os
from helpers.aminoAcids_encoder import encode_amino_acid_to_tensor
from helpers.epitope_encoder import epitope_to_tensor, epitopes_to_tensors
from helpers.utils import find_files, read_lines
from epitope_classifier import epitope_classifier
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from keras.layers import LSTM

import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical


ep_positive, ep_negative = epitope_classifier()
sequencias_positivas = epitopes_to_tensors(ep_positive)
sequencias_negativas = epitopes_to_tensors(ep_negative)

sequence = np.concatenate((sequencias_positivas, sequencias_negativas))

labels = np.concatenate(
    (np.ones(len(ep_positive)), np.zeros(len(ep_negative))))

X_train, X_test, y_train, y_test = train_test_split(
    sequence, labels, test_size=0.2, random_state=42)

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1],  1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1],  1))

# imput layer
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# hidden layer
model = Sequential([
    SimpleRNN(16, return_sequences=True, input_shape=(X_train.shape[1],  1)),
    LSTM(16),
    Dense(2, activation='softmax')
])

model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

model.summary()

model.fit(X_train, y_train, epochs=200, batch_size=16,
          validation_data=(X_test, y_test))

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss}, Accuracy: {accuracy}')


real_epitopes = ['AHCNISRAKWNNTLKQ', 'LNAWGCAFRQVCHTTV',  # positive
                 'SSVAEKLAYAKDILGK', 'QDRLIIVEKFSVEAPK',  # negative
                 'NVTENFDMWKNDMVEQ', 'NHNQNHNHSHNLNPKK',  # positive, negative
                 'YDATIEIKKEEAEYLL', 'LQYEFLIRAIWVSAFV'  # negative
                 ]

seq_real_epitopes = epitopes_to_tensors(real_epitopes)
seq = seq_real_epitopes.reshape(
    (seq_real_epitopes.shape[0], seq_real_epitopes.shape[1],  1))

prediction = model.predict(seq)
for i, prev in enumerate(prediction):
    print(f"Epitope {i+1}: {prev}")

for i, prev in enumerate(prediction):
    class_result = np.argmax(prev)
    if class_result == 0:
        print(f"Epitope {i+1} is negative.")
    else:
        print(f"Epitope {i+1} is positive.")

model.save('rnn_model.keras')
