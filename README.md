<h1>Spotify Global</h1>
Control Spotify from anywhere with Global Hotkeys! No need for the window to be in focus, working for all users (free & premium).

<hr>
<h3>How it works</h3>
This program works registering key presses with <i>keyboard</i> and using <i>pywinauto</i> to send the equivalent hotkey command to the Spotify application.
Because it doesn't use Spotify's API, it's completely functional for all Spotify accounts.
And because the command is sent <b>only</b> to the Spotify window, it doesn't affect any of your other audio sources!

<h3>Download</h3>
Click <a href="https://github.com/mavvos/SpotifyGlobal/releases/latest">here</a> for the latest version.

If you don't have python installed, download the .exe version and it should work as any other normal app.

<h3>Your first time opening</h3>
The first time you run the program, it will try to find Spotify's executable in the default installation folder, if it's not found there, you'll be prompted to type your Spotify's application path.

Which by default is located at:
```
C:\Users\~\AppData\Roaming\Spotify\Spotify.exe
```
After that, a file (options.txt) is created containing your default path and your hotkeys, so you don't need to keep retyping.

If you wish to <b>customise your hotkeys</b>, simply locate your options.txt and alter the value that follows the "="

A normal hotkey looks something like this:
```
VolDown=shift+2
```

Keys are written as you expect them to be, in plain english, so to change the hotkey above, you could put something like:
```
VolDown=alt+shift+p
```

That way, to send the command Volume Down to Spotify, you would have to press simultaneously <i>ALT SHIFT P</i>

<h3>Default controls</h3>
<h6>Hotkey in Program = Expected Command</h6>

```
SHIFT + 8     = Volume Up
SHIFT + 2     = Volume Down
SHIFT + 4     = Previous Track
SHIFT + 6     = Next Track
SHIFT + 5     = Play/Pause
SHIFT + 1     = Go back 5 seconds
SHIFT + 3     = Go forward 5 seconds
SHIFT + 7     = Like/Dislike Track
SHIFT + 9     = Quit program
```

<h3>Known problems and bugs</h3>
<ul>
<li><b>Spotify needs to be closed</b> when you run this program. The program takes care of oppening Spotify for you, in fact it <b>has</b> to open Spotify for it to work, if your Spotify is already running when you try oppening this, thep program will just crash and not work.</li>
<li>Program doesn't seem to work with the Microsoft Store version of Spotify (because you can't access Spotify's path folder, lol).</li>
<li>If you spam pressing hotkeys you can get stuck in a loop where the commands keep repeating, to fix this restart application.</li>
<li>If you delete any line from options.txt after your first launch, the program will crash, to fix this just delete the options.txt file alltogether and a new one will be created for you on next launch.</li>
<li>Spotify needs to be open as a window for the program to work, if Spotify is minimized it will keep popping up when you press a hotkey, to fix this just let Spotify's window open and click away to your other programs.</li>
<li>Sometimes the message about app running takes longer than normal to appear.</li>
<li>If you are not on Windows, there's a high chance the program won't work for you, because it uses the library <i>pywinauto</i>.</li>
</ul>
