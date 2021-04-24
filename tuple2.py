def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


tups = [("Aishwarya", 22), ("Tejal", 21), ("Sameen", 21),
        ("Sagu", 20), ("Anil", 25), ("Niharika", 23),
        ("Siddanth", 21), ("Renuka", 50)]
dictionary = {}
print(Convert(tups, dictionary))