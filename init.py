class Meny:
    def __init__(self):
        self.list = 0

    def print_list(self):
        count = len(self.list) - 1
        for i in self.list:
            print(str(count) + ". " + i[0])
            count -= 1

    def select_list(self, answer):
        count = len(self.list) - 1
        for i in self.list:
            if count == int(answer):
                print("\n" + i[0])
                return i[1]()
            count -= 1

class Meny_main(Meny):
    def __init__(self):
        self.list = [
            ["Telnet", Meny_telnet],
            ["SSH", Meny_ssh],
            ["Exit", Exit]
        ]

class Meny_telnet(Meny):
    def __init__(self):
        self.list = [
            ["Scan telnet", Meny_main],
            ["Exit", Exit]
        ]

class Meny_ssh(Meny):
    def __init__(self):
        self.list = [
            ["Scan SSH", Meny_main],
            ["Exit", Exit]
        ]

class Exit(Meny):
    def __init__(self):
        raise SystemExit(1)

def main():
    print("Welcome to greenade")
    x = Meny_main()
    while True:
        x.print_list()
        x = x.select_list(input())

main()
