dict1={2:"orange",3:"banana",1:"apple"}
print(f"Dictionary1:{dict1}")
l=list(dict1.items())
l.sort()
print("Ascending order is:",l)
l=list(dict1.items())
l.sort(reverse=True)
print("Decending order is:",l)
dict2={4:"plum",5:"Cherry"}
print(f"Dictionary1:{dict2}")
dict1.update(dict2)
print(f"Dictionary after merging:{dict1}")