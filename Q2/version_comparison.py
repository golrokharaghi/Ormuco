
def version_comparison(str1, str2):
    """
    Function VersionComparison takes two version strings as input
    and determines whether one is greater than, equal, or less than the other.

    As an example: 1.2 is greater than 1.1, but a.b is less than a.b.a

    Parameters:
        str1 : string representing a version
        str2 : string representing a version

    Returns:
        Message indicating if one version is greater than, equal, or less than the other.
    """

    # In case the version string has a delimiter other than '.' like: '1-2', replace it with '.'
    s1 = "".join([ c if c.isalnum() else "." for c in str1 ])
    s2 = "".join([ c if c.isalnum() else "." for c in str2 ])

    v1 = s1.split('.')
    v2 = s2.split('.')

    # If two versions do not have the same length, insert zero to the one with the shortest length
    if len(v1) < len(v2):
        v1 = v1 + ['0'] * (len(v2) - len(v1))
    else:
        v2 = v2 + ['0'] * (len(v1) - len(v2))

    # Compare two versions element by element
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return('{} is greater than {}'.format(str1, str2))
        elif v1[i] < v2[i]:
            return('{} is less than {}'.format(str1, str2))

    return('{} is equal to {}'.format(str1, str2))
