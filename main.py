from my_package.message_formatter import format_message
def main():
    messages = ["Hello World!", "Nature shine" ]
    for msg in messages:
        print(format_message(msg))
        print()


if __name__ == "__main__":
    main()
