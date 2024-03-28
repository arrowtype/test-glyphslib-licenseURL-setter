"""
    Use GlyphsLib to set the 'licenseURL' parameter of a Glyphs font.
"""

from glyphsLib import GSFont

fontPath = "./TestFont.glyphs"

font = GSFont(fontPath)

font.manufacturerURL = "https://arrowtype.com"
font.licenseURL = "https://opensource.org/license/mit"

font.save(fontPath)