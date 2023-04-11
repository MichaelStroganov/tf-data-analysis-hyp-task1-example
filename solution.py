import pandas as pd
import numpy as np
import math


chat_id = 1004085803 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  alpha = 0.03
  p1 = y_success/x_success
  p2 = y_cnt/x_cnt
  z = (p1 - p2) / math.sqrt(p1*(1-p1)/x_success + p2*(1-p2)/y_success)
  z_alpha = abs(norm.ppf(alpha/2))
  if abs(z) > z_alpha:
    return False
  else:
    return True
