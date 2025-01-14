

def test_search_for_element(home_page):
    item = 'zapato'

    home_page.search_item_from_home(item)
    home_page.verify_results_are_listed()


def test_search_for_multiple_elements(home_page):
    item_1 = 'zapato'
    item_2 = 'celular'

    home_page.search_item_from_home(item_1)
    home_page.verify_results_are_listed()
    home_page.search_item_from_results(item_2)
    home_page.verify_results_are_listed(item_2)


def test_search_invalid_result(home_page):
    invalid_item = 'asdasdsa'

    home_page.search_item_from_home(invalid_item)
    home_page.verify_no_results_are_found()


def test_search_for_merchant(home_page):
    merchant = 'amazon.mx'

    home_page.search_item_from_home(merchant)
    home_page.verify_merchant_is_listed(merchant)

