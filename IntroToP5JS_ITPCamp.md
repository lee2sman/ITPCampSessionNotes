Intro To P5JS
=============

* Welcome
* Background/expectations
* Overview of today's class


# What is Processing?

* Who invented it? Why? What is it used for? 
* Concept of a digital sketch / fast iteration
* Review a basic program
* Setup and Draw loop

# What is P5JS?
* Goals
* Who invented it? Why? What is it used for?
* P5js is a JavaScript library
* JavaScript - a programming language used as part of web browsing. Allows scripts to interact with user, control browser, communicate asynchronously, alter document contents.
* library - a collection of resources used to develop software. Designed for re-use. Extends functionality of a language. Can be used by multiple programs that have no relation to each other.

# Differences from Processing

* It's a Javascript library (as opposed to a Java subclass)
* Syncronous versus asynchronous
* Served by a server!
* Can interact with the web - CSS, HTML, DOM functionality. Can work with other libraries.

# Install / Get P5JS libraries

* Download P5JS libraries
* Download the editor
* Get a text editor program such as SublimeText or Atom

# Starter code

```
// Homage to Black Square
// CC0 Lee Tusman 2015

function setup() {
  createCanvas(800,800);
  background(255);
  rectMode(CENTER);
}

function draw() {
  fill(0);
  rect(width/2,height/2,width/2,height/2);
}
```

# Using a server to serve your program

* Why do you have to do this?
* Using python simpleserver to serve your programs

```
cd path/to/folder
python -m SimpleHTTPServer
```
Open your browser and navigate to [localhost:8000](http://localhost:8000/)

# Let's Make something

* Homage to Malevich Black Square - talk about color b&w / rgb
* Make a Rothko
* Ok, let's do some more colorfield/minimalism. Make a Mondrian / Agnes Martin / Webdriver Torso piece.
* Ode to MS Paint - using mouseX and mouseY, random color generation

# Let's extend functionality: playing sound

* Adding P5Sound library
* How to load sound / getting it to work with your Digital Modernism







