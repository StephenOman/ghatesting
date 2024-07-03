from datetime import date

def get_message():
    today = date.today().strftime('%d/%m/%Y')
    message = "Hello world. Today's date is "
    return message + today

if __name__ == '__main__':
    print(get_message())