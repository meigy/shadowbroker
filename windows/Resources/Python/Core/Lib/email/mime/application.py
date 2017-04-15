# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: application.py
"""Class representing application/* type MIME documents."""
__all__ = [
 'MIMEApplication']
from email import encoders
from email.mime.nonmultipart import MIMENonMultipart

class MIMEApplication(MIMENonMultipart):
    """Class for generating application/* MIME documents."""

    def __init__(self, _data, _subtype='octet-stream', _encoder=encoders.encode_base64, **_params):
        """Create an application/* type MIME document.
        
        _data is a string containing the raw application data.
        
        _subtype is the MIME content type subtype, defaulting to
        'octet-stream'.
        
        _encoder is a function which will perform the actual encoding for
        transport of the application data, defaulting to base64 encoding.
        
        Any additional keyword arguments are passed to the base class
        constructor, which turns them into parameters on the Content-Type
        header.
        """
        if _subtype is None:
            raise TypeError('Invalid application MIME subtype')
        MIMENonMultipart.__init__(self, 'application', _subtype, **_params)
        self.set_payload(_data)
        _encoder(self)
        return