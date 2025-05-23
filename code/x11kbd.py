"""Control an X11 keyboard, calling arbitrary code for given keycodes.

It requires the Xlib python module from : http://python-xlib.sourceforge.net.

A utility class is provided for volume control of an OSS audio channel.  OSS
is a linux-specific module, but the X11 keyboard control should work under any
X11 system.

Also, a default set of actions is given for the Microsoft Wireless Multimedia
keyboard.  These defaults use KDE, XMMS, mozilla and gthumb, reflecting my own
preferences.  Use simply as an example for your own customizations.

This is basically a rewrite of a great little script found at
http://www.larsen-b.com/Article/184.html.

KDE/XMMS Notes:

  1. Set the sound system in KDE to use OSS for sound (Control Panel->Sound
  and Multimedia->Sound System -> Hardware) and auto-suspend if idle after 1
  second (Sound System->General).  This allows XMMS to have access to the OSS
  audio device directly.
 
  2. Configure XMMS to use OSS for output."""

__author__ = 'Fernando Perez <Fernando.Perez@colorado.edu>'
__date__   = 'Fri Dec 24 02:01:45 MST 2004'

# Stdlib modules
import os
from commands import getoutput
from sets import Set
try:
    import ossaudiodev
except:
    # the MixerChannel class won't work, but the rest will work for X11
    # systems besides linux (ossaudiodev is linux-specific)
    pass

# Xlib gives python access to Xlib, the raw X11 library
from Xlib import X
from Xlib.display import Display

class MixerChannel:
    """Volume control for a named channel of an OSS Mixer device."""

    def __init__(self,name):
        """Return a named channel of the OSS mixer device.
        
        List of all valid audio channel names: ossaudiodev.control_labels."""
        
        self.name      = name
        self.channel   = ossaudiodev.control_labels.index(name)
        self.mixer     = ossaudiodev.openmixer()
        self.saved_vol = self.mixer.get(self.channel)
        self.is_muted  = False

    def get_volume(self):
        return self.mixer.get(self.channel)

    def set_volume(self,vols):
        self.mixer.set(self.channel,vols)

    def clip(self,val):
        """Clip  a value to the 0-100 range, the valid range for volumes."""
        if val<0: return 0
        elif val>100: return 100
        else: return val

    def change_volume(self,vchange):
        """Change volume by vchange amount.

        If the channel is muted, for positive changes it only gets unmuted.
        Negative changes are applied but the channel remains muted, so they
        only become visible when the chanel is unmuted."""
        
        if self.is_muted:
            if vchange>0:
                self.unmute()
                # don't actualy increase the volume on the first time for a
                # muted channel, just return.
                return
            else:
                left,right     = self.saved_vol
                self.saved_vol = self.clip(left+vchange),self.clip(right+vchange)
        if not self.is_muted:
            left,right  = self.get_volume()
            new_vols    = self.clip(left+vchange),self.clip(right+vchange)
            self.set_volume(new_vols)

    def increase_volume(self):
        """Increase volume by fixed amount (+2)"""
        self.change_volume(+2)

    def decrease_volume(self):
        """Decrease volume by fixed amount (-2)"""
        self.change_volume(-2)

    def unmute(self):
        self.set_volume(self.saved_vol)
        self.is_muted = False

    def mute(self):
        self.saved_vol = self.get_volume()
        self.set_volume((0,0))
        self.is_muted = True

    def mute_toggle(self):
        if self.is_muted: self.unmute()
        else: self.mute()

