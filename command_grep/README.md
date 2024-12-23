# Лабораторная работа: Команда grep

## Цель

Познакомиться с основными возможностями команды `grep` для поиска текста в файлах и потоках ввода.

## Теоретическая справка

Команда `grep` (Global Regular Expression Print) - это мощный инструмент командной строки Linux для поиска строк,
соответствующих заданному шаблону, в файлах или потоке ввода. Основной синтаксис команды:

```bash
grep [опции] шаблон [файлы]
```

| Название                      | Описание                                                       |
|-------------------------------|----------------------------------------------------------------|
| -i (или --ignore-case)	       | игнорировать регистр символов при поиске                       |
| -v (или --invert-match)       | выводить строки, не соответствующие шаблону                    |
| -n (или --line-number)        | выводить номера строк вместе с результатами                    |
| -c (или --count)              | выводить только количество найденных строк                     |
| -r (или -R, --recursive)      | рекурсивный поиск по каталогам                                 |
| -w (или --word-regexp)        | искать только целые слова, а не подстроки                      |
| -l (или --files-with-matches) | выводить только имена файлов, в которых есть совпадения        |
| -h (или --no-filename)        | не выводить имя файла в результатах поиска                     |
| -E (или --extended-regexp)    | использовать расширенные регулярные выражения                  |
| -o, --only-matching           | выводить только ту часть строки, которая соответствует шаблону |

## Практика

Создайте текстовую дерикторию test_dir и в ней два файла: example_1.txt и example_2.txt, со следующим содержимым:

#### example_1.txt

```
This is the first line.
    Second line is here.
 A THIRD LINE here too, and it's also Third.
        fourth line is also here.
Fifth Line is here, again!
    this is the sixth line.
Last line.
```

#### example_1.txt

```
    The quick brown fox jumps over the lazy dog.
Another line with text, but no "line" word.
    This file also has some content, which is different.
Is this also the second file? Yes, it is.
 line appears once here in the second file.
And yet another line.
The End.
```

### Задание 1: Базовый поиск

Найдите все строки, содержащие слово line в файле example.txt.

```
grep line example.txt
```

Результат:

```
This is the first line.
    Second line is here.
        fourth line is also here.
    this is the sixth line.
```

### Задание 2: Количество строк

Найдите количество строк в файлах директории test_dir, которые содержат целое слово this
и при этом не учитывают его регистр

```
grep -r -w -i -c "this" test_dir
```

Результат:

```
test_dir/example_1.txt:2
test_dir/example_2.txt:1
```

## Лабораторная

Вашей задачей будет найти количество человек в файле ```file.txt``` для которых выполняются условия:

1. у человека есть номер в формате ```phone: +7 (XXX) XXX-XX-XX```
2. у человека есть email в формате ```email: *@*.*```, где * - один или больше символов

#### Входные данные:

Гарантируется, что:

1. у человека есть имя
2. каждый человек, его номер и email, если они есть, написаны в одной отдельной строке
3. email написан после номера

#### Выходные данные

Количество людей с верными форматами номеров и emailов.