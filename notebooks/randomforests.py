# supporting lib for Random Forests
# Nitin Borwankar
# Open Data Science Training


map_dict = {'laying':1, 'sitting':2, 'standing':3, 'walk':4, 'walkup':5, 'walkdown':6} 

def remap_col(df,colname, mapping=None):
  """'mapping' is a dict sending old col elements to new ones, perhaps changing data types even.
      very useful for mapping factor columns from R to integer columns for Python
  """
  if not mapping:
    global map_dict
    mapping = map_dict.copy()
    
  df[colname] = df[colname].map(lambda x: mapping[x]) 
  return df

def intersect(a,b):
  """Intersect two lists"""
  return [val for val in a if val in b]

def errormeasures(orig, pred, activity):
  """docstring for errormeasures"""
  n = len(orig)
  origtrue = []
  origfalse = []
  predtrue = []
  predfalse = []
  
  for i in range(1,n+1):
    if(orig[i] == act):
      origtrue.append(i)          
    else: 
      origfalse.append(i)          

    if(pred[i] == act):
      predtrue.append(i)          
    else:
      predfalse.append(i)
      
      
  # compute the members of the quadrant
  truepos = len(intersect(origtrue, predtrue))
  trueneg = len(intersect(origfalse, predfalse))
  falsepos = len(intersect(origfalse, predtrue))
  falseneg = len(intersect(origtrue, predfalse))
      
                    
  # compute the 4 measures below
  #
  # PosPred:    Positive Predictive Value
  # NegPred:    Negative Predictive Value
  # Sens:       Sensitivity
  # Spec:       Specificity
    
  pospred = truepos/(truepos + falsepos)
  negpred = trueneg/(trueneg + falseneg)
  sens    = truepos/(truepos + falseneg)
  spec    = trueneg/(trueneg + falsepos)
  
  return [truepos,trueneg,falsepos,falseneg,pospred,negpred,sens,spec]
  
  
