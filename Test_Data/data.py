# data of magnus project
import random
class magnus_data:
    url="https://magnus.jalatechnologies.com/"
    char=["sri","ram","arun","pavan","mani","karun"]
    char1="qwqewqasdmasmdsamdska"
    namee=random.choice(char)
    first_name=namee
    initial=random.choice(char1)
    last_name=initial
    email_id=namee+initial+"@gmail.com"

    # to generate random mobile number
    ph_no=[]
    # 1st number should be in the range of 6 to 9
    ph_no.append(random.randint(6,10))
    #loop is used to use other 9 digits
    # others should be in the range of 0 to 10
    for i in range(1,10):
        ph_no.append(random.randint(0,9))
    mobile_number=""
    for i in ph_no:
        mobile_number=mobile_number+str(i)
    # date of birth generator
    dob=str(random.randint(10,30))+"/"+str(random.randint(1,12))+"/"+str(random.randint(1950,2050))
    loc=["krishnagiri","coimbatore","ooty","chennai","bangalore","salem","hosur","vellore","ambur"]
    loc1=["tamil nadu","karnataka","kerala","maharastra","goa","delhi","kolkata","mumbai"]
    address=str(random.randint(1,10))+"/"+str(random.randint(100,999))+" "+random.choice(loc)+" "+random.choice(loc1)+" "+str(random.randint(600000,699999))+mobile_number
