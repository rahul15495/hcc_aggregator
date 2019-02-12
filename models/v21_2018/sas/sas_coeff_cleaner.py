import os

base_dir = os.path.dirname(__file__)
fname_in = os.path.join(base_dir, "coeff_21.csv")
fname_out = os.path.join(base_dir, "coeff_21_cleaned.csv")

with open(fname_in, "rt") as infile:
    row1 = infile.readline()
    row2 = infile.readline()
    names = [x.strip() for x in row1.split(",")]
    values = [x.strip() for x in row2.split(",")]
    pairs = zip(names, values)

    with open(fname_out, "wt") as outfile:
        for pair in pairs:
            outfile.write(pair[0] + "," + pair[1] + "\n")

