import phonenumbers

from phonenumbers import geocoder
number = input("enter the number you want to check with country code : ")
print(number)

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "IND")
print(carrier.name_for_number(service_number, "en"))