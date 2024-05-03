import random, secrets
from browserforge.injectors.playwright import NewContext
from browserforge.fingerprints import FingerprintGenerator
from playwright_stealth import stealth_sync

# function to order boxes on usps to a given target
def playwright_browser(playwright, target, url, box_count) -> None:
    '''
    function to go to usps, check out x amount of boxes, create an account, and confirm the shipping
    '''
    fingerprints = FingerprintGenerator()
    fingerprint = fingerprints.generate()
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    stealth_sync(page)
    page.goto(f"{url}")

    try:
        page.locator("#cartQuantity", timeout=2000).click()
        page.locator("#cartQuantity").fill(f"{box_count}") # default amount is 1
    except:
        if box_count != 1:
            page.locator("#availabilityControl span").nth(str(box_count-1)).click()

    print("[*] Adding to cart..")
    page.get_by_role("button", name="Add to Cart").click()
    print("[*] Checking out..")
    page.get_by_role("link", name="Check Out Now").click()
    print("[*] Creating a fake account..")

    # set a username
    page.get_by_role("link", name="Sign Up Now").click()
    page.get_by_label("* Username").click()
    page.get_by_label("* Username").fill(f"{target.random_last_name + str(secrets.randbits(random.randint(4,11))) + target.random_first_name}")

    # stupid lil password
    page.get_by_label("* Password").click()
    password = f'P@ssW0rd0912'
    page.get_by_label("* Password").fill(password)
    page.get_by_label("* Password").press("Tab")
    page.get_by_label("* Re-Type Password").click()
    page.get_by_label("* Re-Type Password").fill(password)

    # set security code as a random city for the hell of it (get it over wit)
    page.get_by_label("* First Security Question").select_option("2")
    page.locator("#tsecAnswer1").click()
    page.locator("#tsecAnswer1").fill(f"{target.random_city}")
    page.get_by_label("* Second Security Question").select_option("1")
    page.locator("#tsecAnswer2").click()
    page.locator("#tsecAnswer2").fill(f"{target.random_city}")
    page.locator("#tsecAnswer2Match").click()
    page.locator("#tsecAnswer2Match").fill(f"{target.random_city}")
    page.locator("#tsecAnswer1Match").click()
    page.locator("#tsecAnswer1Match").fill(f"{target.random_city}")

    # set email, first name, last name, phone number, zip code, and abbreviated state
    page.get_by_label("Personal Account").check()
    page.get_by_label("* Email Address").click()
    page.get_by_label("* Email Address").fill(f"{target.random_email}")
    page.get_by_label("* Email Address").press("Tab")
    page.get_by_label("* Re-Type Email Address").click()
    page.get_by_label("* Re-Type Email Address").fill(f"{target.random_email}")
    page.get_by_label("* Re-Type Email Address").press("Tab")
    page.get_by_label("* Phone").click()
    page.get_by_label("* Phone").fill(target.random_phone_number)
    page.get_by_label("* First Name").click()
    page.get_by_label("* First Name").fill(f"{target.random_first_name}")
    page.get_by_label("* Last Name").click()
    page.get_by_label("* Last Name").fill(f"{target.random_last_name}")
    page.get_by_role("textbox", name="* Street Address").click()
    page.get_by_role("textbox", name="* Street Address").click()
    page.get_by_role("textbox", name="* Street Address").fill(f"{target.street}")
    page.get_by_role("textbox", name="* City").click()
    page.get_by_role("textbox", name="* City").fill(f"{target.city}")
    page.locator("#sstate").select_option(f"{target.state}")
    page.get_by_label("ZIP Code™", exact=True).click()
    page.get_by_label("ZIP Code™", exact=True).fill(f"{target.zip_code}")

    # click the "verify address" button and "create account" button
    page.get_by_text("Verify Address").click()
    page.get_by_text("Create Account").click()

    # wait 7 seconds..
    page.wait_for_timeout(timeout=7000)

    # try to check out..
    print("[*] Checking out...")
    page.get_by_role("button", name="Check Out Now").click()
    page.wait_for_selector('.ship-to-this-address-btn')
    page.click('.ship-to-this-address-btn')

    # depending on the address.. this button will appear..
    try:
        print("[*] Confirming ground shipment option..")
        page.get_by_label("USPS Ground Advantage™:", timeout=2000).check()
    except:
        pass
    
    # depending on the address.. this button will appear..
    try:
        print("[*] Confirming shipment..")
        page.get_by_role("button", name="Confirm Shipment", timeout=2000).click()
    except:
        pass
    print("[*] Placing Order..")

    # page.wait_for_selector('#placeMyOrderBtn')
    # page.click('#placeMyOrderBtn')
    page.get_by_role("button", name="Place My Order").click()
    page.wait_for_timeout(15000) # keeping this here so the user can "agree" to the terms & conditions..
    context.close()
    browser.close()
