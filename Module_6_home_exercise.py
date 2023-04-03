import sys
import datetime
from datetime import date
#from datetime import datetime
from datetime import datetime as dt
import time
import os

def write_to_file(fn='',user_message_news='',user_message_ad='',user_message_joke='', user_Location_news='',ad_expiration_date='',meter_value='',res=''):
        with open(fn, 'a') as f:
            
                f.write("news--------------------\n" + user_message_news + "\n" + user_Location_news + "," + time.strftime("%d/%m/%Y %H.%M") )
                f.write("\n------------------------\n")
           
                f.write("Private ad---------\n" + user_message_ad + "\n"  + "Actual until: " + ad_expiration_date + "," + str(res) + " days left" )
                f.write("\n-------------------\n")
            
                f.write("Joke of the day ------------\n" + user_message_joke + "\n" + "Funny meter – " + meter_value + " of ten")
                f.write("\n-------------------\n")
                
                return      


def read_from_file(pattern):
    import re
    delimiter=':'
    # Open the file for reading
    with open(fn_input, 'r') as file:

        # Loop through each line in the file
        for line in file:

            # Use the search() function to search for a pattern at the beginning of the line
            if re.search(pattern, line):

                # If a match is found, print the line
                return line.split(delimiter)[1].strip()



# Below function handles the over all function for news , ad and joke based on the selection
def selection_logic():
    

        user_message_news=read_from_file('^news')
        user_Location_news=read_from_file('^Location')           
        user_message_ad = read_from_file('^Private')
        ad_expiration_date = read_from_file('^Actual')
        user_message_joke = read_from_file('^Jok')
        meter_value = read_from_file('^rating')
        now = datetime.datetime.now()
        date_string = now.strftime('%Y/%m/%d')
        
        res = (dt.strptime(ad_expiration_date, "%Y/%m/%d") - dt.strptime(date_string, "%Y/%m/%d")).days
        
        write_to_file(fn=fn,user_message_news=user_message_news,user_message_ad=user_message_ad,user_message_joke=user_message_joke,user_Location_news=user_Location_news,ad_expiration_date=ad_expiration_date,meter_value=meter_value,res=res)



        return 
   

fn = str(input('Please give the location of Output file'))

fn_input = str(input('Please give the location of input file'))


selection_logic()

os.remove(fn_input)

print("Output file is generated")
######################################################