text = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

empty = []
offset = 10
for char in text:
  temp = ord(char)
  if temp >= 97 and temp <= 122:
    new_char = chr((temp - 97 + offset) % 26 + 97)
    empty.append(new_char)
  elif temp >= 65 and temp <= 90:
    new_char = chr((temp - 65 + offset) % 26 + 65)
    empty.append(new_char)
  else :
    empty.append(char)
  
sentence = " ".join(empty)
print(sentence)