class X11Keyboard:
    """Controllable keyboard which executes arbitrary actions for a given set
    of keycodes."""

    def __init__(self,keycodes,actions):
        """Initialize with a dict of keycodes and one of actions.

        The keys in the keycodes dict must be a subset of those in the actions
        dictionary.  These establish the mapping between actual keycodes and
        executable actions.

        The actions are a dictionary of keycode/function pairs, where each
        function will be called (with no arguments) when the given keycode is
        generated by a keypress event.

        The rationale behind this initialization mechanism is the following:
        the actions dict is a mapping from generic labels to executable
        actions, which can contain many actions and be generic for multiple
        similar keyboards.  When initializing a specific X11Keyboard instance,
        you only need to pass a simpler dict indicating the specific keycodes
        for the actions you wish to implement."""
                
        keys = {}
        for button,keycode in keycodes.iteritems():
            try:
                keys[keycode] = actions[button]
            except KeyError:
                raise KeyError("Unsupported action: %s " % button)
        self.keys = keys

    def control(self):
        """Control an X11 keyboard.  Press Ctrl-C to stop."""

        # current display
        root = Display().screen().root

        # we tell the X server we want to catch keyPress event
        root.change_attributes(event_mask = X.KeyPressMask)

        # Inform X11 of which keys we'll be trapping
        keys = self.keys
        for keycode in keys:
            root.grab_key(keycode, X.AnyModifier, 1,
                          X.GrabModeAsync, X.GrabModeAsync)

        # Endless loop which listens for events
        next_event = root.display.next_event
        KeyPress = X.KeyPress
        try:
            while 1:
                event = next_event()
                if event.type == KeyPress:
                    # For KeyPress events, event.detail is the keycode
                    keys[event.detail]()
        except KeyboardInterrupt:
            pass

def syscall(cmd,bg=True):
    """Return a callable which will execute the given command when called.

    By default, the command is backgrounded and the shell returns immediately,
    set bg to False to change this."""
    
    if bg: call = '%s &' % cmd
    else: call = cmd
    return lambda: os.system(call)

def syscall_once(cmd,bg=True):
    """Like syscall, but the cmd is only run if not already running."""

    ps_check = 'ps -C %s -o pid=' % cmd
    if bg: call = '%s &' % cmd
    else: call = cmd
    def run_once():
        isrunning = getoutput(ps_check)
        if not isrunning: os.system(call)
    return run_once

def MSWirelessKbdActions(audio_channel='Pcm  '):
    """Build a dictionary of default actions for MS Wirelesss Multimedia
    keyboards.

    By default, the audio controls use the Pcm channel, just like XMMS.  The
    list of all valid audio channel names is ossaudiodev.control_labels."""
    
    audio = MixerChannel(audio_channel)
    return dict(# Left buttons
                MyDocuments = syscall('konqueror $HOME'),
                MyPictures  = syscall('gthumb'),
                MyMusic     = syscall('konqueror $HOME/music'),
                # Volume controls
                Mute        = audio.mute_toggle,
                VolumePlus  = audio.increase_volume,
                VolumeMinus = audio.decrease_volume,
                # Media playing
                PlayPause   = syscall('xmms --session=0 --play-pause'),
                Stop        = syscall('xmms --session=0 --stop'),
                Previous    = syscall('xmms --session=0 --rew'),
                Next        = syscall('xmms --session=0 --fwd'),
                Media       = syscall_once('xmms'),
                # Right buttons
                Mail        = syscall('mozilla -mail'),
                WebHome     = syscall('mozilla'),
                Messenger   = syscall_once('gaim'),
                # Numpad buttons
                Calculator  = syscall('xcalc'),
                LogOff      = syscall('dcop kdesktop default logout'),
                Sleep       = syscall('xscreensaver-command -lock'),
                )

# Example usage:
if __name__ == '__main__':
    # Get a set of default actions to initialize the keyboard
    actions = MSWirelessKbdActions('Pcm  ')
    # Build table of keycodes specific to a keyboard.  To find the correct
    # keycodes generated by a given keyboard, use xev.
    keycodes = dict(# Left tools
                    MyDocuments = 228,
                    MyPictures  = 231,
                    MyMusic     = 237,
                    # Media oval
                    Mute        = 166,
                    PlayPause   = 159,
                    Stop        = 151,
                    VolumePlus  = 158,
                    VolumeMinus = 165,
                    Previous    = 164,
                    Next        = 162,
                    Media       = 129,
                    # Right tools
                    Mail        = 236,
                    WebHome     = 130,
                    Messenger   = 218,
                    # Numpad tools
                    Calculator  = 161,
                    LogOff      = 214,
                    Sleep       = 223,
                    )
    # Build the keyboard object and activate its control method
    MyKbd = X11Keyboard(keycodes,actions)
    print 'Press Ctrl-C to stop.'
    MyKbd.control()
    print 'Bye!'
