# Bandit Pre-Requisites Write-Up

---

## About

[Bandit Homepage](https://overthewire.org/wargames/bandit/bandit0.html)

Edit your SSH configuration file, ` ~/.ssh/config`, to create a 
shortcut for logging into overthewire's SSH server.
This will work for each level.

After completing the following steps, each "bandit"
level can be logged in with the following syntax:

`$ ssh bandit[N]@otw` (where '[N]' is the level number)

*instead of*

`$ ssh bandit1@bandit.labs.overthewire.org -p 2220`

each time.

---

## Steps

0. Create the `~/.ssh` directory if it does not exist:

`$ mkdir ~/.ssh`


1. Create/open `~/.ssh/config`: 

`$ nano ~/.ssh/config`


2. Add the following text to the `~/.ssh/config` file:

```
Host otw
    HostName bandit.labs.overthewire.org
    User bandit"$1"
    Port 2220
```

Line by line, these configuration settings accomplish the following:

- `Host otw` : shorten the hostname, `bandit.labs.overthewire.org`, to
 just `otw` for easier typing.

- `HostName bandit.labs.overthewire.org` : specify the actual hostname
 to connect to with SSH.

- `User bandit"$1"` : for each level, the username is `bandit[N]` where
 '[N]' is the level number. Here, `"$1"` is a variable that means,
 "whatever number follows." As long as username `bandit` is followed
 with a valid level number when logging in, SSH will connect to the
 appropriate user account on OverTheWire's remote server.

- `Port 2220` : the port number specified on the
  "bandit" [homepage](https://overthewire.org/wargames/bandit/).

---

## Commands & Tactics Used

---

### Commands

1. `mkdir`

2. `cd`

3. `nano`

---

### Tactics

1. Edit SSH configuration file to create a login shortcut for the
 bandit wargame.
