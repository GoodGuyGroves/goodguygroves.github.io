resource "aws_route53_zone" "private_zone" {
    name = "russ.awsvpc"
    comment = "Zone for internal name resolution"
    tags = {
        Name = "Private Zone - russ.awsvpc"
    }
    vpc {
        vpc_id = aws_vpc.terraform_vpc.id
        vpc_region = var.AWS_REGION
    }
}

# resource "aws_route53_record" "dynamodb" {
#     zone_id = aws_route53_zone.private_zone.zone_id
#     name = "dynamodb.russ.awsvpc"
#     type = "CNAME"
#     ttl = "300"
#     records = [aws_dynamodb_table.personal_website.??]
# }

# output "dynamodb_dns" {
#   value = aws_route53_record.dynamodb.fqdn
# }