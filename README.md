# AFinn 111 Project

### Introduction
This program is a simple sentiment analysis program that utilizes [AFINN 111](http://www2.imm.dtu.dk/pubdb/pubs/6010-full.html) to analyze text from user's input. This program was inspired by The Coding Train's videos on a similar program created within JavaScript. This program however; is written in python and utilizes a bit of preprocessing for text before comparing with the AFINN 111 wordlist. 

### Limitations & Functions.
This program is a very simplistic way to analyze sentences for sentiment analysis. Since the program only will compare words to a possible score of sentiment there are many other variables that are not considered such as context, lexical chunks, and how word sentiment can be changed depending on the relationship within a sentence. This program is very limited, but can be further improved for the future. The biggest limitation is that the program will break down sentences into words and score those words, but will not consider the sentence as one whole unit and score sentiment as a holistic analysis. In other words, sentences such as "I found an abandoned dog yesterday" will be considered negative since the word abandoned is scored negatively within the AFINN 111 wordlist, but this sentence may be more of a positive one.

### Future Improvements
I may try and find a way to either add more words within the wordlist, or I could possibly figure out ways to include chunks of words instead of scoring single words. This won't help score sentences sentiment from a holistic perspective, but can greatly improve the analysis of chunks of words instead of words themselves. This may take a bit of more research and further analysis for me to perform, so as of now might be something I might return to at a later date.
