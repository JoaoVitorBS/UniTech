# -*- coding: utf-8 -*-

from unitech import __version__


def unitech_version(request):
    return {'versao': __version__}
