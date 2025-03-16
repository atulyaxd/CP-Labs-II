subjects = {1:'EM', 2:'EM-II', 3:'EP', 4:'IMCE', 5:'EC'}

subjects.pop(5)
subjects.update({5:'CP'})
print(subjects.keys())
print(subjects.values())
subjects.get(2)
subjects.popitem()
subs = subjects.copy()
print(subjects)
print(id(subjects), id(subs), sep="\t")
