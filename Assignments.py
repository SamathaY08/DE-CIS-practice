#!/usr/bin/env python
# coding: utf-8

# ### Write a program to print full names from two lists, one containing first names and second containing last names

# In[1]:


firstname=["Samatha","Mouni","Vignesh"]
lastname=["Yeddula","Yerra","Ravichandran"]
Fullname=[]
if len(firstname)==len(lastname):
    for i in range(len(firstname)):
        Fullname.insert(1,(firstname[i]+" "+lastname[i]))
    print(Fullname)
elif len(firstname)>len(lastname):
    print("Missing Lastnames")
else:
    print("Missing Firstnames")


# ### Write a program to print previous month, previous quarter, future month, and current quarter in form of list

# In[2]:


def getfuturemonth(y,mm):
    if mm==1:
        Previousmonth =12
        future_mon=str(y+1)+str(Previousmonth)
        return future_mon
    elif mm<=10:
        Previousmonth=mm-1
        future_mon=str(y+1)+'0'+str(Previousmonth)
        return future_mon
    else:
        Previousmonth=mm-1
        future_mon=str(y+1)+str(Previousmonth)
        return future_mon
    
def getpreviousmonth(y,mm):
    if mm==1:
        Previousmonth =12
        prev_mon=str(y-1)+str(Previousmonth)
        return prev_mon
    elif mm<=10:
        Previousmonth=mm-1
        prev_mon=str(y)+'0'+str(Previousmonth)
        return prev_mon
    else:
        Previousmonth=mm-1
        prev_mon=str(y)+str(Previousmonth)
        return prev_mon

def currentquarter(Q,y):
    currentquarter=Q+'_'+str(y)
    return currentquarter
    

def getpreviousquarter(Q,y):
    q=int(Q[1])
    if q in range(2,5):
        prevquanum= q-1
        previousquarter='Q'+str(prevquanum)+'_'+str(y)
        return previousquarter
    else:
        prevquanum=4
        previousquarter='Q'+str(prevquanum)+'_'+str(y-1)
        return previousquarter
    
def example(currdate,q):
    n=len(currdate)
    mm=int(currdate[n-2:])
    y=int(currdate[:n-2])
    Q=q
    prev_month=getpreviousmonth(y,mm)
    future_mon=getfuturemonth(y,mm)
    curr_quarter=currentquarter(Q,y)
    prev_quater=getpreviousquarter(Q,y)
    

    dict1=dict({'prev_month':prev_month,'future_month':future_mon,'current Quarter':curr_quarter,'previous_quater':prev_quater})
    return dict1
def main():
    curr_date=input()
    quater=input()
    print(example(curr_date,quater))

main()


# In[3]:


main()


# In[4]:


main()

