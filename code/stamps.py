def stamps(stp):
  # Your code here
  five, two, one = 0, 0, 0
  while stp != 0:
    if stp >= 5:
      five = five + 1
      stp = stp - 5
    elif stp >= 2:
      two = two + 1
      stp = stp - 2
    else:
      one = one + 1
      stp = stp - 1
  return five, two, one

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
