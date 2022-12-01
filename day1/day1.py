def day1(yeet):
    print("Day 1.1: {}".format(max(yeet)))


def day2(yeet):
    print("Day 1.2: {}".format(sum(sorted(yeet, reverse=True)[:3])))


def main():
    with open('input.txt') as file:
        input_file = file.read().split('\n\n')
        total = [sum([int(i) for i in k.split('\n')]) for k in input_file]
        day1(total)
        day2(total)

if __name__ == '__main__':
    main()