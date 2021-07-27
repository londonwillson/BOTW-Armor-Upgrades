import numpy as np

def main():
  text =  np.loadtxt('BOTWupgrades.csv', dtype = str, delimiter = ',')

  item = text[:,0]
  number = text[:,1]

  list = np.empty((1,2), dtype=np.dtype('U100'))
  for i in range(len(item)):
      if i == 0:
          list [0,0] = item[0]
          list [0,1] = number[0]
      elif item[i] in list[:,0]:
          index = np.where(list[:,0] == item[i])[0]
          list[index,1] = str(float(list[index,1]) + float(number[i]))
      else:
          list = np.append(list,[[item[i],number[i]]], axis = 0)
  np.savetxt("BOTWUpgradeList.txt", list, delimiter=",", fmt = '%s,%s' )

main()