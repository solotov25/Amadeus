# from datetime import date

# from pages.home_page import HomePage
# from pages.flight_page import FlightPage


# def test_round_trip_outbound_and_return_selection(page):
#     home = HomePage(page)
#     flight = FlightPage(page)

#     # Step 1: site loads, Trip Type defaults to "Round trip"
#     home.open()
#     home.round_trip_is_selected_by_default()

#     # Step 2: click Destination -> "All the airports" dropdown appears
#     # home.open_destination()

#     # Step 3: choose San Andres (ADZ) -> departure calendar opens
#     home.choose_destination()

#     # Step 4: choose a future departure date -> return calendar opens
#     # departure = home.choose_departure_date()
#     assert departure > date.today()

#     # Step 5: choose a return date after departure -> "Who's flying?" appears
#     return_date = home.choose_return_date()
#     assert return_date > departure

#     # Step 6: add one adult (1 -> 2), plus and minus are enabled
#     home.verify_increase_adults()

#     # Step 7: confirm passengers -> dropdown is dismissed
#     home.confirm_passengers()

#     # Step 8: search -> booking page appears
#     home.search_flights()

#     # Steps 9-11: outbound flight (earliest) with Classic fare
#     flight.choose_earliest_flight()
#     flight.choose_classic_fare()
#     flight.continue_with_restrictions()

#     # Steps 12-14: return flight (latest) with Light fare
#     flight.choose_latest_flight()
#     flight.choose_light_fare()
#     flight.continue_with_restrictions_and_expect_continue()