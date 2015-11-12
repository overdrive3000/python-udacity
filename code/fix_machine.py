def fix_machine(debris, product):
  ### WRITE YOUR CODE HERE ###
  i = 0
  for s in product:
    if debris.find(s, i):
      i = i + 1
  if i == len(product):
    return product
  return "Give me something that's not useless next time."
                                                        

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'
