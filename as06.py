word = input("input a word:")
lowercase = word.lower()

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)

    vowel_counts[vowel] = count
    counts = vowel_counts.values()
    totalvowels = sum(counts)



print(totalvowels)
decision = input("Would you like to know how many times each vowel appeared in the word?(yes or no):")
if decision == "yes":
    print(vowel_counts)