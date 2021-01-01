from collections import namedtuple
Student = namedtuple('Student',['Name','USN','Specialization'])
'''
Student is like a class 
Name,USN and Specializations are like instances of the class
'''


##Example
Anirudh = Student(Name='Anirudh',USN=2,Specialization='ISE')
#print(type(Anirudh))
<class '__main__.Student'>
print(Anirudh.Name,Anirudh.USN,Anirudh.Specialization)
#o/p:Anirudh 2 ISE
