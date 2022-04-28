# JG's Newgen Face Script

A basic Python script for Football Manager 2022 that helps assign faces to Newgens from the famous NewGAN Facepack.

It seems that the team behind the original NewGAN Manager have largely abandoned it, so created my own. I take no credit for the original concept, I merely refined it.

# DISCLAIMER

> I will not offer support for this, in any way. I simply don't have the time to help everyone with their issues. I'm sharing this because it was requested, but if you can't make it work, I'm sorry, but I won't be helping you.

> This will work with any facepack that follows the folder structure shown here. For simplicity's sake, I will write the instructions based around the original NewGAN facepack, simply because it's what most will be using anyways.

## How to use it

### Setting Up

1. Ensure that you have downloaded and installed the latest version of Python from: [https://www.python.org/downloads/](https://www.python.org/downloads/).

1. Download the files in this repository.

1. Download the NewGAN facepack from this page: [https://fm-base.co.uk/resources/newgan-facepack.1266/download](https://fm-base.co.uk/resources/newgan-facepack.1266/download)

1. Extract the file to a dedicated folder in your FM 2022 folder, usually located at: `%userprofile%\Documents\Sports Interactive\Football Manager 2021\graphics\newgen faces`.

1. If you do not have a `newgen faces` folder, simply create one. If you downloaded the files from this repository, it should all extract automatically.

1. Ensure that `Newgen_Faces.rtf`, `Script_faces.bat`, `Script_faces.py` and `config.xml` are all located in this `newgen faces` folder.

1. Add the files in the `views` folder to `%userprofile%\Documents\Sports Interactive\Football Manager 2021\views`.

### In-Game

1. Open Football Manager 2022.

1. Click on "Scouting", then scroll over "Players" and click on "Player Search".

1. Filter your "Player Search" to only show Newgens. You might need the In-Game Editor for this step, or find a filter for it online.

1. Import the correct view, in this case, `SCRIPT FACES player search`.

1. Select the players you want to assign a face to, and press `CTRL + P`. A pop-up should appear, and you need to select `Text File`. Make sure this file is named `Newgen_faces.rtf`. You should be able to just click on it in the folder structure, the same place you placed the files earlier.

### Running the Script

1. Double-click on `Script_faces.bat`.

1. Wait. Depending on the number of players you have selected, this may take multiple hours, especially the first time. I suggest leaving it overnight. Just be patient. It will inform you when it's done.

### In-Game

1. Go to "Preferences" and click "Reload Skin".

1. Enjoy your new Newgen faces!