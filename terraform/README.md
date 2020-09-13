## SSH

Create SSH key-pair in current working directory in "${PWD}"/.ssh and add path to .tfvars
```
mkdir .ssh
chmod 700 .ssh
ssh-keygen -b 8192 -C "Terraform"
```

## terraform.tfvars

```
AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""
AWS_REGION     = ""
SSH_PRIV_KEY_NAME = ""
SSH_PUB_KEY_NAME = ""
SSH_PRIV_KEY_PATH = ""
SSH_PUB_KEY_PATH = ""
```