# Spotify Global
Control Spotify from anywhere with Global Hotkeys! No need for the window to be in focus, working for all users (free & premium).

#
### How it works
This program works registering key presses with _keyboard_ and using _pywinauto_ to send the equivalent hotkey command to the Spotify application.
Because it doesn't use Spotify's API, it's completely functional for all Spotify accounts. And because the command is sent **only** to the Spotify window, it doesn't affect any of your other audio sources!
#
### Download
Find the updated version here: https://github.com/mavvos/SpotifyGlobal/releases/latest \
If you don't have python installed, download the .exe version and it should work as any other normal app.

#
### Your first launch
The first time you run the program, it'll try to find Spotify's executable in the default installation folder, if it is not found there, you'll be prompted to type your Spotify's application path.
Which by default is located at\
C:\Users\\~\AppData\Roaming\Spotify\Spotify.exe

After that, a file (options.txt) is created containing your default path and your hotkeys, so you don't need to keep retyping.\
\
If you wish to **customise your hotkeys**, simply locate your options.txt and alter the value that follows the "_=_"\
A normal hotkey looks something like this:
>VolDown=shift+2
>
Keys are written as you expect them to be, in plain english, so to change the hotkey above, you could put something like
>VolDown=alt+shift+p
>
That way, to send the command Volume Down to Spotify, you would have to press simultaneously _ALT SHIFT P_
#
### Default controls
###### Hotkey in Program = Expected Command
SHIFT + 8         = Volume Up      
SHIFT + 2         = Volume Down    
SHIFT + 4         = Previous Track      
SHIFT + 6         = Next Track       
SHIFT + 5         = Play/Pause        
SHIFT + 1         = Go back 5 seconds       
SHIFT + 3         = Go forward 5 seconds     
SHIFT + 7         = Like/Dislike Track    
SHIFT + 9         = Quit program
#
### Known problems and bugs
- **Spotify needs to be closed** when you run this program. The program takes care of oppening Spotify for you, in fact it **has** to open Spotify for it to work, if your Spotify is already running when you try oppening this, it'll just crash and not work.
- Program doesn't seem to work with the Microsoft Store version of Spotify (because you can't access Spotify's path folder, lol)
- If you spam press hotkeys you can get stuck in a loop where the commands keep repeating forever, to fix this restart application.
- If you delete any line from options.txt after your first launch, the program will crash, to fix this just delete the options.txt file alltogether and a new one will be created for you on your next launch.
- Spotify needs to be open as a window for the program to work, if you minimize it Spotify will keep popping up bothering you, to fix this just let Spotify's window open and click away to your other programs.
- Sometimes the message about app running takes longer than normal to appear.
- If you are not on Windows, there's a high chance the program won't work for you, because of the library _pywinauto_ that is used.
