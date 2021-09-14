import argparse

FIXED = 55

def to_deci(num_bit, expression):
    deci = 0
    length = len(expression)
    for i in range(length):
        sim = expression[length - i - 1]
        if sim >= "A":
            deci += num_bit ** i * (ord(sim.upper()) - FIXED)
        else:
            deci += num_bit ** i * int(sim)
    return deci
    
def deci_to(num_bit, expression):
    num = int(expression)
    new_exp = ""
    while num != 0:
        quo = num % num_bit
        num //= num_bit
        new_exp += str(quo) if quo < 10 else str(chr(quo + FIXED))
    return new_exp[::-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bit', type=int, help='Bit base')
    parser.add_argument('--exp', type=str, help='Expression to convert')
    parser.add_argument('--r', action='store_true', help='Reverse direction')
    opt = parser.parse_args()
    if opt.r:
        print(deci_to(opt.bit, opt.exp))
    else:
        print(to_deci(opt.bit, opt.exp))
        

