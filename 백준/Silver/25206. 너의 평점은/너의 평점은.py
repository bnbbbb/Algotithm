dic = { 'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' :0.0}
total_credit = 0
weighted_sum = 0
for _ in range(20):
    _, point, subject = input().split()
    if subject != 'P':
        total_credit += float(point)
        weighted_sum += float(point) * dic[subject]
    

if total_credit == 0:
    print(0.0)
else:
    gpa = weighted_sum / total_credit
    print(round(gpa, 6))