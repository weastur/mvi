# mvi

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Minimal Viable Infrastructure

```shell
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
ansible -i inventory.py all -m ping
ansible-inventory -i inventory.py --graph --vars
```

## test infra

```shell
brew install pulumi/tap/pulumi
pulumi login
export HCLOUD_TOKEN=XXXXXXXXXXXXXX
pulumi up
```
