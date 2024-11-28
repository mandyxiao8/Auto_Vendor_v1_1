# QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。
# 從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
# 請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

def find_last_position(n):
  if 0 <= n <= 100:
    people = list(range(1, n+1))
    index = 0
      
    while len(people) > 1:
      index = (index + 2) % len(people)
      people.pop(index)

    print(f"第{people[0]}順位")
  else:
    print("人數 n 是 0~100")

find_last_position(9)