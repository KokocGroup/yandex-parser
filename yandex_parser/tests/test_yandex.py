# -*- coding:utf-8 -*-
import unittest

from yandex_parser.exceptions import YandexParserError
from yandex_parser.tests import YandexParserTests
from yandex_parser.yandex import YandexParser
from yandex_parser.yandex_bar import YandexBarParser
from yandex_parser.yandex_suggest import YandexSuggestParser


class YandexParserTestCase(YandexParserTests):

    def test_captcha_1(self):
        html = self.get_data('captcha_1.html')
        parser = YandexParser(html)

        captcha_data = parser.get_captcha_data()
        exp = {
            'url': u'http://yandex.ru/captchaimg?aHR0cDovL3MuY2FwdGNoYS55YW5kZXgubmV0L2ltYWdlP2tleT1kM1I3SDhDRGlTT3RlVzNvYk9zcFo4bk1lc0NOUjhXQw,,_0/1435077202/853e18711cde74266e45da1315dacee2_2bf39001bd241d1c6539b7db6a0464ad', 
            'form_action': '/checkcaptcha',
            'form_data': {
                'key': 'd3R7H8CDiSOteW3obOspZ8nMesCNR8WC_0/1435077202/853e18711cde74266e45da1315dacee2_ff263da232b103004f79fe4c4e139913', 
                'retpath': 'http://yandex.ru/yandsearch?p=0&text=%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5+%D0%B1%D0%B0%D0%BD%D0%BA%D0%B8&site=&numdoc=50&lr=213_cefc8bbe530fbaf69685556720f14a26'
            }
        }
        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(captcha_data, exp)
   
       
    def test_bar_info_1(self):
        html = self.get_data('bar_info_1.xml')
        parser = YandexBarParser(html)
        exp = {
            'domain': u'kokoc.com', 
            'title': u'Тема: Продвижение сайтов', 
            'url': u'http://yaca.yandex.ru/yca/', 
            'rang': u'5', 
            'value': u'1600', 
            'textinfo': u"""Тема: Продвижение сайтов
Регион: Москва
Источник: Официальный
Сектор: Коммерческие"""
        }
        bar = parser.get_bar_info()
        for k, v in exp.iteritems():
            self.assertEquals(bar[k], v)
   
    def test_suggest_1(self):
        html = self.get_data('suggest_1.html')
        parser = YandexSuggestParser(html)
        exp = [
            u"окна пластиковые расчет стоимости онлайн",
            u"окна рехау официальный сайт",
            u"окна роста официальный сайт",
            u"окна 21 век официальный сайт",
            u"окна калева официальный сайт",
            u"окна комфорта официальный сайт москва",
            u"окна роста",
            u"окна века или рехау что лучше",
            u"окна хоббит москва официальный сайт",
            u"окна комфорта"        
        ]
        suggest = parser.get_suggest()
        self.assertEquals(suggest, exp)
           
    def test_region_code_1(self):
        html = self.get_data('region_code_1.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(parser.get_region_code(), 213)
   
    def test_pagination_exists_1(self):
        html = self.get_data('serp_1.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertTrue(parser.pagination_exists())
   
    def test_pagination_exists_2(self):
        html = self.get_data('serp_3.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertFalse(parser.pagination_exists())
   
    def test_pagecount_1(self):
        html = self.get_data('serp_1.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(parser.get_pagecount(), 124000000)
   
    def test_pagecount_2(self):
        html = self.get_data('serp_2.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(parser.get_pagecount(), 354000)
   
    def test_pagecount_3(self):
        html = self.get_data('serp_3.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(parser.get_pagecount(), 22)
   
    def test_not_found(self):
        html = self.get_data('not_found_1.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertTrue(parser.is_not_found())

    def test4(self):
        html = self.get_data('bad-content.html')
        self.assertFalse(YandexParser.is_yandex(html))

    def test12(self):
        html = self.get_data('v1-2016-02-17.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 228000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'qpstol.ru')
        self.assertEquals(serp['sn'][49]['d'], 'moskva.tiu.ru')

    def test13(self):
        html = self.get_data('v1-2016-02-17-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 195000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'roomer.ru')
        self.assertEquals(serp['sn'][49]['d'], 'mybabytoys.ru')

    def test14(self):
        html = self.get_data('v1-2016-02-17-2.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 593000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'youtube.com')
        self.assertEquals(serp['sn'][49]['d'], 'modmine.net')

    def test15(self):
        html = self.get_data('v1-2016-02-17-3.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 3000000)
        self.assertEquals(len(serp['sn']), 20)
        self.assertEquals(serp['sn'][0]['d'], 'irr.ru')
        self.assertEquals(serp['sn'][19]['d'], 'avito.ru')

    def test16(self):
        html = self.get_data('v1-2016-02-17-4.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 527000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'watches.ru')
        self.assertEquals(serp['sn'][49]['d'], 'omax-msk.ru')

    def test17(self):
        html = self.get_data('v1-2016-02-18.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 1000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'stihi-rus.ru')
        self.assertEquals(serp['sn'][49]['d'], '4ernovik.ru')

    def test18(self):
        html = self.get_data('v1-2016-02-18-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 6000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'mylcd.info')
        self.assertEquals(serp['sn'][49]['d'], 'shop.bbk.ru')

    def test19(self):
        html = self.get_data('v1-2016-02-20.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 3000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'youtube.com')
        self.assertEquals(serp['sn'][49]['d'], 'truba.com')

    def test20(self):
        html = self.get_data('2016-05-19.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 377000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'mebelaero.ru')
        self.assertEquals(serp['sn'][0]['s'], u'Стол PICASSO. 07.04.2016 Компания «AERO» является поставщиком продукции в самый большой в Европе и Москве Porsche-центр.')
        self.assertEquals(serp['sn'][49]['d'], 'stolnadom.ru')
        self.assertEquals(serp['sn'][49]['s'], u'Столы. Мебельный интернет-магазин Стол на Дом .RU - магазин стильной мебели. ... Интернет-магазин мебели - простой способ купить столы в Москве и в России.')

    def test21(self):
        html = self.get_data('2016-06-14-one-res.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 1)
        self.assertEquals(len(serp['sn']), 1)
        self.assertEquals(serp['sn'][0]['d'], 'mogilev.pulscen.by')
        self.assertEquals(serp['sn'][0]['s'], u'Информация о предложениях в рубрике Столешницы для кухни для Могилева. ... Столешницы для кухни в Могилеве. 30 товаров и услуг от 2 поставщиков.')

    def test22(self):
        html = self.get_data('2016-06-14-thousands.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 50000)
        self.assertEquals(len(serp['sn']), 30)
        self.assertEquals(serp['sn'][0]['d'], 'mogilev.deal.by')
        self.assertEquals(serp['sn'][0]['s'], u'Широкий выбор поставщиков, у которых можно купить столешницы и комплектующие в Могилеве по лучшей цене. ... Столешницы для кухни Quartzforms.')
        self.assertEquals(serp['sn'][29]['d'], 'mirdereva.ru')
        self.assertEquals(serp['sn'][29]['s'], u'Столешницы для кухни из дерева. от 1082 р/м2.')

    def test23(self):
        html = self.get_data('2016-06-14-millions.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 13000000)
        self.assertEquals(len(serp['sn']), 30)
        self.assertEquals(serp['sn'][0]['d'], 'otdelka-trade.ru')
        self.assertEquals(serp['sn'][0]['s'], u'Столешница в продаже 28 вида товаров. Доставка по Москве и регионам. Звоните!')
        self.assertEquals(serp['sn'][29]['d'], 'mdvm.ru')
        self.assertEquals(serp['sn'][29]['s'], u'Говоря столешница, многие подразумевают кухонные столешницы, но столешницы из ДСП и МДФ используют не только как столешницы для кухни...')

    def test24(self):
        html = self.get_data('2016-06-16.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 612000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'exmob.net')
        self.assertEquals(serp['sn'][0]['s'], u'На первом месте самый удобный из них, а именно с помощью SMS. Отправляете сообщение с текстом «СТОП 5051» на аналогичный номер 5051.')
        self.assertEquals(serp['sn'][49]['d'], 'depositfiles.com')
        self.assertEquals(serp['sn'][49]['s'], u'...номерам», введя короткий номер или идентификатор услуги в строке поиска ... SMS-сообщение с текстом «СТОП » на номер 5051 (смс бесплатно в домашнем регионе)')

    def test25(self):
        html = self.get_data('2016-06-16-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 168000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'diamed.ru')
        self.assertEquals(serp['sn'][0]['s'], u'О клинике. Клиника «Диамед» у метро Щелковская открыла свои двери для пациентов в мае 2001 года.')
        self.assertEquals(serp['sn'][49]['d'], 'clinics.webtst.ru')
        self.assertEquals(serp['sn'][49]['s'], u'«Диамед» - это сеть клиник, удобно расположенных в районах Москвы. ... В медицинском центре «Диамед» на Щелковской работают опытные...')

    def test26(self):
        html = self.get_data('2016-07-26.html')

        parser = YandexParser(html)
        serp1 = parser.get_serp()

        cleaned_html = parser.get_clean_html()
        parser = YandexParser(cleaned_html)
        serp2 = parser.get_serp()
        self.assertDictEqual(serp1, serp2)

    def test27(self):
        html = self.get_data('2016-07-31.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 29000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'videopartner.kinopoisk.ru')
        self.assertEquals(serp['sn'][0]['t'], u'КонтрольКиноПоиск')
        self.assertEquals(serp['sn'][0]['s'], u'')
        self.assertEquals(serp['sn'][49]['d'], '8serials.ucoz.ru')
        self.assertEquals(serp['sn'][49]['s'], u'Чтобы смотреть Контроль (2004) онлайн бесплатно - регистрация не нужна и смс отправлять не надо, у нас все БЕСПЛАТНО. Для просмотра бесплатных фильмов, мультфильмов, сериалов...')

    def test28(self):
        html = self.get_data('2016-08-01.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 2000000)
        self.assertEquals(len(serp['sn']), 30)
        self.assertEquals(serp['sn'][0]['d'], 'otvet.mail.ru')
        self.assertEquals(serp['sn'][0]['t'], u'Ответы@Mail.Ru: Посоветуйте профессионального фотографа в Кемерово. И желательно что бы можно...')
        self.assertEquals(serp['sn'][0]['s'], u'Пользователь натуська задал вопрос в категории Обработка и печать фото и получил на него 1 ответ...')

        self.assertEquals(serp['sn'][2]['d'], 'xn----gtbm8afgk0g.xn--p1ai')
        self.assertEquals(serp['sn'][2]['fl'], 1)
        self.assertEquals(serp['sn'][2]['t'], u'Студия F"')

        self.assertEquals(serp['sn'][29]['d'], 'kindtoys.ru')
        self.assertEquals(serp['sn'][29]['s'], u'Свадебный фотограф кемерово. 21:42:01 - Диана:Каталог свадебных фирм в Кемерово в рубрике Фотографы.')

    def test29(self):
        html = self.get_data('2016-08-12.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 5000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'kinopoisk.megogo.net')
        self.assertEquals(serp['sn'][0]['t'], u'НянькиКиноПоиск')
        self.assertEquals(serp['sn'][0]['s'], u'')

        self.assertEquals(serp['sn'][1]['d'], 'kinogo.co')
        self.assertEquals(serp['sn'][1]['fl'], 0)
        self.assertEquals(serp['sn'][1]['t'], u'Няньки (1995) смотреть онлайн бесплатно')

        self.assertEquals(serp['sn'][49]['d'], 'filmix.net')
        self.assertEquals(serp['sn'][49]['s'], u'Трейлеры, семейный, комедия. Режиссер: Ашот Кещян. В ролях: Николай Наумов, Арарат Кещян, Аглая Шиловская и др. Главная героиня – жесткая и хваткая бизнес-леди по имени Валентина, которая является владелицей успешной туристической компании.')

    def test30(self):
        html = self.get_data('2016-08-15.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 9000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'ttfr.ru')
        self.assertEquals(serp['sn'][0]['t'], u'Федерация настольного тенниса России')
        self.assertEquals(serp['sn'][0]['s'], u'Календарь и результаты соревнований. Рейтинги теннисистов. Описание структуры федерации. Список официальных документов. Новости настольного тенниса. Контакты.')

        self.assertEquals(serp['sn'][49]['d'], 'ttplayspb.com')
        self.assertEquals(serp['sn'][49]['t'], u'ttplayspb - forum ttplayspb')
        self.assertEquals(serp['sn'][49]['s'], u'Admin » 06 авг 2016, 15:56 » в форуме World table tennis. ... ЛЮБИТЕЛЬСКИЙ настольный теннис в г.Санкт-Петербург.')

    def test31(self):
        html = self.get_data('2016-08-15-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 323000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'novaposhta.ua')
        self.assertEquals(serp['sn'][0]['t'], u'Термінова і експрес доставка: транспортно-логістичні...')
        self.assertEquals(serp['sn'][0]['s'], u'Весь спектр логістичних послуг, швидка та надійна доставка документів, кореспонденції та листів по Україні ★ Клієнтська подтримка 24/7 ☎ 0-800-500-609...')

        self.assertEquals(serp['sn'][39]['d'], '_www.nm.ru')
        self.assertEquals(serp['sn'][39]['t'], u'_www.nm.ru')
        self.assertEquals(serp['sn'][39]['s'], '')
        self.assertEquals(serp['sn'][39]['savedCopy'], None)

        self.assertEquals(serp['sn'][49]['d'], 'market.yandex.ru')
        self.assertEquals(serp['sn'][49]['t'], u'Купить холодильник Indesit BIA 18 — выгодные цены...')
        self.assertEquals(serp['sn'][49]['s'], u'DPD, Энергия, Экспресс-почта, Эксист, УралТрансСервис, Экспресс-курьер, Почта России, ПЭК, Новая Почта, Желдорэкспедиция, ЖелдорАльянс, Деловые Линии...')

    def _print_sn(self, serp):
        for sn in serp['sn']:
            print sn['p'], sn['d'], sn['u'], sn['t'], sn['s']

if __name__ == '__main__':
    unittest.main()
