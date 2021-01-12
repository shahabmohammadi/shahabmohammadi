"""
Module to create README for Github Profile.
"""

import io
from datetime import datetime


def create_readme():
    """
    Creates the Readme.md from the Readme template.
    """

    readme = io.open('../readme.md', 'w+')
    for line in io.open('readme.template.md', 'r'):
        line = line.replace('{{age}}', get_age('1994-09-19'))
        readme.write(line)
    readme.close()


def get_age(dob):
    """
    Returns the age of the entity.
    """

    now = datetime.now()
    dob = datetime.strptime(dob, '%Y-%m-%d')
    age = (now - dob).days
    return str(age)



def main():
    """
    Main function for the Module.
    """

    create_readme()


if __name__ == '__main__':
    main()
