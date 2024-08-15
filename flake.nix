{
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in
  {
    packages.${system}.default = pkgs.writers.writePython3Bin "get_input" {
      libraries = [ pkgs.python3Packages.requests ];
    } ''
      import requests
      import sys

      year, day = sys.argv[1], sys.argv[2]
      url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
      cookie = open('cookie.txt').read().strip()

      r = requests.get(url, cookies={'session': cookie})
      print(r.text)
    '';
  };
}
