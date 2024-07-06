{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs, ... }:
  let
    system = "x86_64-linux";

    pkgs = import nixpkgs { inherit system; };
    beamPkgs = with pkgs.beam_minimal; packagesWith interpreters.erlang_27;
    erlang = beamPkgs.erlang;
    elixir = beamPkgs.elixir_1_17;
    hex = beamPkgs.hex;
    elixir_ls = beamPkgs.elixir-ls;
  in {
    devShells."${system}".default = pkgs.mkShell {
      buildInputs = [
        erlang
        elixir
        hex
        elixir_ls
        pkgs.inotifyTools
        pkgs.nodejs
      ];

      ERL_INCLUDE_PATH = "${erlang}/lib/erlang/usr/include";
      ERL_AFLAGS = "-kernel shell_history enabled";

      shellHook = ''
        # Allow mix to work on local directory
        mkdir -p .nix-mix
        mkdir -p .nix-hex
        export MIX_HOME=$PWD/.nix-mix
        export HEX_HOME=$PWD/.nix-hex
        export ERL_LIBS=$HEX_HOME/lib/erlang/lib

        # Concat paths
        export PATH=$MIX_HOME/bin:$PATH
        export PATH=$MIX_HOME/escripts:$PATH
        export PATH=$HEX_HOME/bin:$PATH
      '';
    };
  };
}
