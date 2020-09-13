resource "aws_key_pair" "russ_terraform_key" {
  key_name   = var.SSH_PUB_KEY_NAME
  public_key = file(var.SSH_PUB_KEY_PATH)
}

resource "aws_dynamodb_table" "personal_website" {
  name           = "russ-website-stats"
  billing_mode   = "PAY_PER_REQUEST"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "id"

  attribute {
    name = "id"
    type = "N"
  }

  tags = {
    Name        = "personal-website"
  }
}