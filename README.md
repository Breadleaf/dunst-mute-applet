# Dunst Mute Applet

I wrote this for i3, it probably works with other WMs but I haven't tested.

## Install

```
cd ~/.config/i3
git clone https://github.com/breadleaf/dunst-mute-applet.git
echo "exec --no-startup-id ~/.config/i3/dunst-mute-applet/start.sh 2 >> ~/.config/i3/dunst-mute-applet/dunst-mute-applet.log 2>&1" >> config
```

Restart i3 and you should see a new icon in your status bar.

## Usage

Right click the icon then click on either toggle or quit.
