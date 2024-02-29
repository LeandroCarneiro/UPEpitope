import tensorflow as tf

# Define a dictionary to map one-letter codes to full amino acid names
amino_acid_codes = {
    'A': 'Alanine',
    'R': 'Arginine',
    'N': 'Asparagine',
    'D': 'Aspartic acid',
    'C': 'Cysteine',
    'E': 'Glutamic acid',
    'Q': 'Glutamine',
    'G': 'Glycine',
    'H': 'Histidine',
    'I': 'Isoleucine',
    'L': 'Leucine',
    'K': 'Lysine',
    'M': 'Methionine',
    'F': 'Phenylalanine',
    'P': 'Proline',
    'S': 'Serine',
    'T': 'Threonine',
    'W': 'Tryptophan',
    'Y': 'Tyrosine',
    'V': 'Valine',
    'X': 'Termination'
}

# Function to encode an amino acid letter to a tensor


def encode_amino_acid_to_tensor(letter):
    index = list(amino_acid_codes.keys()).index(letter)

    # Create a one-hot encoded tensor for the given letter
    encoded_tensor = tf.one_hot(indices=index, depth=len(amino_acid_codes))
    return encoded_tensor


# # Example usage
# encoded_tensor = encode_amino_acid_to_tensor('A')
# print(encoded_tensor)
# encoded_tensor = encode_amino_acid_to_tensor('K')
# print(encoded_tensor)
# encoded_tensor = encode_amino_acid_to_tensor('W')
# print(encoded_tensor)
# encoded_tensor = encode_amino_acid_to_tensor('Y')
# print(encoded_tensor)
