def split_passwds(passwds_file):
    with open(passwds_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        username, passwd = line.split()
        level = username[6:]

        filename = f"{username}.txt"
        with open(filename, "w") as f:
            f.write(passwd)

split_passwds("passwds/bandit_pwds.txt")