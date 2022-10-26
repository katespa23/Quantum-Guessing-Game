import math
import cmath
import statistics
import numpy 
import random
from decimal import Decimal

print("Welcome to the Quantum State Game!")
print("The goal of the game is to make the minumum number of guesses towards a state based on taking spin measurements in the x, y and z directions")
print(" ")
knowledge = input("Is this your first time playing and/or do you need some more background rules of the game, enter y/n")
if knowledge == "y":
  print("This game has 2 roles, Apparatus and the Experimenter. The Apparatus will secretly choose a state (row) from that table of quantum spin-1/2 states in front of you. The Experimenter will ask the apparatus to measure the unknown state in a certain direction. The apparatus will roll a die to determine if that measurement is positive or negative in accordance with the table. The experimenter will enter that measurement into this code (following the prompts) and after a set number of measurements, this code will tell you what the state most likely is. If our guess is wrong, then you continue to make measurements and guess again. After a correct guess, or 20 measurements, the round ends. The players switch roles. A complete game is 3 rounds.")
else:
  print(" ")
print(" ")
print("The scoring criteria is as follows:")
print("Each measurement taken is worth one point, and guessing a state incorrectly is worth 5 points. If you make an incorrect guess, you will be asked to take atleast 3 more measurements before guessing again. This will in turn, up your score. The catch is, this is scored like a golf game. The lowest score wins!")
print(" ")

understanding = input("if you understand this, enter y to continue. If you are still confused, enter n and reread the directions. They will stay there as long as you need, just restart the game, and enter y to play.")

if understanding == "y":
  print("Okay, let's continue!")
else:
  exit()
  

print(" ")
print("First thing is first, let's enter in the possible initial states for the game before starting: ")



# User inputs the probabilities of each measurement to initialize the specific game we're playin

penalty = 5 #points for incorrect guess
maxguess = 30 # maximum number of measurements allowed
dsize = 20 # size of the dice used for rolling

#These are the x y and z states so we can use them to calculate probabilities later on
xplusstateket = [[1/(math.sqrt(2))], [1/(math.sqrt(2))]]
xplusstatebra = [1/(math.sqrt(2)), 1/(math.sqrt(2))]

xminusstateket = [[1/(math.sqrt(2))], [-1/(math.sqrt(2))]]
xminusstatebra = [1/(math.sqrt(2)), -1/(math.sqrt(2))]

r1 = 0
i1 = 1/math.sqrt(2)
c1 = complex(r1,i1)
yplusstateket = [[1/(math.sqrt(2))], [c1]]
yplusstatebra = [1/(math.sqrt(2)), c1]

i2 = -1/math.sqrt(2)
c2 = complex(r1, i2)
yminusstateket = [[1/math.sqrt(2)], [c2]]
yminusstatebra = [1/math.sqrt(2), c2]

zplusstateket = [[1], [0]]
zplusstatebra = [1,0]

zminusstateket = [[0],[1]]
zminusstatebra = [0,1]


R = 1
C = 2

numstates = input("how many states are there? ")
numstates_1 = int(numstates)

d = {}
dprobxplus = {}
dprobxminus = {}
dprobyplus = {}
dprobyminus = {}
dprobzplus = {}
dprobzminus = {}
stopindex = 0
step = -1

#These states will be used for all 3 rounds
for i in range(numstates_1, stopindex, step):
  
  state = []
  
  psi1 = float(input("enter the first row of the state: "))
  
  psi2real = float(input("enter the real part of the second row: "))
  psi2imag = float(input("input the imaginary part of the  second row: "))
  psi2 = complex(psi2real, psi2imag)
  
  state = [[psi1],[psi2]]
  d["state {0}".format(i)] = state
  
  print(state)
  
  pxplus = numpy.dot(xplusstatebra, state)
  probxplus = (abs(pxplus))**2
  print("the probability of x in the order plus, minus is :")
  print(probxplus)
  dprobxplus["probxplus{0}".format(i)] = probxplus

  probxminus = 1 - probxplus
  print(probxminus)
  dprobxminus["probxminus{0}".format(i)] = probxminus

  pyplus = numpy.dot(yplusstatebra, state)
  probyplus = 1-((abs(pyplus))**2)
  print("The probability of y in the order plus, minus is:")
  print(probyplus)
  dprobyplus["probyplus{0}".format(i)] = probyplus

  probyminus = 1-probyplus
  print(probyminus)
  dprobyminus["probyminus{0}".format(i)] = probyminus

  pzplus = numpy.dot(zplusstatebra, state)
  probzplus = (abs(pzplus))**2
  dprobzplus["probzplus{0}".format(i)] = probzplus

  probzminus = 1-probzplus
  dprobzminus["probzminus{0}".format(i)] = probzminus

  
  print("The probability of z in the order plus, minus is:")
  print(probzplus)
  print(probzminus)

