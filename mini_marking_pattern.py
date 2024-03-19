marks_a=int(input("Enter the marks of subject A out of 50\n"))
marks_b=int(input("Enter the marks of subject B out of 50\n"))
marks_c=int(input("Enter the marks of subject c out of 50\n"))
marks_d=int(input("Enter the marks of subject D out of 50\n"))

#To check the total marks of the candidates
total_marks=(marks_a + marks_b + marks_c + marks_d)
print ("The total marks of the candidate is:",total_marks)

#To check the percentage of marks for the candidate
marks_percentage =(total_marks/200)*100 
print("The total percentage of marks for the candidate is :",marks_percentage)

#To check the grades
if total_marks < 30:
    print("The grade is F\n")
elif total_marks >= 30 and total_marks <60 :
    print("The grade is C\n")
elif total_marks >= 60 and total_marks <85 :
    print("The grade is B\n")
elif total_marks >= 85 :
    print ("The grade is A\n")
else :
    print("Invalid marks entered")
