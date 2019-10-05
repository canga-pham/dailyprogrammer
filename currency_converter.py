import requests


def currency_converter(from_currency, amount, to_currency = "EUR"):
    """
    converts chosen amount from one currency to another
    :param from_currency: convert from this currency, format: abbreviation of the currency, e.g. 'EUR'
    :param to_currency: convert to this currency,  format: abbreviation of the currency, e.g. 'EUR'
    :param amount: amount in from_currency to be converted, format: float
    :return: converted amount in to_currency
    """
    rate_api = "https://api.exchangeratesapi.io/latest"

    params = {"base": from_currency.upper(), "symbols": to_currency.upper()}

    rate_request = requests.request("GET", rate_api, params = params)

    rate = rate_request.json()['rates'][to_currency.upper()]

    return rate*amount