from pages.home_page import HomePage
from pages.flight_page import FlightPage
from pages.summary_page import SummaryTrip
from pages.services_requests import ServiceRequest

def test_round_trip_is_selected_by_default(page):
    """
    Preconditions:
        - Site locale is pinned to en-US (see conftest.py).
        - Runs in headed real Chrome, since Akamai blocks headless Chromium.
    """
    
    home = HomePage(page)
    flight = FlightPage(page)
    summary = SummaryTrip(page)
    service = ServiceRequest(page)

    # HomePage steps
    home.open()
    home.round_trip_is_selected_by_default()
    home.choose_one_way()
    home.choose_destination()
    home.choose_destination_date()
    home.verify_increase_adults()
    home.confirm_passengers()
    home.search_flights()
    
    # FlightPage steps
    # page.pause()
    flight.choose_first_flight()
    flight.choose_light_fare()

    # SummaryTrip steps
    # Passenger 1
    summary.choose_gender()
    summary.enter_first_name()
    summary.enter_last_name()
    summary.choose_birthday()
    summary.choose_nationality()
    summary.next_button()
    
    # Passenger 2
    summary.choose_gender()
    summary.enter_first_name()
    summary.enter_last_name()
    summary.choose_birthday()
    summary.choose_nationality()
    summary.next_button()

    # Booking Holder info
    summary.select_passenger()
    summary.select_phone_prefix()
    summary.select_phone_number()
    summary.enter_email()
    summary.confirm_email()
    summary.accept_privacy_policy()
    summary.go_to_services()

    # Service requested
    service.select_no_baggage()
    service.select_priority_boarding()
    service.go_to_payment()