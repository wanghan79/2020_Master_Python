import random
import string


def generate_set():
    set_s = set()
    for i in range(0, 1000):
        set_s.add(random.uniform(0, 100))
    for i in range(0, 1000):
        len = random.randint(1, 10)
        value = ''.join(random.sample(string.ascii_letters + string.digits, len))
        set_s.add(value)
    return set_s


def pick_needed():
    set_in_pick_needed = generate_set()
    set_needed = set()
    for element_needed in set_in_pick_needed:
        if isinstance(element_needed, float):
            if (element_needed >= 20) and (element_needed <= 50):
                set_needed.add(element_needed)
        elif isinstance(element_needed, str):
            if "at" in element_needed:
                set_needed.add(element_needed)
    return set_needed


def main():
    set_in_main = pick_needed()
    for element in set_in_main:
        print(element)


if __name__ == '__main__':
    main()
