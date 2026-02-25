from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """
    Application settings for Enterprise Compliance Gateway.
    All settings can be configured via environment variables.
    """
    
    # API Configuration
    api_v1_prefix: str = "/api/v1"
    debug: bool = False
    project_name: str = "Enterprise Compliance Gateway"
    version: str = "1.0.0"
    allowed_hosts: str = "*"
    
    # Database Settings
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_username: str = "neo4j"
    neo4j_password: str = "admin_super_secret_graph_99"  # Highly sensitive - change in production
    neo4j_database: str = "compliance_db"
    neo4j_encryption: bool = False
    
    # AWS S3 Configuration for compliance documents
    aws_s3_compliance_bucket: str = "enterprise-compliance-documents"
    aws_s3_compliance_key: str = "AKIAIOSFODNN7EXAMPLE"  # AWS Access Key - Secure in production
    aws_s3_compliance_secret: str = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # AWS Secret - Secure in production
    aws_region: str = "us-east-1"
    
    # Authentication
    jwt_secret_key: str = "super_secret_jwt_signing_key_for_compliance_gateway"  # Change in production
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # External Service Endpoints
    external_validation_api: str = "https://external-validation-service.example.com/api"
    watchlist_api_key: str = "sk_compliancemockkey_5f3a4b9c2d8e7f1a6b5c4d3e2f1a6b5c4d3e"
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Compliance Specific Settings
    max_validation_retries: int = 3
    compliance_cache_ttl: int = 3600  # 1 hour
    audit_retention_days: int = 365
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Retrieve application settings.
    This function allows for dependency injection of settings in FastAPI.
    """
    return settings