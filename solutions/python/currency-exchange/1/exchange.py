
def exchange_money(budget, exchange_rate):
    """Returns the value of the exchanged currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Returns the amount of money that is left from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Return the number of bills that would be given back.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return number_of_bills * denomination


def get_number_of_bills(amount, denomination):
    """Returns the number of whole bills that you can receive within the given amount.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return int(amount / denomination)


def get_leftover_of_bills(amount, denomination):
    """Returns the amount that is kept by the booth.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Returns the maximum value of the new currency after calculating the exchange rate plus the spread (percentage taken as an Exchange Fee).

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_percentage = exchange_rate * spread / 100
    exchange_fee = exchange_rate + spread_percentage
    exchanged_amount = exchange_money(budget, exchange_fee)

    return int(exchanged_amount - get_leftover_of_bills(exchanged_amount, denomination))