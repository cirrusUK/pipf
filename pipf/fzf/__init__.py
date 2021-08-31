from subprocess import call
import os


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    call(f"{dir_path}/run.sh", shell=True)


if __name__ == "__main__":
    main()
