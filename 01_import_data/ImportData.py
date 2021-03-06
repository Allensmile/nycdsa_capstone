from ParseJSON import *


# Switch to directory of file you wish to import
import os
os.getcwd()
dir_path = './01_External/01_Yelp/'
dir_path = '../01_External/01_Yelp/'
dir_path = '../../01_External/01_Yelp/'
os.chdir(dir_path)


# Import data
bus = ParseJSON(fileName=dir_path+'yelp_academic_dataset_business.json')
chk = ParseJSON(fileName=dir_path+'yelp_academic_dataset_checkin.json')
rev = ParseJSON(fileName=dir_path+'yelp_academic_dataset_review.json')
tip = ParseJSON(fileName=dir_path+'yelp_academic_dataset_tip.json')
usr = ParseJSON(fileName=dir_path+'yelp_academic_dataset_user.json')

# Extract three levels deep
attr = ProcessID(bus, 'attributes')
type = ProcessID(bus, 'type')
cat = ProcessID(bus, 'cat')
amb = ProcessID(attr, 'Ambience')
casual = ProcessID(amb, 'casual')
