from msilib.schema import Directory
import os
from time import time

# Using readlines()
file1 = open('pass rush draft.txt', 'r')
file2 = open('edge All Pro Bank pff.txt', 'r')
file3 = open('draft names.txt', 'r')
Lines = file1.readlines()
average_allpro = file2.readlines()
draft_names = file3.readlines() 
count = 0
combine_pffstats = []
allpro_combine = []
names = []

#print(len(player_comparison))

# Strips the newline character
for line in Lines:
    combine_pffstats.append(line)

for line2 in average_allpro:
    allpro_combine.append(line2)

for line3 in draft_names:
    names.append(line3)

average_for_allpro = []
Combine_line = []
player_comparison = []
ideal_traits = []
average_for_allpro = allpro_combine[9].split('\t')

for player in combine_pffstats:
    
    Combine_line = player.rstrip('\n').split('\t')

    if (Combine_line[0] == 'player'):
        continue

    
    if Combine_line[22] == '':
        true_prgrade = float(average_for_allpro[13])
    else:
        true_prgrade = float(Combine_line[22])
    
    #print(true_prgrade)
    
    if Combine_line[27] == '':
        win_rate = float(average_for_allpro[14])
    else:
        win_rate = float(Combine_line[27])
    
    #print(win_rate)

    if Combine_line[29] == '':
        prp = float(average_for_allpro[17])
    else:
        prp = float(Combine_line[29])

    float_avg13 = float(average_for_allpro[13])
    float_avg14 = float(average_for_allpro[14])
    float_avg16 = float(average_for_allpro[16])   
    float_avg17 = float(average_for_allpro[17])
    
    
    
    Total_pressures = float(Combine_line[33])
    

    

    if(
        (float_avg13 -5 <= true_prgrade <= float_avg13 +10)
       and ((float_avg14 -5.00)  <= win_rate <= (float_avg14+25.00))
       and ((float_avg16 -5) <= Total_pressures <= (float_avg16 + 300))
       and ((float_avg17 -3) <= prp <= (float_avg17 + 300))
       and (Combine_line[2] == 'ED')
       ):
        player_comparison.append(player)
    
    


#for j in names:
    #for i in player_comparison:
        #named = i.split('\t')
        #if j == named[0]:
            #player_comparison.remove(i)


final_results = []
for i in player_comparison:
    named = i.rstrip('\n').split('\t')
    for n in names:
        na = n.rstrip('\n')
        if named[0] == na:
            final_results.append(i)

 







      

with open('pff_stats.txt', 'w') as f:
    f.write('player	player_id	position	team_name	player_game_count	batted_passes	declined_penalties	franchise_id	grades_pass_rush_defense	hits	hurries	pass_rush_opp	pass_rush_percent	pass_rush_win_rate	pass_rush_wins	penalties	prp	sacks	snap_counts_pass_play	snap_counts_pass_rush	total_pressures	true_pass_set_batted_passes	true_pass_set_grades_pass_rush_defense	true_pass_set_hits	true_pass_set_hurries	true_pass_set_pass_rush_opp	true_pass_set_pass_rush_percent	true_pass_set_pass_rush_win_rate	true_pass_set_pass_rush_wins	true_pass_set_prp	true_pass_set_sacks	true_pass_set_snap_counts_pass_play	true_pass_set_snap_counts_pass_rush	true_pass_set_total_pressures \n')
    for w in final_results:
        f.write(w)
        f.write('\n')





        





