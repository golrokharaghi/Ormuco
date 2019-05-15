
def line_overlap (line1, line2):
    """
    Function Overlap takes the coordinates of two lines on x axis
    and determines whether they overlap, or not.
    For example (1,5) and (2,6) overlap, (3,1) and (2,5) overlap,
    but (-1,5) and (6,8) do not overlap.

    Parameters:
        line1 : tuple (float, float)
        line2 : tuple (float, float)

    Returns:
        Message indicating if the lines overlap or not.
   """

    if (min(line1) > max(line2)) or (min(line2) > max(line1)):
        return('The lines {} and {} don\'t overlap.'.format(line1, line2))
    else:
        return('The lines {} and {} overlap.'.format(line1, line2))
