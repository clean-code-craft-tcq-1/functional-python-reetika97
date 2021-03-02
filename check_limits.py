
import sys  
Battery_range= [[0,45], [20,80], [-sys.maxsize,0.8]]

flag_range=[True, True, True]

def check_ranges(param,high,lo):
  if param>high:
    return 'H'
  elif param<lo:
    return 'L'
  else: 
    return True
  
def Alert_OOR(flags):
  if 'H' in flags or 'L' in flags:
    return False
  else: 
    return True
  
def Breached_param(flags):
  param=['temperature', 'soc', 'charge_rate']
  breach_report={'temperature':'Normal', 'soc':'Normal', 'charge_rate':'Normal'}
  for i in range(0,3):
    if flags[i]=='H':
      breach_report[param[i]]='High'
    else:
      breach_report[param[i]]='Low'
      
  print(breach_report)

def battery_is_ok(temperature, soc, charge_rate):
  param=[temperature, soc, charge_rate]
  flag_range=[True, True, True]
  for i in range(0,3):
    flag_range[i]=check_ranges(param[i],Battery_range[i][1],Battery_range[i][0])
  if Alert_OOR(flag_range)==False:
    Breached_param(flag_range)
  return (Alert_OOR(flag_range))

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
