def get_customer_incorrect(customer_name, customer_paid, melon_cost, number_of_melons):

	customer_expected = number_of_melons * melon_cost
	if customer_expected == customer_paid:
	    print(f"{customer_name} - paid ${customer_paid:.2f},",
	          f"expected ${customer_expected:.2f}"
	          )
	elif customer_expected > customer_paid:
	    print(f"{customer_name} UNDERPAIND - paid ${customer_paid:.2f},",
	          f"expected ${customer_expected:.2f}"
	          )
	elif customer_expected < customer_paid:
	    print(f"{customer_name} OVERPAID - paid ${customer_paid:.2f},",
	          f"expected ${customer_expected:.2f}"
	          )


order_log = open("customer-orders.txt")
for line in order_log:
	line = line.rstrip()
	words = line.split("|")

	customer_number = int(words[0])
	customer_name = words[1]
	number_of_melons = float(words[2])
	customer_paid = float(words[3])
	melon_cost = 1.00



	get_customer_incorrect(customer_name, customer_paid, melon_cost, number_of_melons)



order_log.close()
