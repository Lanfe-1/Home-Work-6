# Home Work 6.1
# V1
# import string

user_input = input("Введіть дві літери через дефіс (наприклад, 'a-c'): ")
all_letters = string.ascii_letters
start, end = user_input.split('-')
start_index = all_letters.index(start)
end_index = all_letters.index(end)
result = all_letters[start_index:end_index + 1]
print(result)
#
# # V2

import string

ALL_LETTERS = string.ascii_letters
SEPARATOR = "-"

user_input = input("Enter letters in format: 'a-c' ").strip()

if len(user_input) == 3:
    first_letter = user_input[0]
    second_letter = user_input[2]
    separator = user_input[1]

    if first_letter.isalpha() and second_letter.isalpha() and separator == SEPARATOR:
        start_index = ALL_LETTERS.index(first_letter)
        end_index = ALL_LETTERS.index(second_letter)

        if start_index > end_index:
            start_index, end_index = end_index, start_index

        result = ALL_LETTERS[start_index:end_index + 1]
        print(result)

# Home Work 6.3

number = int(input("Введіть число: "))

while number > 9:
    temp_number = str(number)
    number = 1
    for char in temp_number:
        if char.isdigit():
            number *= int(char)
    print(number)


# Home Work 6.2

def format_time(seconds):
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 60 * 60
    SECONDS_IN_DAY = 24 * 60 * 60

    days, remaining_seconds = divmod(seconds, SECONDS_IN_DAY)
    hours, remaining_seconds = divmod(remaining_seconds, SECONDS_IN_HOUR)
    minutes, remaining_seconds = divmod(remaining_seconds, SECONDS_IN_MINUTE)
    secs = remaining_seconds

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    secs = str(secs).zfill(2)

    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    return f"{days} {day_word}, {hours}:{minutes}:{secs}"


user_input = int(input("Введіть кількість секунд (0-8639999): "))

if 0 <= user_input < 8640000:
    result = format_time(user_input)
    print(result)
else:
    print("Число має бути більше або дорівнювати 0 і менше ніж 8640000.")