import pandas as pd
import numpy as np
import math
from scipy.stats import norm


chat_id = 1004085803 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  alpha = 0.03
  p1 = x_success/x_cnt
  p2 = y_success/y_cnt
  z = (p1 - p2)/math.sqrt(p1*(1-p1)/x_cnt + p2*(1-p2)/y_cnt)
  z_alpha = abs(norm.ppf(alpha/2))
  if abs(z) > z_alpha:
    return True
  else:
    return False
