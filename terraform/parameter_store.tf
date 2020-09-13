resource "aws_ssm_parameter" "dynamodb_arn" {
  name  = "/database/personal_website/arn"
  type  = "String"
  value = aws_dynamodb_table.personal_website.arn
}