student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#print(f"Highest score is: {max(student_scores)}")

#print(type(student_scores[0]))

high_score = student_scores[0]

for x in student_scores:
  if x > high_score:
    high_score = x


print(high_score)
