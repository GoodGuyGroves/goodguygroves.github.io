# VPC
resource "aws_vpc" "terraform_vpc" {
  cidr_block           = "10.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = true
  enable_dns_hostnames = true
  enable_classiclink   = false
  tags = {
    Name = "terraform vpc"
  }
}

# Public
resource "aws_subnet" "terraform-public-1a" {
  vpc_id                  = aws_vpc.terraform_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "af-south-1a"
  tags = {
    Name = "terraform public 1a"
  }
}

resource "aws_subnet" "terraform-public-1b" {
  vpc_id                  = aws_vpc.terraform_vpc.id
  cidr_block              = "10.0.2.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "af-south-1b"
  tags = {
    Name = "terraform public 1b"
  }
}

resource "aws_subnet" "terraform-public-1c" {
  vpc_id                  = aws_vpc.terraform_vpc.id
  cidr_block              = "10.0.3.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "af-south-1c"
  tags = {
    Name = "terraform public 1c"
  }
}

# Private
resource "aws_subnet" "terraform-private-1a" {
  vpc_id                  = aws_vpc.terraform_vpc.id
  cidr_block              = "10.0.4.0/24"
  map_public_ip_on_launch = false
  availability_zone       = "af-south-1a"
  tags = {
    Name = "terraform private 1a"
  }
}

resource "aws_subnet" "terraform-private-1b" {
  vpc_id                  = aws_vpc.terraform_vpc.id
  cidr_block              = "10.0.5.0/24"
  map_public_ip_on_launch = false
  availability_zone       = "af-south-1b"
  tags = {
    Name = "terraform private 1b"
  }
}

resource "aws_subnet" "terraform-private-1c" {
  vpc_id                  = aws_vpc.terraform_vpc.id
  cidr_block              = "10.0.6.0/24"
  map_public_ip_on_launch = false
  availability_zone       = "af-south-1c"
  tags = {
    Name = "terraform private 1c"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "terraform-gw" {
  vpc_id = aws_vpc.terraform_vpc.id
  tags = {
    Name = "terraform-gw"
  }
}

# Route Tables
resource "aws_route_table" "terraform-public" {
  vpc_id = aws_vpc.terraform_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.terraform-gw.id
  }
  tags = {
    Name = "terraform-public"
  }
}

# Public Route Table associations
resource "aws_route_table_association" "terraform-public-1a" {
  subnet_id      = aws_subnet.terraform-public-1a.id
  route_table_id = aws_route_table.terraform-public.id
}

resource "aws_route_table_association" "terraform-public-1b" {
  subnet_id      = aws_subnet.terraform-public-1b.id
  route_table_id = aws_route_table.terraform-public.id
}

resource "aws_route_table_association" "terraform-public-1c" {
  subnet_id      = aws_subnet.terraform-public-1c.id
  route_table_id = aws_route_table.terraform-public.id
}

resource "aws_route_table" "terraform-private" {
  vpc_id = aws_vpc.terraform_vpc.id
  tags = {
    Name = "terraform-private"
  }
}

resource "aws_route_table_association" "terraform-private-1a" {
  subnet_id      = aws_subnet.terraform-private-1a.id
  route_table_id = aws_route_table.terraform-private.id
}

resource "aws_route_table_association" "terraform-private-1b" {
  subnet_id      = aws_subnet.terraform-private-1b.id
  route_table_id = aws_route_table.terraform-private.id
}

resource "aws_route_table_association" "terraform-private-1c" {
  subnet_id      = aws_subnet.terraform-private-1c.id
  route_table_id = aws_route_table.terraform-private.id
}