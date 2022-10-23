# read result.csv and store it in a list of json
import csv
import random
import time

print('''
                            ░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒░░▒▒░░░░▒▒░░                            
                      ░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓░░░░░░▒▒▒▒░░░░░░▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░░░░░░░                        
                  ░░▒▒░░░░░░░░▒▒▓▓▒▒▒▒▒▒▓▓▒▒░░░░▒▒██▓▓▓▓░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒░░░░░░░░▒▒                    
                ▒▒▓▓▓▓▒▒▓▓▓▓▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░                
            ░░▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒░░▒▒▓▓▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓▒▒░░▒▒              
          ░░▒▒▒▒░░░░░░▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░██▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒░░░░▒▒░░░░░░░░            
        ░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░        
      ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓██▒▒▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒░░░░░░░░░░░░        
    ░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓██▒▒▓▓▓▓██▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓░░░░░░░░░░░░░░░░      
    ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒░░▒▒▒▒██▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░    
  ░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░    
  ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓██▓▓▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░  
  ░░▒▒░░░░░░░░░░░░░░░░░░██▓▓▒▒░░▒▒▒▒▓▓▒▒░░░░░░░░░░░░▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒░░▒▒▓▓▓▓░░██▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▒▒░░▓▓░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓░░░░░░░░▓▓░░░░▒▒▓▓██▒▒▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░  
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▒▒▓▓▒▒▒▒▓▓▒▒▒▒░░░░▒▒▒▒▒▒▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒░░░░░░▒▒▓▓▒▒▒▒▓▓░░░░░░░░░░░░░░▒▒░░░░░░  
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░▒▒▒▒▒▒▓▓▓▓████▓▓▓▓▓▓▓▓▓▓░░░░▒▒▒▒░░▓▓▒▒░░▓▓░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░▒▒░░░░░░▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓░░▒▒░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒██▓▓▒▒▒▒░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░░░  
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░  
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓██▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░░░░░▒▒▓▓▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░░░  
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░▒▒▓▓▒▒▓▓░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒▓▓████████▓▓░░░░░░░░░░░░░░  
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░██▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░    
    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▓▓░░░░▒▒░░░░░░░░    
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒▒▒░░░░      
      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░          
          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░            
            ░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒              
                ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░                
                  ░░░░░░░░░░░░▒▒░░░░▒▒░░░░▒▒░░▒▒░░░░░░░░░░      ░░  ░░                              ░░░░░░▒▒                    
                      ░░░░░░░░            ░░░░░░  ░░░░░░                                        ░░░░░░░░                        
                            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                            

''')

with open('/home/ctf/result.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)

correct = 0
wrong = 0

for i in range(50):
    print(f"Question {i+1}/50. Currently {correct} correct and {wrong} wrong.")
    # randomly select a row from result
    row = random.choice(result[1:])
    ip, city, lat, lon = row
    # randomly decide if we query as ip or lat/lon
    time_start = time.time()
    if random.randint(0, 1):
        print('IP:', ip)
        res = input('City: ')
        if time.time() - time_start > 1:
            print("Too slow!")
            wrong += 1
        elif res.lower().strip() != city:
            print("Wrong.")
            wrong += 1
        else:
            print("Correct!")
            correct += 1
    else:
        print(f'Coordinate (lat, lon): {lat}, {lon}')
        res = input('City: ')
        if time.time() - time_start > 1:
            print("Too slow!")
            wrong += 1
        elif res.lower().strip() != city:
            print("Wrong.")
            wrong += 1
        else:
            print("Correct!")
            correct += 1
    if wrong >= 25:
        print("You lost!")
        exit(0)

if correct >= 25:
    print("Congrats! Here is your flag: cvctf{4r3_y0u_4_R34L_Ge@r41nB0L7?}")