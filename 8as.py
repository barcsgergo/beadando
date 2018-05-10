


def lcs(a,b):

    if not a or not b:
        return ''

    x, xs, y, ys = a[0], a[1:], b[0], b[1:]

    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(a, ys), lcs(xs, b), key=len)


print(lcs('valami','lamiamidrmekmf'))