DIAL_CODES = [
    (86,'china'),
    (91,'india'),
    (1,'u s'),
]

country_code = {country:code for code,country in DIAL_CODES}
print(country_code)

print({country.upper():code for code,country in DIAL_CODES})