print("For the rest of the game, you will be prompted to enter measurements and make guesses, just follow along with the prompts for these.")

  #This is all relative to round 1:
dx ={}
for k in range (4, stopindex, step): 
  x = input("ask for an x measurement")
  if x == "+":
    a= 1
  else:
    a = 0
  dx["a{0}".format(k)] = a
xplusses = sum(dx.values())
xminusses = 4- xplusses
print("the number of x plus measurements is")
print(xplusses)

dy = {}
for k in range (4, stopindex, step): 
  y = input("ask for a y measurement")
  if y == "+":
    b= 1
  else:
    b = 0
  dy["b{0}".format(k)] = b
yplusses = sum(dy.values())
yminusses = 4- yplusses
print("the number of y plus measurements is")
print(yplusses)

dz = {}
for k in range (4, stopindex, step):
  z = input("ask for a z measurement")
  if z=="+":
    c=1
  else:
    c=0
  dz["c{0}".format(k)] = c
zplusses = sum(dz.values())
zminusses = 4-zplusses
print("the number of z plus measurements is")
print(zplusses)


#This dictionary allows us to save each state we enter under a different name
#print("The last state entered was")
#print(d["state 1"])
#print("The states entered were")
#print(d)
#THIS IS HOW YOU CALL A STATE
#THIS WILL CALL THE FIRST STATE YOU ENTERED
#print(d["state " + numstates])


#calculating the experimental probabilities
expxplus = float(xplusses/(xplusses+xminusses))
expxminus = float(xminusses/(xplusses+xminusses))
expyplus = float(yplusses/(yplusses+yminusses))
expyminus = float(yminusses/(yplusses+yminusses))
expzplus = float(zplusses/(zplusses+zminusses))
expzminus = float(zminusses/(zplusses+zminusses))

#telling the user the experimental probabilities
#maybe we don't need this
print("The experimental probabilites of each state are as follows:")
print("x plus: ")
print(expxplus)
print("x minus: ")
print(expxminus)
print("y plus: ")
print(expyplus)
print("y minus: ")
print(expyminus)
print("z plus: ")
print(expzplus)
print("z minus: ")
print(expzminus)

print("Choose the state that matches this mix of probabilities ")

dprobxplusl = list(dprobxplus.values())
np_dprobxplusl = numpy.asarray(dprobxplusl)
np_dprobxpluslf = [float(x) for x in dprobxplusl]
closest1idx = (numpy.abs(np_dprobxplusl - expxplus)).argmin()
closest1 = dprobxplusl[closest1idx]
print("The most likely probability of xplus is:")
print(closest1)

dprobyplusl = list(dprobyplus.values())
np_dprobyplusl = numpy.asarray(dprobyplusl)
np_dprobypluslf = [float(x) for x in dprobyplusl]
closest2idx = (numpy.abs(np_dprobyplusl - expyplus)).argmin() 
closest2 = dprobyplusl[closest2idx]
print("The most likely probability of yplus is:")
print(closest2)

dprobzplusl = list(dprobzplus.values())
np_dprobzplusl = numpy.asarray(dprobzplusl)
np_dprobzpluslf = [float(x) for x in dprobzplusl]
closest3idx = (numpy.abs(np_dprobzplusl - expzplus)).argmin() 
closest3 = dprobzplusl[closest3idx]
print("The most likely probability of zplus is:")
print(closest3)

for n in range(1, numstates_1 +1):
  n1 = str(n)
  if closest1==dprobxplus["probxplus" + n1] and closest2==dprobyplus["probyplus" + n1] and closest3==dprobzplus["probzplus" + n1]:
    print("guess state, ")
    print(numstates_1 +1 - n)
  else:
    print(" ")


if closest1==probxplus and closest2==probyplus and closest3==probzplus:
  print(state)
  # idk how to do this with the dictionary but basically my idea was to output the state number like "most like 'state 4'" or whatever number it is according to how the probabilities compare to the ones saved


