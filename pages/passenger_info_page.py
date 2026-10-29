
from playwright.sync_api import Page, expect


class PassengerInfoPage:
    def __init__(self, page: Page):
        self.page = page

        # Passenger information locators
        self.gender_dropdown = page.get_by_role(
            "combobox", name="Gender"
        )

        self.first_name_input = page.get_by_test_id(
            "first-name-input"
        )

        self.last_name_input = page.get_by_test_id(
            "last-name-input"
        )

        # Date of birth dropdowns
        self.birth_day_dropdown = page.get_by_role(
            "combobox", name="Day"
        )

        self.birth_month_dropdown = page.get_by_role(
            "combobox", name="Month"
        )

        self.birth_year_dropdown = page.get_by_role(
            "combobox", name="Year"
        )

        # Nationality field
        self.nationality_dropdown = page.locator(
            '[data-test="TA-tp-Nationality"]'
        )

        # Next Button
        self.next_booking_holder_button = page.get_by_role("button", name="Next")

        # Booking holder fields
        self.passenger_list_dropdown = page.get_by_role(
            "combobox", name="Passenger"
        )
        self.phone_prefix_dropdown = page.get_by_role(
            "combobox", name="Prefix"
        )
        self.phone_number_input = page.get_by_role(
            "textbox", name="Phone number"
        )
        self.email_input = page.get_by_role(
            "textbox", name="E-mail address"
        )
        self.confirmation_email_input = page.get_by_role(
            "textbox", name="Confirm E-mail address"
        )

        self.privacy_policy_checkbox = page.get_by_role(
            "checkbox",
            name="I accept the processing of my personal data in accordance with the Privacy Policy"
        )

        # Continue Button
        self.continue_button = page.get_by_role("button", name="Continue")


    # METHODS

    def choose_gender(self, gender: str):
        self.gender_dropdown.choose_option(label=gender)

    def enter_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def enter_date_of_birth(
        self, day: str, month: str, year: str
    ):
        self.birth_day_dropdown.choose_option(label=day)
        self.birth_month_dropdown.choose_option(label=month)
        self.birth_year_dropdown.choose_option(label=year)

    def choose_nationality(self, nationality: str):
        self.nationality_dropdown.click()

        # Assumes the nationality options are accessible by role
        self.page.get_by_role(
            "option", name="Colombia", exact=True
        ).click()

    def click_next_button(self):
        self.next_booking_holder_button().click()

    def select_passenger(self, passenger: str):
        self.passenger_list_dropdown.select_option(
            label=passenger
        )

    def select_phone_prefix(self, prefix: str):
        self.phone_prefix_dropdown.select_option(
            label=prefix
        )

    def enter_phone_number(self, phone_number: str):
        self.phone_number_input.fill(phone_number)

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def confirm_email(self, email: str):
        self.confirm_email_input.fill(email)

    def accept_privacy_policy(self):
        self.privacy_policy_checkbox.check()
        expect(self.privacy_policy_checkbox).to_be_checked()

    def go_to_services(self, email: str):
        self.continue_button.click()
        