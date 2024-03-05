# $ nix-shell --pure
#
# Requires to have nix installed or using NixOS.
# 
{ pkgs ? import <nixpkgs> { } }:

let
  my-python = pkgs.python3;
  python-package-set = my-python.withPackages (p: with p; [
    black
    isort
    poetry-core
    pytenable
    pytest
    rich
    twine
    typer
    validators
  ]
  );
in
pkgs.mkShell {
  buildInputs = [
    python-package-set
  ];

  shellHook = ''
    export ACCESS_KEY="ae0bf3d57f8f8f6bcd8d01d3aedde60937d08647da4d89a6eb4dba2a9bee5d5d"
    export SECRET_KEY="5f671a64819221e6b5c2361016af7dcaeb30de359009fee589b3a5d85dea11b4"
    PYTHONPATH=${python-package-set}/${python-package-set.sitePackages}
  '';
}
