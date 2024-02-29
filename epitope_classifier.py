from helpers.aminoAcids_encoder import encode_amino_acid_to_tensor
from helpers.utils import find_files, read_lines


def epitope_classifier():
    positive_epitopes = []
    negative_epitopes = []

    all_epitopes = find_files('datasets/abcpred16.txt')[0]
    lines = read_lines(all_epitopes)
    for line in lines:
        epitope, flag = line.strip().split()
        flag = False if flag == '0' else True

        if (flag):
            positive_epitopes.append(epitope)
        else:
            negative_epitopes.append(epitope)

    return positive_epitopes, negative_epitopes


# # Example usage
# positive_epitopes, negative_epitopes = epitope_classifier()
# result = len(positive_epitopes)
# print(result)
# result = len(negative_epitopes)
# print(result)
