# TODO and FIXME finder #

The easy way to find TODO and FINDME annotations in your project!

## Features ##

* **files** allows to find todo/fixme in one or more files specified by user
* **catalog** allows to find todo/fixme in catalog specified by user

### Installation: ###
1.    Clone repository using `git clone https://github.com/miloszhoc/TodoFinder.git` command.
2.    cd into _todo_finder_ folder.
3.    Type `python setup.py install` or `python3 setup.py install` in order to install program.
    
   To see all commands - type `ftfinder -h`

## Usage ##
The usage is simple and requires to specify the file or catalog which will be used to search for "todo" or "fixme"
annotations.

* `ftfinder files <file(s) name>` - search for "todo" or "fixme" annotations in given file(s).

* `ftfinder catalog <catalog name> <ext>` - search for "todo" or "fixme" annotations for given extension in the catalog.
  In this mode you can also specify if you want to exclude some directories or files.

You can also specify if you want o see only Todo or Fixme annotations by passing appropriate flag (see section below).
The default mode shows both fixme and todo.

## Arguments ##

* **files**    
  _positional arguments:_       
  `file_name`    file or files to open    
  _optional arguments:_    
  `-h, --help`   help message    
  `-f, --fixme`  show only FIXME    
  `-t, --todo`   show only TODO

* **catalog**    
  _positional arguments:_    
  `path`                  path to catalog    
  `ext`                   file extension    
  _optional arguments:_    
  `-h, --help`            help message    
  `-f, --fixme`           show only FIXME    
  `-t, --todo`            show only TODO    
  `-e [EXCLUDE [EXCLUDE ...]], --exclude [EXCLUDE [EXCLUDE ...]]` excluded files and folders
