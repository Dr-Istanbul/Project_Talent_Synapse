# Cloud Infrastructure (AWS) - Project Synapse

## AWS Service Architecture

### Compute & Orchestration
| Service | Purpose | Configuration |
|---------|---------|---------------|
| **Amazon EKS** | Container orchestration for AI agents | Managed node groups, Spot instances for cost optimization |
| **AWS Lambda** | Serverless functions for event-driven tasks | Python runtime, 3GB memory for ML inference |
| **AWS Step Functions** | Complex workflow orchestration | State machines for multi-agent coordination |
| **Amazon ECS** | Container management for microservices | Fargate for serverless containers |

### Data Storage Layer
| Service | Data Type | Configuration |
|---------|-----------|---------------|
| **Amazon S3** | Documents, models, raw data | Multi-tier storage (Standard, Intelligent-Tiering) |
| **Amazon RDS (PostgreSQL)** | Structured data, user profiles | Multi-AZ deployment, Read replicas |
| **Amazon DynamoDB** | Session state, real-time data | On-demand capacity, Global tables |
| **Amazon ElastiCache (Redis)** | Caching, session management | Cluster mode enabled |
| **Amazon Neptune** | Knowledge graphs, skill ontologies | Graph database for relationships |

### AI/ML Services
| Service | Function | Models |
|---------|----------|--------|
| **Amazon SageMaker** | Model training & deployment | Custom skill extraction models |
| **Amazon Bedrock** | Foundation model access | Claude, Titan, Jurassic models |
| **Amazon Comprehend** | NLP and text analysis | Custom entity recognition |
| **Amazon Rekognition** | Document processing | Resume parsing from images |
| **Amazon Kendra** | Intelligent search | Semantic search across profiles |

### Streaming & Messaging
| Service | Purpose | Configuration |
|---------|---------|---------------|
| **Amazon Kinesis** | Real-time data streams | Multiple shards for parallel processing |
| **Amazon SQS** | Agent-to-agent messaging | FIFO queues for ordered processing |
| **Amazon SNS** | Notifications and alerts | Multi-protocol (Email, SMS, Push) |
| **Amazon EventBridge** | Event bus for system events | Rule-based routing |

### Security & Governance
| Service | Security Function | Features |
|---------|-------------------|----------|
| **AWS Cognito** | User authentication & authorization | Social identity providers, MFA |
| **AWS KMS** | Encryption key management | Customer-managed keys |
| **AWS CloudTrail** | API activity monitoring | Multi-region logging |
| **AWS WAF** | Web application firewall | Bot control, rate limiting |
| **AWS Shield** | DDoS protection | Advanced protection tier |

## Network Architecture

### VPC Design
```yaml
VPC CIDR: 10.0.0.0/16
Public Subnets: 10.0.1.0/24, 10.0.2.0/24 (2 AZs)
Private Subnets: 10.0.3.0/24, 10.0.4.0/24 (2 AZs)
Database Subnets: 10.0.5.0/24, 10.0.6.0/24 (2 AZs)