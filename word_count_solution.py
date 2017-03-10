def words(word):
				
  string_dict = {}
		
  list_of_words = word.split()
		
		
  for word in list_of_words:
		
    if word.isdigit():
		
      word = int(word)
		
    if word in string_dict:
		
      string_dict[word] += 1
		
		
    else:
		
      string_dict[word] = 1
		
  return string_dict
