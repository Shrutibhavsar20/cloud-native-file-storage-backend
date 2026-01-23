resource "aws_db_subnet_group" "db_subnet" {
  name = "${var.project_name}-db-subnet-group"

  subnet_ids = [
    aws_subnet.private.id,
    aws_subnet.private_2.id
  ]

  tags = {
    Name = "${var.project_name}-db-subnet"
  }
}

resource "aws_db_instance" "postgres" {
  identifier          = "${var.project_name}-postgres"
  engine              = "postgres"
  engine_version      = "15"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  db_name             = "filesdb"
  username            = "postgres"
  password            = "postgres123"   # move later
  skip_final_snapshot = true
  publicly_accessible = false

  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  db_subnet_group_name   = aws_db_subnet_group.db_subnet.name
}


