from typing import Union


def get_executed_message(data: list) -> list:
    """
    Показывает транзакции по EXECUTED и сортирует по дате
    """
    items = [item for item in data if item.get('state') == "EXECUTED"]
    items.sort(key=lambda x: x.get('date'), reverse=True)
    return items


def share_message(item: dict) -> str:
    """
    Показывает сообщения в заданном формате.
    """
    date = get_date(item.get('date'))
    desc = item.get('description')
    from_ = cover_from_to_message(item.get('from'))
    to_ = cover_from_to_message(item.get('to'))
    amount = item.get('operationAmount').get('amount')
    currency = item.get('operationAmount').get('currency').get('name')

    if from_:
        from_ = from_ + ' -> '

    return f'{date} {desc}\n{from_}{to_}\n{amount} {currency}'


def get_date(dt: str) -> str:
    """
    Возвращает дату в формате ДД.ММ.ГГГГ
    """
    sep = '.'
    d = dt[0:10].split(sep='-')
    return d[2] + sep + d[1] + sep + d[0]


def cover_from_to_message(msg: Union[str, None]) -> str:
    """
    Скрывает номер счета/карты для полей <откуда>, <куда>.
    """

    if msg is None:
        return ''

    msg_split = msg.split(sep=' ')
    if msg_split[0] == 'Счет':
        number_hidden = cover_account_number(msg_split[-1])
    else:
        number_hidden = cover_card_number(msg_split[-1])
    return ' '.join(msg_split[:-1]) + ' ' + number_hidden


def cover_card_number(number: str) -> str:
    """
    Показывает номер карты по блокам первые 6 цифр и последние 4
    """
    if number.isdigit() and len(number) == 16:
        return number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
    else:
        raise Exception("Номер карты не валидный!")


def cover_account_number(number: str) -> str:
    """
    показывает 4 последних цифры счета.
    """
    if number.isdigit() and len(number) >= 4:
        return '**' + number[-4:]
    else:
        raise Exception("Номер счета не валидный!")


