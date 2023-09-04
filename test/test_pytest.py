from utils import functions


def test_get_date():
    assert functions.get_date('2019-08-26T10:50:58.294041') == '26.08.2019'


def test_cover_from_to_message():
    assert functions.cover_from_to_message('Visa Gold 7305799447374042') == 'Visa Gold 7305 79** **** 4042'
    assert functions.cover_from_to_message('Visa Platinum 8990922113665229') == 'Visa Platinum 8990 92** **** 5229'
    assert functions.cover_from_to_message('Visa Classic 6216537926639975') == 'Visa Classic 6216 53** **** 9975'
    assert functions.cover_from_to_message('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert functions.cover_from_to_message('MasterCard 9175985085449563') == 'MasterCard 9175 98** **** 9563'
    assert functions.cover_from_to_message('МИР 1582474475547301') == 'МИР 1582 47** **** 7301'
    assert functions.cover_from_to_message('Счет 28429442875257789335') == 'Счет **9335'


def test_cover_from_to_message_empty():
    assert functions.cover_from_to_message(None) == ''


def test_cover_account_number():
    assert functions.cover_account_number('75651667383060284188') == '**4188'
    assert functions.cover_account_number('72082042523231456215') == '**6215'


def test_cover_card_number():
    assert functions.cover_card_number('9447344650495960') == '9447 34** **** 5960'
    assert functions.cover_card_number('8201420097886664') == '8201 42** **** 6664'


def test_share_message():
    data = {
        'id': 41428829,
        'state': 'EXECUTED',
        'date': '2019-07-03T18:35:29.512364',
        'operationAmount': {
            'amount': '8221.37',
            'currency': {
                'name': 'USD.',
                'code': 'USD'
            }
        },
        'description': 'Перевод организации',
        'from': 'MasterCard 7158300734726758',
        'to': 'Счет 35383033474447895560'
    }

    result = '''03.07.2019 Перевод организации
MasterCard 7158 30** **** 6758 -> Счет **5560
8221.37 USD.'''
    assert functions.share_message(data) == result
