#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#   print_hi('PyCharm')

# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(elbow,below):
      print(elbow,below)
    # Convert string into lists
      list1 = list(elbow)
      list2 = list(below)
    # Sort the list value
      list1.sort()
      list2.sort()

      position = 0
      matches = True

      while position < len(elbow) and matches:
            if list1[position]==list2[position]:
                position = position + 1
            else:
                matches = False

      return matches

print(find_anagram('elbow','below'))


# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    return {"as": 10, "would": 20}

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
      # [assignment] Add your code here
      read_text = open('story.txt', 'r')

      return read_text


def count_words():
      rtext = read_file_content("./story.txt")

      # Make a dictionary with no entries.
      d = dict()

      # Iterate over the entire file's lines.
      for textline in rtext:
            # Remove the newline character and any leading spaces.
            textline = textline.strip()

            # To avoid case mismatches,
            # convert the characters in the line to lowercase.
            textline = textline.lower()

            # Break the line up into words.
            splitwords = textline.split(" ")

            # Repeat for each word in a line
            for word in splitwords:
                  # Determine if the word is in the dictionary
                  if word in d:
                        # Increment word count by 1
                        d[word] = d[word] + 1
                  else:
                        # Insert the word into the dictionary with count 1
                        d[word] = 1

      return d


words = count_words()
# Print the dictionary's contents
for key in list(words.keys()):
      print(key, ":", words[key])
