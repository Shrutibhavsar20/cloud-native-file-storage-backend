output "ec2_public_ip" {
  value = aws_instance.backend.public_ip
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}

output "s3_bucket_name" {
  value = aws_s3_bucket.files.bucket
}
