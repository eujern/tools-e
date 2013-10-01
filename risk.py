"""Deploy Risk Evaluator"""

#imports
import sys

from optparse import OptionParser
from sh import git

# constants
REPO_DIR = ""

# exception classes
# interface functions
# classes

# internal functions & classes

def main():
    usage = "Usage: %prog <prevrev> <currev>"
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()
    if len(args) != 2:
        parser.error("incorrect number of arguments")

    print "Repository at: " + REPO_DIR
    repo = git.bake(_cwd=REPO_DIR, _tty_out=False)

    # just to verify
    repo.status()

    print "Repository verified."

    commits  = repo.log(args[0]  + '..' + args[1], '--pretty=format:%h', '--no-color').splitlines()

    print "Number of revisions: " + `len(commits)`

    count = 0

    for revision in commits:
        diffs = repo.show(revision, '--oneline').splitlines()
        # skip first 5 lines
        for line in diffs[5:]:
            if line.startswith("-") or line.startswith("+"):
                count += 1

    print "Lines changed: " + `count`

if __name__ == '__main__':
    status = main()
    sys.exit(status)
