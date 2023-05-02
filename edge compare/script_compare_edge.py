from msilib.schema import Directory
import os
from time import time

# Using readlines()
file1 = open('edge combine results.txt', 'r')
file2 = open('edge all pro.txt', 'r')
Lines = file1.readlines()
average_allpro = file2.readlines()
  
count = 0
Combine_results = []
allpro_combine = []


# Strips the newline character
for line in Lines:
    Combine_results.append(line)

for line2 in average_allpro:
    allpro_combine.append(line2)

#for i in Combine_results:
#    print(i)

#print(len(Combine_results))
    

average_for_allpro = []
Combine_line = []
player_comparison = []
ideal_traits = []
#Combine_line = Combine_results[2].split('\t')
#print(average_allpro)

average_for_allpro = allpro_combine[9].split('\t')
#print(average_for_allpro[9])
for player in Combine_results:
    Combine_line = player.rstrip('\n').split('\t')

    #print(Combine_line)

    
    if (Combine_line[0] == 'Name' or Combine_line[0] == "Column1"):
        continue

    height = round(int(Combine_line[3]), -1) 
    arm_length = float(Combine_line[6]) / 100
    

        
    if Combine_line[14] == '':
        broad_jump = 10.385
    elif (Combine_line[14] == '--'):
        broad_jump = 10.385
    else:
        broad_jump = (float(Combine_line[14])) /100
        

    
    if Combine_line[9] == '':
        yd_dash = 4.624
    elif (Combine_line[9] == '--'):
        yd_dash = 4.624
    else:
        yd_dash = (float(Combine_line[9]))

    #if Combine_line[9] == '':
    #    yd_dash = 4.4275
    #else:
        #r = Combine_line[13] %
    #    yd_dash = (float(Combine_line[9]))


    
    
    if Combine_line[13] =='':
        vert = 36.375
    elif(Combine_line[13] == '--'):
        vert = 36.375
    else:    
        vert = float(Combine_line[13]) 
    
    if Combine_line[11] == '--' or ' ':
        three_cone = 6.9767
    else:
        #r = Combine_line[13] %
        three_cone = float(Combine_line[11]) 

    if Combine_line[8] == '':
        yd_10 = 1.578
    elif(Combine_line[8]== '--'):
        yd_10 = 1.578
    else:
        yd_10 = float(Combine_line[8]) 
    
    if Combine_line[10] == '':
        bench_press = 23.5
    elif(Combine_line[10]== '--'):
        bench_press = 23.5
    else:
        bench_press = float(Combine_line[10]) 
    
    
    hand = float(Combine_line[5])/100

    #print(bench_press)
    
    
    
    int_avg1 = int(average_for_allpro[1])
    int_avg2 = int(average_for_allpro[2])
    float_avg3 = float(average_for_allpro[3])
    float_avg4 = float(average_for_allpro[4])
    float_avg5 = float(average_for_allpro[5])
    float_avg6 = float(average_for_allpro[6])
    float_avg7 = 10.385
    float_avg8 = float(average_for_allpro[8])
    float_avg11 = float(average_for_allpro[11])
    float_avg12 = float(average_for_allpro[12])
    
    
    weight = int(Combine_line[4])
    #print(type(int_avg1))
    #print(type(height))
    #print()
    #print(float_avg7)
    #print(broad_jump)
    print(weight)
    if(
        (int_avg1 -889 <= height <= int_avg1+100)
       and ((int_avg2 -15.00)  <= weight <= (int_avg2+25.00))
       and ((float_avg3 -2) <= arm_length <= (float_avg3 + 3))
       and ((float_avg4 - 1.5) <= hand <= (float_avg4+2.0))
       and ((float_avg5 -1) <= yd_dash <= (float_avg5+.05))
       and ((float_avg6 - 3.0) <= vert <= (float_avg6+10.0))
       and ((float_avg7 - .8) <= broad_jump <= (float_avg7+3.0))
       and ((float_avg8 -.05) <= three_cone <=(float_avg8+1))
       and ((float_avg12 -1 ) <= yd_10 <=(float_avg12 +.05))
       and ((float_avg11 - 5) <= bench_press <=(float_avg11 + 20))
       ):
        player_comparison.append(player)
        
    

for i in player_comparison:
    print(i)

print(len(player_comparison))




    
