from Bio import pairwise2, Align

# Ваша матрица PAM250
pam250 = [
    [2, -2, 0, 0, -3, 1, -1, -1, -1, -2, -1, 0, 1, 0, -2, 1, 1, 0, -6, -3],
    [-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4, 0, -2, -2, -8, 0],
    [0, -5, 4, 3, -6, 1, 1, -2, 0, -4, -3, 2, -1, 2, -1, 0, 0, -2, -7, -4],
    [0, -5, 3, 4, -5, 0, 1, -2, 0, -3, -2, 1, -1, 2, -1, 0, 0, -2, -7, -4],
    [-3, -4, -6, -5, 9, -5, -2, 1, -5, 2, 0, -3, -5, -5, -4, -3, -3, -1, 0, 7],
    [1, -3, 1, 0, -5, 5, -2, -3, -2, -4, -3, 0, 0, -1, -3, 1, 0, -1, -7, -5],
    [-1, -3, 1, 1, -2, -2, 6, -2, 0, -2, -2, 2, 0, 3, 2, -1, -1, -2, -3, 0],
    [-1, -2, -2, -2, 1, -3, -2, 5, -2, 2, 2, -2, -2, -2, -2, -1, 0, 4, -5, -1],
    [-1, -5, 0, 0, -5, -2, 0, -2, 5, -3, 0, 1, -1, 1, 3, 0, 0, -2, -3, -4],
    [-2, -6, -4, -3, 2, -4, -2, 2, -3, 6, 4, -3, -3, -2, -3, -3, -2, 2, -2, -1],
    [-1, -5, -3, -2, 0, -3, -2, 2, 0, 4, 6, -2, -2, -1, 0, -2, -1, 2, -4, -2],
    [0, -4, 2, 1, -3, 0, 2, -2, 1, -3, -2, 2, 0, 1, 0, 1, 0, -2, -4, -2],
    [1, -3, -1, -1, -5, 0, 0, -2, -1, -3, -2, 0, 6, 0, 0, 1, 0, -1, -6, -5],
    [0, -5, 2, 2, -5, -1, 3, -2, 1, -2, -1, 1, 0, 4, 1, -1, -1, -2, -5, -4],
    [-2, -4, -1, -1, -4, -3, 2, -2, 3, -3, 0, 0, 0, 1, 6, 0, -1, -2, 2, -4],
    [1, 0, 0, 0, -3, 1, -1, -1, 0, -3, -2, 1, 1, -1, 0, 2, 1, -1, -2, -3],
    [1, -2, 0, 0, -3, 0, -1, 0, 0, -2, -1, 0, 0, -1, -1, 1, 3, 0, -5, -3],
    [0, -2, -2, -2, -1, -1, -2, 4, -2, 2, 2, -2, -1, -2, -2, -1, 0, 4, -6, -2],
    [-6, -8, -7, -7, 0, -7, -3, -5, -3, -2, -4, -4, -6, -5, 2, -2, -5, -6, 17, 0],
    [-3, 0, -4, -4, 7, -5, 0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2, 0, 10],
]

# Ваши белковые последовательности
protein_seq1 = "MFWWQEMGY"
protein_seq2 = "MRENQEMGY"

# Преобразуем матрицу PAM250 в словарь
alphabet = "ACDEFGHIKLMNPQRSTVWY"
substitution_matrix_dict = {}
for i, amino_acid1 in enumerate(alphabet):
    for j, amino_acid2 in enumerate(alphabet):
        substitution_matrix_dict[(amino_acid1, amino_acid2)] = pam250[i][j]

import numpy as np

def needleman_wunsch(seq1, seq2, substitution_matrix, gap_penalty):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    # Инициализация матрицы для вычислений
    score_matrix = np.zeros((len_seq2 + 1, len_seq1 + 1))

    # Заполнение первой строке и первого столбца
    for i in range(1, len_seq2 + 1):
        score_matrix[i, 0] = score_matrix[i-1, 0] + gap_penalty
    for j in range(1, len_seq1 + 1):
        score_matrix[0, j] = score_matrix[0, j-1] + gap_penalty

    # Заполнение оставшейся части матрицы
    for i in range(1, len_seq2 + 1):
        for j in range(1, len_seq1 + 1):
            match = score_matrix[i-1, j-1] + substitution_matrix[f'({seq1[j-1]}, {seq2[i-1]})']
            delete = score_matrix[i-1, j] + gap_penalty
            insert = score_matrix[i, j-1] + gap_penalty
            score_matrix[i, j] = max(match, delete, insert)

    # Выравнивание
    align_seq1 = ""
    align_seq2 = ""
    i, j = len_seq2, len_seq1
    while i > 0 or j > 0:
        current_score = score_matrix[i, j]
        diagonal_score = score_matrix[i-1, j-1] if i > 0 and j > 0 else float('-inf')
        up_score = score_matrix[i, j-1] if j > 0 else float('-inf')
        left_score = score_matrix[i-1, j] if i > 0 else float('-inf')

        if current_score == diagonal_score + substitution_matrix[seq1[j-1], seq2[i-1]]:
            align_seq1 = seq1[j-1] + align_seq1
            align_seq2 = seq2[i-1] + align_seq2
            i -= 1
            j -= 1
        elif current_score == up_score + gap_penalty:
            align_seq1 = seq1[j-1] + align_seq1
            align_seq2 = '-' + align_seq2
            j -= 1
        elif current_score == left_score + gap_penalty:
            align_seq1 = '-' + align_seq1
            align_seq2 = seq2[i-1] + align_seq2
            i -= 1

    return align_seq1, align_seq2, score_matrix[len_seq2, len_seq1]

# Ваши данные
seq1 = "MFWWQEMGY"
seq2 = "MRENQEMGY"

needleman_wunsch(seq1, seq2, substitution_matrix_dict, 2)