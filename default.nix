# $ nix-shell --pure
#
# Requires to have nix installed or using NixOS.
# 
{ pkgs ? import <nixpkgs> { } }:

let
  my-python = pkgs.python3;
  python-package-set = my-python.withPackages (p: with p; [
    click
    pytenable
    tqdm
    isort
    black
  ]
  );
in
pkgs.mkShell {
  buildInputs = [
    python-package-set
  ];

  shellHook = ''
    export ACCESS_KEY=""
    export SECRET_KEY=""
    PYTHONPATH=${python-package-set}/${python-package-set.sitePackages}
    python audiness.py
  '';
}
