import sciencii.periodic_table as periodic_table
import sys

def main():
    arg_num = len(sys.argv)
    if arg_num == 1:
        print("You must input an element.")
    else:
        for i in range(1,arg_num):
            periodic_table.get_art(sys.argv[i])

if __name__ == "__main__":
    main()