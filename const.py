SUPPORTED_LOCALES = [
    'en_US', 'fr-FR', 'fr-BE'
]

SUPPORTED_CURRENCIES = [
    #'AED',
    #'AUD',
    #'BGN',
    #'BRL',
    #'CAD',
    'CHF',
    # 'CZK',
    # 'DKK',
    'EUR',
    # 'GBP',
    #'HKD',
    #'HRK',
    #'HUF',
    #'ILS',
    #'ISK',
    #'JPY',
    #'MXN',
    #'MYR',
    #'NOK',
    #'NZD',
    #'PHP',
    #'PLN',
    #'RON',
    #'RUB',
    #'SEK',
    #'SGD',
    #'THB',
    #'TWD',
    #For testing purposes, USD is used, but it should not be used in production
    'USD',
    #'ZAR'
]

# Can probably remove these
DEFAULT_PAYMENT_METHOD_CODES = {
    # Primary payment methods.
    'demo',
    'card',
    #'ideal',
    # Brand payment methods.
    'visa',
    'mastercard',
    #'amex',
    #'discover',
    'taler'
}

PAYMENT_METHODS_MAPPING = {
    'taler': 'taler',
    #'apple_pay': 'applepay',
    'card': 'creditcard'
    #'bank_transfer': 'banktransfer',
    #'kbc_cbc': 'kbc',
    #'p24': 'przelewy24',
    #'sepa_direct_debit': 'directdebit',
}
