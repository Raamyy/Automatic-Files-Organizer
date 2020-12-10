import sys
from organise_files.organize_files import organise_directory
def main():
    directory_tobe_cleaned = ""
    if len(sys.argv) < 2:
        print(f"""Please enter a directory to clean. 
        as \"py {sys.argv[0]} path/to/directory\"""")
        exit()
    else:
        directory_tobe_cleaned = sys.argv[1]
    organise_directory(directory_tobe_cleaned)
    print("Done!")


if __name__ == "__main__":
    main()