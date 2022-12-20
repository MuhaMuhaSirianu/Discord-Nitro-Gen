from base64 import urlsafe_b64decode
from http.client import REQUEST_ENTITY_TOO_LARGE
from optparse import check_builtin
import random
import string
from urllib import request


def gen():
    import random

    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    lower_letter = 'abcefghijklmnopqrstuvxyz'
    digits = '0123456789'

    numbtogen = input('how many do I generate')
    upper, lower, nums, = True, True, True,
    all = ""

    if upper:
        all += upper_letter
    if lower:
        all += lower_letter
    if nums: 
        all += digits

        lenght = 23
        amount = numbtogen

        for x in range(int(numbtogen)):
            nitro = ''.join(random.sample(all, lenght))
            print('discord.gift/'+nitro)


            #there is a chance u will get nitro u need to use every single code
            #to see

gen()
gen()
gen()