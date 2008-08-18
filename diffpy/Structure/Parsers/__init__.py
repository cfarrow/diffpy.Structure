########################################################################
#
# Structure         by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2007 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################

"""Conversion plugins for various structure formats

The recognized structure formats are defined by subclassing StructureParser,
by convention these classes are named P_<format>.  The parser classes should
to override the parseLines() and toLines() methods of StructureParser.
Any structure parser needs to be registered in parser_index module.

For normal usage it should be sufficient to use the routines provided
in this module.
"""

__id__ = "$Id$"

def getParser(format):
    """Return Parser instance for a given structure format.
    Raises StructureFormatError exception when format is not defined.
    """
    from import_helper import StructureFormatError
    from parser_index import parser_index
    if format not in parser_index:
        raise StructureFormatError, "no parser for '%s' format" % format
    pmod = parser_index[format]['module']
    exec "import %s as pm" % pmod
    return pm.getParser()

def inputFormats():
    """Return list of implemented input structure formats"""
    from parser_index import parser_index
    input_formats = [ fmt for fmt, prop in parser_index.iteritems()
            if prop['has_input'] ]
    input_formats.sort()
    return input_formats

def outputFormats():
    """return list of implemented output structure formats"""
    from parser_index import parser_index
    output_formats = [ fmt for fmt, prop in parser_index.iteritems()
            if prop['has_output'] ]
    output_formats.sort()
    return output_formats

# End of file