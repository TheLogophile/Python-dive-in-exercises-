# Write a program that generates a random vehicle license plate number.

import random

VALID_PLATE_PARTS = {
    "letters": [
        "ب", "ج", "د", "س", "ص", "ط", "ق", "ل", "م", "ن", "و", "هـ", "ی",  # letters allowed for private plates
        "الف", "پ", "ت", "ث", "ع", "ک", "ش", "ف", "ز", "ژ",  # letters used in special plates
    ],
    "province_codes": [
        "10", "11", "20", "22", "33", "40", "44", "50", "55", "60", "66", "77", "88", "99",  # Tehran
        "21", "30", "38", "68", "78",  # Alborz
        "12", "32", "36", "42", "74",  # Khorasan Razavi
        "26", "52",  # North & South Khorasan
        "13", "23", "43", "53", "67",  # Isfahan
        "63", "73", "83", "93",  # Fars
        "14", "24", "34",  # Khuzestan
        "62", "72", "82", "92",  # Mazandaran
        "15", "25", "35",  # East Azerbaijan
        "17", "27", "37",  # West Azerbaijan
        "45", "65", "75",  # Kerman
        "46", "56", "76",  # Gilan
        "85", "95",  # Sistan & Baluchestan
        "19", "29", "39",  # Kermanshah
        "59", "69",  # Golestan
        "84", "94",  # Hormozgan
        "48", "58",  # Bushehr
        "31", "41",  # Lorestan
        "51", "61",  # Kurdistan
        "18", "28", "38",  # Hamedan
        "87", "97",  # Zanjan
        "47", "57",  # Markazi
        "91",  # Ardabil
        "16",  # Qom
        "79", "89",  # Qazvin
        "86", "96",  # Semnan
        "54", "64",  # Yazd
        "98",  # Ilam
        "71", "81",  # Chaharmahal & Bakhtiari
        "49",  # Kohgiluyeh & Boyer-Ahmad
    ]
}

def gen_plate():
    left = "".join(str(num) for num in random.choices(range(1, 10), k=2))
    middle = "\u200E" + random.choice(VALID_PLATE_PARTS["letters"]) + "\u200E"
    right = "".join(str(num) for num in random.choices(range(1, 10), k=3))
    province = random.choice(VALID_PLATE_PARTS["province_codes"])
    parts = [left, middle, right, "- IR" + province]
    return " ".join(parts)

print(gen_plate())