
def possible(target: int, numbers: list):
    if len(numbers) == 1:
        return target == numbers[0] # boolean

    if target % numbers[-1] == 0 and possible(target // numbers[-1], numbers[:-1]):
        return True

    if target > numbers[-1] and possible(target - numbers[-1], numbers[:-1]):
        return True

    str_target = str(target)
    str_last   = str(numbers[-1])
    if len(str_target) > len(str_last) and str_target.endswith(str_last) and possible(int(str_target[:-len(str_last)]), numbers[:-1]):
        return True
    else:
        return False
res = 0
for line in open("7.in"):
    left, right = line.split(':')
    target = int(left)
    numbers = [int(x) for x in right.split()]

    if possible(target, numbers):
        res += target

print(f"Résultat partie 1: {res}")