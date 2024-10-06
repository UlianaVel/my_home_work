def  send_email(message, recipient, sender):
    a = '@'
    cor_address_1_sender = sender[-3:]
    cor_address_1_rec = recipient[-3:]
    cor_address_2_sender = sender[-4:]
    cor_address_2_rec = recipient[-4:]

    if a in sender and a in recipient:
        if cor_address_1_sender == '.ru' or cor_address_2_sender == '.com' or cor_address_2_sender == '.net':
            if cor_address_1_rec == '.ru' or cor_address_2_rec == '.com' or cor_address_2_rec == '.net':
                if recipient == sender:
                    print('Нельзя отправить письмо самому себе!')

                elif sender == 'university.help@gmail.com':
                    print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                    print(f'Текст письма: {message}')
                else:
                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
                    print(f'Текст письма: {message}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')



sender = input("Введите адрес отправителя:")
recipient = input("Введите адрес получателя:")
message = input('Введите текст письма:')
send_email(message, recipient, sender)

