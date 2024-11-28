# 國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]
# 但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]
# 請用一個函數來將學生的成績修正

def adjust_score(input_score):
  correct_scores = []
  for char in input_score:
    tens = char // 10
    units = char % 10

    correct_score = units * 10 + tens
    correct_scores.append(correct_score)

  print(correct_scores)

adjust_score([35, 46, 57, 91, 29])