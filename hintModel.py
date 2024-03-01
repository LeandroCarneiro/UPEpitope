import autokeras as ak
from helpers.aminoAcids_encoder import encode_amino_acid_to_tensor
from helpers.epitope_encoder import epitope_to_tensor, epitopes_to_tensors
from helpers.utils import find_files, read_lines
from epitope_classifier import epitope_classifier
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

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


clf = ak.ImageClassifier()
clf.fit(x_train, y_train)
results = clf.predict(x_test)
