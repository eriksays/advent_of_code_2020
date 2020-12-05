import pandas as pd
from pprint import pprint

def main(ruleset=1):
    #open expenses file and convert to list    
    password_file = pd.read_csv('password_file.csv', header=None, names=["passwords"])
    passwords = password_file["passwords"].to_list()
    pprint(passwords)

    good = []
    bad = []
    for pwd_line in passwords:
    
        #password line is formatted as such
        #6-7 m: mlmrrmm
        #split the line by :
        #[0] is the rule line
        #[1] is the password
        pwd_arr = pwd_line.split(":")
        #and get the formatting rules
        pwd_rules_arr = pwd_arr[0].split(" ")
        #and get minimum and maximum values
        pwd_rules_min = pwd_rules_arr[0].split("-")[0]
        pwd_rules_max = pwd_rules_arr[0].split("-")[1]
        pwd_rules_letter = pwd_rules_arr[1]
        pwd = pwd_arr[1]
        if ruleset == 1:
            
            print(f"The password is {pwd} and must contain a minimum of {pwd_rules_min} and maximum of {pwd_rules_max} instances of the letter {pwd_rules_letter}")
            char_count = pwd.count(pwd_rules_letter)
            print(f"The password: {pwd} contains {char_count} instances of the letter {pwd_rules_letter}")
            if char_count >= int(pwd_rules_min) and char_count <= int(pwd_rules_max):
                print(f"The password is good")
                good.append(pwd)
            else:
                print("The password is not good")
                bad.append(pwd)
        else:
            #ruleset 2
            print(f"The password is {pwd} and the {pwd_rules_min} character must contain {pwd_rules_letter} and the {pwd_rules_max} character must not contain {pwd_rules_letter}")
            start_char = pwd[int(pwd_rules_min)]
            last_char =  pwd[int(pwd_rules_max)]
            print(f"The {pwd_rules_min} is {start_char} and the {pwd_rules_max} is {last_char}")

            #print(f"The {pwd_rules_min} character = {pwd[{pwd_rules_min}]}")
            if start_char == pwd_rules_letter and last_char == pwd_rules_letter:

                print(f"The password is bad")
                #input('example')
                bad.append(pwd)
            elif start_char == pwd_rules_letter or last_char == pwd_rules_letter:
                print("The password is good")
                #input('example')
                good.append(pwd)
            else:
                print("The password is not good")
                #input('example')
                bad.append(pwd)
            

    print("# of good password:{}".format(len(good)))
    print("# of bad password:{}".format(len(bad)))
    

        #print(pwd)
        # for the rules, 
        # the password [pwd] must contain at least a minumum of line [6-7] [m]

  


if __name__ == "__main__":
    #if we're only adding two numbers, leave main() blank, 
    #else, add in 3 for a third loop
    main(2)