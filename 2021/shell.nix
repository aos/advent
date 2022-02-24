let
  rust = import (builtins.fetchTarball
      "https://github.com/oxalica/rust-overlay/archive/master.tar.gz");
  pkgs = import <nixpkgs> { overlays = [ rust ]; };
in
with pkgs;
mkShell {
  buildInputs = [
    rust-bin.stable.latest.default
  ];
}
