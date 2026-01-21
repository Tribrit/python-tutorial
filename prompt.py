students={}
print("Welcome!!!")

def add_new():
 name=(input("Enter name:"))
 Id=int(input("Enter ID:"))
 Marks=int(input("enter marks:"))
 print("Name:",name)
 print("ID:",Id)
 print("marks",Marks)

def display_marks():
   
    print("students details:")
    for student in students:
      print("Student ID:",{'Id'})
      print("Name:",{'name'})
      print ("Marks:",['Marks'])
while True:
  print("/nmenu")
  print("1.Add new student.")
  print("2.Display student.")
  choice=input("Enter your choice from 1-2:")
  if choice  == "1":
    add_new()
  elif choice == "2":
      display_marks()
  else:
    print("Invalid choice")   
