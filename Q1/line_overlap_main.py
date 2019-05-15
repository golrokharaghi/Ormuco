from line_overlap import line_overlap

if __name__ == '__main__':
    try:
        print('Enter the coordinates for the first line:')
        x1,x2 = map(float, input().split())

        print('Enter the coordinates for the second line:')
        x3,x4 = map(float, input().split())

        line1 = (x1, x2)
        line2 = (x3, x4)

        result = line_overlap(line1, line2)
        print(result)

    except ValueError:
        print('Unexpected input format')
