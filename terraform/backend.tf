terraform {
  backend "s3" {
    bucket = "terraform-russellgroves"
    key    = "state/russ.awsvpc/terraform.tfstate"
    region = "af-south-1"
  }
}