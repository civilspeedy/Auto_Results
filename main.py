import sqlite3


class Database:
    def __init__(self):
        self.database = sqlite3.connect("results.db")
        self.database.cursor().execute("""CREATE TABLE IF NOT EXISTS Results(Unit VARCHAR(3) PRIMARY KEY, Medium 
        Varchar(10), Mark INTEGER)""")

    def get_connection(self):
        return self.database


def add_results():
    print("add results")


def view_results():
    print("view results")


def clear_results():
    print("clear results")


def main():
    """Main loop"""
    print("<<Select option:\n[1]Add results\n[2]View Results\n[3]Clear Results>>")
    choice = int(input(">>"))
    match choice:
        case 1:
            add_results()
        case 2:
            view_results()
        case 3:
            clear_results()
        case other:
            print("<<INVALID INPUT>>")


main()
input()