guess = input("Guess: enter y if correct, enter n if incorrect. OR: If none of the states match up with those probabilities (sometimes, you just get some bad luck with dice rolls. happens to the best of us), then enter n to keep making measurements. ")
if guess =="y":
  print("Round ended")
elif guess =="n":
  for i in range(numstates_1 - 1, stopindex, step):
    choice = input("enter n if there is only one state left to guess. Otherwise enter another letter and keep going. ")
    if choice =="n":
      print("Round ended")
    else:
      print("oops")
      x0 = input("ask for another x")
      y0 = input("ask for another y")
      z0= input("ask for another z")
      if x0 == "+":
        a0 = 1
      else:
        a0 = 0
      xplusses = sum(dx.values())+ a0
      xminusses = 6 - xplusses
  
      if y0 == "+":
        b0 = 1
      else:
        b0 = 0
      yplusses = sum(dy.values()) + b0
      yminusses = 6-yplusses

      if z0 == "+":
        c0 = 1
      else:
        c0 = 0
      zplusses = sum(dz.values()) + c0
      zminusses = 6-zplusses

      expxplus0 = float(xplusses/(xplusses+xminusses))
      expxminus0 = float(xminusses/(xplusses+xminusses))
      expyplus0 = float(yplusses/(yplusses+yminusses))
      expyminus0 = float(yminusses/(yplusses+yminusses))
      expzplus0 = float(zplusses/(zplusses+zminusses))
      expzminus0 = float(zminusses/(zplusses+zminusses))

      print("choose the state that matches these     probabilities")
      closest1idx = (numpy.abs(np_dprobxplusl -       expxplus0)).argmin()
      closest1 = dprobxplusl[closest1idx]
      print("The most likely probability of xplus is:")
      print(closest1)

  
      closest2idx = (numpy.abs(np_dprobyplusl -   expyplus0)).argmin() 
      closest2 = dprobyplusl[closest2idx]
      print("The most likely probability of yplus is:")
      print(closest2)

 
      closest3idx = (numpy.abs(np_dprobzplusl -   expzplus0)).argmin() 
      closest3 = dprobzplusl[closest3idx]
      print("The most likely probability of zplus is:")
      print(closest3)
g11 = input("Enter in the number of incorrect guesses")
g1 = int(g11)
score1 = 15 + 5*g1 + 3*g1
print("Your score for this round is ")
print(score1)
score1c = int(input("enter your competitor's score "))
print(score1c)
if score1c > score1:
  diff1 = score1c-score1
  print("you are winning by:")
  print(diff1)
elif score1 > score1c:
  diff1 = score1-score1c
  print("you are losing by: ")
  print(diff1)
else:
  print("you are tied with: ")
  print(score1)


#Now for round 2:
dx2 ={}
for k in range (5, stopindex, step): 
  x2 = input("ask for an x measurement")
  if x2 == "+":
    a2= 1
  else:
    a2= 0
  dx2["a2{0}".format(k)] = a2
xplusses2 = sum(dx2.values())
xminusses2 = 5- xplusses2
print("the number of x plus measurements is")
print(xplusses2)

dy2 = {}
for k in range (5, stopindex, step): 
  y2 = input("ask for a y measurement")
  if y2 == "+":
    b2= 1
  else:
    b2 = 0
  dy2["b2{0}".format(k)] = b2
yplusses2 = sum(dy2.values())
yminusses2 = 5- yplusses2
print("the number of y plus measurements is")
print(yplusses2)

dz2 = {}
for k in range (5, stopindex, step):
  z2 = input("ask for a z measurement")
  if z2=="+":
    c2=1
  else:
    c2=0
  dz2["c2{0}".format(k)] = c2
zplusses2 = sum(dz2.values())
zminusses2 = 5-zplusses2
print("the number of z plus measurements is")
print(zplusses2)

expxplus2 = float(xplusses2/(xplusses2+xminusses2))
expxminus2 = float(xminusses2/(xplusses2+xminusses2))
expyplus2 = float(yplusses2/(yplusses2+yminusses2))
expyminus2 = float(yminusses2/(yplusses2+yminusses2))
expzplus2 = float(zplusses2/(zplusses2+zminusses2))
expzminus2 = float(zminusses2/(zplusses2+zminusses2))

