scores = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0
}

sum_score = 0
my_score = 0
for i in range(20):
    sj, score, grade = input().split()
    score = float(score)
    if grade == 'P':
        #sum_score += score
        continue

    sum_score += score
    my_score += scores[grade]*score
print(my_score/sum_score)