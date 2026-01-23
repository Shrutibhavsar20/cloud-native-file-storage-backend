resource "aws_instance" "backend" {
  ami                    = "ami-0f5ee92e2d63afc18"
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.ec2_sg.id]
  iam_instance_profile   = aws_iam_instance_profile.ec2_profile.name
  key_name = "cloud-native-key-terraform"

  tags = {
    Name = "${var.project_name}-backend"
  }
}
