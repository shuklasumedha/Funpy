list=["tumbling", "forms", "resembling", "meaning", "creating",
      "symphony", "punctuating", "desires", "emoting", "destinies"]

for i in range (10):
    y=(i*7)/8
    print (*list[i])
    print ("_"*i, "."*int(y), sep="\n")
    
list.reverse()

for i in range (10):
    z=(i*8)/7
    print (*list[i])
    print ("_"*i, "."*int(z), sep="\n")
