def reverse_digits(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num
num = int(input("Enter a number to reverse: "))
print(f"Reversed number: {reverse_digits(num)}")
