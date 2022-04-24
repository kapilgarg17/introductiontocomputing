# 01 Average of Three Numbers

n1 =int(input("Enter the First Number"))
n2 =int(input("Enter the Second Number"))
n3 =int(input("Enter the Third Number"))
avg=(n1+n2+n3)/3
print("Average of Three Numbers is",avg)


# 02 Income Tax
gross_income=int(input("Enter gross income"))
dependent=int(input("Number of dependents"))
tax_income=gross_income-10000-(dependent*3000)
tax=0.2*tax_income
print("the person has to pay", tax ,"to income tax officer")

# 03 List
n1=int(input("Number of Students"))
lts=["SID", "Name", "Gender", "Course Name", "CGPA"]
for j in range (n1):
    nlst = []
    SID=int(input("Enter your SID:"))
    Name=input("Enter your Name:")
    Gender=input("Enter your Gender:")#Gender should be M/F and U for unknown
    Course_Name=input("Enter the Course:")
    CGPA=float(input("Enter your CGPA:"))
    nlst.append(SID)
    nlst.append(Name)
    nlst.append(Gender)
    nlst.append(Course_Name)
    nlst.append(CGPA)
    print(lts)
    print(nlst)

# 04 Marks of students
s1=float(input("Enter the marks of Fist Student"))
s2=float(input("Enter the marks of Second Student"))
s3=float(input("Enter the marks of Third Student"))
s4=float(input("Enter the marks of Fourth Student"))
s5=float(input("Enter the marks of Fifth Student"))
slst=[s1, s2, s3, s4, s5]
slst.sort()
print(slst)

# 05
   #(a)
color=["Red", "Green", "White", "Black", "Pink", "Yellow"]
color.pop(3)
print(color)

   #(b)
color[3]="Purple"
print(color)





