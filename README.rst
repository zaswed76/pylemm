pylemm
=====================

**Скрипт приводит к нормальной (словарной) форме список слов английского языка.**

Установка:

   перед установкой один раз выполнить

для mac os::

   echo "PATH=\$PATH:~/Library/Python/2.7/bin" >> ~/.profile

для Linux::

    echo "PATH=\$PATH:~/.local/bin" >> ~/.bashrc

Установить::

   pip install --upgrade --user git+https://github.com/zaswed76/pylemm.git



Пример::

   >>> pylemm
   >>> имя файла или каталога. < q > - выход
   >>> "full_path1 full_path2"

Описание конфига

для mac os путь - **/Users/admin/Library/Python/2.7/lib/python/site-packages/pylemm/etc/conf.json**

для Linux - **/home/vostro/.local/lib/python2.7/
site-packages/pylemm/etc/conf.json**

conf.json::

   {
     # разделитель между словами в csv файле
     "delimiter": ",",
     # расширение целевого файла
     "ext_file": ".csv",
     "target_appendix": "_normal",
     # заполнитель для пустых ячеек
     "empty_filler": "",
     "tag_names": {
       "lemmatization": "LEMM",
       "stemming": "STEMM",
       "not_changed": "NONE"
     },
     "columns_names": {
       "source": "SOURCE",
       "lemm": "LEMM",
       "stemm": "STEMM",
       "tag": "TAG"
     },
     # порядок столбцов слева направо
     "columns_order": [
       "source",
       "lemm",
       "stemm",
       "tag"
     ]

   }