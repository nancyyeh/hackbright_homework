"""Print out all the melons in our inventory."""


from melons import melons_dict


def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for melon, melon_vars in melons_dict.items():
    	print(melon.upper())
    	for melon_var, var in melon_vars.items():
    		print(f"    {melon_var}: {var}")

print_melon(melons_dict)
