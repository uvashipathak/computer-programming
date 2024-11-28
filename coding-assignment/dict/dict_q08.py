"""
@geeksforgeeks
Program to create grade calculator in Python
"""


def calculate_grade(data: dict[str, object]) -> str:
    """
    :param data:
        data of the student including his name, his score in assignments, his score in tests,
        and his score in lab
        The expected structure is:
                 {
                     'name': str,                     # The name of the student
                     'assignments': list[int],        # List of scores from assignments
                     'tests': list[int],              # List of scores from tests
                     'lab': list[int]                 # List of scores from lab works
                 }
    :return:
        his grade based on the following formula:
            score >= 90 : "A"
            score >= 80 : "B"
            score >= 70 : "C"
            score >= 60 : "D"
            score < 60  : "F"
        where score is:
            10% of marks scored from submission of Assignments
            70% of marks scored from Test
            20% of marks scored in Lab-Works
    """
    score = sum(data['assignments']) / 10 + sum(data['tests']) / 70 + sum(data['lab']) / 20
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
