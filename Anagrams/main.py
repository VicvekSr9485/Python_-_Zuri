# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(string1, string2):
        return sorted(string1) == sorted(string2)
        if string1 == string2:
            print(True)
        else:
            print(False)

            
print(find_anagram("brush", "shrub"))

