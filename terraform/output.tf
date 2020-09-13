# VPC

# DynamoDB
output "dynamodb_table_arn" {
  description = "ARN of the DynamoDB table"
  value = aws_dynamodb_table.personal_website.arn
}

output "this_dynamodb_table_id" {
  description = "Name of the DynamoDB table"
  value = aws_dynamodb_table.personal_website.id
}