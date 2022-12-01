def main():
        total = [sum([int(i) for i in k.split('\n')]) for k in open('input.txt', 'r').read().split('\n\n')]
        print("Day 1.1: {} \nDay 1.2: {}".format(max(total), sum(sorted(total, reverse=True)[:3])))


main()
