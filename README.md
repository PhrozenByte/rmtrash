rmtrash 1.13
============

Put files (and directories) in trash using the ```trash-put``` command in a way that is, otherwise as ```trash-put``` itself, compatible to GNUs ```rm``` and ```rmdir```.

[Click here for more information about trash-cli.](https://github.com/andreafrancia/trash-cli)

Installation
------------

Just download both scriptfiles (```rmtrash``` and ```rmdirtrash```) and put them in ```/usr/local/bin```. If you're using Arch Linux, you can also use the [AUR package](https://aur.archlinux.org/packages/rmtrash/).

If you don't want to readjust the usage of ```rm``` and ```rmdir```, a bash alias is probably a great solution for you. Just add the lines

```
alias rm='rmtrash'
alias rmdir='rmdirtrash'
alias sudo='sudo '
```

to your ```~/.bashrc``` (or ```~/.bash_aliases```). Consider adding the ```--forbid-root``` option (see *replacement option* below)! The last line is optional, without you'll notice that ```rmtrash``` and ```rmdirtrash``` won't be called when using ```sudo```.

Requirements
------------

Obviously  ```trash-cli``` (to provide the ```trash-put``` or ```trash``` command) is required. ```rmtrash``` and ```rmdirtrash``` *should* work great with any distribution. If ```rmtrash``` or ```rmdirtrash``` doesn't work with your favourite distribution, please file a bug report. It was written to work with ```bash```.

**You wanna make ```rmtrash``` and ```rmdirtrash``` work with your favorite distribution or improve them in general?** Go on, I appreciate it!

Usage of rmtrash
----------------

```shell
rmtrash [OPTION]... [FILE...]
```

```rmtrash``` supports everything that GNUs ```rm``` does, that means it accepts the following options (see ```--help```):

* Help options:
  * ```--help```: display help and exit
  * ```--version```: output version information and exit

* Application options:
  * ```-f```, ```--force```: ignore nonexistent files, never prompt
  * ```-i```: prompt before every removal
  * ```-I```: prompt once before removing more than three files, or when removing recursively. Less intrusive than ```-i```, while still giving protection against most mistakes
  * ```--interactive[=WHEN]```: prompt according to WHEN: ```never```, ```once``` (```-I```), or ```always``` (```-i```). Without WHEN, prompt always
  * ```--one-file-system```: when removing a hierarchy recursively, skip any directory that is on a file system different from that of the corresponding command line argument
  * ```--no-preserve-root```: do not treat ```/``` specially
  * ```--preserve-root```: do not remove ```/``` (default)
  * ```-d```, ```--dir```: remove empty directories
  * ```-r```, ```-R```, ```--recursive```: remove directories and their contents recursively
  * ```-v```, ```--verbose```: explain what is being done

Usage of rmdirtrash
-------------------

```shell
rmdirtrash [OPTION]... [DIRECTORY...]
```

```rmdirtrash``` supports everything that GNUs ```rmdir``` does, that means it accepts the following options (see ```--help```):
* Help options:
  * ```--help```: display help and exit
  * ```--version```: output version information and exit

* Application options:
  * ```--ignore-fail-on-non-empty```: ignore each failure that is solely because a directory is non-empty
  * ```-p```, ```--parents```: remove DIRECTORY and its ancestors; e.g., ```rmdirtrash -p a/b/c``` is similar to ```rmdirtrash a/b/c a/b a```
  * ```-v```, ```--verbose```: output a diagnostic for every directory processed

Replacement option
------------------

This option is not supposed to be used when calling ```rmtrash``` resp. ```rmdirtrash```. It helps you to control how and in which cases ```rm``` resp. ```rmdir``` are replaced. Without ```--forbid-root```, ```root``` isn't treated specially.

* ```--forbid-root[=HOW]```: forbid user ```root``` to trash files.  When standard input is a terminal, ```ask-forbid``` and ```ask-pass``` will question the user to pass the command to ```/bin/rm```. When standard input is no terminal, ```ask-forbid``` will abort the command, whereas ```ask-pass``` will pass the command to ```/bin/rm```. Use ```pass``` to pass all commands of user ```root``` to ```/bin/rm``` without a query. If user ```root``` should never trash files, use ```always```. In contrast, ```never``` treats ```root``` in no special way. Without ```HOW```, ```ask-forbid``` is assumed

Additional Notes
----------------

For additional information see the ```trash-list``` (or ```list-trash```), ```trash-empty``` (or ```empty-trash```), ```trash-restore``` (or ```restore-trash```) and ```trash-rm``` commands provided by ```trash-cli``` ([Homepage](https://github.com/andreafrancia/trash-cli)) as well as the [FreeDesktop.org Trash Specification](http://www.ramendik.ru/docs/trashspec.html). Note ```trash-put --help``` (or ```trash --help```) and ```rm --help```, too.

**A important note about execution time:**
```rmtrash``` is pretty slow! Because we're indexing all containing files before actually building the trash command (and because it's just a shell script), it is pretty slow when trashing many files. If you want to remove a very large directory (in terms of *many files*), consider using ```trash-put``` or ```rm``` directly. **Never** name ```rmtrash```s scriptfile ```rm``` - this will replace ```rm``` and is definitly not what you actually want! Use a bash alias as described above. The same applies to ```rmdirtrash```.

Typically you won't notice a time delay when using ```rmtrash``` and ```rmdirtrash```, but now you know that there is a time delay...

License & Copyright
-------------------

Copyright (C) 2011-2019  Daniel Rudolf <https://www.daniel-rudolf.de/>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 of the License only.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the [GNU General Public License](LICENSE) for more details.
