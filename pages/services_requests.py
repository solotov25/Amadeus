from playwright.sync_api import Page, expect

class ServiceRequest:
    def __init__(self, page:Page):
        self.page = page
        self.no_baggage_needed_checkbox = page.get_by_role(
            "checkbox",
            name="No, I have what I need"
        )

        self.no_additional_baggage_message = page.get_by_text(
            "You will continue without additional baggage",
            exact=True
        )


        self.priority_boarding_card = page.get_by_text(
            "Priority boarding",
            exact=True
        )

        self.priority_boarding_checkbox = page.get_by_role(
            "checkbox"
        )
        
        self.save_exit_button = Page.get_by_role("button", name="Save and exit")
        self.go_to_payment_button = Page.get_by_role("button", name="Go to payment")

    # Methods
    def select_no_baggage(self):
        if self.no_baggage_needed_checkbox.is_visible():
            self.no_baggage_needed_checkbox.check()

            expect(self.no_baggage_needed_checkbox).to_be_checked()

            expect(
                self.no_additional_baggage_message
            ).to_be_visible()


    def select_priority_boarding(self):
        self.priority_boarding_card.click()

        if not self.priority_boarding_checkbox.is_checked():
            self.priority_boarding_checkbox.check()

        expect(self.priority_boarding_checkbox).to_be_checked()

    def continue_to_passenger_info(self):
        self.go_to_payment_button.click()