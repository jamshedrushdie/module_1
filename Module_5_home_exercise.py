import sys
import datetime
from datetime import date
#from datetime import datetime
from datetime import datetime as dt
import time
import os

fn = input('Please give the location of Output file')   #'C:\\Users\\Jamshed_Rushdie\\Documents\\Output.txt'

# Below function handles the over all function for news , ad and joke based on the selection
def selection_logic(selection='news'):
    user_message='' 
    user_Location_news = ''
    ad_expiration_date = ''
    message='Please enter the text'
    message_loc ='Please enter the location'
    Expiration_date = 'Please enter the Expiry date in YYYY/MM/DD format'
    funny_meter = 'Please enter the rating'
    if selection == 'news':
        user_message = input(message)
        user_Location_news = input(message_loc)
        

        
        # Below block prints the news to file in the required format
        
        if os.path.exists(fn):
            #fh = open(fn, "r")
            with open(fn, 'a') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print("news--------------------\n" + user_message + "\n" + user_Location_news + "," + time.strftime("%d/%m/%Y %H.%M") )
                print("------------------------")
                fn.close()
        else:
            #fh = open(fn, "w")
            with open(fn, 'w') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print("news--------------------\n" + user_message + "\n" + user_Location_news + "," + time.strftime("%d/%m/%Y %H.%M") )
                print("------------------------")
                fn.close()
            
     # Below block prints the ad to file in the required format
    
    elif selection == "ad":
        user_message = input(message)
        ad_expiration_date = input(Expiration_date)
        now = datetime.datetime.now()
        date_string = now.strftime('%Y/%m/%d')
        
        res = (dt.strptime(ad_expiration_date, "%Y/%m/%d") - dt.strptime(date_string, "%Y/%m/%d")).days
        if os.path.exists(fn):
            #fh = open(fn, "r")
            with open(fn, 'a') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print("Private ad---------\n" + user_message + "\n"  + "Actual until: " + ad_expiration_date + "," + str(res) + " days left" )
                print("-------------------")
                fn.close()
        else:
            #fh = open(fn, "w")
            with open(fn, 'w') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print("Private ad---------\n" + user_message + "\n"  + "Actual until: " + ad_expiration_date + "," + str(res) + " days left" )
                print("-------------------")
                fn.close()

      # Below block prints the joke to file in the required format
    
    elif selection == "joke":
        user_message = input(message)
        meter_value = input(funny_meter)
        if os.path.exists(fn):
            #fh = open(fn, "r")
            with open(fn, 'a') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print("Joke of the day ------------\n" + user_message + "\n" + "Funny meter – " + meter_value + " of ten")
                print("-------------------")
                fn.close()
        else:
            #fh = open(fn, "w")
            with open(fn, 'w') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print("Joke of the day ------------\n" + user_message + "\n" + "Funny meter – " + meter_value + " of ten")
                print("-------------------")
                fn.close()

    return selection
   

#below block gives the user to choose options : news , ad or joke    
options = ['news', 'ad', 'joke']
user_input = ''
input_message = "Pick an option:\n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'

input_message += 'Your choice: '


while user_input.lower() not in options:
    user_input = input(input_message)
    #print('You picked: ' + user_input)
    myselection=selection_logic(user_input)
    user_input=''
    if myselection not in options: 
        break
######################################################