import os

MAXIM_FILE_NAME = '.maxim-git-repos'
gitCommands = {'fetch': 'git fetch', 'pull': 'git pull --rebase', 'status': 'git status --short --branch'}

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
        return repos
    else:
        print 'run first: init'
        raise Exception('run first: python maxim-git init')

def runInRepos(commands):
    repos = readRepos()
    for r in repos:
        os.chdir(r)
        for command in commands:
            print command
            os.system(command)
        os.chdir('..')

if __name__ == "__main__":
    import sys
    if sys.argv[1] == 'init':
        init()
    else:
        commands = []
        for arg in sys.argv[1:]:
            commands.append(gitCommands[arg])
        runInRepos(commands)
