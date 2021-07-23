def fileopener(inname, outname):
    with open(outname, 'w') as outfile, open(inname, 'r') as infile:
        for line in infile:
            a, b = line.split()
            outfile.write(str(int(a) + int(b)))
    return 0


if __name__ == '__main__':
    fileopener("input.txt", "output.txt")
