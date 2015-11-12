def find_last(string, substring):
  i = 0
  while string.find(substring, i) != -1:
    i = i + 1
  
  if i == 0:
    return -1
  else:
    return i - 1

def udacity(s, t):
  last_pos = -1
  while True:
    pos = s.find(t, last_pos + 1)
    if pos == -1
      return last_pos
    last_pos = pos

print find_last('aaaa', 'a')
print find_last('aaaaa', 'aa')
print find_last('aaaa', 'b')
print find_last("111111111", "1")
print find_last("222222222", "")
print find_last("", "3")
print find_last("", "")
