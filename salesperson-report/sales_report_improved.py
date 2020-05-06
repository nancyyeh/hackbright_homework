"""Generate sales report showing total melons each salesperson sold."""


def melons_person_sales(filename):
    file = open(filename)

    melon_sales = {}

    for line in file:
        line = line.rstrip()
        salesperson, total_value, melons_sold = line.split('|')

        melon_sales[salesperson] = melon_sales.get(salesperson, 0) + int(melons_sold)


    for salesperson, melons in melon_sales.items():
        print(f"{salesperson} has sold {melons} melons" )

melons_person_sales('sales-report.txt')