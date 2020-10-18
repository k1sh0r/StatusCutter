# StatusCutter
A minimalistic way to cut your long videos into 30 seconds segments for whatsapp instead of cutting it manually. It is based on windows server and it can also be used in linux/unix by changing some directories in these files. Visit [kishor.co/StatusCutter](http://kishor.co/StatusCutter) to try it online.


There are 3 things needed for this to work
1. Localhost Server and browser. [Download XAMPP](https://www.apachefriends.org/download.html)
2. Python3 [Download Python3](https://www.python.org/downloads/)
3. moviepy python module [Official installation instruction](https://zulko.github.io/moviepy/install.html)

Setting up
1. Add .py handler to the httd.conf file in apache to allow py scripts to run. [Watch how](https://youtu.be/WhI8MYn8qpo?t=64)
2. Clone this repository to the localhost directory
3. In cutter.py line-1 add the directory in which you've installed python in your computer.
4. Visit localhost/path/you/have/cloned/to/StatusCutter/index.html from localhost in the browser

The rest is self explanatory I guess.


Thanks to [@vjakash](https://github.com/vjakash) for the UI

[kishor.co](http://kishor.co)
