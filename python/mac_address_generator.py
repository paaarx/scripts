import random


def mac_address_generator(separator='-', case='upper'):

    mac_address = separator.join(f'{hex_number:02x}'.upper() \
        for hex_number in [random.randint(0x0, 0xff) for _ in range(6)])

    if case == 'lower':
        return mac_address
    else:
        return mac_address.upper()