closest1idx2 = (numpy.abs(np_dprobxplusl - expxplus2)).argmin()
closest12 = dprobxplusl[closest1idx2]
print("The most likely probability of xplus is:")
print(closest12)

closest2idx2 = (numpy.abs(np_dprobyplusl - expyplus2)).argmin() 
closest22 = dprobyplusl[closest2idx2]
print("The most likely probability of yplus is:")
print(closest22)

closest3idx2 = (numpy.abs(np_dprobzplusl - expzplus2)).argmin() 
closest32 = dprobzplusl[closest3idx2]
print("The most likely probability of zplus is:")
print(closest32)

for n in range(1, numstates_1 +1):
  n1 = str(n)
  if closest12==dprobxplus["probxplus" + n1] and closest22==dprobyplus["probyplus" + n1] and closest32==dprobzplus["probzplus" + n1]:
    print("guess state, ")
    print(numstates_1 +1 - n)
  else:
    print(" ")

guess2 = input("Guess: enter y if correct, enter n if incorrect. OR: If none of the states match up with those probabilities (sometimes, you just get some bad luck with dice rolls. happens to the best of us), then enter n to keep making measurements. ")
if guess2 =="y":
  print("Round ended")
elif guess2 =="n":
  for i in range(numstates_1 - 1, stopindex, step):
    choice2 = input("enter n if there is only one state left to guess. Otherwise enter another letter and keep going.")
    if choice2 =="n":
      print("Round ended")
    else:
      print("oops")
      x02 = input("ask for another x")
      y02 = input("ask for another y")
      z02= input("ask for another z")
      if x02 == "+":
        a02 = 1
      else:
        a02 = 0
      xplusses2 = sum(dx2.values())+ a02
      xminusses2 = 6 - xplusses2
  
      if y02 == "+":
        b02 = 1
      else:
        b02 = 0
      yplusses2 = sum(dy2.values()) + b02
      yminusses2 = 6-yplusses2

      if z02 == "+":
        c02 = 1
      else:
        c02 = 0
      zplusses2 = sum(dz2.values()) + c02
      zminusses2 = 6-zplusses2

      expxplus02 = float(xplusses2/(xplusses2+xminusses2))
      expxminus02 =  float(xminusses2/(xplusses2+xminusses2))
      expyplus02 = float(yplusses2/(yplusses2+yminusses2))
      expyminus02 = float(yminusses2/(yplusses2+yminusses2))
      expzplus02 = float(zplusses2/(zplusses2+zminusses2))
      expzminus02 = float(zminusses2/(zplusses2+zminusses2))

      print("choose the state that matches these     probabilities")
      closest1idx2 = (numpy.abs(np_dprobxplusl -       expxplus02)).argmin()
      closest12 = dprobxplusl[closest1idx2]
      print("The most likely probability of xplus is:")
      print(closest12)

  
      closest2idx2 = (numpy.abs(np_dprobyplusl -   expyplus02)).argmin() 
      closest22 = dprobyplusl[closest2idx2]
      print("The most likely probability of yplus is:")
      print(closest22)

 
      closest3idx2 = (numpy.abs(np_dprobzplusl -   expzplus02)).argmin() 
      closest32 = dprobzplusl[closest3idx2]
      print("The most likely probability of zplus is:")
      print(closest32)
g22 = input("Enter in the number of incorrect guesses")
g2 = int(g22)
score2 = 15 + 5*g2 + 3*g2
print("Your score for this round is ")
print(score2)
print("Your total score thus far is ")
print(score1 + score2)
score2c = int(input("enter your competitor's score this round "))
print("their total score is:")
print(score2c + score1c)
if score1c + score2c > score1+ score2:
  diff2 = (score1c + score2c) - (score1+score2)
  print("you are winning by:")
  print(diff2)
elif score1 + score2 > score1c+score2c:
  diff2 = (score1+score2)-(score1c+score2c)
  print("you are losing by: ")
  print(diff2)
else:
  print("you are tied with: ")
  print(score1+score2 )

#Now for Round 3:

dx3 ={}
for k in range (5, stopindex, step): 
  x3 = input("ask for an x measurement")
  if x3 == "+":
    a3= 1
  else:
    a3= 0
  dx3["a3{0}".format(k)] = a3
xplusses3 = sum(dx3.values())
xminusses3 = 5- xplusses3
print("the number of x plus measurements is")
print(xplusses3)

