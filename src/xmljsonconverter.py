"""
.. module:: xmljsonconverteri

   This module provides a conversion tool for converting from JSON to XML.
"""

class XMLJSONConverter():
  """
  .. class:: XMLJSONConverter()

     This class provides a conversion tool for converting from JSON
     files to XML.
  """

  def convertJSONtoXML(self, json_file, xml_file):
    """
    .. method:: convertJSONtoXML(json_file, xml_file)

       This method converts the JSON in the given file to the XML and
       outputs to the given file.

       The implementer of this method is responsible for opening both
       files, reading from the JSON file and writing to the XML
       file. He must ensure that all the proper error handling is
       performed.

       :param str json_file: A string representing a file path to a
                             JSON file.
       :param str xml_file: A string representing a file path to
                            output XML after converting it from the
                            given JSON file
       :returns: None
       :rtype: NoneType
    """
    # Todo: Implement this method
    raise NotImplementedError
