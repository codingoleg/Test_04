rows = [
    {"date": "2023-10-10", "phone_num": "70000000000", "email": "email000000@mail.ru", "text": "0 text"},
    {"date": "2023-10-10", "phone_num": "70000000000", "email": "email111111@mail.ru", "text": "1 text"},
    {"date": "2023-10-11", "phone_num": "71111111111", "email": "email111111@mail.ru", "text": "1 text"},
    {"date": "2023-10-12", "phone_num": "73333333333", "email": "email222222@mail.ru", "text": "2 text"},
    {"date": "2023-10-13", "phone_num": "73333333333", "email": "email333333@mail.ru", "text": "3 text"},
    {"date": "2023-10-14", "phone_num": "74444444444", "email": "email444444@mail.ru", "text": "4 text"}
]

testcases_valid = [
    {"date": "2023-10-10", "phone_num": "70000000000"},
    {"date": "2023-10-11"},
    {"date": "11.10.2023"},
    {"text": "1 text"},
    {"phone_num": "73333333333", "email": "email222222@mail.ru"},
    {"phone_num": "73333333333"},
    {"date": "14.10.2023", "phone_num": "74444444444", "email": "email444444@mail.ru", "text": "4 text"}
]

responses_valid = [
    [rows[0], rows[1]],
    [rows[2]],
    [rows[2]],
    [rows[1], rows[2]],
    [rows[3]],
    [rows[3], rows[4]],
    [rows[5]]
]

testcases_default_response = [
    {},
    {"phone_num": None},
    {"date": None, "phone_num": None, "email": None, "text": None}
]

testcases_date_invalid = [
    {"date": "29.02.2023"},
    {"date": "11.20.2023"},
    {"date": "11.10.202"},
    {"date": "-11.10.2023"}
]

testcases_email_invalid = [
    {"email": "email@mail.ru@"},
    {"email": "email@mail."},
    {"email": "email"},
    {"email": "@emailmail.ru"}
]

testcases_phone_num_invalid = [
    {"phone_num": "700000"},
    {"phone_num": "90000000000"}
]