dy3 = {}
for k in range (5, stopindex, step): 
  y3 = input("ask for a y measurement")
  if y3 == "+":
    b3= 1
  else:
    b3 = 0
  dy3["b3{0}".format(k)] = b3
yplusses3 = sum(dy3.values())
yminusses3 = 5- yplusses3
print("the number of y plus measurements is")
print(yplusses3)

dz3 = {}
for k in range (5, stopindex, step):
  z3 = input("ask for a z measurement")
  if z3=="+":
    c3=1
  else:
    c3=0
  dz3["c3{0}".format(k)] = c3
zplusses3 = sum(dz3.values())
zminusses3 = 5-zplusses3
print("the number of z plus measurements is")
print(zplusses3)

expxplus3 = float(xplusses3/(xplusses3+xminusses3))
expxminus3 = float(xminusses3/(xplusses3+xminusses3))
expyplus3 = float(yplusses3/(yplusses3+yminusses3))
expyminus3 = float(yminusses3/(yplusses3+yminusses3))
expzplus3 = float(zplusses3/(zplusses3+zminusses3))
expzminus3 = float(zminusses3/(zplusses3+zminusses3))

closest1idx3 = (numpy.abs(np_dprobxplusl - expxplus3)).argmin()
closest13 = dprobxplusl[closest1idx3]
print("The most likely probability of xplus is:")
print(closest13)

closest2idx3 = (numpy.abs(np_dprobyplusl - expyplus3)).argmin() 
closest23 = dprobyplusl[closest2idx3]
print("The most likely probability of yplus is:")
print(closest23)

closest3idx3 = (numpy.abs(np_dprobzplusl - expzplus3)).argmin() 
closest33 = dprobzplusl[closest3idx3]
print("The most likely probability of zplus is:")
print(closest33)

for n in range(1, numstates_1 +1):
  n1 = str(n)
  if closest13==dprobxplus["probxplus" + n1] and closest23==dprobyplus["probyplus" + n1] and closest33==dprobzplus["probzplus" + n1]:
    print("guess state, ")
    print(numstates_1 +1 - n)
  else:
    print(" ")

guess3 = input("Guess: enter y if correct, enter n if incorrect. OR: If none of the states match up with those probabilities (sometimes, you just get some bad luck with dice rolls. happens to the best of us), then enter n to keep making measurements. ")
if guess3 =="y":
  print("Round ended")
elif guess3 =="n":
  for i in range(numstates_1 - 1, stopindex, step):
    choice3 = input("enter n if there is only one state left to guess. Otherwise enter another letter and keep going.")
    if choice3 =="n":
      print("Round ended")
    else:
      print("oops")
      x03 = input("ask for another x")
      y03 = input("ask for another y")
      z03= input("ask for another z")
      if x03 == "+":
        a03 = 1
      else:
        a03 = 0
      xplusses3 = sum(dx3.values())+ a03
      xminusses3 = 6 - xplusses3
  
      if y03 == "+":
        b03 = 1
      else:
        b03 = 0
      yplusses3 = sum(dy3.values()) + b03
      yminusses3 = 6-yplusses3

      if z03 == "+":
        c03 = 1
      else:
        c03 = 0
      zplusses3 = sum(dz3.values()) + c03
      zminusses3 = 6-zplusses3

      expxplus03 = float(xplusses3/(xplusses3+xminusses3))
      expxminus03 =  float(xminusses3/(xplusses3+xminusses3))
      expyplus03 = float(yplusses3/(yplusses3+yminusses3))
      expyminus03 = float(yminusses3/(yplusses3+yminusses3))
      expzplus03 = float(zplusses3/(zplusses3+zminusses3))
      expzminus03 = float(zminusses3/(zplusses3+zminusses3))

      print("choose the state that matches these     probabilities")
      closest1idx3 = (numpy.abs(np_dprobxplusl -       expxplus03)).argmin()
      closest13 = dprobxplusl[closest1idx3]
      print("The most likely probability of xplus is:")
      print(closest13)

  
      closest2idx3 = (numpy.abs(np_dprobyplusl -   expyplus03)).argmin() 
      closest23 = dprobyplusl[closest2idx3]
      print("The most likely probability of yplus is:")
      print(closest23)

 
      closest3idx3 = (numpy.abs(np_dprobzplusl -   expzplus03)).argmin() 
      closest33 = dprobzplusl[closest3idx3]
      print("The most likely probability of zplus is:")
      print(closest33)
