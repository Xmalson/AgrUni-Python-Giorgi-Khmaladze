def split_purchases():
    with open("data.txt", "r") as infile, \
         open("small.txt", "w") as small_file, \
         open("high.txt", "w") as high_file:

        for line in infile:
            line = line.strip()
            if not line:
                continue

            user, product, amount, price = line.split(",")

            amount = float(amount)
            price = float(price)

            total_value = amount * price

            if total_value < 10:
                small_file.write(line + "\n")
            else:
                high_file.write(line + "\n")


split_purchases()