lr = input()
rec_num = int(input())

score = 0

score_type = {
  "1B": 1,
  "2B": 1,
  "RF": 1,
  "3B": -1,
  "SS": -1,
  "LF": -1
}

mul = {
  "L": 1,
  "R": -1
}

for i in range(rec_num):
  type = input()
  score += score_type[type]

score *= mul[lr]

if score > 0:
  print("拉打")
else:
  print("推打")