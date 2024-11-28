# 國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間
# 文字為"Hello welcome to Cathay 60th year anniversary"
# 請寫一個程式計算每個字母(大小寫視為同個字母)出現次數

from collections import Counter

def count_letter_frequency(str):
  filtered_text = [char.upper() for char in str if char != " "]
  char_count = Counter(filtered_text)

  numbers = {char: count for char, count in char_count.items() if char.isdigit()}
  letters = {char: count for char, count in char_count.items() if char.isalpha()}

  for num in numbers.keys():
      print(f"{num} {numbers[num]}")

  for letter in sorted(letters.keys()):
      print(f"{letter} {letters[letter]}")

count_letter_frequency("Hello welcome to Cathay 60th year anniversary")