import plotly.express as px


def main():
    while True:
        print("0 - Exit program")
        print("1 - Input size of prime numbers")
        print("2 - Generate plot")
        option = input("Enter option: ")

        # check option input
        if option not in ['0', '1', '2']:
            print("Option does not exist!\n")
            continue
        if option == '0':
            break
        elif option == '1':
            while True:
                prime_nums = []
                nums = []  # empty list
                size_of_prime_nums = 0
                size_of_prime_nums = input("Input the size of prime numbers to create: ")

                # check size input
                if not size_of_prime_nums.isnumeric():
                    print("Enter reasonable size!")
                    continue

                # cast to int
                size_of_prime_nums = int(size_of_prime_nums)

                # generate numbers list
                for i in range(2, size_of_prime_nums):
                    nums.append(i)

                # generate prime numbers list
                for i in nums:
                    for j in nums:
                        if i == j:
                            continue
                        if i % j == 0:
                            break
                        if j == nums[-1]:
                            prime_nums.append(i)

                # display all prime numbers
                print("Prime numbers are: ")
                for i, num in enumerate(prime_nums):
                    if i % 15 == 0 and i != 0:
                        print(f"{num}, ")
                    elif num == prime_nums[-1]:
                        print(f"{num}\n")
                    else:
                        print(f"{num}, ", end="")
                break

        elif option == '2':
            fig = px.scatter_polar(r=prime_nums, theta=prime_nums, start_angle=0, direction="counterclockwise")
            fig.show()


if __name__ == "__main__":
    main()
