from itertools import combinations
from itertools import permutations
if __name__=="__main__":
    name=input("Your Name\n")
    name=[c for c in name]
    key=input("Permutations or Combination?\n")
    if key=="permutations":
        name=(list(permutations(name)))
        for each in name:
            print("".join(each))
    elif key=="combinations":
        name=(list(combinations(name,(len(name)-1))))
        for each in name:
            print("".join(each))