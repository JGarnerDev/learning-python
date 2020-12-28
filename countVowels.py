def countVowels(str):
    count = 0
    for char in str:
        if char in "aieouAIEOU":
          count += 1
    return count
    

print(countVowels("ass"))
print(countVowels("badger"))
print(countVowels("eeeeey"))