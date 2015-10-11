import csv
import os

#ROOT = '/cygdrive/c/Shourya/Research/Data/WDS/Files/'
#ifile  = open('/cygdrive/c/Shourya/Research/Data/WDS/test.csv', "rb")

# ROOT = '/cygdrive/c/Documents and Settings/q4815vqx/Documents/assisted_chat/shourya/files2/'
ifile  = open('/cygdrive/c/Documents and Settings/q4815vqx/Documents/assisted_chat/shourya/Interactions-Radioshack.csv', "rb")


#ifile  = open("Interactions-Radioshack.csv", "r")


#  this code breaks down the data into smaller parts


reader = csv.reader(ifile)


# dfs_filtered = reader[reader['"CLOSURE_TYPE"'] == "Customer Unavailable"]



rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
	notes_problem_id=row[1]
	action_type=row[14]
	action_transcript=row[36]
	problem_type=row[13]
	problem_subtype=row[12]
	closure_type = row[15]
	prob_resoln_type = row[16]
	print '%s %s' % (action_type, notes_problem_id)
#	print '%s' % action_transcript
	if not(os.path.exists(ROOT+action_type)):
		os.mkdir(ROOT+action_type)	
	f=open(ROOT+action_type+'/'+notes_problem_id+'.txt','w')
	f.write(notes_problem_id+':\n')
	f.write(problem_type+':'+problem_subtype+'\n')
	f.write(closure_type+':'+prob_resoln_type+'\n')
	f.write('----------------------------------'+'\n')
	
	f.write(action_transcript)
	f.close()
#        for col in row:
#           print '(%d) %-8s: %s' % (colnum, header[colnum], col)
#            colnum += 1
            
    rownum += 1

ifile.close()
