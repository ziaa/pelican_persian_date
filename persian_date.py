# -*- coding:utf-8 -*-
from .jdatetime import datetime
from pelican import signals

def article_persian_date(article_generator):
	for article in article_generator.dates:
		article.locale_date = datetime.fromgregorian(day=article.date.day,month=article.date.month,year=article.date.year).strftime(article.date_format)

def register():
	signals.article_generator_finalized.connect(article_persian_date)
