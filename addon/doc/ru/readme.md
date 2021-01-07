# eMule #

*	Авторы: Noelia, Chris, Alberto.
*	NVDA compatibility: 2019.3 or later.
*	загрузить [стабильную версию][1]
*	загрузить [разрабатываемую версию][3]
*	download [version compatible with NVDA 2017.3][4]

This add-on helps to improve accessibility of eMule with nVDA.  It also
provides additional keyboard commands for moving in different windows and
gives Useful information about eMule.

It's based on the eMuleNVDASupport add-on, developed by the same author. You
should uninstall that old add-on to use this one, since both have common
keystrokes and features.

Проверено на [eMule][2] 0.50a.

## Основные команды: ##

*	control+shift+h: перемещение фокуса и мыши к главной панели инструментов.
*	control+shift+t: Чтение текущего окна.
*	control+shift+n: Перемещение фокуса на поле Имя в окне поиска.
*	control+shift+p: В окне поиска, перемещает фокус и мышь в список
  параметров поиска или в поле редактирования вариантов.
*	control+shift+b Перемещение фокуса в список в текущем окне. Например,
  используется в окне поиска, загрузки в окне передачи и т.д.
*	control+shift+o: Перемещение фокуса в поля редактирования только для
  чтения в текущем окне. Например, полученные сообщения IRC, доступные
  серверы и т.д.
*	control+NVDA+f: Если курсор находится в поле редактирования только для
  чтения, откроет диалог поиска, доступный в NVDA.
*	control+shift+l: Перемещение объекта навигатора и мыши к заголовкам
  текущего списка.
*	control+shift+q: Читает первый объект в строке состояния; предоставляет
  информацию о последних действиях.
*	control+shift+w: Читает второй объект в строке состояния; содержит
  информацию о файлах и пользователях на текущем сервере.
*	control+shift+e: Читает третий объект строки состояния; полезно знать
  скорость загрузки / выгрузки.
*	control+shift+r: Читает четвёртый объект строки состояния; отчеты о
  подключении к eD2K и Kad сетям.

## Управление столбцами. ##

Находясь в списке, можно перемещать курсор между строк и столбцов с помощью
alt+ctrl+ стрелок. Следующие команды клавиш здесь также доступны:

*	nvda+control+1-0: читает первые 10 столбцов.
*	nvda+shift+1-0: читает столбцы с 11 по 20.
*	nvda+shift+C: копирует содержимое последнего прочитанного столбца в буфер
  обмена.

## Changes for 4.0 ##
*	Requires NVDA 2019.3 or later.

## Изменения в версии 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Изменения в версии 2.0 ##
*	 Справка дополнения доступна в диспетчере дополнений.

## Изменения в версии 1.2 ##
*	 При перемещении к сообщениям IRC, выделенный текст сообщается правильно.
*	 Комбинации клавиш, использующихся для перемещения в список результатов
   поиска, были обобщены, чтобы иметь возможность перемещать фокус на любой
   доступный список текущего окна.
*	 Команда, используемая для просмотра сообщений IRC, была обобщена, чтобы
   переходить к любому полю редактирования только для чтения, что делает
   возможным просмотреть информацию о соединении в окне сервера.
*	 При перемещении мыши и фокуса на панель инструментов, в некоторых случаях
   были двукратные объявления. Это было исправлено.

## Изменения в версии 1.1 ##
*	 Исправлена ошибка элемента меню eMule в пункте меню помощи NVDA, когда
   имя папки конфигурации Пользователя содержит не латинские буквы.
*	 Горячие клавиши могут теперь быть переназначены с помощью диалога жестов
   ввода NVDA.

## Изменения в версии 1.0 ##
*	 Начальная версия.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: https://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev