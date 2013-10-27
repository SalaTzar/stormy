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

```bash
$ pip install stormy
```

If you'd like to be able to use `stormy` wherever you are, you might want to
install it globally, e.g.:

```bash
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

**NOTE**: You can get your API key information by visiting your account
dashboard (https://api.stormpath.com/ui/dashboard) and clicking through the API
Key options.

```bash
$ stormy configure
```

TODO


## Changelog

v0.0: 10-27-2013

    - Started hacking on the project!  It's 1:24 am!  Woo!
