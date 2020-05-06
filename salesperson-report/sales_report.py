"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
#create list of salespeople and melon sold

f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople: 
    #if saleperson is in salespeople list
        position = salespeople.index(salesperson) 
        #get the position of the salespeson in the salespeople list

        melons_sold[position] += melons
        #add the melon amont in the correspond melon_sold list position
    else:
        #else add person in salespeople list and add the melons sold in another list
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    #for each index in the salespeople list, print out the salespeople list and and melons sold from the two list


#dictionary will be a better way to organize this
