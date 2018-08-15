from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='jejunuMeals',
    version='1.0',
    url='https://github.com/BetaF1sh/commit-telegram-bot',
    license='MIT',
	author='BetaF1sh',
    author_email='iam@muhun.kim',
    description='Remind your commit and coding every day with chat bot!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3',
install_requires=['requests'])
