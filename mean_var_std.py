import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  arr = np.asarray(list)
  arr = arr.reshape((3,3))
  mean = [(arr.mean(axis = 0)).tolist(), (arr.mean(axis=1)).tolist(), (np.mean(arr.flatten())).tolist()]
  variance = [(arr.var(axis = 0)).tolist(),(arr.var(axis=1)).tolist(), (np.var(arr.flatten())).tolist()]
  std = [(arr.std(axis = 0)).tolist(), (arr.std(axis=1)).tolist(), (np.std(arr.flatten())).tolist()]
  max = [(arr.max(axis = 0)).tolist(), (arr.max(axis=1)).tolist(), (np.max(arr.flatten())).tolist()]
  min = [(arr.min(axis = 0)).tolist(), (arr.min(axis=1)).tolist(), (np.min(arr.flatten())).tolist()]
  sum = [(arr.sum(axis = 0)).tolist(), (arr.sum(axis=1)).tolist(), (np.sum(arr.flatten())).tolist()]

  calculations = {
    "mean":mean,
    "variance":variance,
    "standard deviation":std,
    "max":max,
    "min":min,
    "sum":sum}
  



  return calculations