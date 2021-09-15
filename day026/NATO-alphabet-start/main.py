# 1. Create a dictionary in this format:
import pandas
CSV_INPUT = 'nato_phonetic_alphabet.csv'
alpha_df = pandas.read_csv(CSV_INPUT)
alpha_dict = {row.letter:row.code for (key, row) in alpha_df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ').strip().upper()
result_list = [alpha_dict[letter] for letter in word]
print(result_list)
