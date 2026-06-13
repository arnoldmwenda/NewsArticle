with open('article.txt', 'r', encoding = 'utf-8') as file:
  content = file.read()


def count_specific_word(content, searchWord):
  if not content or not searchWord:
    return 0
  content_lower = content.lower()
  searchWord_lower = searchWord.lower()
  clean_chars = []
  for char in content_lower:
    if char.isalnum() or char.isspace():
      clean_chars.append(char)
  clean_content = "".join(clean_chars)
  words_list = clean_content.split()
  word_counter = 0
  for word in words_list:
    if word == searchWord_lower:
      word_counter += 1
  return word_counter

searchWord = input("Enter word to count: ")
match_count = count_specific_word(content, searchWord)

print(f"The word '{searchWord}' appears {match_count} times.")


def identify_most_common_word(content):
  if not content.strip():
    return None
  content_lower = content.lower()
  clean_chars = []
  for char in content_lower:
    if char.isalnum() or char.isspace():
      clean_chars.append(char)
  clean_content = "".join(clean_chars)
  words_list = clean_content.split()
  if not words_list:
    return None
  word_counts = {}
  for word in words_list:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1
  most_frequent_word = ""
  highest_count = 0
  for word, count in word_counts.items():
    if count > highest_count:
      highest_count = count
      most_frequent_word = word
  return most_frequent_word

frequent_word = identify_most_common_word(content)

if frequent_word:
  print(f"The most common word is '{frequent_word}'")
else:
  print("Empty")


def calculate_average_word_length(content):
  if not content.strip():
    return 0
  content_lower = content.lower()
  clean_chars = []
  for char in content_lower:
    if char.isalnum() or char.isspace():
      clean_chars.append(char)
  clean_content = "".join(clean_chars)
  words_list = clean_content.split()
  if not words_list:
    return 0
  total_words = len(words_list)
  total_letters = 0
  for word in words_list:
    total_letters += len(word)
  average_length = total_letters / total_words
  return round(average_length, 2)

average_word_length = calculate_average_word_length(content)

if average_word_length:
  print(f"The average length for each word is {average_word_length}")
else:
  print("Empty")


def count_paragraphs(content):
  if not content.strip():
    return 1
  raw_lines = content.split('\n')
  paragraph_count = 0
  for line in raw_lines:
    if line.strip():
      paragraph_count += 1
  return paragraph_count

number_of_paragraphs = count_paragraphs(content)

if number_of_paragraphs:
  print(f"The number of paragraphs is {number_of_paragraphs}")
else:
  print("Empty")


def count_sentences(content):
  if not content.strip():
    return 1
  sentence_counter = 0
  has_uncounted_text = False
  for char in content:
    if char.isalnum():
      has_uncounted_text = True
    elif char in ('.', '!', '?'):
      if has_uncounted_text:
        sentence_counter += 1
        has_uncounted_text = False
  if has_uncounted_text:
    sentence_counter += 1
  return sentence_counter

number_of_sentences = count_sentences(content)

if number_of_sentences:
  print(f"The number of sentences is {number_of_sentences}")
else:
  print("Empty")