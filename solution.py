import pandas as pd
import numpy as np


chat_id = 1004085803 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  if y_success/x_success > y_cnt/x_cnt:
    return True
  elif y_success/x_success <= y_cnt/x_cnt:
    return False
