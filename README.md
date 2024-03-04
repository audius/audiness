# audiness

Helper scripts to interact with Nessus instances. The CLI allows one to perform tasks on a 
Nessus installation without using the web interface.

## Installation

The package is available in the [Python Package Index](https://pypi.org/project/audiness/).

```bash
$ pip3 install audiness --user
```

For Nix or NixOS users is a package available. Keep in mind that the lastest releases might only
be present in the ``unstable`` channel.

```bash
$ nix-env -iA nixos.audiness
```

## Setup

You have to generate API keys for your users. Click on username in the right upper corner, then
select ``API keys`` and press the ``Generate`` button.

Note the access key and the secrect key somewhere.

If you don't plan to run `audiness` on the same host as your Nessus instance is running then it
could be required that you use port-forwarding to access the Nessus web interface through a tunnel.

```bash
$ ssh -L 8834:localhost:8834 -l your_user_name host.with.nessus
```

## Usage

Use `--help` to get a general overview or `COMMAND --help` for the detailed help.

```bash
$ audiness --help
                                                                                                                                  
 Usage: audiness [OPTIONS] COMMAND [ARGS]...                                                                                      
                                                                                                                                  
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --access-key                TEXT  Nessus API access key [env var: ACCESS_KEY] [default: None] [required]                    │
│ *  --secret-key                TEXT  Nessus API secret key [env var: SECRET_KEY] [default: None] [required]                    │
│    --host                      TEXT  URL to Nessus instance [default: https://localhost:8834]                                  │
│    --install-completion              Install completion for the current shell.                                                 │
│    --show-completion                 Show completion for the current shell, to copy it or customize the installation.          │
│    --help                            Show this message and exit.                                                               │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ folders                                                                                                                        │
│ scans                                                                                                                          │
│ server                                                                                                                         │
│ software                                                                                                                       │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

If you don't want to enter the access key and the secrect key then put them in the
environment of your shell.

```bash
$ export ACCESS_KEY="ae0bf3d57f8f8f6bcd8d01d3aedde60937d08647da4d89a6eb4dba2a9bee5d5d"
$ export SECRET_KEY="5f671a64819221e6b5c2361016af7dcaeb30de359009fee589b3a5d85dea11b4"
```

## License

`audiness` is licensed under MIT, for more details check the LICENSE file.
