import pandas as pd


def main():
    #open expenses file and convert to list    
    expense_file = pd.read_csv('expenses.csv', header=None, names=["expenses"])
    expenses = expense_file["expenses"].to_list()

    #set our matching sum 
    sum = 2020

    #start the first loop
    for x in expenses:
        #and check against each other number
        for y in expenses:

            if int(x) + int(y) == sum:
                print("x:{} + y: {} = {}".format(x,y,sum))
                print("final answer: {}".format(x*y))
                exit()


if __name__ == "__main__":
    main()