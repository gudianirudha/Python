#importing the matplot library
import matplotlib.pyplot as plt
#Creating a list 
subj = []
marks = [] 

# number of records which user wants to enter! 
records = int(input("Enter number of records : ")) 
  
# iterating till the range 
for i in range(0, records): 
    print(" Enter the Subject Name")
    subject = str(input()) 
    subj.append(subject) 
    # adding the elements
    
for i in range(0, records): 
    print("Enter the marks")
    mark = int(input()) 
    marks.append(mark)     


plt.plot(subj,marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("RESULTS")

plt.savefig("Result.jpeg")
