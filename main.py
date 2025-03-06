from methods import get_data
from database import doctors
import argparse

parser = argparse.ArgumentParser(description='Find the the doctor Details from www.andalusiahealth.com')
parser.add_argument('--city',metavar='year',help='Enter the city in a string',type=str)

args = parser.parse_args()

data = get_data(args.city)

result = []
for d in data['providers']:
    info = {}
    if type(d['middleName'])==str and d['middleName'] != '':
        middle_name = d['middleName']+' '
    else:
        middle_name = ''  
    info['full_name'] = d['firstName']+' '+middle_name+d['lastName']
    info['address'] = str(d['address1'])+' '+str(d['address2'])+' '+str(d['city'])+' '+str(d['state'])+' '+str(d['zip'])
    info['phone_number'] = d['officePhoneNumber']
    
    if len(d['locations']['locations'])>1:
        info['has_multiple_locations'] = True
    else:
        info['has_multiple_locations'] = False
    info['accepting_new_patients'] = d['acceptingNewPatients']
    if d['employmentType'] == 'Independent':
        info['employed_provider'] = False
    else:
        info['employed_provider'] = True
    result.append(info)

doctors.insert_many(result)
