from msilib.schema import Directory
import os
from time import time

# Using readlines()
file1 = open('tight end draft.txt', 'r')
file2 = open('te_allprodata.txt', 'r')
file3 = open('draft names_te.txt', 'r')
Lines = file1.readlines()
average_allpro = file2.readlines()
draft_names = file3.readlines() 
count = 0
combine_pffstats = []
allpro_combine = []
names = []


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
average_for_allpro = allpro_combine[10].split('\t')

for player in combine_pffstats:
    
    Combine_line = player.rstrip('\n').split('\t')

    if (Combine_line[0] == 'player'):
        continue

    
    if Combine_line[19] == '':
        off_grade = float(average_for_allpro[13])
    else:
        off_grade = float(Combine_line[19])
    
    #print(true_prgrade)
    
    if Combine_line[7] == '':
        rec_percent = float(average_for_allpro[14])
    else:
        rec_percent = float(Combine_line[7])
    
    #print(win_rate)

    if Combine_line[17] == '':
        drops_rate = float(average_for_allpro[16])
    else:
        drops_rate = float(Combine_line[17])
        
    if Combine_line[8] == '':
        ccr = float(average_for_allpro[18])
    else:
        ccr = float(Combine_line[8])

    if Combine_line[8] == '':
        pblk = float(average_for_allpro[17])
    else:
        pblk = float(Combine_line[8])

    float_avg13 = float(average_for_allpro[13])
    float_avg14 = float(average_for_allpro[14])
    float_avg16 = float(average_for_allpro[16])   
    float_avg17 = float(average_for_allpro[17])
    float_avg18 = float(average_for_allpro[18])
    
    
    
    pblk = float(Combine_line[33])
    

    

    if(
        (float_avg13 -8 <= off_grade <= float_avg13 +100)
       and ((float_avg14 -.00)  <= rec_percent <= (float_avg14+100.00))
       and ((float_avg16 -5) <= drops_rate <= (float_avg16 +100))
       #and ((float_avg17 -3) <= pblk <= (float_avg17 + 300))
       and ((float_avg18 -15) <= ccr <= (float_avg18 + 300))
       and (Combine_line[2] == 'TE')
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

 


for p in player_comparison:
    print(p)




      

with open('pff_stat_te.txt', 'w') as f:
    
    #f.write('player	player_id	position	team_name	player_game_count	batted_passes	declined_penalties	franchise_id	grades_pass_rush_defense	hits	hurries	pass_rush_opp	pass_rush_percent	pass_rush_win_rate	pass_rush_wins	penalties	prp	sacks	snap_counts_pass_play	snap_counts_pass_rush	total_pressures	true_pass_set_batted_passes	true_pass_set_grades_pass_rush_defense	true_pass_set_hits	true_pass_set_hurries	true_pass_set_pass_rush_opp	true_pass_set_pass_rush_percent	true_pass_set_pass_rush_win_rate	true_pass_set_pass_rush_wins	true_pass_set_prp	true_pass_set_sacks	true_pass_set_snap_counts_pass_play	true_pass_set_snap_counts_pass_rush	true_pass_set_total_pressures \n')
    f.write('player	player_id	position	team_name	player_game_count	avg_depth_of_target	avoided_tackles	caught_percent	contested_catch_rate	contested_receptions	contested_targets	declined_penalties	drop_rate	drops	first_downs	franchise_id	fumbles	grades_hands_drop	grades_hands_fumble	grades_offense	grades_pass_block	grades_pass_route	inline_rate	inline_snaps	interceptions	longest	pass_block_rate	pass_blocks	pass_plays	penalties	receptions	route_rate	routes	slot_rate	slot_snaps	targeted_qb_rating	targets	touchdowns	wide_rate	wide_snaps	yards	yards_after_catch	yards_after_catch_per_reception	yards_per_reception	yprr \n')
    for w in final_results:
        f.write(w)
        #f.write('\n')





        





