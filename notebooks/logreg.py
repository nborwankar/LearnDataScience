# logreg supporting functions
# Nitin Borwankar
# Open Data Science Training
  
  
import matplotlib.pyplot as plt
import numpy as np

def nfl_outcomes():
  scores = [3,11,12,13,20,22,21,25, 26,27,28,29,30,31,33,35,37,41,42,43]
  outcomes = [0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1]
  figsize = (8, 5)
  fig = plt.figure(figsize=figsize)
  ax = fig.add_subplot(111)
  line = ax.plot(scores,outcomes,'o')[0]
  #x = np.arange(5,50,5)
  #y = (1.1/30.)*x-0.3
  #line2 = ax.plot(x,y)
  ax.set_title('Win/Loss Outcomes for an NFL team')
  ax.set_xlabel('Score')
  ax.set_ylabel('Proability of a Win')
  ax.set_ylim((-0.1,1.1))
  ax.grid(True)
  #line.set_marker('o')
  #plt.savefig('oo.png',dpi=150)
  plt.show()
  return ax,fig
  
  
def nfl_outcomes_with_line():
  scores = [3,11,12,13,20,22,21,25, 26,27,28,29,30,31,33,35,37,41,42,43]
  outcomes = [0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1]
  figsize = (8, 5)
  fig = plt.figure(figsize=figsize)
  ax = fig.add_subplot(111)
  line = ax.plot(scores,outcomes,'o')[0]
  x = np.arange(5,50,5)
  y = (1.1/30.)*x-0.3
  line2 = ax.plot(x,y)
  ax.set_title('Win/Loss Outcomes for an NFL team')
  ax.set_xlabel('Score')
  ax.set_ylabel('Proability of a Win')
  ax.set_ylim((-0.1,1.1))
  ax.grid(True)
  #line.set_marker('o')
  #plt.savefig('oo.png',dpi=150)
  plt.show()
  return ax,fig
  


def fz(fico,amt,coeff):
  z = coeff[0]+coeff[1]*fico+coeff[2]*amt
  return 1/(1+exp(-1*z))
