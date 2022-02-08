import argparse

parser = argparse.ArgumentParser(description="Example Python CLI")

parser.add_argument("hacker_name", help="Enter the hacker name", type=str)
parser.add_argument("hacker_power", help="Enter the hacker power", type=int)

parser.add_argument("-bh", "--blackhat", default=False, action="store_true")
parser.add_argument("-wh", "--whitehat", default=False, action="store_true")

parser.add_argument("-ht", "--hackertype", choices=["whitehat", "greyhat", "blackhat"])

args = parser.parse_args()
print(args)

hacker_type = "greyhat or unknown"

if args.blackhat:
    hacker_type = "blackhat"

if args.whitehat:
    hacker_type = "whitehat"

print(hacker_type)
