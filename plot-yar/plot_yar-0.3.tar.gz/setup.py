from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(name='plot_yar',
      version='0.3',
      description='Plotting_graphs',
      packages=['plot_yar'],
      author_email='vodyar00@mail.ru',
      zip_safe=False,
      # Длинное описание, которое будет отображаться на странице PyPi. Использует README.md репозитория для заполнения.
	long_description=long_description,
	# Определяет тип контента, используемый в long_description.
	long_description_content_type="text/markdown",
	# URL-адрес, представляющий домашнюю страницу проекта. Большинство проектов ссылаются на репозиторий.
	url="https://github.com/yarvod/plot_yar",
	# Находит все пакеты внутри проекта и объединяет их в дистрибутив.
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	])