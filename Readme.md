# edrn

Editor-assisted rename. Passes a list of filenames to the standard editor for easy mass renaming.

## Usage

Call edrn with a list of filenames:

    $ ls
    Episode 2.mkv
    Episode 3.mkv
    Reign of the Black King.mp4
    The.Fallen.Star.x286.[FpS].mkv

    $ edrn *

Rename the files using your favourite editor:

![Editor screenshot](editor-exampe.png)

Save and close:

    $ ls
    Episode 2.mkv -> The Barbarian - s03e02.mkv
    Episode 3.mkv -> The Barbarian - s03e03.mkv
    Reign of the Black King.mp4 -> The Barbarian - s03e04 - Reign of the Black King.mp4
    The.Fallen.Star.x286.[FpS].mkv -> The Barbarian - s03e01 - The Fallen Star.mkv

## Licence

Copyright 2012 Sijmen Mulder <sjmulder@gmail.com>. Licensed under the 3-clause BSD licence.
