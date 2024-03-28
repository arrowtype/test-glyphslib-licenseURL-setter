# Test: does GlyphsLib successfully set the `licenseURL` of a font?

Expectation: `GSFont(fontPath).licenseURL = "https://opensource.org/license/mit"` should set a GlyphsApp font’s License URL to `https://opensource.org/license/mit`. 

Current experience: The `licenseURL` attribute setter doesn’t seem to have any effect – even though related attributes such as `manufacturerURL` do work.

## Reproduction Steps

1. Git clone this repo and navigate to it in a terminal
2. Make a venv and activate it: `python3 -m venv venv && source venv/bin/activate`
3. Install glyphsLib: `pip install -r requirements.txt`
4. Run `python3 set-glyphs-licenseURL.py`, and check if it has any effect on `TestFont.glyphs`. This should set the license URL, but it (seemingly) doesn’t.
