# -*- coding:utf-8 -*-
"""
Pelican Persian date
====================
A Pelican plugin to convert 'article.locale_date' attribute
from Gregorian calendar into Solar Hijri calendar (AKA Jalali calendar,
Persian calendar, Iranian calendar) which is the official calendar of
Iran and Afghanistan.
"""
# Pelican Persian date
# Copyright (C) 2015  Seyed Zia Eddin Azimi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .jdatetime import datetime
from pelican import signals

def article_persian_date(article_generator):
	for article in article_generator.dates:
		article.locale_date = datetime.fromgregorian(day=article.date.day,month=article.date.month,year=article.date.year).strftime(article.date_format)

def register():
	signals.article_generator_finalized.connect(article_persian_date)
