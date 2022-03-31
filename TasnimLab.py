def Full_Name(First,M,Last):
        print(f"Hello {First.strip().capitalize()} {M.upper():.1s} {Last.capitalize()}")



def Personal_info(name,age="unknown" , country="unknown", profession="unknown"):
    print(f"Hello {name} your age is {age} you are from {country} you are {profession}")



def Skills_progress(name,*skills,**skillswithprogress):
    print(f"Hello {name},\n your skills are:")
    for skill in skills:
        print(f"-{skill}")
    print(f"your skills with progress are:")
    for key,value in skillswithprogress.items():
        print(f"-{key}={value}")
        
        
def cleanword(word):
    if len(word)==1:
        return word
    if word[0]==word[1]:
        return cleanword(word[1:])
    return word[0]+cleanword(word[1:])


def BookMark(MyBM):
    MyBM = [] 
    Max=4 
    while Max>0:
        web= input("add your website without https://") #input the websites
        MyBM.append(f"http://{web.strip().lower()}") #add new website
        Max-=1 #decrese one place frome allowed places
        print(f"website is added,{Max}places left")#the N.O lefted places
        print(MyBM)
    else:
        print("BookMark is full you can not add any website")
    if len(MyBM)>0: #check if the list is full
        MyBM.sort()
        i=0
        print("printing the list of your Bookmarke")
        while i< len(MyBM):
            print(MyBM[i])
            i+=1
        