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
  stormy create_application <name> [<description>]
  stormy destroy_application <name>
  stormy directories
  stormy create_directory <name> [<description>]
  stormy destroy_directory <name>
  stormy accounts <directory_name>
  stormy create_account <directory_name> <email> <password> <first_name> <last_name> [<middle_name>]
  stormy destroy_account <directory_name> <email>
  stormy groups <directory_name>
  stormy create_group <directory_name> <name> [<description>]
  stormy destroy_group <directory_name> <name>
  stormy add_account_to_group <directory_name> <email> <group_name>
  stormy remove_account_from_group <directory_name> <email> <group_name>
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

Not bad, right?


## Changelog

v0.0: 10-29-2013

    - Rolling our v0.0 onto PyPI.  We have a basic feature set.

v0.0: 10-27-2013

    - Started hacking on the project!  It's 1:24 am!  Woo!