g33 = input("Enter in the number of incorrect guesses")
g3 = int(g33)
score3 = 15 + 5*g3 + 3*g3
print("Your score for this round is ")
print(score3)
print("Your final is ")
finalscore = score1+score2+score3
print(finalscore)
score3c = int(input("enter your competitor's score this round "))
print("their total score is:")
print(score2c + score1c+score3c)
if score1c + score2c +score3c > finalscore:
  diff3 = (score1c + score2c + score3c) - (finalscore)
  print("congrats!! you won by:")
  print(diff3)
elif score1 + score2 +score3 > score1c+score2c+score3c:
  diff3 = (finalscore)-(score1c+score2c+score3c)
  print("aw, you lost by: ")
  print(diff3)
else:
  print("you tied at: ")
  print(finalscore)




#i needed something here for the code to compile feel free to delete later
  

  ## here we should have a way to calculate what the most uncertain measurement is and then ask for more of that measurement


#print("x+ probability " + closest1 + "y+ probability" + closest2 + "z+ probability" + closest3)


# find out values for x, y, and z then evaluate possible states that best match probability for Px, Py, and Pz - basically which Px, Py, and Pz have the lowest uncertainty and choose the state that has all the lowest standard deviations
# may have to look at P_plusX, P_minusX, P_plusY, P_minusY, and P_plusZ, P_minusZ
# value = Vx or Vy or Vz # input number
# decide upon a number of guesses (N) we should ask for each state ahead of time and just plug that in for N and run portion of the code that asks for inputs regarding a particular state N times 

# may have to look at P_plusX, P_minusX, P_plusY, P_minusY, and P_plusZ, P_minusZ :(
  
# w/ respect to x

#Theoretical  
#VxPx = Vx*Px
#VxPxsquare = VxSquare*Px
#EVx = sum(VxPx) # expectation value = sum all values*probabilities
#EVVx = sum(VxPxsquare)
#theoryVx = EVVx - EVx
#theoryUx = math.sqrt(theoryVx)
#theoryUmeanX = theoryUx/(math.sqrt(N-1)) # where N = total number of inputs or guesses

# Experimental
#avgVx = statistics.mean(xplusses+xminusses) # mean
#avgVVx = statistics.mean(VVx)
#expVx = avgVVx - avgVx**2
#expUx = math.sqrt(expVx)
#ExpUmeanx = expUx/(math.sqrt(N-1)) # where N = total number of inputs

# w/ respect to y

#Theoretical
#VySquare = Vy**2
#VyPy = Vy*Py
#VyPysquare = VySquare*Py
#EVy = sum(VyPy) # expectation value = sum all values*probabilities
#EVVy = sum(VyPysquare)
#theoryVy = EVVy - EVy
#theoryUy = math.sqrt(theoryVy)
#theoryUmeanY = theoryUy/(math.sqrt(N-1)) # where N = total number of inputs or guesses

# Experimental
#avgVy = mean(Vy) # mean
#avgVVy = mean(VySquare)
#expVy = avgVVy - avgVy**2
#expUy = math.sqrt(expVy)
#ExpUmeanY = expUy/(math.sqrt(N-1)) # where N = total number of inputs

# w/ respect to z

#Theoretical
#VzSquare = Vz**2
#VzPz = Vz*Pz
#VzPysquare = VzSquare*Pz
#EVz = sum(VzPz) # expectation value = sum all values*probabilities
#EVVz = sum(VzPzsquare)
#theoryVz = EVVz - EVz
#theoryUz = math.sqrt(theoryVz)
#theoryUmeanZ = theoryUz/(math.sqrt(N-1)) # where N = total number of inputs or guesses

# Experimental
#avgVz = mean(Vz) # mean
#avgVVz = mean(VzSquare)
#expVz = avgVVz - avgVz**2
#expUz = math.sqrt(expVz)
#ExpUmeanZ = expUz/(math.sqrt(N-1)) # where N = total number of inputs

  
#print("Input the probabilities of each measurement in the order x+, x-, y+, y-, z+, z- for each state: ")





# write loop such that each time you make a measurement, your score adds +1 and each time you guess wrong your score adds +5
# Now we need a way to compare the measurements and  
#decide which is the most probable state 
#what if we use 1 and -1 for the measurements and 
#use divide and conquer to compare the sums and then have that output the probability that x is positive, y is positive, etc? 