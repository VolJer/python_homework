def read_file_into_lines(file_path):
    #this file will be recognised as a module that you can import into your working notebook.
    #import utilities
    #utilities.read_file_into_lines
    """
    A simple function to read a file into
    a list of lines, removing the newline
    character at the end.

    Arguments:
    ==========
    file_path: str
        The location of a text file to read.

    Returns:
    ========
    list[str]
        A list that contains all stripped lines
        of the input text file.
    """
    lines = []
    with open(file_path, 'r') as infile:
        for line in infile.readlines():
            cleaned = line.rstrip()
            lines.append(cleaned)
    return lines

def file_to_list(path):
    lines = []
    with open(path, 'r') as infile:
        for line in infile.readlines():
            lines.append(line.strip())
    return lines