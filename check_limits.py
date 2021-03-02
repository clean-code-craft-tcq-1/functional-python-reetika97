
import sys  
Battery_range= [[0,45], [20,80], [-sys.maxsize,0.8]]

flag_range=[True, True, True]

#Check For parameters within Range
def check_ranges(param,high,lo):
  if param>high:
    return 'High'
  elif param<lo:
    return 'Low'
  else: 
    return 'Normal'

#Alert for deviations
def Alert_OOR(flags):
  if 'High' in flags or 'Low' in flags:
    return False
  else: 
    return True
  
#Breach Report for Functions
def Breached_param(flags):
  param=['temperature', 'soc', 'charge_rate']
  breach_report={'temperature':'Normal', 'soc':'Normal', 'charge_rate':'Normal'}
  for i in range(0,3):
         breach_report[param[i]]=flags[i]
      
  print(breach_report)
  return breach_report

def battery_is_ok(temperature, soc, charge_rate):
  param=[temperature, soc, charge_rate]
  breach_report={'temperature':'Normal', 'soc':'Normal', 'charge_rate':'Normal'}
  flag_range=[True, True, True]
  for i in range(0,3):
    flag_range[i]=check_ranges(param[i],Battery_range[i][1],Battery_range[i][0])
  if Alert_OOR(flag_range)==False:
    breach_report=Breached_param(flag_range)
  return (Alert_OOR(flag_range))

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert((Breached_param(['Normal','High','Low'])=={'temperature':'Normal', 'soc':'High', 'charge_rate':'Low'}) is True)
  #assert((Breached_param(True,True,True)=={'temperature':'Normal', 'soc':'Normal', 'charge_rate':'Normal'}) is True)
