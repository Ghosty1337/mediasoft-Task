def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")


def sort_by_second_array(first_array: list[int], second_array: list[int]):
    interval_list = []
    for i in range(len(second_array)):
        interval_list.append({
            "index": i,
            "value": second_array[i]
        })
    second_array = sorted(interval_list, key=lambda x: x['value'])
    return [first_array[i["index"]] for i in second_array]


def similar_letters(strings_list: list[str]):
    letters = []
    for i in strings_list[0]:
        interval_list = []
        for j in strings_list:
            if i in j:
                interval_list.append(j.replace(i, '', 1))
            else:
                break
        else:
            letters.append(i)
            strings_list = interval_list
    return letters


def main():
    fizzbuzz()
    print(sort_by_second_array([1, 4, 6], [11, 33, 22]))
    print(similar_letters(["bella", "label", "roller"]))
    print(similar_letters(["cool", "lock", "cook"]))
    print(roman_number_to_int("MCMXCIVIX"))


def roman_number_to_int(roman_number: str):
    checks = {
        "IV": 2,
        "IX": 2,
        "XL": 20,
        "XC": 20,
        "CD": 200,
        "CM": 200
    }
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = sum(values[char] for char in roman_number)
    number -= sum(value for key, value in checks.items() if key in roman_number)
    return number


if __name__ == "__main__":
    main()
