# Supporting library for Lin Reg Notebooks
# Author: Nitin Borwankar
# Open Data Science Training

import warnings
# squelch an anaconda "bug" and some python verbosity
# this can move to system wide python if needed
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import patsy 
import statsmodels.api as sm
from numpy.random import RandomState

def make_standard_normal(seed=12345, size=20):
    prng = RandomState(seed)
    return prng.standard_normal(size)


def abline(intercept, gradient, *args, **kwargs):
    global np, plt
    a = plt.gca()
    xlim = a.get_xlim()
    ylim = a.get_ylim()
    
    if args:
        sty = args[0]
    else:
        sty = 'r'
        
    if kwargs:
        lw = kwargs['linewidth']
    else:
        lw = 1

    a.plot(xlim, [intercept + gradient * x for x in xlim], sty, linewidth=lw)
    a.set_xlim(xlim)
    a.set_ylim(ylim)
    return

    
def make_data_points(noise_factor=0.5,seed=12345):
    global np, plt
    sn = make_standard_normal(seed)
    z = noise_factor*sn

    x = np.linspace(0,5,20)
    y = 2*x + 0.5 + z
    return (x,y)
    

def make_single_plot(xarr,yarr,xlabel=None,ylabel=None,title=None, xinches=4, yinches=4, resize=False, show=True):
    global np, plt    
    
    f, ax1 = plt.subplots(ncols=1,nrows=1)
    if resize:
      f.set_size_inches(xinches, yinches)
    
    ax1 = plt.subplot(1,1,1)
    
    if xlabel:
      ax1.set_xlabel(xlabel)
    if ylabel:
      ax1.set_ylabel(ylabel)
    if title:
      ax1.set_title(title)

    if show:
      ax1.plot(xarr,yarr,'o')
    
    return ax1
    
    
def lab_experiment(noise_factor=0.5,seed=12345, exptnum=0):
    global np, plt
    x, y = make_data_points(noise_factor,seed)
    if exptnum:
      title = "Lab Experiment %d"%(exptnum)
    else:
      title = "Lab Experiment"  

    ax = make_single_plot(x,y,'Force','Acceleration', title)
    return ax

    
def lab_experiment_with_line(noise_factor=0.5, gradient_offset=0, intercept_offset=0, style='r', linewidth=1, seed=12345, exptnum=0):
        
    x, y = make_data_points(noise_factor,seed)
    if exptnum:
      title = "Lab Experiment %d"%(exptnum)
    else:
      title = "Lab Experiment"  
    ax = make_single_plot(x,y,'Force','Acceleration', title)
    
    # statsmodel lin reg
    X = sm.add_constant(x)
    model = sm.OLS(y,X)
    gradient, intercept = model.fit().params
    #ax.plot(x,y,'o')
    abline(intercept + intercept_offset,gradient+gradient_offset,style,linewidth)
    return    


def lab_expt_1():
  return lab_experiment_with_line(exptnum=1)
  
def lab_expt_2():
  return lab_experiment_with_line(0.6,0.2,0.1,'g',1,123456,2)  


def two_lab_experiments():
  lab_expt_1()
  lab_expt_2()
  return  
    
def linreg_example(x=None,y=None):
    z = 0.65*make_standard_normal(size=20)
    if x is None:
      x = np.linspace(0,5,20)
      y = 2*x + 0.5 + z
    
    X = sm.add_constant(x)
    model = sm.OLS(y,X)
    gradient, intercept = model.fit().params
  
    plt.plot(x,y,'o')
    abline(intercept,gradient,'r',linewidth=1)
    print "Intercept = %f" % (intercept)  
    print "Slope = %f"% (gradient)
    

def linreg_sm(x,y):
  X = sm.add_constant(x)
  model = sm.OLS(y,X)
  gradient, intercept = model.fit().params
  return (gradient, intercept)
    
############### Exploration ##############


def make_hist():
  plt.figure()
  loansmin = pd.read_csv('../datasets/loanf.csv')
  fico = loansmin['FICO.Score']
  p = fico.hist()


def make_boxplot():
  plt.figure()
  loansmin = pd.read_csv('../datasets/loanf.csv')
  p = loansmin.boxplot('Interest.Rate','FICO.Score')
  
  q = p.set_xticklabels(['640','','','','660','','','','680','','','','700',
  '720','','','','740','','','','760','','','','780','','','','800','','','','820','','','','840'])
  q0 = p.set_xlabel('FICO Score')
  q1 = p.set_ylabel('Interest Rate %')
  q2 = p.set_title('                          ')
  

############## Analysis ###############
"""
# this goes as full script in notebook
import pylab as pl
import numpy as np
#from sklearn import datasets, linear_model
import pandas as pd
import statsmodels.api as sm

# import the cleaned up dataset
df = pd.read_csv('../datasets/loanf.csv')

intrate = df['Interest.Rate']
loanamt = df['Loan.Amount']
fico = df['FICO.Score']

# reshape the data from a pandas Series to columns 
# the dependent variable
y = np.matrix(intrate).transpose()
# the independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# put the two columns together to create an input matrix 
# if we had n independent variables we would have n columns here
x = np.column_stack([x1,x2])

# create a linear model and fit it to the data
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

"""











############## Candidate code snippets below - we may need these in future iterations ###############


"""
from scipy import stats
>>> x = [5.05, 6.75, 3.21, 2.66]
>>> y = [1.65, 26.5, -5.93, 7.96]
>>> gradient, intercept, r_value, p_value, std_err = stats.linregress(x,y)
"""

"""

from numpy import arange,array,ones,linalg
from pylab import plot,show

xi = arange(0,9)
A = array([ xi, ones(9)])
# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
w = linalg.lstsq(A.T,y)[0] # obtaining the parameters

# plotting the line
line = w[0]*xi+w[1] # regression line
plot(xi,line,'r-',xi,y,'o')
show()

"""



"""
from numpy import arange,array,ones,linalg
from pylab import plot,show

xi = arange(0,9)
A = array([ xi, ones(9)])
# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
w = linalg.lstsq(A.T,y)[0] # obtaining the parameters

# plotting the line
line = w[0]*xi+w[1] # regression line
plot(xi,line,'r-',xi,y,'o')
show()
"""









    
    
    