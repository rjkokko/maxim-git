import os

MAXIM_FILE_NAME = '.maxim-git-repos'
gitShorthands = {'fetch': 'git fetch', 'pull': 'git pull --rebase', 'status': 'git status --short --branch'}

def printHelp():
    print
    print 'maxim [help] [init] [git_shorthand]... [command]...'
    print ''
    print 'init'
    print '        Creates .maxim-git-repos files'
    print 'git_shorthand>...'
    print '        Available commands are'
    print '        fetch'
    print '        pull'
    print '        status'
    print '<command>...'
    print '        Any bash command.'
    print ''
    print 'examples:'
    print "       maxim pull"
    print ''
    print "       maxim fetch status"
    print ''
    print "       maxim 'git checkout master' pull"
    print ''
    print "       maxim pwd 'ls -la'"


def init():
    dirs = []
    for entry in os.listdir('.'):
        if os.path.isdir(entry) and os.path.isdir(entry + '/' + '.git'):
            dirs.append(entry)

    if os.path.exists(MAXIM_FILE_NAME):
        print 'maxim-git intialized already'
    else:
        f = open(MAXIM_FILE_NAME, 'w')
        for dir in dirs:
            print dir
            f.write(dir + '\n')
        f.close()
        print 'Initialized maxim-git repositories file'

def readRepos():
    if os.path.exists(MAXIM_FILE_NAME):
        f = open(MAXIM_FILE_NAME, 'r')
        repos = []
        for line in f:
            repos.append(line.replace('\n', ''))
        f.close()
        return repos
    else:
        print 'run first: init'
        raise Exception('run first: maxim init')

def runInRepos(commands):
    repos = readRepos()
    for repo in repos:
        print '--------------------------------------'
        os.chdir(repo)
        for command in commands:
            print './' + repo + '$ ' + command
            ret = os.system(command)
            if ret > 0:
                raise Exception(ret)
        os.chdir('..')

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2 or sys.argv[1] == 'help' or sys.argv[1] == '--help' or sys.argv[1] == '-h':
        printHelp()
    elif sys.argv[1] == 'init':
        init()
    else:
        commands = []
        for arg in sys.argv[1:]:
            if arg in gitShorthands:
                commands.append(gitShorthands[arg])
            else:
                commands.append(arg)
        runInRepos(commands)
