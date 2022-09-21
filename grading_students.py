def round_off(grade):
    if grade < 38:
        return grade
    else:
        diff = 5 - grade%5
        if diff < 3:
            return grade + diff
        else:
            return grade

n = int(input())

for _ in range(n):
    grade = int(input())
    print(round_off(grade))
