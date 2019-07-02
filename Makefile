FLAKE8?=	flake8
MYPY?=		mypy

BLACK_ARGS=	--skip-string-normalization

lint:: flake8 mypy

flake8:
	${FLAKE8} repology-export.py repologyexport/exports

mypy:
	${MYPY} repology-export.py repologyexport/exports

black:
	${BLACK} ${BLACK_ARGS} --check repology-linkchecker.py linkchecker/**/*.py

black-reformat:
	${BLACK} ${BLACK_ARGS} repology-linkchecker.py linkchecker/*.py linkchecker/*/*.py
