# maxim-git
Machine gun like productivity with multiple Git repos. Runs given commands in Git subdirectories. 

## Installation
Install python
```
git clone git@github.com:rjkokko/maxim-git.git
cd maxim-git
./instal-maxim-git.sh
```
Go to the parent directory of your Git repositories and run
```
maxim init
```
You are ready to shoot commands!

## Examples
Fetch remotes and show statuses
```
maxim fetch status
```
Checkout masters and pull remotes
```
maxim 'git checkout master' pull
```
Run any terminal command. Use quotation marks with arguments.
```
maxim pwd 'ls -la'
```

## Kudos
Inspiration from @jteuho's pommit. https://github.com/jteuho/scripts
