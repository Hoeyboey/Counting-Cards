# Counting-Cards

At Codebar, I found a challenge online at CodeAbbey that asked you to create a 
program that would tell you the value of any hand in blackjack, and whether 
you're bust. If you've never played the game, the aim is to get as close to 21 
without going over, where picture cards count as 10, and aces can count as 
either 1 or 11, depending on what's better for you. 

So, if you run this, you can input your hand, and it will give you the 
statistical likelihood of going over 21 with the next draw. It takes into 
account the number of cards left in the deck, their values, and whether you're 
holding an ace or not. After that, you can also put in the cards you know other
players hold. Then, it will give an updated statistical likelihood.

If you're reading this now, I've uploaded this the morning after, and it's very
basic, probably not PEP 8 compliant, and so on. I'm about to work on this 
further, make it clearer to use, and so on. I also don't know the mathematics of
actual card counting, so once the current version is complete, I'll be checking
out quite how that works.
