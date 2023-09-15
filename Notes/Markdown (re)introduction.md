---
tags:
  - notes
  - slss
  - y2023
  - programming-level-2
---

# Headings  
We create headings in markdown using hash (#) symbols  
To create subheadings, we can use multiple hash symbols
## This is a level 2 subheading
### This is a level 3 subheading
###### This is a level 3 subheading
# Modifying Text Style  
We use asterisks to modify text styling, specifically bold and italics  
e.g.  
I want this **word** specifically to be bold  
I want this *word* to be italicized  
I want this ***word*** to be both
## Strikethrough  
ASIDE: If we want to place a character is a *keyword*  or reserved word and we want to LITERAL character, use the forward slash (\)  
e.g. if we want to put an asterisk we do this \\\*We can also strikethrough characters using the tilde (~)  
I want to strikethrough this specific ~~word~~  
~~This sentence is struck-through~~
# Links  
We can create things in our Markdown files  
[One tool to use.]([[https://chat.openai.com](https://chat.openai.com/)]([https://chat.openai.com/))](https://chat.openai.com/)))  
Exercise:  
* If you have an Openai account, do the following:  
* ask Chatgpt to create for you markdown code that is a link to two websites of your choice  
* If you don't have Chatgpt/Openai, create two links to websites of your choice in the space below*e.g. [My favourite website right now]()e.g. if you use Openai  ,put in their code and in italics say that it's from Chatgpt  

[YouTube]([[https://www.youtube.com/)/from](https://www.youtube.com/)/from)](https://www.youtube.com/)/from](https://www.youtube.com/)/from)) chatgpt/  

[Example Educational Website]([[https://www.khanacademy.org/)/from](https://www.khanacademy.org/)/from)](https://www.khanacademy.org/)/from](https://www.khanacademy.org/)/from)) chatgpt/  
________________________________________________________________________  
[YouTube Video]([https://youtu.be/p5fnHWznTBQ?si=xj8oHH1GsT8RGFjS/)/from](https://youtu.be/p5fnHWznTBQ?si=xj8oHH1GsT8RGFjS)*/from)](https://youtu.be/p5fnHWznTBQ?si=xj8oHH1GsT8RGFjS/)/from](https://youtu.be/p5fnHWznTBQ?si=xj8oHH1GsT8RGFjS)*/from)) chatgpt*/  

[Hitman]([https://rentahitman.com/)/from](https://rentahitman.com/)/from)](https://rentahitman.com/)/from](https://rentahitman.com/)/from)) chatgpt/  

# Sonic
!(Cute Sonic)[https://i1.sndcdn.com/artworks-7yWcu9G3xv0jmQPJ-Zk0R5w-t500x500.jpg]
________________________________________________________________________  

# Blockquotes  
Block quotes allow us to emphasize a bigger chunk of text. We use carets (>) to create blockquotes.>This is an example of a blockquote  
>This is line two of the blockquote  
>  
>This is the fourth line of the blockquote; the third is blank# Lists  
We can create both unordered and ordered lists  
## Unordered Lists  
To create each point, we use (\*) with a space behind it  
We can create sublists by placing **TABS** before the asterisk e.g.  
* dairy  
* eggs  
* milk  
* cheese  
* juice


## Ordered Lists  
If there is a specific order to the elements in our list,  
we create ordered lists, we use numbers, followed by periods to create ordered lists e.g.  
1. Put butter into mixing bowl  
2. Add sugar to butter (*hold shift to get the second line*)  
   Add both brown and regular sugar  
3. Use the mixer to cream the butter and sugar together

# Tables  
We can organize information in tables using Markdown  
We use dashes (-) and pipes (|)Tables in Markdown require headings e.g.

| Name        | Age        | Sign        | Superpower      |
| ---         | ---        | ---         | ---             |
| Bruce Wayne | 35         | Aquarius    | Intelligence/ $ |
| Mr. Ubial   | Unaging    | All of them | Dad strength    |
| Yourself    | Your age   | Your Sign   | Super strength  |

---

tags:

  - programming-startup

---

# Creating a repository

`git init`

​

# Checking Status

`git status`

​

# Identity

`git config --global user.name "<username>"`

`git config --global user.email "<email address>"`

​

# Adding files to the stage

`git add <path>`

​

# Commit

`git commit -m "<commit message>"`

​---

tags:

  - programming-startup

---

## Change directory

``` bash

cd <something>

```

You can go back one level to the *parent directory* using:

``` bash

cd ..

```

​

## Make folder

``` bash

mkdir <name of folder>

```

​

## List contents of folder

``` bash

ls

```