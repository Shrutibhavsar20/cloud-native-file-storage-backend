# Cloud-Native File Storage Backend on AWS

## 1. Project Overview
A cloud-native backend application that allows users to upload, list, and download files securely using AWS-managed services.  
The system stores files in **Amazon S3** and file metadata in **Amazon RDS (PostgreSQL)**, following real-world backend architecture.

---

## 2. What This Project Demonstrates
- Secure file storage using Amazon S3
- Metadata storage using Amazon RDS (PostgreSQL)
- Backend API built with FastAPI
- IAM role-based access (no hardcoded credentials)
- Cloud-native architecture similar to production systems

---

## 3. AWS Services Used 

### Amazon VPC
- Isolated network for backend resources  
- Public subnet for EC2  
- Private subnet for RDS  

### Amazon EC2
- Hosts the FastAPI backend  
- Exposes API to the internet  

### Amazon RDS (PostgreSQL)
- Stores file metadata (filename, S3 key, timestamps)  
- Accessible only from EC2 via Security Group  

### Amazon S3
- Stores uploaded files  
- Files are accessed via pre-signed URLs  

### IAM Role
- Attached to EC2  
- Grants permission to access S3 securely  

### Security Groups
- **EC2 SG**: allows HTTP (8000) and SSH  
- **RDS SG**: allows PostgreSQL access only from EC2  

---

## 4. Common Steps Used While Creating AWS Resources
- Created VPC and subnets  
- Configured Security Groups for restricted access  
- Attached IAM role to EC2  
- Used private networking for database  
- Avoided hardcoding credentials  

---

## 5. Backend Application Flow
1. Client uploads file via API  
2. File is stored in Amazon S3  
3. File metadata is stored in RDS  
4. Client lists files from RDS  
5. Download uses a temporary S3 pre-signed URL  

---

## 6. API Endpoints

### Upload File
POST /files/upload
Uploads file to S3 and stores metadata in RDS.

### List Files
GET /files
Returns list of uploaded files.

### Download File
GET /files/{file_id}/download
Generates a secure pre-signed URL for file download.

---

## 7. Project Structure
app/
├── main.py → FastAPI entry point
├── config.py → Environment configuration
├── database.py → Database connection
├── models.py → Database models
├── routes/
│ └── files.py → File APIs
├── services/
│ └── s3.py → S3 operations


---

## 8. Security Practices Used
- IAM roles instead of access keys  
- Private database access  
- Temporary pre-signed URLs  
- `.env` excluded from version control  

---

## 9. Infrastructure Automation (Terraform)
After manual setup, the same infrastructure is recreated using **Terraform** to enable repeatable and automated deployments.

---

## 10. Key Learning Outcomes
- Understanding AWS service integration  
- Designing secure cloud architectures  
- Backend development with FastAPI  
- Manual to Infrastructure-as-Code (IaC) transition  
