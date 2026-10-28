from playwright.sync_api import Page

class ServiceRequest:
    def __init__(self):
        no_bags = Page.get_by_title("")
        no_bags_confirmation = Page.get_by_title("")
        priority_boarding = Page.get_by_title("")
        priority_all_passengers = Page.get_by_title("")
        save_exit_button = Page.get_by_title("")
        go_to_payment_button = Page.get_by_title("")