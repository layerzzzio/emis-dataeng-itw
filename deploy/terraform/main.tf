variable "aws_region" {
  default = ""
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "etl_data" {
  bucket = var.s3_bucket_name
  acl    = "private"
  tags = {
    Environment = var.environment
  }
}

resource "aws_ecr_repository" "etl_app" {
  name                 = var.ecr_repository_name
  image_tag_mutability = "MUTABLE"
  tags = {
    Environment = var.environment
  }
}

# You can add more AWS resources here as required by your application
