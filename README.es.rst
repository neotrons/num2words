num2words - Convierte números a palabras en múltiples idiomas
=============================================================

.. image:: https://img.shields.io/pypi/v/num2words.svg
   :target: https://pypi.python.org/pypi/num2words

.. image:: https://travis-ci.org/savoirfairelinux/num2words.svg?branch=master
    :target: https://travis-ci.org/savoirfairelinux/num2words

.. image:: https://coveralls.io/repos/github/savoirfairelinux/num2words/badge.svg?branch=master
    :target: https://coveralls.io/github/savoirfairelinux/num2words?branch=master


``num2words`` es una librería que convierte números como ``42`` a palabras como ``cuarenta y dos``.
Es compatible con varios idiomas (consulte la lista a continuación para obtener una lista completa de idiomas) e incluso puede generar números ordinales como ``cuadragésimo segundo``
(aunque esta última característica es un poco problemática para algunos idiomas en este momento).

El proyecto está alojado en GitHub_. Las contribuciones son bienvenidas.

.. _GitHub: https://github.com/savoirfairelinux/num2words

Lea esto en otro idioma: English_, Español_

.. _English: ./README.rst

.. _Español: ./README.es.rst

instalación
------------

La forma más fácil de instalar ``num2words`` es usar pip::

    pip install num2words

De lo contrario, puede descargar el paquete fuente y luego ejecutar::

    python setup.py install

El conjunto de pruebas en esta libreria es nuevo, así que es bastante simple, pero se puede ejecutar con::

    python setup.py test

Uso
----

Solo hay una función para usar::

    >>> from num2words import num2words
    >>> num2words(42)
    forty-two
    >>> num2words(42, to='ordinal')
    forty-second
    >>> num2words(42, lang='es')
    cuarenta y dos

Además del argumento numérico, hay dos argumentos opcionales.

**to:** El convertidor a usar. Los valores admitidos son:

* ``cardinal`` (por defecto)
* ``ordinal``
* ``ordinal_num``
* ``year``
* ``currency``

**lang:** El idioma en el que convertirá el número. Los valores admitidos son:

* ``en`` (Ingles, por defecto)
* ``ar`` (Árabe)
* ``cz`` (Checo)
* ``de`` (Alemán)
* ``dk`` (Danés)
* ``en_GB`` (Ingles - Gran Bretaña)
* ``en_IN`` (Ingles - India)
* ``es`` (Español)
* ``es_CO`` (Español - Colombia)
* ``es_VE`` (Español - Venezuela)
* ``eu`` (EURO)
* ``fi`` (Finlandés)
* ``fr`` (Francés)
* ``fr_CH`` (Francés - Suiza)
* ``fr_BE`` (Francés - Bélgica)
* ``fr_DZ`` (Francés - Argelia)
* ``he`` (Hebreo)
* ``id`` (Indonesio)
* ``it`` (Italiano)
* ``ja`` (Japonés)
* ``lt`` (Lituano)
* ``lv`` (Letón)
* ``no`` (Noruego)
* ``pl`` (Polaco)
* ``pt_BR`` (Portugués - Brasileño)
* ``sl`` (Esloveno)
* ``ru`` (Ruso)
* ``tr`` (Turco)
* ``th`` (Tailandés)
* ``vn`` (Vietnamita)
* ``nl`` (Dolandés)
* ``uk`` (Ucraniano)

Puede proporcionar valores como ``fr_FR``; si el país no existe pero el
lenguaje lo hace, el código volverá al lenguaje base (i.e. ``fr``). Si
usted proporciona un idioma no compatible, se genera, ``NotImplementedError`` un error.
Por lo tanto, si desea llamar a ``num2words`` con un respaldo, puede hacer::

    try:
        return num2words(42, lang=mylang)
    except NotImplementedError:
        return num2words(42, lang='en')

Además, algunos conversores e idiomas admiten otros argumentos opcionales
que son necesarios para hacer que el convertidor sea útil en la práctica.

Wiki
----
Para obtener información adicional sobre alguna localización, consulte la Wiki_.
And feel free to propose wiki enhancement.

.. _Wiki: https://github.com/savoirfairelinux/num2words/wiki

Historia
--------

``num2words`` se basa en una libreria antigua, ``pynum2word``, creado por Taro Ogawa
en 2003. Desafortunadamente, la biblioteca dejó de ser mantenida y el autor no pudo ser ubicado.
Había otro desarrollador, Marius Grigaitis, que en 2011 añadió soporte lituano, pero no asumió
el mantenimiento del proyecto

Por lo tanto, me baso en las mejoras de Marius Grigaitis and volvi a publicar
``pynum2word`` como ``num2words``.

Virgil Dupras, Savoir-faire Linux
