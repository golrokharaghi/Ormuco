from version_comparison import version_comparison

if __name__ == '__main__':
    try:
        print("Enter the first version string:")
        str1 = input()
        print("Enter the second version string:")
        str2 = input()

        result = version_comparison(str1, str2)
        print(result)

    except ValueError:
        print('Unexpected input format')
