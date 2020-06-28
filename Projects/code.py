# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

#concatenating a new record to a existing array file
census = np.concatenate((data, new_record))

#filtering the age column
age = census[:,0]

#statistics of age determination to visualize the major groups of people
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

#filtering the race column
race = census[:,2]

#filtering the different types of races
race_0, race_1, race_2, race_3, race_4 = race[race==0], race[race==1], race[race==2], race[race==3], race[race==4] 

#determining the number of people in each races
[len_0, len_1, len_2, len_3, len_4] = [len(race_0), len(race_1), len(race_2), len(race_3), len(race_4)]

l = [len_0, len_1, len_2, len_3, len_4]

#finding out the minority race
minority_race = l.index(min(l))
print('Race ',minority_race)

#filtering the senior citizens
senior_citizens = census[age>60]

#total working hours
working_hours_sum = np.sum(senior_citizens[:,6])
print(working_hours_sum)

#number of senior citizens
senior_citizens_len = len(senior_citizens)

#average working hour of one senior citizen
avg_working_hours = round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)

#filtering number of education had 
education_num = census[:,1]

#filtering the highly and poorly educated people
high = census[education_num>10,:]
low = census[education_num<=10,:]

#finding out the average income
avg_pay_high = round(np.mean(high[:,7]),2)
avg_pay_low = round(np.mean(low[:,7]),2)
print(avg_pay_high,avg_pay_low)

#justifying whether education plays a role in income
if avg_pay_high>avg_pay_low:
    print('Better education leads to higher income')
else:
    print('Education does\'nt matter to get a higher pay')



