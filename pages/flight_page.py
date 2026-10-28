
from playwright.sync_api import Page, expect


class FlightPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.best_price_button = page.get_by_role(
            "button", name="Best price"
        )

        self.first_flight = page.locator(
            "/html/body/app-root/main/avail-page/div/avail-cont/"
            "avail-pres/div/avail-list-pres/div[1]/expander-elem/div"
        )

        self.light_fare_button = self.page.locator('button[aria-label^="Fare type LIGHT"]')

    # Methods
    def choose_best_price(self):
        expect(self.best_price_button).to_be_visible()
        expect(self.best_price_button).to_be_enabled()
        self.best_price_button.click()

    def choose_first_flight(self):
        self.choose_best_price()
        expect(self.first_flight).to_be_visible()
        self.first_flight.click()

    def choose_light_fare(self):
        self.light_fare_button.click()
        expect(self.page).not_to_have_url(self.page.url)
