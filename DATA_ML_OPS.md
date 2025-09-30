
## 2. `DATA_ML_OPS.md`

```markdown
# Data & ML Ops Stack - Project Synapse

## Feature Store Architecture

### Feast Feature Store
```yaml
project: project_synapse
registry: s3://synapse-feast-registry/
online_store:
  type: dynamodb
  region: us-east-1
offline_store:
  type: s3
  bucket: synapse-offline-store