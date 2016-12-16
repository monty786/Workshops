__author__ = 'jc437351'

scores = []
score = int(input("score: "))
while score >= 0:
    scores.append(score)
    score = int(input("score: "))
if scores != []:
    print("your highest score is", max(scores))


