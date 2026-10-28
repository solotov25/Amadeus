from playwright.sync_api import Page

class PassengerInfo:
    def __init__(self):
        # Passenger fields
        gender_passenger = Page.get_by_title("")
        first_name_passenger = Page.get_by_title("")
        last_name_passenger = Page.get_by_title("")
        birthday_passenger = Page.get_by_title("")
        nationality_passenger = Page.get_by_title("")

        # Next Button
        next_booking_holder_button = Page.get_by_title("")

        # Booking holder fields
        name_booking_holder = Page.get_by_title("")
        phone_prefix_booking_holder = Page.get_by_title("")
        phone_booking_holder = Page.get_by_title("")
        email_booking_holder = Page.get_by_title("")
        email_confirmation = Page.get_by_title("")

        # Privacy Policy
        privacy_policy = Page.get_by_title("")

        # Continue Button
        continue_button = Page.get_by_title("")
