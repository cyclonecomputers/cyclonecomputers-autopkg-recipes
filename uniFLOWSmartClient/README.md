# uniFLOW SmartClient
This folder contains generic recipes for the [uniFLOW SmartClient](https://www.uniflowonline.com/en/technology-integrations/uniflow-smartclient/). The recipes require that you download the ISO file directly from your uniFLOW print server and supply that to the recipe (see usage instructions below for more detail).

This recipe is adapted from the instructions provided by user andymason on the [Jamf Nation forums](https://community.jamf.com/general-discussions-2/canon-uniflow-smart-client-for-mac-creating-a-useable-pkg-installer-30158#).

I also note that there is an [existing recipe for uniFLOW in the MLBZ521-recipes repository](https://github.com/autopkg/MLBZ521-recipes/tree/master/uniFLOW) but this relies the ISO being saved to a local file path rather than just being passed at the command line.

## Usage
In order to use these recipes you will need to obtain a copy of the uniFLOW client installer ISO.

### Download Install Media
1. Log into your uniFLOW online via a web browser.
2. Click "Start Printing" in the left-hand sidebar.
3. Click the button to download the SmartClient for Mac (under the printer driver section).
4. This should download an image file with the `.iso` extension.

### Using the ISO with Recipes
When you run any of the recipes in this folder you will need to supply the ISO file using the `-p` flag in AutoPkg.

E.g.
```
autopkg run -v com.github.cyclonecomputers.pkg.uniFLOWSmartClient -p ~/Downloads/SmartClientMac.iso_macos_x.y.z.iso
```
