# stormy

A CLI tool for managing (and working with) Stormpath.

![Stormy Logo](https://github.com/rdegges/stormy/raw/master/assets/stormy.jpg)


## Intro

[Stormpath](http://stormpath.com/) is one of my favorite tools.  They're an API
company that handles user accounts and authentication.

The idea is that instead of building your own users database, APIs, etc. -- you
instead just hit their servers to do things like:

- Create user accounts securely (HTTPs, bcrypt, etc.).
- Manage user permissions, group memberships, etc.
- Authenticate users securely.
- Etc.

This works particularly well for service oriented applications, where your user
data must be accessible by more than one codebase.  For instance -- if you've
got a website that needs to let users log into their accounts, as well as
developer API which must also authenticate users -- Stormpath becomes extremely
useful.

In my experience, they totally rock, and you should use them.


## Installation

You can install stormy on any \*nix computer with `pip` installed.  Just run the
following from your terminal:

```console
$ pip install stormy
```

If you'd like to be able to use `stormy` wherever you are, you might want to
install it globally, e.g.:

```console
$ sudo pip install stormy
```

:)


## Usage

Before you get started, you'll want to go create a
[Stormpath account](https://api.stormpath.com/register).  Once you've got that
setup, you'll need to give `stormy` your credentials so it can access your
account.

Just run `stormy configure` from the terminal to get started.  Your credentials
will be stored in a file named `~/.stormy`.  The `configure` command will prompt
you for your API key information.

**NOTE**: You can get your API key information by visiting your
[account dashboard](https://api.stormpath.com/ui/dashboard) and clicking
through the API Key options.

```console
$ stormy configure
```

Next, take a look at the help output (`stormy help` on the CLI):

```console
$ stormy help
Usage:
  stormy configure
  stormy applications
  stormy create_application
    (<name> | -n <name> | --name <name>)
    [(<description> | -d <description> | --description <description>)]
  stormy destroy_application (<name> | -n <name> | --name <name>)
  stormy directories
  stormy create_directory
    (<name> | -n <name> | --name <name>)
    [(<description> | -d <description> | --description <description>)]
  stormy destroy_directory (<name> | -n <name> | --name <name>)
  stormy accounts (<directory> | -d <directory> | --directory <directory>)
  stormy create_account
    (<directory> | -d <directory> | --directory <directory>)
    (<email> | -e <email> | --email <email>)
    (<password> | -p <password> | --password <password>)
    (<first_name> | -f <first_name> | --first-name <first_name>)
    (<last_name> | -l <last_name> | --last-name <last_name>)
    [(<middle_name> | -m <middle_name> | --middle-name <middle_name>)]
  stormy destroy_account
    (<directory> | -d <directory> | --directory <directory>)
    (<email> | -e <email> | --email <email>)
  stormy groups (<directory> | -d <directory> | --directory <directory>)
  stormy create_group
    (<directory> | -d <directory> | --directory <directory>)
    (<name> | -n <name> | --name <name>)
    [(<description> | -d <description> | --description <description>)]
  stormy destroy_group
    (<directory> | -d <directory> | --directory <directory>)
    (<name> | -n <name> | --name <name>)
  stormy add_account_to_group
    (<directory> | -d <directory> | --directory <directory>)
    (<email> | -e <email> | --email <email>)
    (<group> | -g <group> | --group <group>)
  stormy remove_account_from_group
    (<directory> | -d <directory> | --directory <directory>)
    (<email> | -e <email> | --email <email>)
    (<group> | -g <group> | --group <group>)
  stormy (-h | --help)
  stormy --version
```

Let's say you want to list all of your Stormpath applications -- **easy!** --
just run `stormy applications` and BAM, you'll see them all listed!

```console
$ stormy applications
Stormpath Applications
----------------------
{
  "Stormpath": {
    "description": "Manages access to the Stormpath Console and API.",
    "status": "ENABLED"
  },
  "test": {
    "description": "Randall's Test Application",
    "status": "ENABLED"
  }
}
----------------------
```

Now, let's say you want to create a new directory of users.  A directory is
basically a container that holds a bunch of user accounts.  To do this, we can
use the `create_directory` command:

```console
$ stormy create_directory "Users" "All website users."
Successfully created directory!
```

You could also accomplish the above by using either the short or long options as
well; for instance:

```console
$ stormy create_directory --description "All website users." -n "Users"
Successfully created directory!
```

Both work the same way.

Not bad, right?  Now that you know the basics, you should be able to figure the
rest out.


## Help

Need help?  Can't figure something out?  If you think you've found a bug, please
open an issue on the GitHub issue tracker.

Otherwise, [shoot me an email](mailto:r@rdegges.com)!


## Changelog

v0.1: 10-30-2013

    - Adding more flexible CLI options.  You can now use positional options,
      short options, or long options!

v0.0: 10-29-2013

    - Rolling our v0.0 onto PyPI.  We have a basic feature set.

v0.0: 10-27-2013

    - Started hacking on the project!  It's 1:24 am!  Woo!
