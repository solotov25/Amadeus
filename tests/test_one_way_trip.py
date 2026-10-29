from pages.home_page import HomePage
from pages.flight_page import FlightPage
from pages.summary_page import SummaryTrip
from pages.services_requests import ServiceRequest
from pages.passenger_info_page import PassengerInfoPage

def test_round_trip_is_selected_by_default(page):
    """
    Preconditions:
        - Site locale is pinned to en-US (see conftest.py).
        - Runs in headed real Chrome, since Akamai blocks headless Chromium.
    """
    
    home = HomePage(page)
    flight = FlightPage(page)
    summary = SummaryTrip(page)
    passenger = PassengerInfoPage(page)
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
    summary.continue_to_passenger_info()

    # Passenger info step
    # Passenger 1
    passenger.choose_gender()
    passenger.enter_first_name()
    passenger.enter_last_name()
    passenger.enter_date_of_birth()
    passenger.choose_nationality()
    passenger.click_next_button()
    
    # Passenger 2
    passenger.choose_gender()
    passenger.enter_first_name()
    passenger.enter_last_name()
    passenger.enter_date_of_birth()
    passenger.choose_nationality()
    passenger.click_next_button()

    # Booking Holder info
    passenger.select_passenger()
    passenger.select_phone_prefix()
    passenger.enter_phone_number()
    passenger.enter_email()
    passenger.confirm_email()
    passenger.accept_privacy_policy()
    passenger.go_to_services()

    # Service requested
    service.select_no_baggage()
    service.select_priority_boarding()
    service.go_to_payment()