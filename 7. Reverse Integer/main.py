def reverse(x: int) -> int:
    result = ""
    minus = False
    if x < 0:
        minus = True
        x *= -1
    while x > 9:
        result += f"{x % 10}"
        x //= 10
    result = int(result + f"{x}")
    if minus:
        result *= -1
    return result

