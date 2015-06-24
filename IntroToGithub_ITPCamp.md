Intro to GitHub
===============

#Process
* Welcome
* Goals for today
* Background/expectation of students

#What Is GitHub?

* Git is a source code version control system, which a series of "commits" or snapshots of your code. You make the commits manually.

* GitHub is a [website](github.com) where you can publish your Git repositories for public download and possible collaboration.

##Why Use It?

*   track changes (a.k.a. version control = undo or go back to earlier version of your program if you made a mistake)
*   to share your code with others

##Version Control models

*   _centralized_ - one central server. each person checks out and merges changes to a main server. only one person can "check out" the code at a time.
*   _distributed_ - each person has a local repository. when they make changes, they "check in" with the main online copy and reconcile the two together. (GitHub is this style)

#Goals of Git

*   It's fast - add to your team and code base quickly
*   it's distributed
*   each commit has a corresponding [hash](https://en.wikipedia.org/wiki/Hash_function) (meaning every single change is tracked)
*   everyone working on the code has a local copy of the history of the program

##Additional notes

*   At first, Git and GitHub are confusing! It's okay! You'll learn with practice/repetition
*   You can use GitHub on the command line/terminal or with a program (like GitHub For Mac).
*   Yes, this is _the _standard that most people use to distribute code
*   You can even use this to post just text or other non-code files online
*   People like using GitHub because it allows them to easily share code, write notes about it, find code from other people, and even allow people to easily comment and offer code suggestions to each other
*   We primarily started using GitHub in the terminal, which is why the notes you see below are all terminal commands. We switched to the GitHub application near the end.
*   A mental model to use: Pretend you are working on a Word document and you hit undo. Then you hit undo again. Then again. GitHub is a much more robust way to go back and forth in different versions of your own code. (that's called version control). 
*   _You add and commit your code on your own computer (git), and when you are ready you push it online to your repository on your github page._
*   If you fork (aka copy) someone else's code/program, you pull it onto your computer so that you can edit the code. Afterwards, you can push it to your own online repository (aka repo) or you can do a pull request to the original code and that person will look at your code and decide to integrate the two together (or not).

#Terms

* **Command Line** - The computer program we use to input Git commands. On a Mac, it’s called Terminal. On a PC, it’s a non-native program that you download when you download Git for the first time (we’ll do that in the next section). In both cases, you type text-based commands, known as prompts, into the screen, instead of using a mouse.

* **Repository** - A directory or storage space where your projects can live. Sometimes GitHub users shorten this to “repo.” It can be local to a folder on your computer, or it can be a storage space on GitHub or another online host. You can keep code files, text files, image files, you name it, inside a repository.

* **Version Control** - Basically, the purpose Git was designed to serve. When you have a Microsoft Word file, you either overwrite every saved file with a new save, or you save multiple versions. With Git, you don’t have to. It keeps “snapshots” of every point in time in the project’s history, so you can never lose or overwrite it.

* **Commit** - This is the command that gives Git its power. When you commit, you are taking a “snapshot” of your repository at that point in time, giving you a checkpoint to which you can reevaluate or restore your project to any previous state.

* **Branch** How do multiple people work on a project at the same time without Git getting them confused? Usually, they “branch off” of the main project with their own versions full of changes they themselves have made. After they’re done, it’s time to “merge” that branch back with the “master,” the main directory of the project.

*This section comes from [ReadWriteWeb](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1).*



#Setup Git

1. [Signup](https://github.com/) for an account on Github
2. Install [Git](http://git-scm.com/downloads).
3. Open the Terminal (Mac) or the Git Bash app you installed (Windows) or other command line (Linux). 
4. Set your default name. Run ```git config --global user.name "Your Name Here"```
5. Set your default email. Run ```git config --global user.email "your_email@youremail.com"```

#Git Commands

```git init``` Initializes a new Git repository. Until you run this command inside a repository or directory, it’s just a regular folder. Only after you input this does it accept further Git commands.

```git config``` Short for “configure,” this is most useful when you’re setting up Git for the first time.

```git help``` Forgot a command? Type this into the command line to bring up the 21 most common git commands. You can also be more specific and type “git help init” or another term to figure out how to use and configure a specific git command.

```git status``` Check the status of your repository. See which files are inside it, which changes still need to be committed, and which branch of the repository you’re currently working on.

```git add``` This does not add new files to your repository. Instead, it brings new files to Git’s attention. After you add files, they’re included in Git’s “snapshots” of the repository.

```git commit``` Git’s most important command. After you make any sort of change, you input this in order to take a “snapshot” of the repository. Usually it goes git commit -m “Message here.” The -m indicates that the following section of the command should be read as a message.

```git branch``` Working with multiple collaborators and want to make changes on your own? This command will let you build a new branch, or timeline of commits, of changes and file additions that are completely your own. Your title goes after the command. If you wanted a new branch called “cats,” you’d type git branch cats.

```git checkout``` Literally allows you to “check out” a repository that you are not currently inside. This is a navigational command that lets you move to the repository you want to check. You can use this command as git checkout master to look at the master branch, or git checkout cats to look at another branch.

```git merge``` When you’re done working on a branch, you can merge your changes back to the master branch, which is visible to all collaborators. git merge cats would take all the changes you made to the “cats” branch and add them to the master.

```git push``` If you’re working on your local computer, and want your commits to be visible online on GitHub as well, you “push” the changes up to GitHub with this command.

```git pull``` If you’re working on your local computer and want the most up-to-date version of your repository to work with, you “pull” the changes down from GitHub with this command.

#Create Your First Repo

1. Go to [Github.com](http://github.com) and click plus and New Repository.
2. Give it a name and short description. Let's call this MyProject. Click the *Create Repository* button.
3. Go back to the terminal. Type ```mkdir ~/MyProject``` to make a directory (folder) called MyProject inside your home folder.
4. To get into that folder, we type ```cd ~/MyProject```. ```cd``` means change directory. It lets us navigate through folders on our computer in the command line.
5. We're inside the folder. We type ```git init``` to initialize it and have git track its changes.
	6. Let's make a readme file. Make a file called README and type a description and save it with a .md extension (see later section on markdown, the formatting system that is favored by github for readme and text files). 
7. Type ```git status``` to see if git notices there's a new file. It should say that there is an *untracked* file.
8. ```git add ReadMe``` to track the file
9. ```git commit -m "Initial commit of ReadMe"``` The m indicates we're saving a message about what we're doing.
10. We want to push these changes online. First we need to connect our local folder on our computer to the online repo. ```git add git remote add origin https://github.com/username/myproject.git```
11. Now let's push these changes to our online repo. ```git push origin master```
12. Log back into your github online and you should see those changes!

#Website fun

* Follow coder-people you like to see their repos
* Search by language
* Fork other's projects
* Pull requests and issues and wikis, oh my!

#Markdown

* Markdown is a markup language with plain text formatting syntax designed so that it can be converted to HTML and many other formats using a tool by the same name. Markdown is used by github (and other sites) to format text and readme files. You can do it in the terminal, in a text editor, on github.com or with the program [Mou](http://25.io/mou/), among others.
* Many places to learn markdown, such as [here](https://en.wikipedia.org/wiki/Markdown) on wikipedia.
 
#More Git

*To see all your commits**

*   git log

OR

*   git log --pretty=oneline
*

**GUI/Graphical Interface**

[](http://git-scm.com/downloads/guis)http://git-scm.com/downloads/guis

**Undoing Local Changes If You Make A Mistake**

*   git rm -f my_incorrect_file.txt
*

**Branching**

*   git checkout -b version2

Adding new lines

*   git add hello_world.txt
*   git commit -m "Adding changes"

Find which branch you're in

*   git branch

**Merging Branches**

*   git merge version2

 
Here is a wee note, probably not a great addition. (mifga)
