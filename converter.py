import data_handler


def get_data():
    data = data_handler.testquery()
    for i in data:
        print(i['country'])


def main():
    get_data()


if __name__ == "__main__":
    main()
