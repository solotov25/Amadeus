from playwright.sync_api import Page, expect

class SummaryTrip:
    def __init__(self, page:Page):
        self.page = page
        self.continue_button = page.get_by_role("button", name="Continue")

    # Methods
    def continue_to_passenger_info(self):
        self.continue_button.click()
