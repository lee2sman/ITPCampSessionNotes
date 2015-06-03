Intro To The Command Line
=========================

#Welcome

* About Me
* Goals of this session
* What do you want to learn? (questions?)

#Why use the command line in 2015?

*   simplicity and minimalism (see [article](http://en.wikipedia.org/wiki/Unix_philosophy) on Unix philosophy)
*   ubiquity - nearly every computer from OS X, Raspberry Pi to web servers, internet devices, routers and robots can be controlled through the command line, and even more devices are being created that can be interacted with that are online (the so-called "Internet Of Things")
*   Works on devices that don't have a screen, mouse, etc
*   Some tasks are lightyears faster (instant) when calling the command from the command line instead of using a specific application or having to find a specific program to download from the internet
*   write your own scripts for common commands/procedures that you need to do on your computer (_random example: you could create a command to batch resize a folder of photos and rename them.)_


# Philosophy of the Command Line

*   The OSX command prompt is a place where you can type commands to manipulate files on your computer or launch programs that perform complex tasks.
*   In some ways the command prompt is the _simplest_ kind of computer interface. You are probably more familiar with interfaces that have windows and buttons, but the command prompt is an interface entirely driven by text input. Type a command. The command is performed. You are prompted to enter another command. Yes, it is _that_ simple.
*   Writing a program for the command prompt is _much easier_ than writing a program with a graphical interface (windows and buttons). So much easier, in fact, that the majority of programs written today are written for the command prompt. This is why learning to use the command prompt will open up a whole new world for you. You will have access to a vast array of programs and technologies that were previously off-limits. 

*   _taken from _[The Designers Guide To The OS X Command Prompt](http://wiseheartdesign.com/articles/2010/11/12/the-designers-guide-to-the-osx-command-prompt/)

#How to access the command line

* Mac Os X - Terminal
* On Windows we're going to use PowerShell. If you have Windows 7 or later, do this: 1. Click Start. 2. In "Search programs and files" type: powershell 3. Hit Enter.

#Definitions

The **command-line interface**, sometimes referred to as the CLI, is a tool into which you can type text commands to perform specific tasks—in contrast to the mouse's pointing and clicking on menus and buttons. Since you can directly control the computer by typing, many tasks can be performed more quickly, and some tasks can be automated with special commands that loop through and perform the same action on many files—saving you, potentially, loads of time in the process.

The application or user interface that accepts your typed responses and displays the data on the screen is called a **shell**, and there are many different varieties that you can choose from, but the most common these days is the **Bash** shell, which is the default on Linux and Mac systems in the **Terminal** application.

**Bash** is a Unix shell and command language written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell. It was released in 1989! It has been distributed widely as a default shell on Linux and OS X. In the late 1990s, Bash was a minor player among multiple commonly used shells; at present Bash has overwhelming favor.

Bash is a command processor that typically runs in a text window, where the user types commands that cause actions. Bash can also read commands from a file, called a script. 

#Getting Started

* moving around
* some simple commands/programs
* piping
* package managers / how to get "programs" with Brew

#The Commands

###pwd

* print working directory

###ls

* First, let's display a list of files inside the active folder. You can pass a number of parameters to the command to display extra details or change the sorting. For instance, if I add -l to the end of my ls command, I'll see a detailed listing; -S will sort by file size; and -r will reverse the sorting. You could use a combination of these together, like this command, which will show all files sorted by file size with the largest files at the bottom:
* if you do -a there are two entries for "." and ".." at the beginning of the list. These represent the current folder—the "." folder—and the parent folder—the ".." folder.

* ls -a
* ls -1
* on a PC it is DIR

###cd

change between directories using the cd command

* cd
* cd .
* cd ..
* cd -

###mkdir

* make a fdolder

###rmdir

* remove it

###touch

* make a blank file

###rm

* delete a blank file
* rm filename
* rm * (remove everything in the file)

###nano filename

* edits or creates a file to edit

###more or less

* lets you read contents of a screen

###Find a Text String in Files

The grep command can be used to quickly find text within files, even searching through subdirectories. For instance, if you wanted to search through all files in the current directory and below it for "text string", you could use this command:

grep –ir "text string" *

###man

Manuals/help

###Stop a command

Control - C
Quit out of reading with q


##Command Redirection

Each command line application can accept standard input and writes to standard output, and you can use the > or | operators to redirect output from one command into another, which lets you chain commands together into much more powerful commands.


For instance, if you want to use ls –l to display a list of files but it keeps scrolling off the screen, you can pipe the output from the ls –l command into the input of the more command by using the | character:

ls –l | more

If you wanted to save the output of that list directly into a file instead of displaying on the console, you could use the > operator to redirect the output into a file instead:

ls -l > filename.list

You could then use the cat command to display the contents of that file, pipe that into the grep command (detailed further below), and then redirect that output into a separate file:

cat filename.list | grep keyword > filefound.list

## Running a Script in the Current Folder

If you have an application or shell script in the current folder, you can't simply type the name of the command and expect it to start. You'll need to add a ./ to the beginning of the command in order to start it. Why? Because in the Bash shell, the current directory, or "." folder, is not included in the system path. So to launch scriptname.sh in the current folder, you'll need to use:

./scriptname.sh

##History

Up and down arrow keys

##Using Aliases
Aliases save you loads of time by shortening long, complicated commands down into really simple ones, or by setting the default parameters to a command so you don't have to type them every time. For instance, if you wanted to set up an alias for installing packages on your Ubuntu setup that's quicker and simpler than sudo apt-get install packagename, you could use something like this:

alias ll="ls -l"

###Package Manager - Homebrew

* Homebrew is a package manager, sort of like an open source app store for the terminal on OS X. Go to [this website](brew.sh) and it will tell you to copy this command to the terminal and run it to install brew on your system.

```ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

Some useful brew programs:

* Fish (an alternative Shell i prefer) - brew install fish
* imagemagick - brew install imagemagick
* sox - audio player and audio manipulating - brew install sox 
* fortune - gives you a random fortune - brew install fortune 
* mailcheck - checks all of your inboxes at once - brew install mailcheck
