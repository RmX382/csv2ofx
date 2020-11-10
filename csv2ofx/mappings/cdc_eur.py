from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter

mapping = {
    'has_header': True,
    'is_split': False,
    'bank': 'Crypto.com',
    'currency': 'EUR',
    'delimiter': ',',
    'date': itemgetter('Timestamp (UTC)'),
    'date_fmt': '%Y-%m-%d',
    'amount': itemgetter('Native Amount'),
    'desc': itemgetter('Transaction Description'),
}
