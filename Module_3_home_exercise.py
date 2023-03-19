mytext="""tHis iz your homeWork, copy these Text to variable.tHis iz your homeWork, copy these Text to variable.


You NEED TO normalize it fROM letter CASEs point OF View. also, create one MORE senTENCE witH LAST 
WoRDS of each existlNG SENtence and add it to the END OF this Paragraph.


it iZ misspeLLing here. fix"iZ" with correct "is", but ONLY when it Iz a mistAKE.


last izTO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL 
whitespaces. I got 87."""


# In[2]:


#print(mytext)


# In[3]:


mylist=list(mytext.split('\n\n\n')) # Slpit the paragraphs using \n\n\n


# In[4]:


mylist[0]=mylist[0].capitalize().replace('iz','is') # replace iz with is


# In[5]:


mylist[1]='. '.join([(x.capitalize().replace('existlng','existing')) for x in mylist[1].split('. ')]) # split the sencond paragraph on ". " then capitalize the sentence and also replace existlng with existing , then join back the sentences


# In[6]:


mylist[2]='. '.join([(x.replace('x"iZ','x "iz').capitalize().replace(' iz ',' is ')) for x in mylist[2].split('. ')]) # split the sencond paragraph on ". " then capitalize the sentence and also replace iz with existing is  and normalize x"iZ' with 'x "iz' , then join back the sentences



# In[7]:


mylist[3]='. '.join([(x.capitalize().replace('iz','is ').replace('tex','text')
              .replace('Carefull','Careful')) for x in mylist[3].split('. ')]) # split the 3rd paragraph on ". " then capitalize the sentence and also replace tex with text and Carefull with Careful , then join back the sentences



# In[8]:


appendlist=[x.split(" ")[-1] for x in list(mytext.replace('\n','').lower().split('.'))[:-1]] # create a list with last word of each sentences by first creating a list by splitting with "." and then agin splitting the items in the list with " " and getting the last value. :-1 is to remove a addition Blank which comes during the initial spilitting by "."


# In[9]:


appendlist


# In[10]:


mylist.append(' '.join([x for x in appendlist]).capitalize().replace('tex','text')+'.') # append the above list 


# In[11]:


finaltext='\n'.join([x for x in mylist]) # join all the paragraphs with only one line spacing


# In[12]:


print(finaltext)


# In[13]:


#count all whitespaces
finaltext.replace('\n',' ').count(' ')   # white spaces will be 87 + the number of white spaces in the new sentence created with last words of each sentences


# In[ ]: