import sqlite3


class Database:
    def __init__(self):
        self.database = sqlite3.connect("results.db")
        self.database.cursor().execute("""CREATE TABLE IF NOT EXISTS Results(Unit VARCHAR(3) PRIMARY KEY, Medium 
        Varchar(10), Mark INTEGER)""")

    def add_results(self, unit, medium, mark):
        self.database.execute("""INSERT INTO Results(Unit, Medium, Mark) VALUES(?, ?, ?)""",
                              (unit, medium, mark))
        self.database.commit()
        self.database.close()
        return True

    def view_results(self):
        print("view results")

    def clear_results(self):
        print("clear results")


def main():
    """Main loop"""
    print("<<Select option: [1]Add results [2]View Results [3]Clear Results>>")
    choice = int(input(">>"))
    match choice:

        case 1:
            entries = {1: "unit code", 2: "medium of assessment", 3: "mark"}
            second_loop = True
            unit = ""
            medium = ""
            mark = ""

            for entry in entries:
                first_loop = True
                second_loop = True

                while first_loop:
                    choice = input(f"<<Enter {entries[entry]}>>\n>>")

                    while second_loop:
                        yes_or_no = input(f"<<{entries[entry]} is {choice}. Is that correct?[y]/[n]>>\n>>").lower()

                        if yes_or_no == "y":
                            match entry:
                                case 1:
                                    unit = choice
                                case 2:
                                    medium = choice
                                case 3:
                                    mark = choice

                            first_loop = False
                            second_loop = False

                        if yes_or_no == "n":
                            second_loop = False

                        if yes_or_no != "y" and yes_or_no != "n":
                            print("<<Invalid input. Please try again.>>")

            print(unit, medium, mark)
            print("<<Now adding to Database>>")

            data = Database()

            if data.add_results(unit, medium, mark):
                print("<<Results successfully added to Database>>")

            else:
                print("<<Something went wrong>>")

        case 2:
            data = Database()
            data.view_results()
        case 3:
            data = Database()
            data.clear_results()
        case other:
            print("<<INVALID INPUT>>")


main()
input()
