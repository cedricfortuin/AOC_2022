def day1(file):
    print("Day 1: {}".format(max(file)))




def main():
    with open('test.txt') as file:
        input_file = file.read().split('\n\n')
        total = [sum([int(i) for i in k.split('\n')]) for k in input_file]
        day1(total)

if __name__ == '__main__':
    main()