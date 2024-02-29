
import tensorflow as tf
from helpers.aminoAcids_encoder import encode_amino_acid_to_tensor
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def epitope_to_tensor(embededEpitope):
    epitopeTensor = []
    for amino in embededEpitope:
        epitopeTensor.append(encode_amino_acid_to_tensor(amino))
    # Concatenate all tensors in the list along the first axis (axis=0)
    # This assumes that all tensors have the same shape except for the first dimension
    # which is the sequence length.
    concatenated_tensor = tf.concat(epitopeTensor, axis=0)

    return concatenated_tensor


def epitopes_to_tensors(epitopes):
    tokenizer = Tokenizer(char_level=True)
    tokenizer.fit_on_texts(epitopes)

    # Converte as sequências para números
    sequences = tokenizer.texts_to_sequences(epitopes)

    # Preenche as sequências para que todas tenham o mesmo comprimento
    sequences = pad_sequences(sequences, padding='post')

    return sequences
