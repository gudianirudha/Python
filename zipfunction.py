names=("Anirudha","Kumar","Suresh","Venugopal")
branches=("ISE","CSE","MECH","EE")
info=list(zip(names,branches))
print(info)

#2nd example
names=("Anirudha","Kumar","Suresh","Venugopal","Sukesh")
branches=("ISE","CSE","MECH","EE","EC")

info=(zip(names,branches))
for a,b in info:
    print(a,b)
  
