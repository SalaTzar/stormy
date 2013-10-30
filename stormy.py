#!/usr/bin/env python
"""
stormy
~~~~~~

A CLI tool for managing (and working with) Stormpath (https://stormpath.com/).

Usage:
  stormy configure
  stormy applications
  stormy create_application <name> [<description>]
  stormy destroy_application <name>
  stormy directories
  stormy create_directory <name> [<description>]
  stormy destroy_directory <name>
  stormy accounts <directory_name>
  stormy create_account <directory_name> <email> <password> <first_name> <last_name> [<middle_name>]
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

    def applications(self):
        """List all available applications."""
        json = {}

        print 'Stormpath Applications'
        print '----------------------'
        for application in self.client.applications:
            json[application.name] = {
                'description': application.description,
                'status': application.get_status(),
            }

        print dumps(json, indent=2, sort_keys=True)
        print '----------------------'

    def create_application(self, name, description):
        """Create a new application."""
        try:
            application = self.client.applications.create({
                'name': name,
                'description': description,
            })
            print 'Successfully created application!'
        except Error, e:
            print 'ERROR: Failed to create application!'
            print 'DETAILS:', e.message

    def destroy_application(self, name):
        """Destroy an application."""
        try:
            application = self.client.applications.search(name)[0]

            input = raw_input('Are you sure you want to destroy the application %s? (y\\n) ' % name)
            if input.strip().lower() == 'y':
                application.delete()
                print 'Successfully destroyed application!'
            else:
                print 'Bailing out.'

        except IndexError:
            print 'ERROR: Could not find application %s!' % name

    def directories(self):
        """List all available directories."""
        json = {}

        print 'Stormpath Directories'
        print '---------------------'
        for directory in self.client.directories:
            json[directory.name] = {
                'description': directory.description,
                'status': directory.get_status(),
            }

        print dumps(json, indent=2, sort_keys=True)
        print '----------------------'

    def create_directory(self, name, description):
        """Create a new directory."""
        try:
            self.client.directories.create({
                'name': name,
                'description': description,
            })
            print 'Successfully created directory!'
        except Error, e:
            print 'ERROR: Failed to create directory!'
            print 'DETAILS:', e.message

    def destroy_directory(self, name):
        """Destroy a directory."""
        try:
            directory = self.client.directories.search(name)[0]

            input = raw_input('Are you sure you want to destroy the directory %s? (y\\n) ' % name)
            if input.strip().lower() == 'y':
                directory.delete()
                print 'Successfully destroyed directory!'
            else:
                print 'Bailing out.'

        except IndexError:
            print 'ERROR: Could not find directory %s!' % name

    def accounts(self, directory_name):
        """List all available accounts for the specified application."""
        json = {}

        try:
            directory = self.client.directories.search(directory_name)[0]

            print 'Stormpath Accounts'
            print '------------------'
            for account in directory.accounts:
                json[account.email] = {
                    'username': account.username,
                    'full_name': account.full_name,
                    'given_name': account.given_name,
                    'middle_name': account.middle_name,
                    'surname': account.surname,
                    'status': account.get_status(),
                }

            print dumps(json, indent=2, sort_keys=True)
            print '------------------'
        except IndexError:
            print 'ERROR: Could not find directory %s!' % directory

    def create_account(self, directory_name, email, password, first_name,
            last_name, middle_name):
        """Create a new user account for the specified application."""
        try:
            directory = self.client.directories.search(directory_name)[0]
            directory.accounts.create({
                'email': email,
                'password': password,
                'given_name': first_name,
                'surname': last_name,
                'middle_name': middle_name,
            })
            print 'Successfully created account!'
        except IndexError:
            print 'ERROR: Could not find directory %s!' % directory_name
        except Error, e:
            print 'ERROR: Failed to create account!'
            print 'DETAILS:', e.message, e.code


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
    elif arguments['create_application']:
        stormy.create_application(
            arguments['<name>'],
            arguments['<description>']
        )
    elif arguments['destroy_application']:
        stormy.destroy_application(arguments['<name>'])
    if arguments['directories']:
        stormy.directories()
    elif arguments['create_directory']:
        stormy.create_directory(
            arguments['<name>'],
            arguments['<description>']
        )
    elif arguments['destroy_directory']:
        stormy.destroy_directory(arguments['<name>'])
    elif arguments['accounts']:
        stormy.accounts(arguments['<directory_name>'])
    elif arguments['create_account']:
        stormy.create_account(
            arguments['<directory_name>'],
            arguments['<email>'],
            arguments['<password>'],
            arguments['<first_name>'],
            arguments['<last_name>'],
            arguments['<middle_name>'],
        )


if __name__ == '__main__':
    main()
