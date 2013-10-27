#!/usr/bin/env python
"""
stormy
~~~~~~

A CLI tool for managing (and working with) Stormpath (https://stormpath.com/).

Usage:
  stormy configure
  stormy (-h | --help)
  stormy --version

Options:
  -h --help  Show this screen.
  --version  Show version.

Written by Randall Degges <http://www.rdegges.com/>.
"""


from json import dumps, loads
from os import chmod
from os.path import exists, expanduser
from sys import exit
from textwrap import wrap

from docopt import docopt
from stormpath.client import Client
from stormpath.error import Error


##### GLOBALS
CONFIG_FILE = expanduser('~/.stormy')
VERSION = 'stormy 0.0'


class Stormy(object):
    """Our Stormpath CLI manager."""

    def __init__(self):
        """Initialize our Stormpath client, or die tryin' >:)"""
        if exists(CONFIG_FILE):
            credentials = loads(open(CONFIG_FILE, 'rb').read())
            self.client = Client(api_key={
                'id': credentials.get('stormpath_api_key_id'),
                'secret': credentials.get('stormpath_api_key_secret'),
            })
        else:
            print 'No API credentials found!  Please run stormy configure to set them up.'
            exit(1)


def configure():
    """
    Initializing stormy.

    This will store the user's API credentials in: ~/.stormy, and ensure the
    API credentials specified actually work.
    """
    print 'Initializing `stormy`...\n'
    print "To get started, we'll need to get your Stormpath API credentials.  Don't have a Stormpath account?  Go get one!  https://stormpath.com/"

    finished = False
    while not finished:
        api_key_id = raw_input('Enter your API Key ID: ').strip()
        api_key_secret = raw_input('Enter your API Key Secret: ').strip()
        if not (api_key_id or api_key_secret):
            print '\nNot sure how to find your Stormpath API credentials?'
            print 'Log into your Stormpath account, then visit your dashboard and use the "Manage Existing Keys" link.\n'
            continue

        # Validate the API credentials.
        client = Client(api_key={
            'id': api_key_id,
            'secret': api_key_secret,
        })
        try:
            applications = client.applications
            print '\nSuccessfully initialized stormy!'
            print 'Your API credentials are stored in the file:', CONFIG_FILE, '\n'
            print 'Run stormy for usage information.'

            with open(CONFIG_FILE, 'wb') as stormycfg:
                stormycfg.write(dumps({
                    'stormpath_api_key_id': api_key_id,
                    'stormpath_api_key_secret': api_key_secret,
                }, indent=2, sort_keys=True))

            # Make the stormy configuration file only accessible to the current
            # user -- this makes the credentials a bit more safe.
            chmod(CONFIG_FILE, 0600)

            finished = True
        except Error:
            print '\nYour API credentials are not working, please verify they are correct, then try again.\n'


def main():
    """Handle user input, and do stuff accordingly."""
    arguments = docopt(__doc__, version=VERSION)

    # Handle the configure as a special case -- this way we won't get invalid
    # API credential messages when we're trying to configure stormy.
    if arguments['configure']:
        configure()
        return

    stormy = Stormy()
    if arguments['applications']:
        stormy.applications()


if __name__ == '__main__':
    main()
