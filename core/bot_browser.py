import random, secrets
from browserforge.injectors.playwright import NewContext
from browserforge.fingerprints import FingerprintGenerator
from playwright_stealth import stealth_sync

# function to order boxes on usps to a given target
def playwright_browser(playwright, target) -> None:
    '''
    function to go to usps, check out x amount of boxes, create an account, and confirm the shipping
    '''
    fingerprints = FingerprintGenerator()
    fingerprint = fingerprints.generate()
    browser = playwright.chromium.launch(headless=False, proxy={'server':'http://72.10.164.178:7443'})
    context = browser.new_context()
    page = context.new_page()
    stealth_sync(page)
    page.goto("https://store.usps.com/store/product/shipping-supplies/priority-mail-flat-rate-padded-envelope-P_EP14PE")
    page.locator("#availabilityControl span").first.click(click_count=5) # default amount of boxes..
    print("[*] Adding to cart..")
    page.get_by_role("button", name="Add to Cart").click()
    print("[*] Checking out..")
    page.get_by_role("link", name="Check Out Now").click()
    print("[*] Creating a fake account..")

    # set a username
    page.get_by_role("link", name="Sign Up Now").click()
    page.get_by_label("* Username").click()
    page.get_by_label("* Username").fill(f"{target.random_last_name + target.random_first_name + str(secrets.randbits(random.randint(4,11)))}")

    # stupid lil password
    page.get_by_label("* Password").click()
    password = f'P@ssW0rd{str(random.randint(1,10000))}'
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

    '''
    Program stops here due to usps taking the service down..
    '''

    # wait 7 seconds..
    page.wait_for_timeout(timeout=7000)

    # try to check out..
    print("[*] Checking out...")
    page.get_by_role("button", name="Check Out Now").click()
    page.locator("input[name=\"ci22426006164\"]").click()
    page.locator("input[name=\"ci22426006164\"]").press("ArrowRight")
    page.locator("input[name=\"ci22426006164\"]").fill("1")
    try:
        page.get_by_role("button", name="Update").click()
        page.get_by_role("button", name="Check Out Now").click()
    except Exception as msg:
        print(msg)
        pass
    page.get_by_role("button", name="Ship to this Address").click()
    page.get_by_label("USPS Ground Advantage™:").check()
    page.get_by_role("button", name="Confirm Shipment").click()
    page.get_by_role("button", name="Place My Order").click()
    page.wait_for_timeout(30000) # keeping this here so the user can "agree" to terms button..
    context.close()
    browser.close()
