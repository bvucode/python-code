import time, math
a, b = 0, 0
print("\x1b[2J", end='')
while True:
    z = [0] * 1760
    s = [' '] * 1760
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(a)
            f = math.sin(j)
            g = math.cos(a)
            h = d + 2
            r = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(b)
            n = math.sin(b)
            t = c * h * g - f * e
            x = int(40 + 30 * r * (l * h * m - t * n))
            y = int(12 + 15 * r * (l * h * n + t * m))
            o = int(x + 80 * y)
            q = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 22 > y and y > 0 and x > 0 and 80 > x and r > z[o]:
                z[o] = r
                s[o] = ".,-~:;=!*#$@"[q if q > 0 else 0]
    print('\x1b[H', end='')
    for k in range(1761):
        print((s[k] if k % 80 else '\n'), end='')
        a += 0.00004
        b += 0.00002
