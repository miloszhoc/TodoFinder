# TODO and FIXME finder #

## Features ##
*    **files** allows to find todo/fixme in one or more files specified by user
*    **catalog** allows to find todo/fixme in catalog specified by user

## Usage ##
todo
## Arguments ##
*    **files**    
_positional arguments:_       
`file_name`    file or files to open    
_optional arguments:_    
  `-h, --help`   help message    
  `-f, --fixme`  show only FIXME    
  `-t, --todo`   show only TODO    

*    **catalog**    
_positional arguments:_    
`path`                  path to catalog    
`ext`                   file extension    
_optional arguments:_    
`-h, --help`            help message    
`-f, --fixme`           show only FIXME    
`-t, --todo`            show only TODO    
`-e [EXCLUDE [EXCLUDE ...]], --exclude [EXCLUDE [EXCLUDE ...]]` excluded files and folders
