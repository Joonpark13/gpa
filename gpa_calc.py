import os
from nuapiclient import NorthwesternAPIClient

client = NorthwesternAPIClient(os.environ["NUAPI_KEY"])

class Course:

    def __init__(self, title, term, subject, catalog_num, unit, grade):
        self.title = title
        self.term = term
        self.subject = subject
        self.catalog_num = catalog_num
        self.unit = unit
        self.grade = grade

    def __repr__(self):
        return (self.subject + " " + self.catalog_num + " " + self.title +
                " \nUnits: " + str(self.unit) + " Grade point: " +
                str(self.grade) + "\n")


""" Parses the courses taken in a term

:param term_id: term id used in the api, necessary for querying
:param term_name: term name used in the api and transcript, stored in
    the Course object
:param term_data: list of strings, each string is a line from the
    transcript within this term

:return: a list of course objects for this term
"""
def parse_term(term_id, term_name, term_data):
    courses = []
    # Get all subjects in that term
    subjects = client.subjects(term = term_id)
    # Parse text transcript file
    for line in term_data:
        # If line starts with subject, parse line, create Course object
        if len(line.split()) > 0 and line.split()[0] in [x["symbol"] for x in subjects]:
            title = line[20:54].rstrip()
            subject = line.split()[0]
            catalog_num = line[10:20].rstrip()
            try:
                unit = float(line[54:58])
                grade = float(line[77:82])
                course = Course(title, term_name, subject, catalog_num, unit, grade)
                courses.append(course)
            except ValueError:
                pass
    return courses

def cum_gpa():
    # Calculate and return cumulative gpa
    pass

# Interactive GAP calculation
def main():
    # A complete list of all courses from transcript
    courselist = []

    # Get all terms
    terms = [{"name":x['name'], "id":x["id"]} for x in client.terms()]
    # If beginning of line matches a term, parse all lines following that term
    # until the next term
    term_lines = []
    with open("transcript.txt", 'r') as file:
        for line in file:
            # Take the first two words of each line and compare to a term name
            if len(line.split()) >= 2:
                stripped_line = line.split()[0] + " " + line.split()[1]
            else:
                stripped_line = ""
            # If a term line has been found, parse the current list, then reset
            # the list
            if stripped_line in [x["name"] for x in terms]:
                courselist += parse_term(x["id"], stripped_line, term_lines)
                term_lines = []
            else:
                term_lines.append(line)

    # User interaction

if __name__ == "__main__":
    main()