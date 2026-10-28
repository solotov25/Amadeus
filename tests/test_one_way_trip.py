from pages.home_page import HomePage
from pages.flight_page import FlightPage
from pages.summary_page import SummaryTrip

def test_round_trip_is_selected_by_default(page):
    home = HomePage(page)
    flight = FlightPage(page)
    # summary = SummaryTrip(page)

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
    page.pause()
    # flight.choose_first_flight()
    # flight.choose_light_fare()

    # SummaryTrip steps
    # summary