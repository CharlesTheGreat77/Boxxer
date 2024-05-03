import argparse, json, re
from playwright.sync_api import Playwright, sync_playwright, expect
from core.profile import Target
from core.bot_browser import playwright_browser

# set args.
parser = argparse.ArgumentParser(description='ship a target a bunch of boxes', usage='python3 boxxer.py --help')
parser.add_argument('-s', '--street', help='specify the street address [1600 Gabaldon Rd]', type=str, required=True)
parser.add_argument('-st', '--state', help='specify the street address [Nevada]', type=str, required=True)
parser.add_argument('-c', '--city', help='specify the city the address resides in [Las Vegas]', type=str, required=True)
parser.add_argument('-z', '--zip', help='specify the zip code of the address [87112]', type=int, required=True)
parser.add_argument('-size', '--size', help='specify the box size [options: small, medium, side-medium large]', default='small', required=False)
parser.add_argument('-a', '--amount', help='specify the amount of boxes to send [default: 1]', type=int, default=1, required=False)
args = parser.parse_args()

# verify input before proceeding
print(f"[?] Information correct? (Y/n)")
print(f" -> Street Address: {args.street}, {args.city}, {args.state}, {args.zip}")
correct_info = input("boxxer(address_info)> ")
if correct_info == 'n' or correct_info == 'N':
    print(parser.usage)
    exit()

# load box size urls
with open('boxes.json', 'r') as file:
    boxes = json.load(file)['boxes']

# set attributes
target = Target(args.street, args.city, args.zip)
target.state = target.get_abbreviated_states(args.state)
target.random_first_name, target.random_last_name, target.random_city = target.get_random_information()
target.random_phone_number = target.get_random_phone_number()
target.random_email = target.get_random_email(target.random_first_name, target.random_last_name)


# big ahhh check to make sure attributes are solid.. 
if all([target.state, target.random_city, target.random_phone_number, target.random_email, target.random_first_name, target.random_last_name, target.random_city]):
    with sync_playwright() as playwright:
        playwright_browser(playwright, target, boxes[f'{args.size}'], args.amount)
