from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter

mapping = {
    'has_header': True,
    'is_split': False,
    'bank': itemgetter('Nom de la connexion'),
    'currency': 'EUR',
    'delimiter': '	',
    'account': itemgetter('Nom du compte'),
    'date': itemgetter('Date'),
    'date_fmt': '%d/%m/%Y',
    'amount': itemgetter('Montant'),
    'desc': itemgetter('Libelle'),
    'notes': itemgetter('Notes'),
    'class': itemgetter('Categorie'),
}
