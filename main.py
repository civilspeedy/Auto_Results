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

    def close(self):
        self.database.close()


def view_results():
    print("view results")


def clear_results():
    print("clear results")


def main():
    """Main loop"""
    data = Database()
    print("<<Select option:\n[1]Add results\n[2]View Results\n[3]Clear Results>>")
    choice = int(input(">>"))
    match choice:
        case 1:
            while True:
                unit = input("<<<Enter the unit code>>\n>>")
                response = input(f"<<Unit is '{unit}'>>\n<<Is that correct? [y]/[n]>>\n>>")  # confirming user choice
                if response.lower() == "y":
                    break
        case 2:
            view_results()
        case 3:
            clear_results()
        case other:
            print("<<INVALID INPUT>>")


main()
input()
