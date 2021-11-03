# rand-passwd

![Screenshot of random passwords](img/screenshot.png)

Just a random password generator, saving for posterity.  If it's useful to someone, great!  More than likely you already have a better utility, though.  The hope is that these passwords will be both random, and relatively easy to memorize.

The idea behind it was simple; I built a simple Markov chain from /usr/share/dict/words, didn't keep the frequency of letters, and simply keep track of what the previous chosen character is and use the dict to pick a new one based on the previous one.  Unless, of course, the previous letter was a consonant, and then I choose a random vowel.
