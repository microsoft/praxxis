If you've been in the data science world for any period of time, you probably have already heard of the jupyter notebook. An elegant, executable, markdown friendly document with specially marked cells for executing code in a number of "kernels" such as python or r. 

This technology has really been adopted by those in the data science field for a couple of reasons. 

- The format lends itself extremely well to sharing executed output with graphs, useful when you want to share your output for things like ML training graphs 
- Python is part of the backbone of jupyter, which is a language data scientists tend to prefer
- They're more interactive than an IDE, and better for prototyping
- It's easy to teach by example when the documentation and the code exist in the same place
- Documentation on the code and the code itself stay up to date by by being edited in the same place

But if you think about it, really anyone could benefit from any of these features. Having interactive, beautifully documented, shareable code that is easy to teach from could help anyone working on anything from troubleshooting to database management.

## _So why aren't we using them?_

A lot of the pain points of Jupyter come from the way that they have to be run. Since jupyter notebooks are a very visual format, running them out of a GUI can be challenging at times. 

Upon that, in order to set parameters, most of the time the notebooks must be edited directly to remove hardcoded defaults such as usernames and passwords. As a result, people need to edit every default in every notebook before it is run, save a copy, and hope it doesn't get shared, ultimately defeating the purpose of using a shareable format to begin with.

They're also sometimes hard to find! Even if you've written a huge library of useful notebooks for yourself and your friends, updating that library and searching through it without any kind of framework in place to help you could end up taking longer than just writing a new notebook.

There comes a time when the time it takes to find and run a notebook becomes more challenging than simply writing the code yourself. 


## Introducing Praxxis


With this in mind, we set out to be that change, and hopefully create a better tool to help the world move in the direction of executable documentation. 


