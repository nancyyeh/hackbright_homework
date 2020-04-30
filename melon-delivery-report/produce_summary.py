def print_delivered_details(day, file):

    print("Day", day)

    delivery_log = open(file)
    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {melon} {count}s for total of ${amount}")
    
    delivery_log.close()

day1_file = "um-deliveries-20140519.txt"
day2_file = "um-deliveries-20140520.txt"
day3_file = "um-deliveries-20140521.txt"

print_delivered_details(1, day1_file)
print_delivered_details(2, day2_file)
print_delivered_details(3, day3_file)