def read_in_chunks(file_object, chunk_size=1024):
  """Lazy function (generator) to read a file piece by piece.
  Default chunk size: 1k."""
  while True:
    data = file_object.read(chunk_size)
    if not data:
      break
    yield data

fn = "commonwords.txt"

pals = []
#with open(fn) as f:
#  for piece in read_in_chunks(f):
#    words = piece.split("\n") 
#    for word in words:
#      if word.lower() == word[::-1] and len(word) > 1:
#        pals.append(word)

#for p in pals:
#  print(p)

pals2 = []

#with open(fn) as f:
#  for piece in read_in_chunks(f):
#    words = piece.split("\n") 
#    for word1 in words:
#      for word2 in words:
#        word1word2 = word1+word2
#        if word1word2.lower() == word1word2[::-1] and len(word1word2) > 2:
#          #pals2.append(word1word2)
#          print(word1word2)

pals3 = []

with open(fn) as f:
  for piece in read_in_chunks(f):
    words = piece.split("\n") 
    words = [x.strip() for x in words]
    words = [x for x in words if x!=""]
    for word1 in words:
      for word2 in words:
        if word1 != word2 and len(word1)!=1:
          for word3 in words:
             for word4 in words:
               word = word1+word2+word3 + word4
               if word.lower() == word[::-1] and len(word) > 3:
                 pals3.append(word)
                 print(word1, word2, word3, word4, sep=" ")
               for word5 in words:
                 word_ = word1+word2+word3 + word4 + word5
                 if word_.lower() == word_[::-1] and len(word_) > 3:
                   pals3.append(word_)
                   print(word1, word2, word3, word4, word5, sep=" ")
                 


print(pals3)
