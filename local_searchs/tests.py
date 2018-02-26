def evalue():
    yield 3, 5, 8

i = list(evalue())
print(i)