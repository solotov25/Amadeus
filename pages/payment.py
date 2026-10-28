from playwright.sync_api import Page

class Payment:
    def __init__(self):
        departure_aiport = Page.get_by_title("")
        arrival_airport = Page.get_by_title("")
        travel_date = Page.get_by_title("")
        fare = Page.get_by_title("")
        flight_number = Page.get_by_title("")
        total_price = Page.get_by_title("")