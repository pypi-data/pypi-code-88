# TBlock - An anticapitalist ad-blocker that uses the hosts file
# Copyright (C) 2021 Twann <twann@ctemplar.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__license__ = 'GPLv3'
__version__ = '1.1.4'

run_help = '''TBlock - An anticapitalist ad-blocker that uses the hosts file
Copyright (c) 2021 Twann <twann@ctemplar.com>

usage: tblock <operation> <options>

<operations>
* General
  -h  --help                              Show this help page
  -s  --status                            Show status information
  -v  --version                           Show version information
* Rules
  -a  --allow        [domain]             Allow a domain
  -b  --block        [domain]             Block a domain
  -r  --redirect     [domain]  [ip]       Redirect a domain to another address
  -d  --delete-rule  [domain]             Delete a rule for a domain
  -l  --list-rules   [options]            List active rules
* Filters
  -S  --subscribe    [filter]             Subscribe to a new filter
  -C  --add-custom   [id]     [file/url]  Subscribe to a custom filter
  -R  --remove       [filter]             Remove a filter (unsubscribe)
  -U  --update       [filter]             Update a filter
  -Q  --search       [query]  [options]   Search a query in the filter lists
  -M  --mod          [a|b|r]  [filter]    Change permissions of a filter
  -X  --change-id    [filter] [new-id]    Change the ID of a custom filter
  -I  --info         [filter]             Show information about a filter
  -L  --list         [options]            List all filters
  -Y  --sync                              Update remote filters repository
* Hosts
  -H  --update-hosts                      Update hosts file
  -D  --restore                           Restore default hosts file

<options>
* General options
  -f  --force                             Do not prompt user for anything
* Filters options
  -y  --with-sync                         Update remote filters repository
* List options
  -t  --standard                          Only show standard rules
  -u  --user                              Only show user rules
  -c  --custom                            Only show custom filters
  -k  --subscribing                       Only show subscribed filters
  -n  --unsubscribing                     Only show unsubscribed filters
  -w  --on-remote-repo                    Only show filters available on remote repository

For more information, see tblock(1)'''

run_converter_help = '''TBlockc - TBlock's built-in filter converter
Copyright (c) 2021 Twann <twann@ctemplar.com>

usage: tblockc [file] {-s,--syntax} [syntax] {-o,--output} [output_file] <options>

<options>
* General
  -h  --help                              Show this help page
  -f  --force                             Do not prompt user for anything
  -v  --version                           Show version information
* Converting
  -0  --zero                              Redirect domains to 0.0.0.0 instead of 127.0.0.1 (hosts)
  -c  --comments                          Also convert comments
  -o  --output       [file]               Original syntax of the filter to convert (required)
  -s  --syntax       [syntax]             New syntax to use (required)
  -i  --input-syntax [syntax]             Specify the syntax of the filter
* Other
  -g  --get-syntax   [file]               Scan a filter to get its syntax

<syntax>
  adblockplus                             AdBlock Plus syntax
  hosts                                   Hosts file format
  dnsmasq                                 dnsmasq.conf syntax
  list                                    Simple domain blacklist
  tblock                                  TBlock filter syntax
  opera                                   Opera filter syntax

For more information, see tblockc(1)'''
