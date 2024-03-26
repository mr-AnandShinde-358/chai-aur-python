order_size="Medium"
extra_shot=True

if extra_shot:
    coffee = order_size + " Coffee With an extra shot"
else:
    coffee = order_size + " coffee"

print("Order:",coffee)
