import os
from nuapiclient import NorthwesternAPIClient

client = NorthwesternAPIClient(os.env["NUAPI_KEY"])

class Course:

    def __init__(self, title, term, subject, catalog_num, unit, grade):
        self.title = title
        self.subject = subject
        self.catalog_num = catalog_num
        self.unit = unit
        self.grade = grade


# A complete list of all courses from transcript
courselist = []

""" Parses the courses taken in a term

:param term_id: term id used in the api, necessary for querying
:param term_name: term name usedi in the api and transcript, stored in
    the Course object
:param term_data: list of strings, each string is a line from the
    transcript within this term

:return: a list of course objects for this term
"""
def parse_term(term_id, term_name, term_data):
    # Parse text transcript file
    #       If line starts with subject, parse line, create Course object
    pass

def cum_gpa():
    # Calculate and return cumulative gpa
    pass

# Interactive GAP calculation
def main():
    # Get all terms
    # If beginning of line matches a term, parse all lines following that term until the next term

    pass

    # User interaction

if __name__ == "__main__":
    main()