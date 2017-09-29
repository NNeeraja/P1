fruit_basket = ["apple","banana","mango","grapes","orange"]
guess_fruit=raw_input("Guess fruit name: ")
wg = 0
for i in fruit_basket:
    if i == guess_fruit: 
      print fruit_basket.index(guess_fruit)
      print "correct"
      wg = wg +1
      break
if wg == 0:
  print "wrong guess"

""" if guess_fruit == i:
    print "your guess is right"
 break

print "wrong gues" """

