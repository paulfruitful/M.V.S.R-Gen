import random
from colorama import Fore

print(""" *************************  ***********    *************************
         **************************              **********************************
         ***********************************************************************************      
         ***************************************************************************************
         *             **************  M.V.S.R  GENERATOR ************************   ****************
         ***********************************************************************************************  
         *                   ######## CODED BY PAUL FRUITFUL #############            ********************
         *                        /////  COLLAB WITH LORD CRYPTO HACKER//////        ***********************       
         *             *    CONTACT ME AT +2348114483062               #           ***************************
         *             ****************************                    #           ****************************
         *             *               ####### For Educational Purposes ########### ****************************
         *             *                                                     *************************************
         **********************************************************************************************************
         *             ******************************************************
##########################################################################################
###################################################################################################
               #################################################################
                     ##############################################

""")


options=[Fore.BLUE+"1. MasterCard",Fore.BLUE+"2. VisaCard",Fore.BLUE+"3. Recharge Card",Fore.BLUE+"4. SSN"]
print("""Choose one of the options
""")
print(f"""{options[0]}
""")
print(f"""{options[1]}
""")
print(f"""{options[2]}
""")
print(f"""{options[3]}
""")
user=input(Fore.LIGHTYELLOW_EX+'Choose one option:')

def generate_master():
    #Card number
    cardhead= random.randint(2000,2999)#for the card's beginning 
    cardbody=random.randint(1023,9999)#for the second four digits in the card number
    cardbody2=random.randint(2347,6789)
    cardend=random.randint(5555,9032)
    output=print(f"Card number:{cardhead}-{cardbody}-{cardbody2}-{cardend}") 
    #Random dates for the cards
    dateday=random.randint(1,31)
    dateyear=random.randint(1988,2025)
    output2=print(f'Date:{dateday}/{dateyear}')
    #Random dates for the cvv
    cvv=random.randint(111,999)
    output3= print(f'Cvv:{cvv}')
    print('CC info')
    print(f"""{output}
    {output2}
    {output3}
    """)
    return
if user=="1":
    for i in range(150):
        generate_master()

def generate_visa():
    #Card number
    cardhead= random.randint(4123,4999)#for the card's beginning 
    cardbody=random.randint(1023,9999)#for the second four digits in the card number
    cardbody2=random.randint(2347,6789)
    cardend=random.randint(5555,9032)
    output=print(f"Card number:{cardhead}-{cardbody}-{cardbody2}-{cardend}") 
    #Random dates for the cards
    dateday=random.randint(1,31)
    dateyear=random.randint(1988,2035)
    output2=print(f'Date:{dateday}/{dateyear}')
    #Random dates for the cvv
    cvv=random.randint(111,999)
    output3= print(f'Cvv:{cvv}')
    print('CC info')
    print(f"""{output}
    {output2}
    {output3}
    """)
    return
if user=="2":
    for i in range(150):
        generate_visa()
def rechargegen():
    recard1=random.randint(46564,49999)
    recard2=random.randint(75637,82289)
    result=print(f"#200 Glo Card: 40931-{recard1}-{recard2}")
    print(result)
    return

def ssngen():
    ssn1=random.randint(29,99)
    ssn2=random.randint(1111,9999)
    print(f'264-{ssn1}-{ssn2}')
    return

if user=="3":
    print("""
    Choose Recharge Card
    """)
    print("""1. Glo
    """)
    print(Fore.YELLOW+"""It is only Glo for now I will be bringing other networks later
    """)
    rechargecard=input(Fore.GREEN+"Choose option:")
    print(rechargecard)
    if rechargecard=="1":
        for i in range(101):
            rechargegen()

if user=="4":
    for i in range(101):
        ssngen()

