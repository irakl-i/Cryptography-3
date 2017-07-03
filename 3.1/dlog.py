import math

# Find x such that g^x = h (mod p)
# 0 <= x <= max_x


hash_dict = {}


def discrete_log(g, h, p, max_x):
    b = 1 << 20
    gp_inverse = pow(g, p - 2, p)  # works if p is prime, which it is.
    g_pow = pow(g, b, p)
    res = 0

    med = h
    for i in xrange(b):
        hash_dict[med] = i
        med *= gp_inverse
        med %= p

    ned = 1
    for j in xrange(b):
        if ned in hash_dict:
            res = hash_dict[ned]
            break
        ned *= g_pow
        ned %= p

    print j * b + res


def main():
    p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
    g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
    h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
    max_x = 1 << 40  # 2^40
    discrete_log(g, h, p, max_x)


if __name__ == '__main__':
    main()
