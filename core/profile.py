import json, random, secrets
from typing import Optional, Tuple

# class for a given target to send boxes to
class Target:
    def __init__(self, street_address, city, zip_code):
        self.street = street_address
        self.city = city
        self.zip_code = zip_code
        self.state = ''
        self.random_first_name = ''
        self.random_last_name = ''
        self.random_city = ''
        self.random_email = ''
        self.random_phone_number = ''

    # function grab a random phone number from phone_numbers.json
    def get_random_phone_number(self) -> Optional[str]: # outputs none if error occurs
        '''
        return a random phone number 
        '''
        try:
            with open('phone_numbers.json', 'r') as numbers_file:
                phone_numbers = json.load(numbers_file)
            return secrets.choice(phone_numbers['numbers'])

        except FileNotFoundError as err:
            print(f"[-] Error: File not found.. names.json or city_states.json..\n -> {err}")
        except OSError:
            print("[-] Error: OS error occured..")
        except Exception as err:
            print(f"[-] Error: Unexpected error occured..\n -> {err}")
        return None # return none if error occurs 

    # function to get the abbreviation of a US state from city_states.json
    def get_abbreviated_states(self, state: str) -> Optional[str]:
        '''
        returns abbreviated US state
        '''
        try:
            with open('city_states.json', 'r') as states_file:
                states = json.load(states_file)['states']
                # cleanest I could think of to loop through each key, pair and get the abbreviation..
                return [(abbr) for abbr, state_name in states.items() if state_name==state][0]
            return None  # return None if state is not found

        except FileNotFoundError as err:
            print(f"[-] Error: File not found.. names.json or city_states.json..\n -> {err}")
        except OSError:
            print("[-] Error: OS error occurred..")
        except Exception as err:
            print(f"[-] Error: Unexpected error occurred..\n -> {err}")
        return None

    # function to get a random first and last name, and city from names.json & city_states.json
    def get_random_information() -> Optional[Tuple[str, str, str]]:
        '''
        return random first name, last name, and random city
        '''
        try:
            with open('names.json', 'r') as name_file, open('city_states.json', 'r') as city_file:
                names = json.load(name_file)
                cities = json.load(city_file)
            return secrets.choice(names['first_names']), secrets.choice(names['last_names']), secrets.choice(cities['cities'])

        except FileNotFoundError as err:
            print(f"[-] Error: File not found.. names.json or city_states.json..\n -> {err}")
        except OSError:
            print("[-] Error: OS error occured..")
        except Exception as err:
            print(f"[-] Error: Unexpected error occured..\n -> {err}")
        return None

    # function to create a random email address from the given input (first and last name)
    def get_random_email(self, first_name: str, last_name: str) -> Optional[str]:
        '''
        return a random email address from the given providers below
        '''
        try:
            # I tried.. better than nothing
            provider_list = ['@gmail.com', '@aol.com', '@protonmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com']
            email_creation = [first_name, str(secrets.randbits(random.randint(4,11))), last_name]
            random.shuffle(email_creation)
            random.shuffle(email_creation) # not even sure if this helped that much tbh.. random lib is broken
            return ''.join(email_creation) + str(secrets.choice(provider_list))

        except Exception as err:
            print(f"[-] Error: Unexpected error occured..\n -> {err}")
        return None