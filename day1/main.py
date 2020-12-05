import pandas as pd


def main(sums=2):
    #open expenses file and convert to list    
    expense_file = pd.read_csv('expenses.csv', header=None, names=["expenses"])
    expenses = expense_file["expenses"].to_list()

    #set our matching sum 
    sum = 2020

    #start the first loop
    for x in expenses:
        #and check against each other number
        for y in expenses:
            if sums == 2:
                if int(x) + int(y) == sum:
                    print("x:{} + y: {} = {}".format(x,y,sum))
                    print("final answer: {}".format(x*y))
                    exit()
            else:
                for z in expenses:
                   if int(x) + int(y) + int(z) == sum:
                    print("x:{} + y:{} + z:{} = {}".format(x,y,z,sum))
                    print("final answer: {}".format(x*y*z))
                    exit() 


if __name__ == "__main__":
    #if we're only adding two numbers, leave main() blank, 
    #else, add in 3 for a third loop
    main(3)