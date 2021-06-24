# pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

#importing number from file
number = ""
with open('number.txt', 'r') as f:
    number = f.read()

# enter your phone number with country code (ex - "+9112345677")
phone_number = phonenumbers.parse(number)

# this will give the country name
print(geocoder.description_for_number(phone_number, 'en'))

# this will print the service provider
print(carrier.name_for_number(phone_number, 'en'))

# this will print the timezone
print(timezone.time_zones_for_number(phone_number))

# thanks for watching 😀