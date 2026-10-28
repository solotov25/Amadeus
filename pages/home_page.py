import re
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.avianca.com/en"

        self.accept_cookies = page.get_by_role("button", name="Accept")
        
        #Define homepage locators 
        self.round_trip = page.get_by_role("radio", name="Round trip")
        self.one_way_trip = page.get_by_role("radio", name="One way")
        self.return_date_field = page.get_by_role("button", name="Return")
        self.destination_dropdown = page.get_by_role("combobox", name="Destination")
        self.destination_option = page.get_by_role("option", name="San Andres, Colombia ADZ")
        self.departure = page.get_by_role("button", name="Departure")

        # Locate valid date
        self.departure_date = self.page.locator(
            '//button[contains(@aria-label, "Hoy")]'
            '/following::button[@data-name="dayCell" and not(@disabled)][1]'
        )

        # Locators for increment passenger number
        self.adults_incrementer = page.locator(
                '//span[normalize-space()="Adults"]'
                '/ancestor::div[contains(@class, "flex-col")]'
                '/following-sibling::div[@data-name="incrementer"]'
            )
        self.adults_count = self.adults_incrementer.locator(
            "xpath=./span"
        )

        self.adults_increase_button = (
            self.adults_incrementer.get_by_role(
                "button", name="Increase"
            )
        )

        self.adults_decrease_button = (
            self.adults_incrementer.get_by_role(
                "button", name="Decrease"
            )
        )

        self.total_count = self.page.get_by_role("button", name="Select passengers")
        self.confirm_passengers_button = page.get_by_role("button", name="Confirm")
        self.search_button = page.get_by_role("button", name="Search")
                

    # METHODS

    def open(self):        
        # Open testing page and accept cookies 
        self.page.goto(self.url, wait_until="domcontentloaded")
        self.accept_cookies.click()


    def round_trip_is_selected_by_default(self):
        # Round trip button is selected by default
        expect(self.round_trip).to_have_attribute("aria-checked", "true")
    

    def choose_one_way(self):
        # Click one way button
        self.one_way_trip.click()
        expect(self.return_date_field).to_be_hidden()

    def choose_destination(self):
        self.destination_dropdown.click()
        expect(self.destination_option).to_be_visible()
        self.destination_option.click()
        expect(self.destination_dropdown).to_have_value("San Andres (ADZ)")

    def choose_destination_date(self):
        self.departure.click()

        # Select the enabled date immediately after today
        expect(self.departure_date).to_be_enabled()
        self.departure_date.click()

        expect(self.departure).to_have_value(
            re.compile(r"^\d{2}/\d{2}/\d{4}$")
        )


    def verify_increase_adults(self):
        expect(self.adults_count).to_have_text("1")
        self.adults_increase_button.click()
        expect(self.adults_count).to_have_text("2")
        expect(self.adults_increase_button).to_be_enabled()
        expect(self.adults_decrease_button).to_be_enabled()

    def confirm_passengers(self):
        self.confirm_passengers_button.click()
        expect(self.total_count).to_contain_text("2")

    def search_flights(self):
        self.search_button.click()
        expect(self.page).not_to_have_url(self.url)