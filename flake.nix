{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = inputs @ {
    nixpkgs,
    flake-utils,
    ...
  }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;

        config.allowUnfree = true;
      };
    in {
      devShells = {
        default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python312
            python312Packages.pip
            pipenv
            docker-compose
          ];
        };
      };
    }
  );
}