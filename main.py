import json
from utils.functions import get_executed_message, share_message


def main():
    with open('utils/operations.json', encoding='utf-8') as fp:
        data = json.load(fp)

    items = get_executed_message(data)

    for i in range(5):
        print(share_message(items[i]))
        print()


if __name__ == '__main__':
    main()
