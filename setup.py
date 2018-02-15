try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Create randomized multiple choice quizzes with answer keys.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/rand_quiz_021118_1',
	'download_url': 'https://github.com/sunnylam13/rand_quiz_021118_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['random'],
	'scripts': [],
	'name': 'Randomized Multiple Choice Answer Quizzes with Answer Keys'
}

setup(**config)